from flask import Flask, request

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(threadName)s - %(levelname)s - %(message)s')
try:
    from py_zipkin.zipkin import zipkin_span, ZipkinAttrs
except: ImportError:\
    logging.info("Error importing py_zipkin package")
from flask_restplus import Api, Resource
import requests, sys
from model.response import resp_resource
from model.req_parser_model import MemberName_schema
from name_normalization.dhp_nameparser import name_normalization

app_name = sys._xoptions.get("app_name",'ms-name-normalization')
ZipkinURL = sys._xoptions.get("ZipkinURL",'http://localhost:9411/api/v1/spans')

app = Flask(__name__)
api = Api(app, version="v1", title="Name Normalization Service", description="This service removes prefixes, suffixes "
                                                                             "and special character from a peron "
                                                                             "name", default="Name Normalization",
          default_mediatype="aplication/json")
req_post = api.model('post_req', resp_resource)

def http_transport(encoded_span):
    body =  encoded_span
    requests.post(
        ZipkinURL,
        data=body,
        headers={'Content-Type': 'application/x-thrift'},
    )

bad_req_msg = "Required field 'name' is missing"
bad_data_msg = "Missing data for field 'name' cannot be null"


def process_req(req_payload):
    # logging.info(f"request received {req_payload}")
    if len(req_payload.errors) > 0:
        logging.info(f"Bad request received, json element 'name' missing in request")
        return {'error': bad_req_msg} #, 406
    elif len(req_payload.data['name']) == 0 or len(req_payload.data['name']) is None:
        logging.info(f"No value supplied for tag name")
        return {'error': bad_data_msg} #, 400
    out_name = name_normalization(req_payload.data['name'])
    logging.info(f"Respone: {out_name}")
    return out_name


@api.route('/normalize')
class Index(Resource):
    @api.expect(req_post)
    def post(self):
        mem_name_schema = MemberName_schema()
        req_payload = mem_name_schema.load(api.payload)
        logging.info(f"request received {req_payload}")
        try:
            with zipkin_span(
                    service_name='service1',
                    zipkin_attrs=ZipkinAttrs(
                        trace_id=request.headers['X-B3-TraceID'],
                        span_id=request.headers['X-B3-SpanID'],
                        parent_span_id=request.headers['X-B3-ParentSpanID'],
                        flags=request.headers['X-B3-Flags'],
                        is_sampled=request.headers['X-B3-Sampled'],
                    ),
                    span_name='index_service1',
                    transport_handler=http_transport,
                    port=6000,
                    sample_rate=100,  # 0.05, # Value between 0.0 and 100.0
            ):
                resp_out = process_req(req_payload)
        except (KeyError, NameError, ConnectionError, ConnectionRefusedError)as err:
            logging.info(err)
        try:
            with zipkin_span(
                    service_name='service1',
                    span_name='index_service1',
                    transport_handler=http_transport,
                    port=6000,
                    sample_rate=100,  # 0.05, # Value between 0.0 and 100.0
            ):
                resp_out = process_req(req_payload)
        except (KeyError, NameError, ConnectionError, ConnectionRefusedError)as err:
            logging.info(err)
            resp_out = process_req(req_payload)
        resp_keys = resp_out.keys()
        if 'name' in resp_keys:
            return resp_out, 201
        elif resp_out['error'] == bad_data_msg:
            return resp_out, 406
        else:
            return resp_out, 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
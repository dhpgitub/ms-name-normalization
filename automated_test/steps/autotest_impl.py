# file:features/steps/step_tutorial01.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then, configuration
from hamcrest import assert_that
# from lib import CopyData,CreateParmFile,InfoRemoteConn,EnvDetails, CmpResultSet
from builtins import str
import os, requests, logging
configuration.options
global_data_holder = {}
html_headers = {"Content-Type": "application/json", "Accept": "application/json"}


@given('the original name is {org_name}')
def step_impl(context, org_name):
    global global_data_holder
    response = requests.post(url='http://127.0.0.1:5000/normalize', json={"name": org_name}, headers=html_headers)
    assert response.status_code is 201
    logging.info(f"{response.json()}")
    global_data_holder = response.json()


@when('I run call name_normalization service')
def step_impl(context):
    pass


@then('I verify outputs and should match {normalized_name}')
def step_impl(context,normalized_name): 
    global global_data_holder
    logging.info(f'in then {global_data_holder}')
    assert(normalized_name.upper() == global_data_holder['name'].strip())
    # assert(True is True)
    
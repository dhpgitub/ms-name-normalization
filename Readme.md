# MS-NAME-NORMALIZATION
 
This services is written using python flask module that does name normalization i.e. remove below listed suffixes and special character if present in name received in request.

* `suffixs`: [ DR* ESQ* JR* MD* MRS* MS* PHD* REV* RN* SR* V*,DR*,ESQ*,JR*,MD*,MRS*,MS*,PHD*,REV*,RN*,SR*,V*/DR*/ESQ*/JR*/MD*/MRS*/MS*/PHD*/REV*/RN*/SR*/V* IV*,IV*/IV* III*,III*/III* II*,II*/II* I*,I*/I* MR*,MR*/MR"]
* `special_chars`: [",", "-", "!", r"'", "()", "&", ";", "+", "*", ".", r"/", ":", ";", "?", "="]

# Project Structure

```
ms-name-normalization
│   .gitignore
│   app.py
│   Dockerfile
│   Jenkinsfile
│   k8s_deply_app.yaml
│   k8s_service_app.yaml
│   Readme.md
│   requirements.txt
│
├───automated_test
│   │   nameNormalization.feature
│   │
│   └───steps
│           autotest_impl.py
│
├───model
│   │   req_parser_model.py
│   │   response.py
│   │   __init__.py
│
├───name_normalization
│   │   config.py
│   │   dhp_nameparser.py
│   │   __init__.py
│
├───test
    │   test_app.py   

```

## Setup

Install `all dependencies` need for this project using pip and requirements.txt:

```
$ pip install -r requirements.txt
```

## Deployment and Configuration
Set below environment variables before app starts.

* `app_name`: Use this to set name of services to run under, default value is set to **project name**.
* `ZipkinURL`: Specify ZipKin server to send trace information to, default value is set to **http://localhost:9411/api/v1/spans**.
* `doc_switch`: If not set then default value is set to **None** means Swagger UI is disabled.

### Starting the application
```
$ python app.py
```

To deploy this services to docker use `Dockerfile` and to deploy this services to kubernetes use `k8s_deply_app.yaml` and `k8s_service_app.yaml` files.

## Usage and example

Once the service is started, open http://0.0.0.0:5000/ goto /Swagger-UI.html to get swagger documataion for this service.

## Running the tests

Change working directory to `automated_test` and run below command to run automated test.

```
$ behave
```

Run below command to get information on additional aggruments that can be passed to above command to run automated test more specific.

```
$ behave --help
```

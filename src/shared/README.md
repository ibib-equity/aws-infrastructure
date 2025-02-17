=Shared Sub Project=

==Description==
The Shared sub project contains functions used in the data catalog project. These functions are listed below...

===get_auth_token===
This function is used to pull the auth token from Azure.

===import_sync===
This function is used in order to create assets (db,table,column,etc.) in collibra use cases where the changes must be 
tracked. The json_file is a .json file which is what the import api from collibra expects.

===parse_openapi_spec===
Here the open api spec is parsed and prepped to be written to collibra


==Instructions==

In order to set this package up we used Poetry. Since our package was already setup, we didn't need to initialize a new 
project. Please see the steps below:
1. poetry init
2. poetry install

===Next Steps===
The next steps will be taken in the Concourse pipeline where a poetry build will package the shared functions into a
wheel. This will be loaded into the layers, so the lambdas can pull these functions in.
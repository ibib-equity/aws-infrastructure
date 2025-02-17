expected_payload = [
   {
      "resourceType":"Domain",
      "identifier":{
         "name":"Swagger Petstore - OpenAPI 3.0",
         "community":{
            "name":"APIs"
         }
      },
      "type":{
         "name":"Physical Data Dictionary"
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"Swagger Petstore - OpenAPI 3.0",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "attributes":{
         "Description":[
            {
               "value":"This is a sample Pet Store Server based on the OpenAPI 3.0 specification.  You can find out more about\nSwagger at [https://swagger.io](https://swagger.io). In the third iteration of the pet store, we've switched to the design first approach!\nYou can now help us improve the API whether it's by making changes to the definition itself or to the code.\nThat way, with time, we can improve the API in general, and expose some of the new features in OAS3.\n\n_If you're looking for the Swagger 2.0/OAS 2.0 version of Petstore, then click [here](https://editor.swagger.io/?url=https://petstore.swagger.io/v2/swagger.yaml). Alternatively, you can load via the `Edit > Load Petstore OAS 2.0` menu option!_\n\nSome useful links:\n- [The Pet Store repository](https://github.com/swagger-api/swagger-petstore)\n- [The source API definition for the Pet Store](https://github.com/swagger-api/swagger-petstore/blob/master/src/main/resources/openapi.yaml)"
            }
         ],
         "URL":[
            {
               "value":"https://petstore3.swagger.io/api/v3"
            }
         ]
      },
      "type":{
         "name":"API"
      },
      "relations":{
         "00000000-0000-0000-0000-000000007005:SOURCE":[
            {
               "name":"PUT /pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"GET /pet/findByStatus",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"GET /pet/findByTags",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"GET /pet/{petId}",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /pet/{petId}/uploadImage",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"GET /store/inventory",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /store/order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"GET /store/order/{orderId}",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /user/createWithList",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"GET /user/login",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"GET /user/{username}",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"PUT /pet",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"API Endpoint"
      },
      "relations":{
         "00000000-0000-0000-0000-000000007005:TARGET":[
            {
               "name":"Swagger Petstore - OpenAPI 3.0",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"id",
      "identifier":{
         "name":"Pet > id",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"name",
      "identifier":{
         "name":"Pet > name",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"id",
      "identifier":{
         "name":"Pet > category > id",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"name",
      "identifier":{
         "name":"Pet > category > name",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"photoUrls",
      "identifier":{
         "name":"Pet > photoUrls",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"array"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"id",
      "identifier":{
         "name":"Pet > tags > id",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"name",
      "identifier":{
         "name":"Pet > tags > name",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"status",
      "identifier":{
         "name":"Pet > status",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"Pet",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Table"
      },
      "relations":{
         "018da964-d53a-7b18-a8c8-044dbd47a622:SOURCE":[
            {
               "name":"PUT /pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"Pet > id",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > name",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > category > id",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > category > name",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > photoUrls",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > tags > id",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > tags > name",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > status",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"POST /pet",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"API Endpoint"
      },
      "relations":{
         "00000000-0000-0000-0000-000000007005:TARGET":[
            {
               "name":"Swagger Petstore - OpenAPI 3.0",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"id",
      "identifier":{
         "name":"Pet > id",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"name",
      "identifier":{
         "name":"Pet > name",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"id",
      "identifier":{
         "name":"Pet > category > id",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"name",
      "identifier":{
         "name":"Pet > category > name",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"photoUrls",
      "identifier":{
         "name":"Pet > photoUrls",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"array"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"id",
      "identifier":{
         "name":"Pet > tags > id",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"name",
      "identifier":{
         "name":"Pet > tags > name",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"status",
      "identifier":{
         "name":"Pet > status",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"Pet",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Table"
      },
      "relations":{
         "018da964-d53a-7b18-a8c8-044dbd47a622:SOURCE":[
            {
               "name":"POST /pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"Pet > id",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > name",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > category > id",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > category > name",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > photoUrls",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > tags > id",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > tags > name",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > status",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"GET /pet/findByStatus",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"API Endpoint"
      },
      "relations":{
         "00000000-0000-0000-0000-000000007005:TARGET":[
            {
               "name":"Swagger Petstore - OpenAPI 3.0",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"GET /pet/findByTags",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"API Endpoint"
      },
      "relations":{
         "00000000-0000-0000-0000-000000007005:TARGET":[
            {
               "name":"Swagger Petstore - OpenAPI 3.0",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"GET /pet/{petId}",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"API Endpoint"
      },
      "relations":{
         "00000000-0000-0000-0000-000000007005:TARGET":[
            {
               "name":"Swagger Petstore - OpenAPI 3.0",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"id",
      "identifier":{
         "name":"Pet > id",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"name",
      "identifier":{
         "name":"Pet > name",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"id",
      "identifier":{
         "name":"Pet > category > id",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"name",
      "identifier":{
         "name":"Pet > category > name",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"photoUrls",
      "identifier":{
         "name":"Pet > photoUrls",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"array"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"id",
      "identifier":{
         "name":"Pet > tags > id",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"name",
      "identifier":{
         "name":"Pet > tags > name",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"status",
      "identifier":{
         "name":"Pet > status",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Pet",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"Pet",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Table"
      },
      "relations":{
         "018da964-d53a-7b18-a8c8-044dbd47a622:SOURCE":[
            {
               "name":"GET /pet/{petId}",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"Pet > id",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > name",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > category > id",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > category > name",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > photoUrls",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > tags > id",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > tags > name",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Pet > status",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"POST /pet/{petId}/uploadImage",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"API Endpoint"
      },
      "relations":{
         "00000000-0000-0000-0000-000000007005:TARGET":[
            {
               "name":"Swagger Petstore - OpenAPI 3.0",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"ApiResponse",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"code",
      "identifier":{
         "name":"ApiResponse > code",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"ApiResponse",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"type",
      "identifier":{
         "name":"ApiResponse > type",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"ApiResponse",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"message",
      "identifier":{
         "name":"ApiResponse > message",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"ApiResponse",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"ApiResponse",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Table"
      },
      "relations":{
         "018da964-d53a-7b18-a8c8-044dbd47a622:SOURCE":[
            {
               "name":"POST /pet/{petId}/uploadImage",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"ApiResponse > code",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"ApiResponse > type",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"ApiResponse > message",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"GET /store/inventory",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"API Endpoint"
      },
      "relations":{
         "00000000-0000-0000-0000-000000007005:TARGET":[
            {
               "name":"Swagger Petstore - OpenAPI 3.0",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"POST /store/order",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"API Endpoint"
      },
      "relations":{
         "00000000-0000-0000-0000-000000007005:TARGET":[
            {
               "name":"Swagger Petstore - OpenAPI 3.0",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"Order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"id",
      "identifier":{
         "name":"Order > id",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"petId",
      "identifier":{
         "name":"Order > petId",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"quantity",
      "identifier":{
         "name":"Order > quantity",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"shipDate",
      "identifier":{
         "name":"Order > shipDate",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"status",
      "identifier":{
         "name":"Order > status",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"complete",
      "identifier":{
         "name":"Order > complete",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"boolean"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"Order",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Table"
      },
      "relations":{
         "018da964-d53a-7b18-a8c8-044dbd47a622:SOURCE":[
            {
               "name":"POST /store/order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"Order > id",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Order > petId",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Order > quantity",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Order > shipDate",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Order > status",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Order > complete",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"GET /store/order/{orderId}",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"API Endpoint"
      },
      "relations":{
         "00000000-0000-0000-0000-000000007005:TARGET":[
            {
               "name":"Swagger Petstore - OpenAPI 3.0",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"Order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"id",
      "identifier":{
         "name":"Order > id",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"petId",
      "identifier":{
         "name":"Order > petId",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"quantity",
      "identifier":{
         "name":"Order > quantity",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"shipDate",
      "identifier":{
         "name":"Order > shipDate",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"status",
      "identifier":{
         "name":"Order > status",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"complete",
      "identifier":{
         "name":"Order > complete",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"boolean"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"Order",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"Order",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Table"
      },
      "relations":{
         "018da964-d53a-7b18-a8c8-044dbd47a622:SOURCE":[
            {
               "name":"GET /store/order/{orderId}",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"Order > id",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Order > petId",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Order > quantity",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Order > shipDate",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Order > status",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"Order > complete",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"POST /user/createWithList",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"API Endpoint"
      },
      "relations":{
         "00000000-0000-0000-0000-000000007005:TARGET":[
            {
               "name":"Swagger Petstore - OpenAPI 3.0",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"id",
      "identifier":{
         "name":"User > id",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"username",
      "identifier":{
         "name":"User > username",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"firstName",
      "identifier":{
         "name":"User > firstName",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"lastName",
      "identifier":{
         "name":"User > lastName",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"email",
      "identifier":{
         "name":"User > email",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"password",
      "identifier":{
         "name":"User > password",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"phone",
      "identifier":{
         "name":"User > phone",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"userStatus",
      "identifier":{
         "name":"User > userStatus",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"User",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Table"
      },
      "relations":{
         "018da964-d53a-7b18-a8c8-044dbd47a622:SOURCE":[
            {
               "name":"POST /user/createWithList",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"User > id",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"User > username",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"User > firstName",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"User > lastName",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"User > email",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"User > password",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"User > phone",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"User > userStatus",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"GET /user/login",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"API Endpoint"
      },
      "relations":{
         "00000000-0000-0000-0000-000000007005:TARGET":[
            {
               "name":"Swagger Petstore - OpenAPI 3.0",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"GET /user/{username}",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"API Endpoint"
      },
      "relations":{
         "00000000-0000-0000-0000-000000007005:TARGET":[
            {
               "name":"Swagger Petstore - OpenAPI 3.0",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"id",
      "identifier":{
         "name":"User > id",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"username",
      "identifier":{
         "name":"User > username",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"firstName",
      "identifier":{
         "name":"User > firstName",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"lastName",
      "identifier":{
         "name":"User > lastName",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"email",
      "identifier":{
         "name":"User > email",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"password",
      "identifier":{
         "name":"User > password",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"phone",
      "identifier":{
         "name":"User > phone",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"string"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "displayName":"userStatus",
      "identifier":{
         "name":"User > userStatus",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Column"
      },
      "attributes":{
         "Data Type":[
            {
               "value":"integer"
            }
         ]
      },
      "relations":{
         "00000000-0000-0000-0000-000000007042:TARGET":[
            {
               "name":"User",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   },
   {
      "resourceType":"Asset",
      "identifier":{
         "name":"User",
         "domain":{
            "name":"Swagger Petstore - OpenAPI 3.0",
            "community":{
               "name":"APIs"
            }
         }
      },
      "type":{
         "name":"Table"
      },
      "relations":{
         "018da964-d53a-7b18-a8c8-044dbd47a622:SOURCE":[
            {
               "name":"GET /user/{username}",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"User > id",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"User > username",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"User > firstName",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"User > lastName",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"User > email",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"User > password",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"User > phone",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"User > userStatus",
               "domain":{
                  "name":"Swagger Petstore - OpenAPI 3.0",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   }
]

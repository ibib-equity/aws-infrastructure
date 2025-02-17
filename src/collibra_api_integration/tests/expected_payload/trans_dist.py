expected_payload = [
   {
      "resourceType":"Domain",
      "identifier":{
         "name":"common-prod-api-gateway",
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
         "name":"common-prod-api-gateway",
         "domain":{
            "name":"common-prod-api-gateway",
            "community":{
               "name":"APIs"
            }
         }
      },
      "attributes":{
         "Description":[
            {
               "value":"Proxy to handle requests to crmt lambda functions."
            }
         ],
         "URL":[
            {
               "value":"https://api.common.aws.duke-energy.com"
            }
         ]
      },
      "type":{
         "name":"API"
      },
      "relations":{
         "00000000-0000-0000-0000-000000007005:SOURCE":[
            {
               "name":"GET /geography/area",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"GET /geography/boundaries",
               "domain":{
                  "name":"common-prod-api-gateway",
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
         "name":"GET /geography/area",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"common-prod-api-gateway",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"LatLongGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"currPage",
      "identifier":{
         "name":"LatLongGetResponseModel > metadata > currPage",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"LatLongGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"nextPage",
      "identifier":{
         "name":"LatLongGetResponseModel > metadata > nextPage",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"LatLongGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"landbase_type",
      "identifier":{
         "name":"LatLongGetResponseModel > data > landbase_type",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"LatLongGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"gis_id",
      "identifier":{
         "name":"LatLongGetResponseModel > data > gis_id",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"LatLongGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"source_system_id",
      "identifier":{
         "name":"LatLongGetResponseModel > data > source_system_id",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"LatLongGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"gis_name",
      "identifier":{
         "name":"LatLongGetResponseModel > data > gis_name",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"LatLongGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"alternate_name",
      "identifier":{
         "name":"LatLongGetResponseModel > data > alternate_name",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"LatLongGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"remarks",
      "identifier":{
         "name":"LatLongGetResponseModel > data > remarks",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"LatLongGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"division",
      "identifier":{
         "name":"LatLongGetResponseModel > data > division",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"LatLongGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"landbase_geometry",
      "identifier":{
         "name":"LatLongGetResponseModel > data > landbase_geometry",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"LatLongGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"landbase_geometry_geojson",
      "identifier":{
         "name":"LatLongGetResponseModel > data > landbase_geometry_geojson",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"LatLongGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
         "name":"LatLongGetResponseModel",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"GET /geography/area",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"LatLongGetResponseModel > metadata > currPage",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"LatLongGetResponseModel > metadata > nextPage",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"LatLongGetResponseModel > data > landbase_type",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"LatLongGetResponseModel > data > gis_id",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"LatLongGetResponseModel > data > source_system_id",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"LatLongGetResponseModel > data > gis_name",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"LatLongGetResponseModel > data > alternate_name",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"LatLongGetResponseModel > data > remarks",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"LatLongGetResponseModel > data > division",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"LatLongGetResponseModel > data > landbase_geometry",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"LatLongGetResponseModel > data > landbase_geometry_geojson",
               "domain":{
                  "name":"common-prod-api-gateway",
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
         "name":"GET /geography/boundaries",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"common-prod-api-gateway",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"currPage",
      "identifier":{
         "name":"BoundariesGetResponseModel > metadata > currPage",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"nextPage",
      "identifier":{
         "name":"BoundariesGetResponseModel > metadata > nextPage",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"landbase_type",
      "identifier":{
         "name":"BoundariesGetResponseModel > data > landbase_type",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"gis_id",
      "identifier":{
         "name":"BoundariesGetResponseModel > data > gis_id",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"source_system_id",
      "identifier":{
         "name":"BoundariesGetResponseModel > data > source_system_id",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"gis_name",
      "identifier":{
         "name":"BoundariesGetResponseModel > data > gis_name",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"alternate_name",
      "identifier":{
         "name":"BoundariesGetResponseModel > data > alternate_name",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"remarks",
      "identifier":{
         "name":"BoundariesGetResponseModel > data > remarks",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"division",
      "identifier":{
         "name":"BoundariesGetResponseModel > data > division",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"action_ind",
      "identifier":{
         "name":"BoundariesGetResponseModel > data > action_ind",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"create_timestamp",
      "identifier":{
         "name":"BoundariesGetResponseModel > data > create_timestamp",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"last_update_timestamp",
      "identifier":{
         "name":"BoundariesGetResponseModel > data > last_update_timestamp",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"landbase_geometry_geojson",
      "identifier":{
         "name":"BoundariesGetResponseModel > data > landbase_geometry_geojson",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"landbase_geometry",
      "identifier":{
         "name":"BoundariesGetResponseModel > data > landbase_geometry",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"deleted_indicator",
      "identifier":{
         "name":"BoundariesGetResponseModel > data > deleted_indicator",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
      "displayName":"curr_ind",
      "identifier":{
         "name":"BoundariesGetResponseModel > data > curr_ind",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"BoundariesGetResponseModel",
               "domain":{
                  "name":"common-prod-api-gateway",
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
         "name":"BoundariesGetResponseModel",
         "domain":{
            "name":"common-prod-api-gateway",
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
               "name":"GET /geography/boundaries",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"BoundariesGetResponseModel > metadata > currPage",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"BoundariesGetResponseModel > metadata > nextPage",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"BoundariesGetResponseModel > data > landbase_type",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"BoundariesGetResponseModel > data > gis_id",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"BoundariesGetResponseModel > data > source_system_id",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"BoundariesGetResponseModel > data > gis_name",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"BoundariesGetResponseModel > data > alternate_name",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"BoundariesGetResponseModel > data > remarks",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"BoundariesGetResponseModel > data > division",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"BoundariesGetResponseModel > data > action_ind",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"BoundariesGetResponseModel > data > create_timestamp",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"BoundariesGetResponseModel > data > last_update_timestamp",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"BoundariesGetResponseModel > data > landbase_geometry_geojson",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"BoundariesGetResponseModel > data > landbase_geometry",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"BoundariesGetResponseModel > data > deleted_indicator",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"BoundariesGetResponseModel > data > curr_ind",
               "domain":{
                  "name":"common-prod-api-gateway",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   }
]

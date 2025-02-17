expected_payload = [
   {
      "resourceType":"Domain",
      "identifier":{
         "name":"Asset and Work Management API",
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
         "name":"Asset and Work Management API",
         "domain":{
            "name":"Asset and Work Management API",
            "community":{
               "name":"APIs"
            }
         }
      },
      "attributes":{
         "Description":[
            {
               "value":"REST API for Asset and Work Management"
            }
         ],
         "URL":[
            {
               "value":"https://data.cdassetsandworkmanagement.prod.api.duke-energy.app/equipment"
            }
         ]
      },
      "type":{
         "name":"API"
      },
      "relations":{
         "00000000-0000-0000-0000-000000007005:SOURCE":[
            {
               "name":"POST /compatible-unit-bo",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /compatible-unit",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /compatible-unit-detail",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /compatible-unit-labor",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /compatible-unit-material",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /compatible-unit-service",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /compatible-unit-spec",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /measure-unit",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /site",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /long-description",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /asset",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /asset-attribute",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"POST /asset-spec",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"POST /compatible-unit-bo",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"Asset and Work Management API",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"next_token",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > next_token",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > cu_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"status_desc",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > status_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"status_date",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > status_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"history_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > history_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"uom_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > uom_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"standards_sheet_desc",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > standards_sheet_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_lvl_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > cu_lvl_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_by_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > change_by_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"discipline_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > discipline_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"line_of_business_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > line_of_business_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"region_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > region_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"state_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > state_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"scada",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > scada",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"shape",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > shape",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"alpha_value",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > alpha_value",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"attr_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > attr_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_by_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > change_by_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_date",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > change_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"class_structure_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > class_structure_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_spec_owner",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > cu_spec_owner",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_spec_require",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > cu_spec_require",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_spec_automation",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > cu_spec_automation",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"display_seq",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > display_seq",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"mandatory_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > mandatory_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"uom_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > uom_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"numeric_value",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > numeric_value",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_spec_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > cu_spec_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ref_obj_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > ref_obj_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ref_obj_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > ref_obj_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"section_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > section_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"domain_value",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > domain_value",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"abs_qty_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > abs_qty_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"utility_account_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > utility_account_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ferc_function_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > ferc_function_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"service_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > service_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lighting_ty_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > lighting_ty_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_by_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > change_by_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_date",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > change_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"child_cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > child_cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"child_ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > child_ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_dtl_key",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > cu_dtl_key",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"average_cost",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > average_cost",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"key_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > key_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"allocated_pct",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > allocated_pct",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"hot_cold_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > hot_cold_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"inaccessible_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > inaccessible_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"congest_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > congest_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"soil_ty",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > soil_ty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"coastal_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > coastal_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"voltage_filter",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > voltage_filter",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"pressure_filter",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > pressure_filter",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"parent_cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > parent_cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"parent_ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > parent_ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_dtl_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > cu_dtl_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"qty_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > qty_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"work_function",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > work_function",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"abandon_hours",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > abandon_hours",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"abs_hours_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > abs_hours_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"crew_ty_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > crew_ty_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_by_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > change_by_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_date",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > change_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"craft_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > craft_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_labor_key",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > cu_labor_key",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"hourly_rate",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > hourly_rate",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"install_hours",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > install_hours",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"hot_cold_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > hot_cold_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"inaccessible_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > inaccessible_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"congest_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > congest_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"soil_ty",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > soil_ty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"energized_pct_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > energized_pct_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"inaccessible_pct_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > inaccessible_pct_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"congest_pct_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > congest_pct_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"soil_ty_pct_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > soil_ty_pct_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_labor_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > cu_labor_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"rate_changed_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > rate_changed_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"remove_hours",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > remove_hours",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"site_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > site_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"skill_lvl_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > skill_lvl_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"transfer_hours",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > transfer_hours",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"work_function",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > work_function",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"catalog_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > catalog_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_by_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > change_by_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_date",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > change_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"condition_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > condition_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"contracted_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > contracted_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_material_key",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > cu_material_key",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"drawing_ref_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > drawing_ref_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_material_desc",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > cu_material_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"direct_purchase_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > direct_purchase_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"item_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > item_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"item_set_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > item_set_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"mfg_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > mfg_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"coastal_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > coastal_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"voltage_filter",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > voltage_filter",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"pressure_filter",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > pressure_filter",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"model_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > model_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"override_site_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > override_site_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"override_store_loc_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > override_store_loc_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"override_vendor_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > override_vendor_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_material_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > cu_material_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"material_qty",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > material_qty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"site_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > site_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"stores_loc_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > stores_loc_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"unit_cost_amt",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > unit_cost_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"unit_cost_changed_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > unit_cost_changed_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"uom_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > uom_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"vendor_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > vendor_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"work_function",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > work_function",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"abs_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > abs_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"catalog_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > catalog_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_by_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > change_by_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_date",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > change_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"contracted_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > contracted_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"service_desc",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > service_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"item_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > item_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"item_set_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > item_set_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"hot_cold_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > hot_cold_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"inaccessible_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > inaccessible_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"congest_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > congest_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"soil_ty",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > soil_ty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"order_unt_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > order_unt_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"override_vendor_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > override_vendor_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_service_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > cu_service_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"service_qty",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > service_qty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"site_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > site_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"unit_cost_amt",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > unit_cost_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"unit_cost_changed_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > unit_cost_changed_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"vendor_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > vendor_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"work_function",
      "identifier":{
         "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > work_function",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitBO",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"EquipmentCompatibleUnitBO",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"POST /compatible-unit-bo",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"EquipmentCompatibleUnitBO > next_token",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > cu_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > status_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > status_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > history_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > uom_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > standards_sheet_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > cu_lvl_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > change_by_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > discipline_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > line_of_business_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > region_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > state_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > scada",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > shape",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > alpha_value",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > attr_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > change_by_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > change_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > class_structure_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > cu_spec_owner",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > cu_spec_require",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > cu_spec_automation",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > display_seq",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > mandatory_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > uom_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > numeric_value",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > cu_spec_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > ref_obj_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > ref_obj_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > section_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_spec > domain_value",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > abs_qty_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > utility_account_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > ferc_function_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > service_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > lighting_ty_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > change_by_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > change_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > child_cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > child_ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > cu_dtl_key",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > average_cost",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > key_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > allocated_pct",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > hot_cold_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > inaccessible_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > congest_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > soil_ty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > coastal_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > voltage_filter",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > pressure_filter",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > parent_cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > parent_ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > cu_dtl_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > qty_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_detail > work_function",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > abandon_hours",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > abs_hours_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > crew_ty_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > change_by_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > change_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > craft_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > cu_labor_key",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > hourly_rate",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > install_hours",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > hot_cold_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > inaccessible_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > congest_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > soil_ty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > energized_pct_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > inaccessible_pct_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > congest_pct_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > soil_ty_pct_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > cu_labor_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > rate_changed_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > remove_hours",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > site_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > skill_lvl_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > transfer_hours",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_labor > work_function",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > catalog_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > change_by_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > change_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > condition_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > contracted_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > cu_material_key",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > drawing_ref_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > cu_material_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > direct_purchase_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > item_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > item_set_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > mfg_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > coastal_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > voltage_filter",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > pressure_filter",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > model_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > override_site_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > override_store_loc_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > override_vendor_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > cu_material_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > material_qty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > site_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > stores_loc_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > unit_cost_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > unit_cost_changed_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > uom_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > vendor_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_material > work_function",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > abs_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > catalog_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > change_by_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > change_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > contracted_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > service_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > item_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > item_set_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > hot_cold_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > inaccessible_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > congest_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > soil_ty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > order_unt_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > override_vendor_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > cu_service_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > service_qty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > site_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > unit_cost_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > unit_cost_changed_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > vendor_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitBO > response_list > equipment_compatible_unit_service > work_function",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"POST /compatible-unit",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"Asset and Work Management API",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"next_token",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > next_token",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_account_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > cu_account_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_asset_cd_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > cu_asset_cd_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"auto_expand_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > auto_expand_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"bid_unit_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > bid_unit_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"budget_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > budget_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_by_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > change_by_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_date",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > change_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"class_structure_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > class_structure_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_dtl_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > cu_dtl_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_lvl_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > cu_lvl_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_update_set_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > cu_update_set_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_tmpl_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > asset_tmpl_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"astm_length",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > astm_length",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"average_complex_cost_amt",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > average_complex_cost_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_comm",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > change_comm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"vehicle_color",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > vehicle_color",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"complex_asset_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > complex_asset_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"create_prerequisite_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > create_prerequisite_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_legacy_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > cu_legacy_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_short_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > cu_short_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"dependency_purpose_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > dependency_purpose_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"qty_rule",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > qty_rule",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"dependency_ty_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > dependency_ty_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"discipline_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > discipline_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"exceptional_demand_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > exceptional_demand_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_fac_ty_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > cu_fac_ty_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_finance_asset_ty",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > cu_finance_asset_ty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"line_of_business_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > line_of_business_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"loc_tmpl_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > loc_tmpl_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"manufacturer",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > manufacturer",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"mobile_control_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > mobile_control_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"pre_post_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > pre_post_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"prerequisite_milestone",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > prerequisite_milestone",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"region_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > region_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"rgl_review_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > rgl_review_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"scada",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > scada",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"explode_child_aa_cus",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > explode_child_aa_cus",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"shape",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > shape",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"state_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > state_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"substation_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > substation_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"successor_tsk_ty",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > successor_tsk_ty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_t_e_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > cu_t_e_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"trench_foot_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > trench_foot_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_desc",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > cu_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"expandable_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > expandable_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"financial_wo_desc",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > financial_wo_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"history_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > history_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"job_instruction_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > job_instruction_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > cu_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"sketch_feature_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > sketch_feature_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"span_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > span_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"standards_sheet_desc",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > standards_sheet_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"station_dtl_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > station_dtl_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"statistical_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > statistical_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"status_desc",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > status_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"status_date",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > status_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"support_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > support_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"tsk_ty_desc",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > tsk_ty_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"uom_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > uom_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"work_ty_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > work_ty_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"year_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitResponse > response_list > year_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"EquipmentCompatibleUnitResponse",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"POST /compatible-unit",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"EquipmentCompatibleUnitResponse > next_token",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > cu_account_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > cu_asset_cd_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > auto_expand_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > bid_unit_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > budget_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > change_by_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > change_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > class_structure_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > cu_dtl_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > cu_lvl_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > cu_update_set_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > asset_tmpl_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > astm_length",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > average_complex_cost_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > change_comm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > vehicle_color",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > complex_asset_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > create_prerequisite_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > cu_legacy_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > cu_short_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > dependency_purpose_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > qty_rule",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > dependency_ty_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > discipline_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > exceptional_demand_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > cu_fac_ty_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > cu_finance_asset_ty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > line_of_business_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > loc_tmpl_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > manufacturer",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > mobile_control_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > pre_post_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > prerequisite_milestone",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > region_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > rgl_review_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > scada",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > explode_child_aa_cus",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > shape",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > state_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > substation_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > successor_tsk_ty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > cu_t_e_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > trench_foot_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > cu_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > expandable_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > financial_wo_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > history_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > job_instruction_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > cu_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > sketch_feature_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > span_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > standards_sheet_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > station_dtl_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > statistical_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > status_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > status_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > support_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > tsk_ty_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > uom_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > work_ty_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitResponse > response_list > year_ind",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"POST /compatible-unit-detail",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"Asset and Work Management API",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"next_token",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > next_token",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"abs_qty_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > abs_qty_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"utility_account_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > utility_account_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ferc_function_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > ferc_function_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"service_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > service_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lighting_ty_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > lighting_ty_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_by_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > change_by_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_date",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > change_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"child_cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > child_cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"child_ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > child_ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_dtl_key",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > cu_dtl_key",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"average_cost",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > average_cost",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"key_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > key_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"allocated_pct",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > allocated_pct",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"hot_cold_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > hot_cold_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"inaccessible_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > inaccessible_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"congest_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > congest_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"soil_ty",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > soil_ty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"coastal_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > coastal_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"voltage_filter",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > voltage_filter",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"pressure_filter",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > pressure_filter",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"parent_cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > parent_cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"parent_ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > parent_ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_dtl_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > cu_dtl_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"qty_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > qty_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"work_function",
      "identifier":{
         "name":"EquipmentCompatibleUnitDetailResponse > response_list > work_function",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitDetailResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"EquipmentCompatibleUnitDetailResponse",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"POST /compatible-unit-detail",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"EquipmentCompatibleUnitDetailResponse > next_token",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > abs_qty_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > utility_account_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > ferc_function_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > service_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > lighting_ty_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > change_by_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > change_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > child_cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > child_ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > cu_dtl_key",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > average_cost",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > key_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > allocated_pct",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > hot_cold_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > inaccessible_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > congest_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > soil_ty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > coastal_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > voltage_filter",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > pressure_filter",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > parent_cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > parent_ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > cu_dtl_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > qty_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitDetailResponse > response_list > work_function",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"POST /compatible-unit-labor",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"Asset and Work Management API",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"next_token",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > next_token",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"abandon_hours",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > abandon_hours",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"abs_hours_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > abs_hours_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"crew_ty_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > crew_ty_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_by_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > change_by_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_date",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > change_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"craft_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > craft_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_labor_key",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > cu_labor_key",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"hourly_rate",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > hourly_rate",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"install_hours",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > install_hours",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"hot_cold_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > hot_cold_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"inaccessible_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > inaccessible_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"congest_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > congest_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"soil_ty",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > soil_ty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"energized_pct_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > energized_pct_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"inaccessible_pct_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > inaccessible_pct_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"congest_pct_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > congest_pct_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"soil_ty_pct_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > soil_ty_pct_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_labor_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > cu_labor_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"rate_changed_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > rate_changed_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"remove_hours",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > remove_hours",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"site_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > site_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"skill_lvl_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > skill_lvl_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"transfer_hours",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > transfer_hours",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"work_function",
      "identifier":{
         "name":"EquipmentCompatibleUnitLaborResponse > response_list > work_function",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitLaborResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"EquipmentCompatibleUnitLaborResponse",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"POST /compatible-unit-labor",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"EquipmentCompatibleUnitLaborResponse > next_token",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > abandon_hours",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > abs_hours_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > crew_ty_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > change_by_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > change_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > craft_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > cu_labor_key",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > hourly_rate",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > install_hours",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > hot_cold_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > inaccessible_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > congest_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > soil_ty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > energized_pct_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > inaccessible_pct_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > congest_pct_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > soil_ty_pct_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > cu_labor_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > rate_changed_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > remove_hours",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > site_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > skill_lvl_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > transfer_hours",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitLaborResponse > response_list > work_function",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"POST /compatible-unit-material",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"Asset and Work Management API",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"next_token",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > next_token",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"catalog_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > catalog_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_by_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > change_by_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_date",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > change_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"condition_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > condition_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"contracted_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > contracted_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_material_key",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > cu_material_key",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"drawing_ref_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > drawing_ref_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_material_desc",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > cu_material_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"direct_purchase_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > direct_purchase_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"item_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > item_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"item_set_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > item_set_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"mfg_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > mfg_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"coastal_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > coastal_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"voltage_filter",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > voltage_filter",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"pressure_filter",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > pressure_filter",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"model_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > model_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"override_site_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > override_site_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"override_store_loc_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > override_store_loc_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"override_vendor_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > override_vendor_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_material_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > cu_material_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"material_qty",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > material_qty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"site_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > site_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"stores_loc_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > stores_loc_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"unit_cost_amt",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > unit_cost_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"unit_cost_changed_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > unit_cost_changed_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"uom_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > uom_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"vendor_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > vendor_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"work_function",
      "identifier":{
         "name":"EquipmentCompatibleUnitMaterialResponse > response_list > work_function",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitMaterialResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"EquipmentCompatibleUnitMaterialResponse",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"POST /compatible-unit-material",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > next_token",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > catalog_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > change_by_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > change_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > condition_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > contracted_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > cu_material_key",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > drawing_ref_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > cu_material_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > direct_purchase_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > item_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > item_set_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > mfg_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > coastal_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > voltage_filter",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > pressure_filter",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > model_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > override_site_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > override_store_loc_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > override_vendor_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > cu_material_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > material_qty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > site_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > stores_loc_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > unit_cost_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > unit_cost_changed_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > uom_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > vendor_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitMaterialResponse > response_list > work_function",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"POST /compatible-unit-service",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"Asset and Work Management API",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"next_token",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > next_token",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"abs_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > abs_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"catalog_cd",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > catalog_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_by_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > change_by_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_date",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > change_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"contracted_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > contracted_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"service_desc",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > service_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"item_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > item_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"item_set_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > item_set_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"hot_cold_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > hot_cold_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"inaccessible_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > inaccessible_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"congest_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > congest_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"soil_ty",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > soil_ty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"order_unt_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > order_unt_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"override_vendor_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > override_vendor_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_service_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > cu_service_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"service_qty",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > service_qty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"site_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > site_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"unit_cost_amt",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > unit_cost_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"unit_cost_changed_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > unit_cost_changed_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"vendor_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > vendor_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"work_function",
      "identifier":{
         "name":"EquipmentCompatibleUnitServiceResponse > response_list > work_function",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitServiceResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"EquipmentCompatibleUnitServiceResponse",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"POST /compatible-unit-service",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"EquipmentCompatibleUnitServiceResponse > next_token",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > abs_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > catalog_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > change_by_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > change_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > contracted_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > service_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > item_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > item_set_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > hot_cold_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > inaccessible_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > congest_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > soil_ty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > order_unt_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > override_vendor_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > cu_service_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > service_qty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > site_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > unit_cost_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > unit_cost_changed_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > vendor_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitServiceResponse > response_list > work_function",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"POST /compatible-unit-spec",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"Asset and Work Management API",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"next_token",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > next_token",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"alpha_value",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > alpha_value",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"attr_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > attr_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_by_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > change_by_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_date",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > change_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"class_structure_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > class_structure_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > cu_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_spec_owner",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > cu_spec_owner",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_spec_require",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > cu_spec_require",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_spec_automation",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > cu_spec_automation",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ver_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > ver_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"display_seq",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > display_seq",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"mandatory_ind",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > mandatory_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"uom_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > uom_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"numeric_value",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > numeric_value",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"cu_spec_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > cu_spec_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ref_obj_id",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > ref_obj_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ref_obj_nm",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > ref_obj_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"section_num",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > section_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"domain_value",
      "identifier":{
         "name":"EquipmentCompatibleUnitSpecResponse > response_list > domain_value",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentCompatibleUnitSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"EquipmentCompatibleUnitSpecResponse",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"POST /compatible-unit-spec",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"EquipmentCompatibleUnitSpecResponse > next_token",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > alpha_value",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > attr_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > change_by_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > change_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > class_structure_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > cu_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > cu_spec_owner",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > cu_spec_require",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > cu_spec_automation",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > ver_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > display_seq",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > mandatory_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > uom_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > numeric_value",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > cu_spec_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > ref_obj_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > ref_obj_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > section_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentCompatibleUnitSpecResponse > response_list > domain_value",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"POST /measure-unit",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"Asset and Work Management API",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"MeasureUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"next_token",
      "identifier":{
         "name":"MeasureUnitResponse > next_token",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"MeasureUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"uom_abbr_name",
      "identifier":{
         "name":"MeasureUnitResponse > response_list > uom_abbr_name",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"MeasureUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"content_uid",
      "identifier":{
         "name":"MeasureUnitResponse > response_list > content_uid",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"MeasureUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"uom_desc",
      "identifier":{
         "name":"MeasureUnitResponse > response_list > uom_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"MeasureUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"uom_id",
      "identifier":{
         "name":"MeasureUnitResponse > response_list > uom_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"MeasureUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"measure_unit_uid",
      "identifier":{
         "name":"MeasureUnitResponse > response_list > measure_unit_uid",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"MeasureUnitResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"MeasureUnitResponse",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"POST /measure-unit",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"MeasureUnitResponse > next_token",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"MeasureUnitResponse > response_list > uom_abbr_name",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"MeasureUnitResponse > response_list > content_uid",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"MeasureUnitResponse > response_list > uom_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"MeasureUnitResponse > response_list > uom_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"MeasureUnitResponse > response_list > measure_unit_uid",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"POST /site",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"Asset and Work Management API",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"next_token",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > next_token",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_attr_id",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > asset_attr_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"attr_id",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > attr_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"prefix",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > prefix",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"data_ty",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > data_ty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"inspection_ind",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > inspection_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lob",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > lob",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"attr_desc",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > attr_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"domain",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > domain",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"uom_id",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > uom_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"site_id",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > site_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"EquipmentAssetAttributeResponse",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"POST /site",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"EquipmentAssetAttributeResponse > next_token",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > asset_attr_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > attr_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > prefix",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > data_ty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > inspection_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > lob",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > attr_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > domain",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > uom_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > site_id",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"POST /long-description",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"Asset and Work Management API",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"LongDescriptionResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"next_token",
      "identifier":{
         "name":"LongDescriptionResponse > next_token",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"LongDescriptionResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"trans_key",
      "identifier":{
         "name":"LongDescriptionResponse > response_list > trans_key",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"LongDescriptionResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"trans_column",
      "identifier":{
         "name":"LongDescriptionResponse > response_list > trans_column",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"LongDescriptionResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"trans_table",
      "identifier":{
         "name":"LongDescriptionResponse > response_list > trans_table",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"LongDescriptionResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"info_txt",
      "identifier":{
         "name":"LongDescriptionResponse > response_list > info_txt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"LongDescriptionResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"LongDescriptionResponse",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"POST /long-description",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"LongDescriptionResponse > next_token",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"LongDescriptionResponse > response_list > trans_key",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"LongDescriptionResponse > response_list > trans_column",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"LongDescriptionResponse > response_list > trans_table",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"LongDescriptionResponse > response_list > info_txt",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"POST /asset",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"Asset and Work Management API",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"next_token",
      "identifier":{
         "name":"EquipmentAssetResponse > next_token",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ancestor_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > ancestor_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_id",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > asset_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > asset_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"tag_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > tag_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_ty",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > asset_ty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_uid",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > asset_uid",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"assign_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > assign_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"assign_loc",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > assign_loc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"assignment_comm",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > assignment_comm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"budget_cost_amt",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > budget_cost_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"calendar",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > calendar",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_by",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > change_by",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > change_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"has_children_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > has_children_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"class_structure_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > class_structure_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_criticality",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > asset_criticality",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_activity_cd",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > asset_activity_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_category",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > asset_category",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_option",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > asset_option",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"replacement_override_reason",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > replacement_override_reason",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"replacement_reason",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > replacement_reason",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"barcode",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > barcode",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"budget_year",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > budget_year",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"business_sector",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > business_sector",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"certification_expiry_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > certification_expiry_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"certification_frequency",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > certification_frequency",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"certification_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > certification_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"chargeback_adjustment_pct",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > chargeback_adjustment_pct",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"comments",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > comments",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"commute_driver_effective_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > commute_driver_effective_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"commute_driver",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > commute_driver",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"tag2_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > tag2_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"criticality",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > criticality",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"customer_gl_acct_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > customer_gl_acct_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"customer_split_gl_acct",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > customer_split_gl_acct",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"delivery_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > delivery_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"delivery_loc",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > delivery_loc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_device_ty_cd",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > asset_device_ty_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"dielectric_rated_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > dielectric_rated_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"dielectric_category",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > dielectric_category",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"dielectric_voltage",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > dielectric_voltage",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"drawing_num_1",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > drawing_num_1",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"drawing_num_2",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > drawing_num_2",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"duty_cycle",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > duty_cycle",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ecode",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > ecode",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ehs_compliance",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > ehs_compliance",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"fcard_status_cd",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > fcard_status_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"fcard_status_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > fcard_status_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"documents_file_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > documents_file_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"fuel_card_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > fuel_card_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"fuel_vendor_nm",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > fuel_vendor_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"gl_acct_changed_by",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > gl_acct_changed_by",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"gl_effective_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > gl_effective_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"global_id",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > global_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"gl_owner",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > gl_owner",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"split_gl_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > split_gl_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"order_handler",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > order_handler",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"health_rank",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > health_rank",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"city_limit_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > city_limit_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"service_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > service_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"install_onsite_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > install_onsite_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"invalid_gl_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > invalid_gl_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"failed_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > failed_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"nerc_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > nerc_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"pending_removal_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > pending_removal_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"regulated_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > regulated_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"spare_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > spare_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"scrapped_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > scrapped_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"to_be_sold_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > to_be_sold_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"item_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > item_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"key_nm",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > key_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"last_driver",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > last_driver",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lease_cap_cost_amt",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lease_cap_cost_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"end_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > end_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lease_invoice_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lease_invoice_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lease_invoice_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lease_invoice_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lease_payment_amt",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lease_payment_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"rent_amt",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > rent_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lease_scehdule_desc",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lease_scehdule_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"start_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > start_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lease_state_nm",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lease_state_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"tax_amt",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > tax_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lease_term_desc",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lease_term_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lease_ty_cd",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lease_ty_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"legacy_asset_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > legacy_asset_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"legacy_source",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > legacy_source",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lease_lessor",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lease_lessor",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"line_of_business",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > line_of_business",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"maintained_by",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > maintained_by",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"manufacturer_mount_nm",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > manufacturer_mount_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"manufacture_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > manufacture_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"model_mount_nm",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > model_mount_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"de_model_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > de_model_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"moved_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > moved_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"mpi",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > mpi",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lvl4_node",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lvl4_node",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lvl4_node_desc",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lvl4_node_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lvl5_node",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lvl5_node",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lvl5_node_desc",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lvl5_node_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lvl6_node",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lvl6_node",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lvl6_node_desc",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lvl6_node_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lvl7_node",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lvl7_node",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lvl7_node_desc",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > lvl7_node_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"order_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > order_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"certification_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > certification_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"maintained_outside_duke_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > maintained_outside_duke_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"pitside_vendor",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > pitside_vendor",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"owner_nm",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > owner_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"owner_ty",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > owner_ty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"parking_loc",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > parking_loc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"pay_ct",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > pay_ct",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"pm_rgl_agency",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > pm_rgl_agency",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"pm_spare_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > pm_spare_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"probability_of_failure",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > probability_of_failure",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"customer_split_gl_acct_pct",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > customer_split_gl_acct_pct",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"customer_gl_acct_pct",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > customer_gl_acct_pct",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"projected_delivery_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > projected_delivery_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"projected_replacement_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > projected_replacement_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"purchased_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > purchased_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"purchase_order",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > purchase_order",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"purchase_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > purchase_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"radio_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > radio_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"rational_catastrophic_failure",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > rational_catastrophic_failure",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"rgl_agency",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > rgl_agency",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"de_repair_ty",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > de_repair_ty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"repair_ty",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > repair_ty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"replace_asset_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > replace_asset_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"replacement_cycle_year",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > replacement_cycle_year",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"residual_value",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > residual_value",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"resp_center",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > resp_center",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"customer_contact",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > customer_contact",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"risk_value",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > risk_value",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"serial_mount_nm",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > serial_mount_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"service_condition_env",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > service_condition_env",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"split_changed_by",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > split_changed_by",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"sub_status",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > sub_status",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"sub_status_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > sub_status_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_tag_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > asset_tag_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"temporary_end_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > temporary_end_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"temporary_start_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > temporary_start_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"vehicle_title_cd",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > vehicle_title_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"vendor_ordered_from",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > vendor_ordered_from",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"de_warr_expiry_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > de_warr_expiry_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"warr_start_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > warr_start_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"wo_rgl_agency_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > wo_rgl_agency_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_desc",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > asset_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"expected_life",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > expected_life",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ext_ref_id",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > ext_ref_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"failure_cd",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > failure_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"gl_acct_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > gl_acct_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"meter_group_nm",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > meter_group_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"installation_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > installation_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"running_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > running_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"loc_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > loc_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"maintain_hierarchy_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > maintain_hierarchy_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"manufacturer",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > manufacturer",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_moved_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > asset_moved_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"parent_asset_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > parent_asset_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"physical_loc",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > physical_loc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"feature_class",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > feature_class",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"gis_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > gis_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"accept_warr_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > accept_warr_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"alias_nm",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > alias_nm",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"alias_desc",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > alias_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"component_cd",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > component_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"model_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > model_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"motor_pool_ind",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > motor_pool_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"report_level_cd",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > report_level_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"sold_amt",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > sold_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"sold_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > sold_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"sold_memo_txt",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > sold_memo_txt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"sold_to_cd",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > sold_to_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"make_year",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > make_year",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"priority_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > priority_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"purchase_price_amt",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > purchase_price_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"replacement_cost_amt",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > replacement_cost_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"sender_system_id",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > sender_system_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_serial_num",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > asset_serial_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"site_id",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > site_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"EquipmentAssetResponse > response_list > source_system_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"EquipmentAssetResponse > response_list > status",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"status_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > status_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_tmpl",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > asset_tmpl",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"total_cost_amt",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > total_cost_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"total_downtime_duration",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > total_downtime_duration",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"total_uncharged_cost_amt",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > total_uncharged_cost_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"uncharged_cost_amt",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > uncharged_cost_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_usage_cd",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > asset_usage_cd",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"vendor",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > vendor",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"warr_expiry_date",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > warr_expiry_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"well_maintained",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > well_maintained",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"ytd_cost_amt",
      "identifier":{
         "name":"EquipmentAssetResponse > response_list > ytd_cost_amt",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"EquipmentAssetResponse",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"POST /asset",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"EquipmentAssetResponse > next_token",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > ancestor_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > asset_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > asset_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > tag_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > asset_ty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > asset_uid",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > assign_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > assign_loc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > assignment_comm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > budget_cost_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > calendar",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > change_by",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > change_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > has_children_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > class_structure_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > asset_criticality",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > asset_activity_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > asset_category",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > asset_option",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > replacement_override_reason",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > replacement_reason",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > barcode",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > budget_year",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > business_sector",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > certification_expiry_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > certification_frequency",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > certification_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > chargeback_adjustment_pct",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > comments",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > commute_driver_effective_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > commute_driver",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > tag2_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > criticality",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > customer_gl_acct_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > customer_split_gl_acct",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > delivery_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > delivery_loc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > asset_device_ty_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > dielectric_rated_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > dielectric_category",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > dielectric_voltage",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > drawing_num_1",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > drawing_num_2",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > duty_cycle",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > ecode",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > ehs_compliance",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > fcard_status_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > fcard_status_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > documents_file_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > fuel_card_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > fuel_vendor_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > gl_acct_changed_by",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > gl_effective_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > global_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > gl_owner",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > split_gl_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > order_handler",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > health_rank",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > city_limit_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > service_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > install_onsite_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > invalid_gl_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > failed_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > nerc_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > pending_removal_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > regulated_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > spare_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > scrapped_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > to_be_sold_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > item_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > key_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > last_driver",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lease_cap_cost_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > end_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lease_invoice_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lease_invoice_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lease_payment_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > rent_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lease_scehdule_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > start_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lease_state_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > tax_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lease_term_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lease_ty_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > legacy_asset_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > legacy_source",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lease_lessor",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > line_of_business",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > maintained_by",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > manufacturer_mount_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > manufacture_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > model_mount_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > de_model_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > moved_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > mpi",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lvl4_node",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lvl4_node_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lvl5_node",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lvl5_node_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lvl6_node",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lvl6_node_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lvl7_node",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > lvl7_node_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > order_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > certification_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > maintained_outside_duke_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > pitside_vendor",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > owner_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > owner_ty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > parking_loc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > pay_ct",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > pm_rgl_agency",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > pm_spare_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > probability_of_failure",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > customer_split_gl_acct_pct",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > customer_gl_acct_pct",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > projected_delivery_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > projected_replacement_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > purchased_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > purchase_order",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > purchase_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > radio_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > rational_catastrophic_failure",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > rgl_agency",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > de_repair_ty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > repair_ty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > replace_asset_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > replacement_cycle_year",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > residual_value",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > resp_center",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > customer_contact",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > risk_value",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > serial_mount_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > service_condition_env",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > split_changed_by",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > sub_status",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > sub_status_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > asset_tag_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > temporary_end_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > temporary_start_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > vehicle_title_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > vendor_ordered_from",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > de_warr_expiry_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > warr_start_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > wo_rgl_agency_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > asset_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > expected_life",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > ext_ref_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > failure_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > gl_acct_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > meter_group_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > installation_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > running_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > loc_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > maintain_hierarchy_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > manufacturer",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > asset_moved_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > parent_asset_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > physical_loc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > feature_class",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > gis_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > accept_warr_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > alias_nm",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > alias_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > component_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > model_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > motor_pool_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > report_level_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > sold_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > sold_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > sold_memo_txt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > sold_to_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > make_year",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > priority_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > purchase_price_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > replacement_cost_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > sender_system_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > asset_serial_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > site_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > source_system_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > status",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > status_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > asset_tmpl",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > total_cost_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > total_downtime_duration",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > total_uncharged_cost_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > uncharged_cost_amt",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > asset_usage_cd",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > vendor",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > warr_expiry_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > well_maintained",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetResponse > response_list > ytd_cost_amt",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"POST /asset-attribute",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"Asset and Work Management API",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"next_token",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > next_token",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_attr_id",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > asset_attr_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"attr_id",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > attr_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"prefix",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > prefix",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"data_ty",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > data_ty",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"inspection_ind",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > inspection_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"lob",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > lob",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"attr_desc",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > attr_desc",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"domain",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > domain",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"uom_id",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > uom_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"site_id",
      "identifier":{
         "name":"EquipmentAssetAttributeResponse > response_list > site_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetAttributeResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"EquipmentAssetAttributeResponse",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"POST /asset-attribute",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"EquipmentAssetAttributeResponse > next_token",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > asset_attr_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > attr_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > prefix",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > data_ty",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > inspection_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > lob",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > attr_desc",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > domain",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > uom_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetAttributeResponse > response_list > site_id",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"POST /asset-spec",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"Asset and Work Management API",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "018da964-d53a-7b18-a8c8-044dbd47a622:TARGET":[
            {
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"next_token",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > next_token",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"alpha_value",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > alpha_value",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"attr_id",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > attr_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_num",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > asset_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"asset_spec_id",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > asset_spec_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"base_uom_id",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > base_uom_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_by",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > change_by",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"change_date",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > change_date",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"class_structure_num",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > class_structure_num",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"data_owner",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > data_owner",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"require",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > require",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"linear_specification_id",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > linear_specification_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"mandatory_ind",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > mandatory_ind",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"uom_id",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > uom_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"numeric_value",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > numeric_value",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"section",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > section",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
      "displayName":"site_id",
      "identifier":{
         "name":"EquipmentAssetSpecResponse > response_list > site_id",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"EquipmentAssetSpecResponse",
               "domain":{
                  "name":"Asset and Work Management API",
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
         "name":"EquipmentAssetSpecResponse",
         "domain":{
            "name":"Asset and Work Management API",
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
               "name":"POST /asset-spec",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ],
         "00000000-0000-0000-0000-000000007042:SOURCE":[
            {
               "name":"EquipmentAssetSpecResponse > next_token",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > alpha_value",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > attr_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > asset_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > asset_spec_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > base_uom_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > change_by",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > change_date",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > class_structure_num",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > data_owner",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > require",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > linear_specification_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > mandatory_ind",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > uom_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > numeric_value",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > section",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            },
            {
               "name":"EquipmentAssetSpecResponse > response_list > site_id",
               "domain":{
                  "name":"Asset and Work Management API",
                  "community":{
                     "name":"APIs"
                  }
               }
            }
         ]
      }
   }
]

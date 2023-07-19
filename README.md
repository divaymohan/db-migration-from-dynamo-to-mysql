# db-migration-from-dynamo-to-mysql

## Samlpe collection in dynamo db:- 

```json
{
  "id": {
    "S": "sample"
  },
  "crDt": {
    "N": "1669799580170"
  },
  "bodyType": {
    "S": "jsonBody"
  },
  "bodyWrapper": {
    "S": "FulfillOfferRequest"
  },
  "category": {
    "S": "sample_category"
  },
  "creditFree": {
    "N": "1"
  },
  "headers": {
    "L": [
      {
        "M": {
          "name": {
            "S": "apikey"
          },
          "type": {
            "S": "constant"
          },
          "value": {
            "S": "SAMPLE_VALUE"
          }
        }
      },
      {
        "M": {
          "name": {
            "S": "member-ref-id"
          },
          "type": {
            "S": "constant"
          },
          "value": {
            "S": "DIVAY"
          }
        }
      }
    ]
  },
  "jsonBody": {
    "L": [
      {
        "M": {
          "name": {
            "S": "SiteName"
          },
          "type": {
            "S": "constant"
          },
          "value": {
            "S": "SAMPLE_NAME"
          }
        }
      },
      {
        "M": {
          "name": {
            "S": "AccountName"
          },
          "type": {
            "S": "constant"
          },
          "value": {
            "S": "SAMPLE_NAME"
          }
        }
      },
      {
        "M": {
          "name": {
            "S": "ProductConfigurationId"
          },
          "type": {
            "S": "constant"
          },
          "value": {
            "S": "SAMPLE_ID"
          }
        }
      },
      {
        "M": {
          "name": {
            "S": "AccountCode"
          },
          "type": {
            "S": "constant"
          },
          "value": {
            "S": "DUMMMY_CODE"
          }
        }
      },
      {
        "M": {
          "name": {
            "S": "LegalCopyStatus"
          },
          "type": {
            "S": "constant"
          },
          "value": {
            "S": "Accept"
          }
        }
      },
      {
        "M": {
          "name": {
            "S": "UserConsentForDataSharing"
          },
          "type": {
            "S": "constant"
          },
          "value": {
            "S": "true"
          }
        }
      },
      {
        "M": {
          "name": {
            "S": "ClientKey"
          }
        }
      },
      {
        "M": {
          "name": {
            "S": "RequestKey"
          }
        }
      },
      {
        "M": {
          "name": {
            "S": "PartnerCustomerId"
          }
        }
      },
      {
        "M": {
          "name": {
            "S": "CustomerInfo"
          }
        }
      }
    ]
  },
  "method": {
    "S": "POST"
  },
  "modDt": {
    "N": "1685340153220"
  },
  "type": {
    "S": "initiate"
  },
  "url": {
    "S": "https://sample.com"
  }
}
```

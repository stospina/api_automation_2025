project_post_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "archived": {
      "type": "boolean"
    },
    "billable": {
      "type": "boolean"
    },
    "budgetEstimate": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean"
        },
        "estimate": {
          "type": "integer"
        },
        "includeExpenses": {
          "type": "boolean"
        },
        "resetOption": {
          "type": "string"
        },
        "type": {
          "type": "string"
        }
      },
      "required": [
        "active",
        "estimate",
        "includeExpenses",
        "resetOption",
        "type"
      ]
    },
    "clientId": {
      "type": "string"
    },
    "clientName": {
      "type": "string"
    },
    "color": {
      "type": "string"
    },
    "costRate": {
      "type": "object",
      "properties": {
        "amount": {
          "type": "integer"
        },
        "currency": {
          "type": "string"
        }
      },
      "required": [
        "amount",
        "currency"
      ]
    },
    "duration": {
      "type": "string"
    },
    "estimate": {
      "type": "object",
      "properties": {
        "estimate": {
          "type": "string"
        },
        "type": {
          "type": "string"
        }
      },
      "required": [
        "estimate",
        "type"
      ]
    },
    "estimateReset": {
      "type": "object",
      "properties": {
        "dayOfMonth": {
          "type": "integer"
        },
        "dayOfWeek": {
          "type": "string"
        },
        "hour": {
          "type": "integer"
        },
        "interval": {
          "type": "string"
        },
        "month": {
          "type": "string"
        }
      },
      "required": [
        "dayOfMonth",
        "dayOfWeek",
        "hour",
        "interval",
        "month"
      ]
    },
    "hourlyRate": {
      "type": "object",
      "properties": {
        "amount": {
          "type": "integer"
        },
        "currency": {
          "type": "string"
        }
      },
      "required": [
        "amount",
        "currency"
      ]
    },
    "id": {
      "type": "string"
    },
    "memberships": {
      "type": "array",
      "items": [
        {
          "type": "object",
          "properties": {
            "costRate": {
              "type": "object",
              "properties": {
                "amount": {
                  "type": "integer"
                },
                "currency": {
                  "type": "string"
                }
              },
              "required": [
                "amount",
                "currency"
              ]
            },
            "hourlyRate": {
              "type": "object",
              "properties": {
                "amount": {
                  "type": "integer"
                },
                "currency": {
                  "type": "string"
                }
              },
              "required": [
                "amount",
                "currency"
              ]
            },
            "membershipStatus": {
              "type": "string"
            },
            "membershipType": {
              "type": "string"
            },
            "targetId": {
              "type": "string"
            },
            "userId": {
              "type": "string"
            }
          },
          "required": [
            "costRate",
            "hourlyRate",
            "membershipStatus",
            "membershipType",
            "targetId",
            "userId"
          ]
        }
      ]
    },
    "name": {
      "type": "string"
    },
    "note": {
      "type": "string"
    },
    "public": {
      "type": "boolean"
    },
    "template": {
      "type": "boolean"
    },
    "timeEstimate": {
      "type": "object",
      "properties": {
        "active": {
          "type": "boolean"
        },
        "estimate": {
          "type": "string"
        },
        "includeNonBillable": {
          "type": "boolean"
        },
        "resetOption": {
          "type": "string"
        },
        "type": {
          "type": "string"
        }
      },
      "required": [
        "active",
        "estimate",
        "includeNonBillable",
        "resetOption",
        "type"
      ]
    },
    "workspaceId": {
      "type": "string"
    }
  },
  "required": [
    "archived",
    "billable",
    "budgetEstimate",
    "clientId",
    "clientName",
    "color",
    "costRate",
    "duration",
    "estimate",
    "estimateReset",
    "hourlyRate",
    "id",
    "memberships",
    "name",
    "note",
    "public",
    "template",
    "timeEstimate",
    "workspaceId"
  ]
}
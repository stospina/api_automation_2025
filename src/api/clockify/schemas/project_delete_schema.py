project_delete_schema ={
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "color": {
      "type": "string"
    },
    "duration": {
      "type": "string"
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
    "workspaceId": {
      "type": "string"
    }
  },
  "required": [
    "color",
    "duration",
    "id",
    "memberships",
    "name",
    "note",
    "public",
    "workspaceId"
  ]
}
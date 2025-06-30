clients_post_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "address": {
      "type": "string"
    },
    "archived": {
      "type": "boolean"
    },
    "currencyId": {
      "type": "string"
    },
    "email": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "note": {
      "type": "string"
    },
    "workspaceId": {
      "type": "string"
    }
  },
  "required": [
    "address",
    "archived",
    "currencyId",
    "email",
    "id",
    "name",
    "note",
    "workspaceId"
  ]
}

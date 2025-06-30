project_get_schema= {
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
      "items": {}
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
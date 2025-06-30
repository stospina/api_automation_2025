tasks_post_schema ={
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "assigneeIds": {
      "type": "array",
      "items": [
        {
          "type": "string"
        },
        {
          "type": "string"
        }
      ]
    },
    "billable": {
      "type": "boolean"
    },
    "budgetEstimate": {
      "type": "integer"
    },
    "duration": {
      "type": "string"
    },
    "estimate": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "name": {
      "type": "string"
    },
    "projectId": {
      "type": "string"
    },
    "status": {
      "type": "string"
    },
    "userGroupIds": {
      "type": "array",
      "items": [
        {
          "type": "string"
        },
        {
          "type": "string"
        }
      ]
    }
  },
  "required": [
    "assigneeIds",
    "billable",
    "budgetEstimate",
    "duration",
    "estimate",
    "id",
    "name",
    "projectId",
    "status",
    "userGroupIds"
  ]
}

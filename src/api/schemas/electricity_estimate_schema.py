electricity_estimate_schema = {
    "type": "object",
    "required": ["data"],
    "properties": {
        "data": {
            "type": "object",
            "required": ["id", "type", "attributes"],
            "properties": {
                "id": {"type": "string"},
                "type": {"type": "string", "const": "estimate"},
                "attributes": {
                    "type": "object",
                    "required": [
                        "carbon_kg", "electricity_unit", "electricity_value", "country"
                    ],
                    "properties": {
                        "carbon_kg": {"type": "number"},
                        "electricity_unit": {"type": "string"},  # e.g., "kWh"
                        "electricity_value": {"type": "number"},
                        "country": {"type": "string"},
                        "state": {"type": ["string", "null"]}
                    }
                }
            }
        }
    }
}

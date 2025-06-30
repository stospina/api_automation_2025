flight_estimate_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "FlightEstimateResponse",
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
                        "carbon_mt",
                        "carbon_kg",
                        "carbon_lb",
                        "carbon_g",
                        "estimated_at",
                        "distance_value",
                        "distance_unit",
                        "passengers"
                    ],
                    "properties": {
                        "carbon_mt": {"type": "number"},
                        "carbon_kg": {"type": "number"},
                        "carbon_lb": {"type": "number"},
                        "carbon_g": {"type": "number"},
                        "estimated_at": {"type": "string", "format": "date-time"},
                        "distance_value": {"type": "number"},
                        "distance_unit": {"type": "string", "enum": ["mi", "km"]},
                        "passengers": {"type": "integer"}
                    }
                }
            }
        }
    }
}

"""Generated from Smithy shape ``com.amazonaws.iotevents#DynamoDBv2Action``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.dynamo_table_name
    import capo_iot_events.types.payload


class DynamoDBv2Action(TypedDict, closed=True):
    table_name: "capo_iot_events.types.dynamo_table_name.DynamoTableName"
    """<p>The name of the DynamoDB table.</p>"""
    payload: NotRequired["capo_iot_events.types.payload.Payload"]


# --- restJson1 ser/de ---
def serialize_json(value: DynamoDBv2Action) -> dict:
    out: dict = {}
    out["tableName"] = value["table_name"]
    if "payload" in value:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> DynamoDBv2Action:
    out: DynamoDBv2Action = {}  # type: ignore[typeddict-item]
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    if data.get("payload") is not None:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.deserialize_json(data["payload"])
    return out

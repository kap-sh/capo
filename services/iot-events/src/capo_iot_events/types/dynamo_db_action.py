"""Generated from Smithy shape ``com.amazonaws.iotevents#DynamoDBAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.dynamo_key_field
    import capo_iot_events.types.dynamo_key_type
    import capo_iot_events.types.dynamo_key_value
    import capo_iot_events.types.dynamo_operation
    import capo_iot_events.types.dynamo_table_name
    import capo_iot_events.types.payload


class DynamoDBAction(TypedDict, closed=True):
    hash_key_type: NotRequired["capo_iot_events.types.dynamo_key_type.DynamoKeyType"]
    """<p>The data type for the hash key (also called the partition key). You can specify the following values:</p> <ul> <li> <p> <code>'STRING'</code> - The hash key is a string.</p> </li> <li> <p> <code>'NUMBER'</code> - The hash key is a number.</p> </li> </ul> <p>If you don't specify <code>hashKeyType</code>, the default value is <code>'STRING'</code>.</p>"""
    hash_key_field: "capo_iot_events.types.dynamo_key_field.DynamoKeyField"
    """<p>The name of the hash key (also called the partition key). The <code>hashKeyField</code> value must match the partition key of the target DynamoDB table.</p>"""
    hash_key_value: "capo_iot_events.types.dynamo_key_value.DynamoKeyValue"
    """<p>The value of the hash key (also called the partition key).</p>"""
    range_key_type: NotRequired["capo_iot_events.types.dynamo_key_type.DynamoKeyType"]
    """<p>The data type for the range key (also called the sort key), You can specify the following values:</p> <ul> <li> <p> <code>'STRING'</code> - The range key is a string.</p> </li> <li> <p> <code>'NUMBER'</code> - The range key is number.</p> </li> </ul> <p>If you don't specify <code>rangeKeyField</code>, the default value is <code>'STRING'</code>.</p>"""
    range_key_field: NotRequired[
        "capo_iot_events.types.dynamo_key_field.DynamoKeyField"
    ]
    """<p>The name of the range key (also called the sort key). The <code>rangeKeyField</code> value must match the sort key of the target DynamoDB table. </p>"""
    range_key_value: NotRequired[
        "capo_iot_events.types.dynamo_key_value.DynamoKeyValue"
    ]
    """<p>The value of the range key (also called the sort key).</p>"""
    operation: NotRequired["capo_iot_events.types.dynamo_operation.DynamoOperation"]
    """<p>The type of operation to perform. You can specify the following values: </p> <ul> <li> <p> <code>'INSERT'</code> - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.</p> </li> <li> <p> <code>'UPDATE'</code> - Update an existing item of the DynamoDB table with new data. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key.</p> </li> <li> <p> <code>'DELETE'</code> - Delete an existing item of the DynamoDB table. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key.</p> </li> </ul> <p>If you don't specify this parameter, AWS IoT Events triggers the <code>'INSERT'</code> operation.</p>"""
    payload_field: NotRequired["capo_iot_events.types.dynamo_key_field.DynamoKeyField"]
    """<p>The name of the DynamoDB column that receives the action payload.</p> <p>If you don't specify this parameter, the name of the DynamoDB column is <code>payload</code>.</p>"""
    table_name: "capo_iot_events.types.dynamo_table_name.DynamoTableName"
    """<p>The name of the DynamoDB table. The <code>tableName</code> value must match the table name of the target DynamoDB table. </p>"""
    payload: NotRequired["capo_iot_events.types.payload.Payload"]


# --- restJson1 ser/de ---
def serialize_json(value: DynamoDBAction) -> dict:
    out: dict = {}
    if "hash_key_type" in value:
        out["hashKeyType"] = value["hash_key_type"]
    out["hashKeyField"] = value["hash_key_field"]
    out["hashKeyValue"] = value["hash_key_value"]
    if "range_key_type" in value:
        out["rangeKeyType"] = value["range_key_type"]
    if "range_key_field" in value:
        out["rangeKeyField"] = value["range_key_field"]
    if "range_key_value" in value:
        out["rangeKeyValue"] = value["range_key_value"]
    if "operation" in value:
        out["operation"] = value["operation"]
    if "payload_field" in value:
        out["payloadField"] = value["payload_field"]
    out["tableName"] = value["table_name"]
    if "payload" in value:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> DynamoDBAction:
    out: DynamoDBAction = {}  # type: ignore[typeddict-item]
    if data.get("hashKeyType") is not None:
        out["hash_key_type"] = data["hashKeyType"]
    if data.get("hashKeyField") is not None:
        out["hash_key_field"] = data["hashKeyField"]
    else:
        out["hash_key_field"] = ""
    if data.get("hashKeyValue") is not None:
        out["hash_key_value"] = data["hashKeyValue"]
    else:
        out["hash_key_value"] = ""
    if data.get("rangeKeyType") is not None:
        out["range_key_type"] = data["rangeKeyType"]
    if data.get("rangeKeyField") is not None:
        out["range_key_field"] = data["rangeKeyField"]
    if data.get("rangeKeyValue") is not None:
        out["range_key_value"] = data["rangeKeyValue"]
    if data.get("operation") is not None:
        out["operation"] = data["operation"]
    if data.get("payloadField") is not None:
        out["payload_field"] = data["payloadField"]
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        out["table_name"] = ""
    if data.get("payload") is not None:
        import capo_iot_events.types.payload

        out["payload"] = capo_iot_events.types.payload.deserialize_json(data["payload"])
    return out

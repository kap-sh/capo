"""Generated from Smithy shape ``com.amazonaws.iot#DynamoDBAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.dynamo_key_type
    import capo_iot.types.dynamo_operation
    import capo_iot.types.hash_key_field
    import capo_iot.types.hash_key_value
    import capo_iot.types.payload_field
    import capo_iot.types.range_key_field
    import capo_iot.types.range_key_value
    import capo_iot.types.table_name


class DynamoDBAction(TypedDict, closed=True):
    table_name: "capo_iot.types.table_name.TableName"
    """<p>The name of the DynamoDB table.</p>"""
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the IAM role that grants access to the DynamoDB table.</p>"""
    operation: NotRequired["capo_iot.types.dynamo_operation.DynamoOperation"]
    """<p>The type of operation to be performed. This follows the substitution template, so it can be <code>${operation}</code>, but the substitution must result in one of the following: <code>INSERT</code>, <code>UPDATE</code>, or <code>DELETE</code>.</p>"""
    hash_key_field: "capo_iot.types.hash_key_field.HashKeyField"
    """<p>The hash key name.</p>"""
    hash_key_value: "capo_iot.types.hash_key_value.HashKeyValue"
    """<p>The hash key value.</p>"""
    hash_key_type: NotRequired["capo_iot.types.dynamo_key_type.DynamoKeyType"]
    """<p>The hash key type. Valid values are "STRING" or "NUMBER"</p>"""
    range_key_field: NotRequired["capo_iot.types.range_key_field.RangeKeyField"]
    """<p>The range key name.</p>"""
    range_key_value: NotRequired["capo_iot.types.range_key_value.RangeKeyValue"]
    """<p>The range key value.</p>"""
    range_key_type: NotRequired["capo_iot.types.dynamo_key_type.DynamoKeyType"]
    """<p>The range key type. Valid values are "STRING" or "NUMBER"</p>"""
    payload_field: NotRequired["capo_iot.types.payload_field.PayloadField"]
    """<p>The action payload. This name can be customized.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynamoDBAction) -> dict:
    out: dict = {}
    out["tableName"] = value["table_name"]
    out["roleArn"] = value["role_arn"]
    if "operation" in value:
        out["operation"] = value["operation"]
    out["hashKeyField"] = value["hash_key_field"]
    out["hashKeyValue"] = value["hash_key_value"]
    if "hash_key_type" in value:
        import capo_iot.types.dynamo_key_type

        out["hashKeyType"] = capo_iot.types.dynamo_key_type.serialize_json(
            value["hash_key_type"]
        )
    if "range_key_field" in value:
        out["rangeKeyField"] = value["range_key_field"]
    if "range_key_value" in value:
        out["rangeKeyValue"] = value["range_key_value"]
    if "range_key_type" in value:
        import capo_iot.types.dynamo_key_type

        out["rangeKeyType"] = capo_iot.types.dynamo_key_type.serialize_json(
            value["range_key_type"]
        )
    if "payload_field" in value:
        out["payloadField"] = value["payload_field"]
    return out


def deserialize_json(data: dict) -> DynamoDBAction:
    out: DynamoDBAction = {}  # type: ignore[typeddict-item]
    if data.get("tableName") is not None:
        out["table_name"] = data["tableName"]
    else:
        raise DeserializationError("DynamoDBAction.table_name required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("DynamoDBAction.role_arn required")
    if data.get("operation") is not None:
        out["operation"] = data["operation"]
    if data.get("hashKeyField") is not None:
        out["hash_key_field"] = data["hashKeyField"]
    else:
        raise DeserializationError("DynamoDBAction.hash_key_field required")
    if data.get("hashKeyValue") is not None:
        out["hash_key_value"] = data["hashKeyValue"]
    else:
        raise DeserializationError("DynamoDBAction.hash_key_value required")
    if data.get("hashKeyType") is not None:
        import capo_iot.types.dynamo_key_type

        out["hash_key_type"] = capo_iot.types.dynamo_key_type.deserialize_json(
            data["hashKeyType"]
        )
    if data.get("rangeKeyField") is not None:
        out["range_key_field"] = data["rangeKeyField"]
    if data.get("rangeKeyValue") is not None:
        out["range_key_value"] = data["rangeKeyValue"]
    if data.get("rangeKeyType") is not None:
        import capo_iot.types.dynamo_key_type

        out["range_key_type"] = capo_iot.types.dynamo_key_type.deserialize_json(
            data["rangeKeyType"]
        )
    if data.get("payloadField") is not None:
        out["payload_field"] = data["payloadField"]
    return out

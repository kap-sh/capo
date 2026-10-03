"""Generated from Smithy shape ``com.amazonaws.dynamodb#GetItemOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_map
    import capo_dynamodb.types.consumed_capacity


class GetItemOutput(TypedDict, closed=True):
    item: NotRequired["capo_dynamodb.types.attribute_map.AttributeMap"]
    """<p>A map of attribute names to <code>AttributeValue</code> objects, as specified by <code>ProjectionExpression</code>.</p>"""
    consumed_capacity: NotRequired[
        "capo_dynamodb.types.consumed_capacity.ConsumedCapacity"
    ]
    """<p>The capacity units consumed by the <code>GetItem</code> operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. <code>ConsumedCapacity</code> is only returned if the <code>ReturnConsumedCapacity</code> parameter was specified. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/read-write-operations.html#read-operation-consumption">Capacity unit consumption for read operations</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetItemOutput) -> dict:
    out: dict = {}
    if "item" in value:
        import capo_dynamodb.types.attribute_map

        out["Item"] = capo_dynamodb.types.attribute_map.serialize_aws_json_1_0(
            value["item"]
        )
    if "consumed_capacity" in value:
        import capo_dynamodb.types.consumed_capacity

        out["ConsumedCapacity"] = (
            capo_dynamodb.types.consumed_capacity.serialize_aws_json_1_0(
                value["consumed_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetItemOutput:
    out: GetItemOutput = {}  # type: ignore[typeddict-item]
    if data.get("Item") is not None:
        import capo_dynamodb.types.attribute_map

        out["item"] = capo_dynamodb.types.attribute_map.deserialize_aws_json_1_0(
            data["Item"]
        )
    if data.get("ConsumedCapacity") is not None:
        import capo_dynamodb.types.consumed_capacity

        out["consumed_capacity"] = (
            capo_dynamodb.types.consumed_capacity.deserialize_aws_json_1_0(
                data["ConsumedCapacity"]
            )
        )
    return out

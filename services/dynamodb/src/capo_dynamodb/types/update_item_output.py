"""Generated from Smithy shape ``com.amazonaws.dynamodb#UpdateItemOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_map
    import capo_dynamodb.types.consumed_capacity
    import capo_dynamodb.types.item_collection_metrics


class UpdateItemOutput(TypedDict, closed=True):
    attributes: NotRequired["capo_dynamodb.types.attribute_map.AttributeMap"]
    """<p>A map of attribute values as they appear before or after the <code>UpdateItem</code> operation, as determined by the <code>ReturnValues</code> parameter.</p> <p>The <code>Attributes</code> map is only present if the update was successful and <code>ReturnValues</code> was specified as something other than <code>NONE</code> in the request. Each element represents one attribute.</p>"""
    consumed_capacity: NotRequired[
        "capo_dynamodb.types.consumed_capacity.ConsumedCapacity"
    ]
    """<p>The capacity units consumed by the <code>UpdateItem</code> operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. <code>ConsumedCapacity</code> is only returned if the <code>ReturnConsumedCapacity</code> parameter was specified. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/read-write-operations.html#write-operation-consumption">Capacity unity consumption for write operations</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p>If the table has vector indexes, the response includes a <code>VectorIndexes</code> field with <code>VectorWriteRequestBytes</code> consumed for each affected vector index.</p>"""
    item_collection_metrics: NotRequired[
        "capo_dynamodb.types.item_collection_metrics.ItemCollectionMetrics"
    ]
    """<p>Information about item collections, if any, that were affected by the <code>UpdateItem</code> operation. <code>ItemCollectionMetrics</code> is only returned if the <code>ReturnItemCollectionMetrics</code> parameter was specified. If the table does not have any local secondary indexes, this information is not returned in the response.</p> <p>Each <code>ItemCollectionMetrics</code> element consists of:</p> <ul> <li> <p> <code>ItemCollectionKey</code> - The partition key value of the item collection. This is the same as the partition key value of the item itself.</p> </li> <li> <p> <code>SizeEstimateRangeGB</code> - An estimate of item collection size, in gigabytes. This value is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on that table. Use this estimate to measure whether a local secondary index is approaching its size limit.</p> <p>The estimate is subject to change over time; therefore, do not rely on the precision or accuracy of the estimate.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateItemOutput) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_dynamodb.types.attribute_map

        out["Attributes"] = capo_dynamodb.types.attribute_map.serialize_aws_json_1_0(
            value["attributes"]
        )
    if "consumed_capacity" in value:
        import capo_dynamodb.types.consumed_capacity

        out["ConsumedCapacity"] = (
            capo_dynamodb.types.consumed_capacity.serialize_aws_json_1_0(
                value["consumed_capacity"]
            )
        )
    if "item_collection_metrics" in value:
        import capo_dynamodb.types.item_collection_metrics

        out["ItemCollectionMetrics"] = (
            capo_dynamodb.types.item_collection_metrics.serialize_aws_json_1_0(
                value["item_collection_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateItemOutput:
    out: UpdateItemOutput = {}  # type: ignore[typeddict-item]
    if data.get("Attributes") is not None:
        import capo_dynamodb.types.attribute_map

        out["attributes"] = capo_dynamodb.types.attribute_map.deserialize_aws_json_1_0(
            data["Attributes"]
        )
    if data.get("ConsumedCapacity") is not None:
        import capo_dynamodb.types.consumed_capacity

        out["consumed_capacity"] = (
            capo_dynamodb.types.consumed_capacity.deserialize_aws_json_1_0(
                data["ConsumedCapacity"]
            )
        )
    if data.get("ItemCollectionMetrics") is not None:
        import capo_dynamodb.types.item_collection_metrics

        out["item_collection_metrics"] = (
            capo_dynamodb.types.item_collection_metrics.deserialize_aws_json_1_0(
                data["ItemCollectionMetrics"]
            )
        )
    return out

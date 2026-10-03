"""Generated from Smithy shape ``com.amazonaws.dynamodb#QueryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.consumed_capacity
    import capo_dynamodb.types.integer
    import capo_dynamodb.types.item_list
    import capo_dynamodb.types.key


class QueryOutput(TypedDict, closed=True):
    items: NotRequired["capo_dynamodb.types.item_list.ItemList"]
    """<p>An array of item attributes that match the query criteria. Each element in this array consists of an attribute name and the value for that attribute.</p>"""
    count: "capo_dynamodb.types.integer.Integer"
    """<p>The number of items in the response.</p> <p>If you used a <code>QueryFilter</code> in the request, then <code>Count</code> is the number of items returned after the filter was applied, and <code>ScannedCount</code> is the number of matching items before the filter was applied.</p> <p>If you did not use a filter in the request, then <code>Count</code> and <code>ScannedCount</code> are the same.</p>"""
    scanned_count: "capo_dynamodb.types.integer.Integer"
    """<p>The number of items evaluated, before any <code>QueryFilter</code> is applied. A high <code>ScannedCount</code> value with few, or no, <code>Count</code> results indicates an inefficient <code>Query</code> operation. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Scan.html#Scan.Count">Count and ScannedCount</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p> <p>If you did not use a filter in the request, then <code>ScannedCount</code> is the same as <code>Count</code>.</p>"""
    last_evaluated_key: NotRequired["capo_dynamodb.types.key.Key"]
    """<p>The primary key of the item where the operation stopped, inclusive of the previous result set. Use this value to start a new operation, excluding this value in the new request.</p> <p>If <code>LastEvaluatedKey</code> is empty, then the "last page" of results has been processed and there is no more data to be retrieved.</p> <p>If <code>LastEvaluatedKey</code> is not empty, it does not necessarily mean that there is more data in the result set. The only way to know when you have reached the end of the result set is when <code>LastEvaluatedKey</code> is empty.</p>"""
    consumed_capacity: NotRequired[
        "capo_dynamodb.types.consumed_capacity.ConsumedCapacity"
    ]
    """<p>The capacity units consumed by the <code>Query</code> operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. <code>ConsumedCapacity</code> is only returned if the <code>ReturnConsumedCapacity</code> parameter was specified. For more information, see <a href="https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/read-write-operations.html#read-operation-consumption">Capacity unit consumption for read operations</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: QueryOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_dynamodb.types.item_list

        out["Items"] = capo_dynamodb.types.item_list.serialize_aws_json_1_0(
            value["items"]
        )
    out["Count"] = value.get("count", 0)
    out["ScannedCount"] = value.get("scanned_count", 0)
    if "last_evaluated_key" in value:
        import capo_dynamodb.types.key

        out["LastEvaluatedKey"] = capo_dynamodb.types.key.serialize_aws_json_1_0(
            value["last_evaluated_key"]
        )
    if "consumed_capacity" in value:
        import capo_dynamodb.types.consumed_capacity

        out["ConsumedCapacity"] = (
            capo_dynamodb.types.consumed_capacity.serialize_aws_json_1_0(
                value["consumed_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> QueryOutput:
    out: QueryOutput = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_dynamodb.types.item_list

        out["items"] = capo_dynamodb.types.item_list.deserialize_aws_json_1_0(
            data["Items"]
        )
    if data.get("Count") is not None:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    if data.get("ScannedCount") is not None:
        out["scanned_count"] = data["ScannedCount"]
    else:
        out["scanned_count"] = 0
    if data.get("LastEvaluatedKey") is not None:
        import capo_dynamodb.types.key

        out["last_evaluated_key"] = capo_dynamodb.types.key.deserialize_aws_json_1_0(
            data["LastEvaluatedKey"]
        )
    if data.get("ConsumedCapacity") is not None:
        import capo_dynamodb.types.consumed_capacity

        out["consumed_capacity"] = (
            capo_dynamodb.types.consumed_capacity.deserialize_aws_json_1_0(
                data["ConsumedCapacity"]
            )
        )
    return out

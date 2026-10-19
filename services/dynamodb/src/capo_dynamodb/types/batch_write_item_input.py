"""Generated from Smithy shape ``com.amazonaws.dynamodb#BatchWriteItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.batch_write_item_request_map
    import capo_dynamodb.types.return_consumed_capacity
    import capo_dynamodb.types.return_item_collection_metrics


class BatchWriteItemInput(TypedDict, closed=True):
    request_items: (
        "capo_dynamodb.types.batch_write_item_request_map.BatchWriteItemRequestMap"
    )
    """<p>A map of one or more table names or table ARNs and, for each table, a list of operations to be performed (<code>DeleteRequest</code> or <code>PutRequest</code>). Each element in the map consists of the following:</p> <ul> <li> <p> <code>DeleteRequest</code> - Perform a <code>DeleteItem</code> operation on the specified item. The item to be deleted is identified by a <code>Key</code> subelement:</p> <ul> <li> <p> <code>Key</code> - A map of primary key attribute values that uniquely identify the item. Each entry in this map consists of an attribute name and an attribute value. For each primary key, you must provide <i>all</i> of the key attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for <i>both</i> the partition key and the sort key.</p> </li> </ul> </li> <li> <p> <code>PutRequest</code> - Perform a <code>PutItem</code> operation on the specified item. The item to be put is identified by an <code>Item</code> subelement:</p> <ul> <li> <p> <code>Item</code> - A map of attributes and their values. Each entry in this map consists of an attribute name and an attribute value. Attribute values must not be null; string and binary type attributes must have lengths greater than zero; and set type attributes must not be empty. Requests that contain empty values are rejected with a <code>ValidationException</code> exception.</p> <p>If you specify any attributes that are part of an index key, then the data types for those attributes must match those of the schema in the table's attribute definition.</p> </li> </ul> </li> </ul>"""
    return_consumed_capacity: NotRequired[
        "capo_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]
    return_item_collection_metrics: NotRequired[
        "capo_dynamodb.types.return_item_collection_metrics.ReturnItemCollectionMetrics"
    ]
    """<p>Determines whether item collection metrics are returned. If set to <code>SIZE</code>, the response includes statistics about item collections, if any, that were modified during the operation are returned in the response. If set to <code>NONE</code> (the default), no statistics are returned.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchWriteItemInput) -> dict:
    out: dict = {}
    import capo_dynamodb.types.batch_write_item_request_map

    out["RequestItems"] = (
        capo_dynamodb.types.batch_write_item_request_map.serialize_aws_json_1_0(
            value["request_items"]
        )
    )
    if "return_consumed_capacity" in value:
        import capo_dynamodb.types.return_consumed_capacity

        out["ReturnConsumedCapacity"] = (
            capo_dynamodb.types.return_consumed_capacity.serialize_aws_json_1_0(
                value["return_consumed_capacity"]
            )
        )
    if "return_item_collection_metrics" in value:
        import capo_dynamodb.types.return_item_collection_metrics

        out["ReturnItemCollectionMetrics"] = (
            capo_dynamodb.types.return_item_collection_metrics.serialize_aws_json_1_0(
                value["return_item_collection_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchWriteItemInput:
    out: BatchWriteItemInput = {}  # type: ignore[typeddict-item]
    if data.get("RequestItems") is not None:
        import capo_dynamodb.types.batch_write_item_request_map

        out["request_items"] = (
            capo_dynamodb.types.batch_write_item_request_map.deserialize_aws_json_1_0(
                data["RequestItems"]
            )
        )
    else:
        out["request_items"] = {}
    if data.get("ReturnConsumedCapacity") is not None:
        import capo_dynamodb.types.return_consumed_capacity

        out["return_consumed_capacity"] = (
            capo_dynamodb.types.return_consumed_capacity.deserialize_aws_json_1_0(
                data["ReturnConsumedCapacity"]
            )
        )
    if data.get("ReturnItemCollectionMetrics") is not None:
        import capo_dynamodb.types.return_item_collection_metrics

        out["return_item_collection_metrics"] = (
            capo_dynamodb.types.return_item_collection_metrics.deserialize_aws_json_1_0(
                data["ReturnItemCollectionMetrics"]
            )
        )
    return out

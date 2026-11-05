"""Generated from Smithy shape ``com.amazonaws.dynamodb#BulkOperationUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.bulk_operation_bytes
    import capo_dynamodb.types.non_negative_long_object
    import capo_dynamodb.types.secondary_indexes_bulk_bytes_map
    import capo_dynamodb.types.table_arn
    import capo_dynamodb.types.vector_indexes_bulk_vector_bytes_map


class BulkOperationUsage(TypedDict, closed=True):
    table_name: NotRequired["capo_dynamodb.types.table_arn.TableArn"]
    """<p>The name or ARN of the table associated with the reported usage.</p>"""
    bulk_put_bytes: NotRequired[
        "capo_dynamodb.types.non_negative_long_object.NonNegativeLongObject"
    ]
    """<p>The total number of bulk put bytes used by the operation. This value excludes bulk put vector bytes.</p>"""
    table: NotRequired["capo_dynamodb.types.bulk_operation_bytes.BulkOperationBytes"]
    """<p>The number of bulk put bytes for the table, excluding its indexes.</p>"""
    local_secondary_indexes: NotRequired[
        "capo_dynamodb.types.secondary_indexes_bulk_bytes_map.SecondaryIndexesBulkBytesMap"
    ]
    """<p>The bulk put bytes used on each local secondary index affected by the operation, keyed by index name.</p>"""
    global_secondary_indexes: NotRequired[
        "capo_dynamodb.types.secondary_indexes_bulk_bytes_map.SecondaryIndexesBulkBytesMap"
    ]
    """<p>The bulk put bytes used on each global secondary index affected by the operation, keyed by index name.</p>"""
    vector_indexes: NotRequired[
        "capo_dynamodb.types.vector_indexes_bulk_vector_bytes_map.VectorIndexesBulkVectorBytesMap"
    ]
    """<p>The bulk put vector bytes used on each vector index affected by the operation, keyed by index name.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BulkOperationUsage) -> dict:
    out: dict = {}
    if "table_name" in value:
        out["TableName"] = value["table_name"]
    if "bulk_put_bytes" in value:
        out["BulkPutBytes"] = value["bulk_put_bytes"]
    if "table" in value:
        import capo_dynamodb.types.bulk_operation_bytes

        out["Table"] = capo_dynamodb.types.bulk_operation_bytes.serialize_aws_json_1_0(
            value["table"]
        )
    if "local_secondary_indexes" in value:
        import capo_dynamodb.types.secondary_indexes_bulk_bytes_map

        out["LocalSecondaryIndexes"] = (
            capo_dynamodb.types.secondary_indexes_bulk_bytes_map.serialize_aws_json_1_0(
                value["local_secondary_indexes"]
            )
        )
    if "global_secondary_indexes" in value:
        import capo_dynamodb.types.secondary_indexes_bulk_bytes_map

        out["GlobalSecondaryIndexes"] = (
            capo_dynamodb.types.secondary_indexes_bulk_bytes_map.serialize_aws_json_1_0(
                value["global_secondary_indexes"]
            )
        )
    if "vector_indexes" in value:
        import capo_dynamodb.types.vector_indexes_bulk_vector_bytes_map

        out["VectorIndexes"] = (
            capo_dynamodb.types.vector_indexes_bulk_vector_bytes_map.serialize_aws_json_1_0(
                value["vector_indexes"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BulkOperationUsage:
    out: BulkOperationUsage = {}  # type: ignore[typeddict-item]
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    if data.get("BulkPutBytes") is not None:
        out["bulk_put_bytes"] = data["BulkPutBytes"]
    if data.get("Table") is not None:
        import capo_dynamodb.types.bulk_operation_bytes

        out["table"] = (
            capo_dynamodb.types.bulk_operation_bytes.deserialize_aws_json_1_0(
                data["Table"]
            )
        )
    if data.get("LocalSecondaryIndexes") is not None:
        import capo_dynamodb.types.secondary_indexes_bulk_bytes_map

        out["local_secondary_indexes"] = (
            capo_dynamodb.types.secondary_indexes_bulk_bytes_map.deserialize_aws_json_1_0(
                data["LocalSecondaryIndexes"]
            )
        )
    if data.get("GlobalSecondaryIndexes") is not None:
        import capo_dynamodb.types.secondary_indexes_bulk_bytes_map

        out["global_secondary_indexes"] = (
            capo_dynamodb.types.secondary_indexes_bulk_bytes_map.deserialize_aws_json_1_0(
                data["GlobalSecondaryIndexes"]
            )
        )
    if data.get("VectorIndexes") is not None:
        import capo_dynamodb.types.vector_indexes_bulk_vector_bytes_map

        out["vector_indexes"] = (
            capo_dynamodb.types.vector_indexes_bulk_vector_bytes_map.deserialize_aws_json_1_0(
                data["VectorIndexes"]
            )
        )
    return out

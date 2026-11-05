"""Generated from Smithy shape ``com.amazonaws.dynamodb#VectorIndexesBulkVectorBytesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.bulk_operation_vector_bytes
    import capo_dynamodb.types.index_name

VectorIndexesBulkVectorBytesMap: TypeAlias = dict[
    "capo_dynamodb.types.index_name.IndexName",
    "capo_dynamodb.types.bulk_operation_vector_bytes.BulkOperationVectorBytes",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: VectorIndexesBulkVectorBytesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_dynamodb.types.bulk_operation_vector_bytes

        out[key] = (
            capo_dynamodb.types.bulk_operation_vector_bytes.serialize_aws_json_1_0(
                value
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VectorIndexesBulkVectorBytesMap:
    out: VectorIndexesBulkVectorBytesMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_dynamodb.types.bulk_operation_vector_bytes

        out[key] = (
            capo_dynamodb.types.bulk_operation_vector_bytes.deserialize_aws_json_1_0(
                value
            )
        )
    return out

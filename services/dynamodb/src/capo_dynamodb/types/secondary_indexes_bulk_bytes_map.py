"""Generated from Smithy shape ``com.amazonaws.dynamodb#SecondaryIndexesBulkBytesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dynamodb.types.bulk_operation_bytes
    import capo_dynamodb.types.index_name

SecondaryIndexesBulkBytesMap: TypeAlias = dict[
    "capo_dynamodb.types.index_name.IndexName",
    "capo_dynamodb.types.bulk_operation_bytes.BulkOperationBytes",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: SecondaryIndexesBulkBytesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_dynamodb.types.bulk_operation_bytes

        out[key] = capo_dynamodb.types.bulk_operation_bytes.serialize_aws_json_1_0(
            value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SecondaryIndexesBulkBytesMap:
    out: SecondaryIndexesBulkBytesMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_dynamodb.types.bulk_operation_bytes

        out[key] = capo_dynamodb.types.bulk_operation_bytes.deserialize_aws_json_1_0(
            value
        )
    return out

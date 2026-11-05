"""Generated from Smithy shape ``com.amazonaws.dynamodb#BulkOperationVectorBytes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.non_negative_long_object


class BulkOperationVectorBytes(TypedDict, closed=True):
    bulk_put_vector_bytes: NotRequired[
        "capo_dynamodb.types.non_negative_long_object.NonNegativeLongObject"
    ]
    """<p>The number of bulk put vector bytes used on the vector index.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BulkOperationVectorBytes) -> dict:
    out: dict = {}
    if "bulk_put_vector_bytes" in value:
        out["BulkPutVectorBytes"] = value["bulk_put_vector_bytes"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BulkOperationVectorBytes:
    out: BulkOperationVectorBytes = {}  # type: ignore[typeddict-item]
    if data.get("BulkPutVectorBytes") is not None:
        out["bulk_put_vector_bytes"] = data["BulkPutVectorBytes"]
    return out

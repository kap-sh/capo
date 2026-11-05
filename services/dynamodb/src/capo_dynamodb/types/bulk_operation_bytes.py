"""Generated from Smithy shape ``com.amazonaws.dynamodb#BulkOperationBytes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.non_negative_long_object


class BulkOperationBytes(TypedDict, closed=True):
    bulk_put_bytes: NotRequired[
        "capo_dynamodb.types.non_negative_long_object.NonNegativeLongObject"
    ]
    """<p>The number of bulk put bytes.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BulkOperationBytes) -> dict:
    out: dict = {}
    if "bulk_put_bytes" in value:
        out["BulkPutBytes"] = value["bulk_put_bytes"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BulkOperationBytes:
    out: BulkOperationBytes = {}  # type: ignore[typeddict-item]
    if data.get("BulkPutBytes") is not None:
        out["bulk_put_bytes"] = data["BulkPutBytes"]
    return out

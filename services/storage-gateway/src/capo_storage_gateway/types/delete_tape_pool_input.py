"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteTapePoolInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.pool_arn


class DeleteTapePoolInput(TypedDict, closed=True):
    pool_arn: "capo_storage_gateway.types.pool_arn.PoolARN"
    """<p>The Amazon Resource Name (ARN) of the custom tape pool to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTapePoolInput) -> dict:
    out: dict = {}
    out["PoolARN"] = value["pool_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTapePoolInput:
    out: DeleteTapePoolInput = {}  # type: ignore[typeddict-item]
    if data.get("PoolARN") is not None:
        out["pool_arn"] = data["PoolARN"]
    else:
        out["pool_arn"] = ""
    return out

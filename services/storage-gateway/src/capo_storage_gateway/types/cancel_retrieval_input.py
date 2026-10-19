"""Generated from Smithy shape ``com.amazonaws.storagegateway#CancelRetrievalInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.tape_arn


class CancelRetrievalInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    tape_arn: "capo_storage_gateway.types.tape_arn.TapeARN"
    """<p>The Amazon Resource Name (ARN) of the virtual tape you want to cancel retrieval for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelRetrievalInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    out["TapeARN"] = value["tape_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelRetrievalInput:
    out: CancelRetrievalInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    if data.get("TapeARN") is not None:
        out["tape_arn"] = data["TapeARN"]
    else:
        out["tape_arn"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.storagegateway#RetrieveTapeRecoveryPointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.tape_arn


class RetrieveTapeRecoveryPointInput(TypedDict, closed=True):
    tape_arn: "capo_storage_gateway.types.tape_arn.TapeARN"
    """<p>The Amazon Resource Name (ARN) of the virtual tape for which you want to retrieve the recovery point.</p>"""
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetrieveTapeRecoveryPointInput) -> dict:
    out: dict = {}
    out["TapeARN"] = value["tape_arn"]
    out["GatewayARN"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RetrieveTapeRecoveryPointInput:
    out: RetrieveTapeRecoveryPointInput = {}  # type: ignore[typeddict-item]
    if data.get("TapeARN") is not None:
        out["tape_arn"] = data["TapeARN"]
    else:
        out["tape_arn"] = ""
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    return out

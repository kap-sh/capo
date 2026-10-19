"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteAutomaticTapeCreationPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.gateway_arn


class DeleteAutomaticTapeCreationPolicyInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAutomaticTapeCreationPolicyInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAutomaticTapeCreationPolicyInput:
    out: DeleteAutomaticTapeCreationPolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    return out

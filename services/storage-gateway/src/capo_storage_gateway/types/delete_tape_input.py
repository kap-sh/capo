"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteTapeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_storage_gateway.types.boolean2
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.tape_arn


class DeleteTapeInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    """<p>The unique Amazon Resource Name (ARN) of the gateway that the virtual tape to delete is associated with. Use the <a>ListGateways</a> operation to return a list of gateways for your account and Amazon Web Services Region.</p>"""
    tape_arn: "capo_storage_gateway.types.tape_arn.TapeARN"
    """<p>The Amazon Resource Name (ARN) of the virtual tape to delete.</p>"""
    bypass_governance_retention: NotRequired[
        "capo_storage_gateway.types.boolean2.Boolean2"
    ]
    """<p>Set to <code>TRUE</code> to delete an archived tape that belongs to a custom pool with tape retention lock. Only archived tapes with tape retention lock set to <code>governance</code> can be deleted. Archived tapes with tape retention lock set to <code>compliance</code> can't be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTapeInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    out["TapeARN"] = value["tape_arn"]
    if "bypass_governance_retention" in value:
        out["BypassGovernanceRetention"] = value["bypass_governance_retention"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTapeInput:
    out: DeleteTapeInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("DeleteTapeInput.gateway_arn required")
    if data.get("TapeARN") is not None:
        out["tape_arn"] = data["TapeARN"]
    else:
        raise DeserializationError("DeleteTapeInput.tape_arn required")
    if data.get("BypassGovernanceRetention") is not None:
        out["bypass_governance_retention"] = data["BypassGovernanceRetention"]
    return out

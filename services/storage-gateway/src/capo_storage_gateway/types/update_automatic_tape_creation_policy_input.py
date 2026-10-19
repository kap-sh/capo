"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateAutomaticTapeCreationPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.automatic_tape_creation_rules
    import capo_storage_gateway.types.gateway_arn


class UpdateAutomaticTapeCreationPolicyInput(TypedDict, closed=True):
    automatic_tape_creation_rules: "capo_storage_gateway.types.automatic_tape_creation_rules.AutomaticTapeCreationRules"
    """<p>An automatic tape creation policy consists of a list of automatic tape creation rules. The rules determine when and how to automatically create new tapes.</p>"""
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAutomaticTapeCreationPolicyInput) -> dict:
    out: dict = {}
    import capo_storage_gateway.types.automatic_tape_creation_rules

    out["AutomaticTapeCreationRules"] = (
        capo_storage_gateway.types.automatic_tape_creation_rules.serialize_aws_json_1_1(
            value["automatic_tape_creation_rules"]
        )
    )
    out["GatewayARN"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAutomaticTapeCreationPolicyInput:
    out: UpdateAutomaticTapeCreationPolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("AutomaticTapeCreationRules") is not None:
        import capo_storage_gateway.types.automatic_tape_creation_rules

        out["automatic_tape_creation_rules"] = (
            capo_storage_gateway.types.automatic_tape_creation_rules.deserialize_aws_json_1_1(
                data["AutomaticTapeCreationRules"]
            )
        )
    else:
        out["automatic_tape_creation_rules"] = []
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SynchronizeGatewayTargetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.target_id_list


class SynchronizeGatewayTargetsRequest(TypedDict, closed=True):
    gateway_identifier: (
        "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier"
    )
    """<p>The gateway Identifier.</p>"""
    target_id_list: "capo_bedrock_agentcore_control.types.target_id_list.TargetIdList"
    """<p>The target ID list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SynchronizeGatewayTargetsRequest) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.target_id_list

    out["targetIdList"] = (
        capo_bedrock_agentcore_control.types.target_id_list.serialize_json(
            value["target_id_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> SynchronizeGatewayTargetsRequest:
    out: SynchronizeGatewayTargetsRequest = {}  # type: ignore[typeddict-item]
    if data.get("targetIdList") is not None:
        import capo_bedrock_agentcore_control.types.target_id_list

        out["target_id_list"] = (
            capo_bedrock_agentcore_control.types.target_id_list.deserialize_json(
                data["targetIdList"]
            )
        )
    else:
        out["target_id_list"] = []
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_id
    import capo_bedrock_agentcore_control.types.gateway_status
    import capo_bedrock_agentcore_control.types.status_reasons


class DeleteGatewayResponse(TypedDict, closed=True):
    gateway_id: "capo_bedrock_agentcore_control.types.gateway_id.GatewayId"
    """<p>The unique identifier of the deleted gateway.</p>"""
    status: "capo_bedrock_agentcore_control.types.gateway_status.GatewayStatus"
    """<p>The current status of the gateway deletion.</p>"""
    status_reasons: NotRequired[
        "capo_bedrock_agentcore_control.types.status_reasons.StatusReasons"
    ]
    """<p>The reasons for the current status of the gateway deletion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGatewayResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    import capo_bedrock_agentcore_control.types.gateway_status

    out["status"] = capo_bedrock_agentcore_control.types.gateway_status.serialize_json(
        value["status"]
    )
    if "status_reasons" in value:
        import capo_bedrock_agentcore_control.types.status_reasons

        out["statusReasons"] = (
            capo_bedrock_agentcore_control.types.status_reasons.serialize_json(
                value["status_reasons"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteGatewayResponse:
    out: DeleteGatewayResponse = {}  # type: ignore[typeddict-item]
    if data.get("gatewayId") is not None:
        out["gateway_id"] = data["gatewayId"]
    else:
        out["gateway_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.gateway_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.gateway_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.gateway_status.GatewayStatus", ""
        )
    if data.get("statusReasons") is not None:
        import capo_bedrock_agentcore_control.types.status_reasons

        out["status_reasons"] = (
            capo_bedrock_agentcore_control.types.status_reasons.deserialize_json(
                data["statusReasons"]
            )
        )
    return out

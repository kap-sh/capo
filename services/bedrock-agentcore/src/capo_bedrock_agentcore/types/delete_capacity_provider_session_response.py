"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteCapacityProviderSessionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.capacity_provider_arn
    import capo_bedrock_agentcore.types.capacity_provider_session_status
    import capo_bedrock_agentcore.types.session_id


class DeleteCapacityProviderSessionResponse(TypedDict, closed=True):
    capacity_provider_arn: (
        "capo_bedrock_agentcore.types.capacity_provider_arn.CapacityProviderArn"
    )
    """<p>The Amazon Resource Name (ARN) of the capacity provider associated with the deleted session.</p>"""
    session_id: "capo_bedrock_agentcore.types.session_id.SessionId"
    """<p>The unique identifier of the deleted capacity provider session.</p>"""
    status: "capo_bedrock_agentcore.types.capacity_provider_session_status.CapacityProviderSessionStatus"
    """<p>The current status of the capacity provider session. When the status is <code>Deleting</code>, the session is being deleted and is not available. When the status is <code>Deleted</code>, the session is no longer available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCapacityProviderSessionResponse) -> dict:
    out: dict = {}
    out["capacityProviderArn"] = value["capacity_provider_arn"]
    out["sessionId"] = value["session_id"]
    import capo_bedrock_agentcore.types.capacity_provider_session_status

    out["status"] = (
        capo_bedrock_agentcore.types.capacity_provider_session_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteCapacityProviderSessionResponse:
    out: DeleteCapacityProviderSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("capacityProviderArn") is not None:
        out["capacity_provider_arn"] = data["capacityProviderArn"]
    else:
        out["capacity_provider_arn"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.capacity_provider_session_status

        out["status"] = (
            capo_bedrock_agentcore.types.capacity_provider_session_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore.types.capacity_provider_session_status.CapacityProviderSessionStatus",
            "",
        )
    return out

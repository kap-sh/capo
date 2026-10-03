"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateAIAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.ai_agent_configuration
    import capo_qconnect.types.client_token
    import capo_qconnect.types.description
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.uuid_or_arn_or_either_with_qualifier
    import capo_qconnect.types.visibility_status


class UpdateAIAgentRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_qconnect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>"""
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    ai_agent_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the Amazon Q in Connect AI Agent.</p>"""
    visibility_status: "capo_qconnect.types.visibility_status.VisibilityStatus"
    """<p>The visbility status of the Amazon Q in Connect AI Agent.</p>"""
    configuration: NotRequired[
        "capo_qconnect.types.ai_agent_configuration.AIAgentConfiguration"
    ]
    """<p>The configuration of the Amazon Q in Connect AI Agent.</p>"""
    description: NotRequired["capo_qconnect.types.description.Description"]
    """<p>The description of the Amazon Q in Connect AI Agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAIAgentRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["visibilityStatus"] = value["visibility_status"]
    if "configuration" in value:
        import capo_qconnect.types.ai_agent_configuration

        out["configuration"] = (
            capo_qconnect.types.ai_agent_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateAIAgentRequest:
    out: UpdateAIAgentRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("visibilityStatus") is not None:
        out["visibility_status"] = data["visibilityStatus"]
    else:
        raise DeserializationError("UpdateAIAgentRequest.visibility_status required")
    if data.get("configuration") is not None:
        import capo_qconnect.types.ai_agent_configuration

        out["configuration"] = (
            capo_qconnect.types.ai_agent_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateAgentInsightStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status
    import capo_bedrock_agentcore_control.types.agent_insight_store_encryption_configuration
    import capo_bedrock_agentcore_control.types.agent_insight_store_id
    import capo_bedrock_agentcore_control.types.client_token


class UpdateAgentInsightStoreRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    agent_insight_store_id: "capo_bedrock_agentcore_control.types.agent_insight_store_id.AgentInsightStoreId"
    """<p>Specifies the unique identifier of the Agent Insight Store to update.</p>"""
    enablement_status: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status.AgentInsightStoreEnablementStatus"
    ]
    """<p>Specifies whether the Agent Insight Store accepts new Agent Insights. If you don't specify this parameter, the store's current enablement setting remains unchanged.</p>"""
    encryption_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_insight_store_encryption_configuration.AgentInsightStoreEncryptionConfiguration"
    ]
    """<p>Specifies the encryption mode and key configuration to use for new Agent Insights. If you don't specify this parameter, the store's current encryption configuration remains unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentInsightStoreRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "enablement_status" in value:
        import capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status

        out["enablementStatus"] = (
            capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status.serialize_json(
                value["enablement_status"]
            )
        )
    if "encryption_configuration" in value:
        import capo_bedrock_agentcore_control.types.agent_insight_store_encryption_configuration

        out["encryptionConfiguration"] = (
            capo_bedrock_agentcore_control.types.agent_insight_store_encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAgentInsightStoreRequest:
    out: UpdateAgentInsightStoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("enablementStatus") is not None:
        import capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status

        out["enablement_status"] = (
            capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status.deserialize_json(
                data["enablementStatus"]
            )
        )
    if data.get("encryptionConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.agent_insight_store_encryption_configuration

        out["encryption_configuration"] = (
            capo_bedrock_agentcore_control.types.agent_insight_store_encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    return out

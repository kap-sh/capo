"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AgentInsightStoreSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.agent_insight_store_arn
    import capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status
    import capo_bedrock_agentcore_control.types.agent_insight_store_encryption_configuration
    import capo_bedrock_agentcore_control.types.agent_insight_store_id
    import capo_bedrock_agentcore_control.types.agent_insight_store_status


class AgentInsightStoreSummary(TypedDict, closed=True):
    agent_insight_store_arn: "capo_bedrock_agentcore_control.types.agent_insight_store_arn.AgentInsightStoreArn"
    """<p>The Amazon Resource Name (ARN) of the Agent Insight Store.</p>"""
    agent_insight_store_id: "capo_bedrock_agentcore_control.types.agent_insight_store_id.AgentInsightStoreId"
    """<p>The unique identifier of the Agent Insight Store.</p>"""
    status: "capo_bedrock_agentcore_control.types.agent_insight_store_status.AgentInsightStoreStatus"
    """<p>The current lifecycle status of the Agent Insight Store. Valid values:</p> <dl> <dt>ACTIVE</dt> <dd> <p>The store is available.</p> </dd> <dt>UPDATING</dt> <dd> <p>The service is applying a requested change.</p> </dd> <dt>INACTIVE</dt> <dd> <p>The store does not accept new Agent Insights.</p> </dd> <dt>ERROR</dt> <dd> <p>The store requires intervention.</p> </dd> </dl>"""
    enablement_status: "capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status.AgentInsightStoreEnablementStatus"
    """<p>Specifies whether the Agent Insight Store accepts new Agent Insights. The default value is enabled.</p>"""
    encryption_configuration: "capo_bedrock_agentcore_control.types.agent_insight_store_encryption_configuration.AgentInsightStoreEncryptionConfiguration"
    """<p>Specifies the encryption mode and key configuration that encrypts new Agent Insights and protects the data at rest.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time when the Agent Insight Store was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time when the Agent Insight Store was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentInsightStoreSummary) -> dict:
    out: dict = {}
    out["agentInsightStoreArn"] = value["agent_insight_store_arn"]
    out["agentInsightStoreId"] = value["agent_insight_store_id"]
    import capo_bedrock_agentcore_control.types.agent_insight_store_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.agent_insight_store_status.serialize_json(
            value["status"]
        )
    )
    import capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status

    out["enablementStatus"] = (
        capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status.serialize_json(
            value["enablement_status"]
        )
    )
    import capo_bedrock_agentcore_control.types.agent_insight_store_encryption_configuration

    out["encryptionConfiguration"] = (
        capo_bedrock_agentcore_control.types.agent_insight_store_encryption_configuration.serialize_json(
            value["encryption_configuration"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> AgentInsightStoreSummary:
    out: AgentInsightStoreSummary = {}  # type: ignore[typeddict-item]
    if data.get("agentInsightStoreArn") is not None:
        out["agent_insight_store_arn"] = data["agentInsightStoreArn"]
    else:
        out["agent_insight_store_arn"] = ""
    if data.get("agentInsightStoreId") is not None:
        out["agent_insight_store_id"] = data["agentInsightStoreId"]
    else:
        out["agent_insight_store_id"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.agent_insight_store_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.agent_insight_store_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.agent_insight_store_status.AgentInsightStoreStatus",
            "",
        )
    if data.get("enablementStatus") is not None:
        import capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status

        out["enablement_status"] = (
            capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status.deserialize_json(
                data["enablementStatus"]
            )
        )
    else:
        import typing

        out["enablement_status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status.AgentInsightStoreEnablementStatus",
            "",
        )
    if data.get("encryptionConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.agent_insight_store_encryption_configuration

        out["encryption_configuration"] = (
            capo_bedrock_agentcore_control.types.agent_insight_store_encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "AgentInsightStoreSummary.encryption_configuration required"
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out

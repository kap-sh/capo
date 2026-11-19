"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateAgentInsightStoreResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.agent_insight_store_arn
    import capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status
    import capo_bedrock_agentcore_control.types.agent_insight_store_failure_reason
    import capo_bedrock_agentcore_control.types.agent_insight_store_id
    import capo_bedrock_agentcore_control.types.agent_insight_store_status


class UpdateAgentInsightStoreResponse(TypedDict, closed=True):
    agent_insight_store_arn: "capo_bedrock_agentcore_control.types.agent_insight_store_arn.AgentInsightStoreArn"
    """<p>The Amazon Resource Name (ARN) of the updated Agent Insight Store.</p>"""
    agent_insight_store_id: "capo_bedrock_agentcore_control.types.agent_insight_store_id.AgentInsightStoreId"
    """<p>The unique identifier of the updated Agent Insight Store.</p>"""
    status: "capo_bedrock_agentcore_control.types.agent_insight_store_status.AgentInsightStoreStatus"
    """<p>The lifecycle status of the Agent Insight Store after the update request. Valid values:</p> <dl> <dt>ACTIVE</dt> <dd> <p>The store is available.</p> </dd> <dt>UPDATING</dt> <dd> <p>The service is applying a requested change.</p> </dd> <dt>INACTIVE</dt> <dd> <p>The store does not accept new Agent Insights.</p> </dd> <dt>ERROR</dt> <dd> <p>The store requires intervention.</p> </dd> </dl>"""
    enablement_status: "capo_bedrock_agentcore_control.types.agent_insight_store_enablement_status.AgentInsightStoreEnablementStatus"
    """<p>Specifies whether the Agent Insight Store accepts new Agent Insights after the update request.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time when the Agent Insight Store was last updated.</p>"""
    failure_reason: NotRequired[
        "capo_bedrock_agentcore_control.types.agent_insight_store_failure_reason.AgentInsightStoreFailureReason"
    ]
    """<p>Describes the failure that prevented the Agent Insight Store from reaching its requested lifecycle status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentInsightStoreResponse) -> dict:
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
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> UpdateAgentInsightStoreResponse:
    out: UpdateAgentInsightStoreResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    return out


def redact_sensitive(value: UpdateAgentInsightStoreResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "failure_reason" in value:
        out["failure_reason"] = "*** Sensitive Data Redacted ***"
    return out

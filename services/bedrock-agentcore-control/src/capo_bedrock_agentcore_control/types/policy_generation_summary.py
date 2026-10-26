"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#PolicyGenerationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.policy_generation_arn
    import capo_bedrock_agentcore_control.types.policy_generation_name
    import capo_bedrock_agentcore_control.types.policy_generation_status
    import capo_bedrock_agentcore_control.types.resource
    import capo_bedrock_agentcore_control.types.resource_id
    import capo_bedrock_agentcore_control.types.string


class PolicyGenerationSummary(TypedDict, closed=True):
    policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The identifier of the policy engine associated with this generation request.</p>"""
    policy_generation_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId"
    """<p>The unique identifier for this policy generation request.</p>"""
    name: "capo_bedrock_agentcore_control.types.policy_generation_name.PolicyGenerationName"
    """<p>The customer-assigned name for this policy generation request.</p>"""
    policy_generation_arn: (
        "capo_bedrock_agentcore_control.types.policy_generation_arn.PolicyGenerationArn"
    )
    """<p>The ARN of this policy generation request.</p>"""
    resource: "capo_bedrock_agentcore_control.types.resource.Resource"
    """<p>The resource information associated with this policy generation.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when this policy generation request was created.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when this policy generation was last updated.</p>"""
    status: "capo_bedrock_agentcore_control.types.policy_generation_status.PolicyGenerationStatus"
    """<p>The current status of this policy generation request.</p>"""
    findings: NotRequired["capo_bedrock_agentcore_control.types.string.String"]
    """<p>Findings and insights from this policy generation process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGenerationSummary) -> dict:
    out: dict = {}
    out["policyEngineId"] = value["policy_engine_id"]
    out["policyGenerationId"] = value["policy_generation_id"]
    out["name"] = value["name"]
    out["policyGenerationArn"] = value["policy_generation_arn"]
    import capo_bedrock_agentcore_control.types.resource

    out["resource"] = capo_bedrock_agentcore_control.types.resource.serialize_json(
        value["resource"]
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.policy_generation_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.policy_generation_status.serialize_json(
            value["status"]
        )
    )
    if "findings" in value:
        out["findings"] = value["findings"]
    return out


def deserialize_json(data: dict) -> PolicyGenerationSummary:
    out: PolicyGenerationSummary = {}  # type: ignore[typeddict-item]
    if data.get("policyEngineId") is not None:
        out["policy_engine_id"] = data["policyEngineId"]
    else:
        out["policy_engine_id"] = ""
    if data.get("policyGenerationId") is not None:
        out["policy_generation_id"] = data["policyGenerationId"]
    else:
        out["policy_generation_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("policyGenerationArn") is not None:
        out["policy_generation_arn"] = data["policyGenerationArn"]
    else:
        out["policy_generation_arn"] = ""
    if data.get("resource") is not None:
        import capo_bedrock_agentcore_control.types.resource

        out["resource"] = (
            capo_bedrock_agentcore_control.types.resource.deserialize_json(
                data["resource"]
            )
        )
    else:
        out["resource"] = {"$unknown": {"name": ""}}
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.policy_generation_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.policy_generation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.policy_generation_status.PolicyGenerationStatus",
            "",
        )
    if data.get("findings") is not None:
        out["findings"] = data["findings"]
    return out

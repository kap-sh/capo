"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateAgentProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.aggregation_configurations
    import capo_wellarchitected.types.pillars
    import capo_wellarchitected.types.role_arn
    import capo_wellarchitected.types.sensitive_string


class UpdateAgentProfileRequest(TypedDict, closed=True):
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the profile to update.</p>"""
    display_name: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>The updated display name of the profile.</p>"""
    description: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>The updated description of the profile.</p>"""
    execution_role_arn: NotRequired["capo_wellarchitected.types.role_arn.RoleArn"]
    """<p>The updated ARN of the IAM execution role.</p>"""
    aggregation_configuration: NotRequired[
        "capo_wellarchitected.types.aggregation_configurations.AggregationConfigurations"
    ]
    """<p>The updated aggregation configuration.</p>"""
    business_overview: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>The updated business overview for the profile.</p>"""
    pillars: NotRequired["capo_wellarchitected.types.pillars.Pillars"]
    """<p>The updated Well-Architected Tool Framework pillars for the profile.</p>"""
    deletion_protection: NotRequired["bool"]
    """<p>Indicates whether deletion protection is enabled for the profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentProfileRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "aggregation_configuration" in value:
        import capo_wellarchitected.types.aggregation_configurations

        out["aggregationConfiguration"] = (
            capo_wellarchitected.types.aggregation_configurations.serialize_json(
                value["aggregation_configuration"]
            )
        )
    if "business_overview" in value:
        out["businessOverview"] = value["business_overview"]
    if "pillars" in value:
        import capo_wellarchitected.types.pillars

        out["pillars"] = capo_wellarchitected.types.pillars.serialize_json(
            value["pillars"]
        )
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    return out


def deserialize_json(data: dict) -> UpdateAgentProfileRequest:
    out: UpdateAgentProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("aggregationConfiguration") is not None:
        import capo_wellarchitected.types.aggregation_configurations

        out["aggregation_configuration"] = (
            capo_wellarchitected.types.aggregation_configurations.deserialize_json(
                data["aggregationConfiguration"]
            )
        )
    if data.get("businessOverview") is not None:
        out["business_overview"] = data["businessOverview"]
    if data.get("pillars") is not None:
        import capo_wellarchitected.types.pillars

        out["pillars"] = capo_wellarchitected.types.pillars.deserialize_json(
            data["pillars"]
        )
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    return out


def redact_sensitive(value: UpdateAgentProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "business_overview" in value:
        out["business_overview"] = "*** Sensitive Data Redacted ***"
    return out

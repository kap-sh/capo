"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateAgentProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_wellarchitected.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wellarchitected.types.aggregation_configurations
    import capo_wellarchitected.types.pillars
    import capo_wellarchitected.types.role_arn
    import capo_wellarchitected.types.sensitive_string
    import capo_wellarchitected.types.tags


class CreateAgentProfileRequest(TypedDict, closed=True):
    name: "str"
    """<p>The system name of the profile.</p>"""
    display_name: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>The display name of the profile shown to users.</p>"""
    description: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>A description of the profile.</p>"""
    business_overview: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>The business overview for this profile.</p>"""
    pillars: "capo_wellarchitected.types.pillars.Pillars"
    """<p>The Well-Architected Tool Framework pillars to associate with this profile.</p>"""
    deletion_protection: NotRequired["bool"]
    """<p>Indicates whether deletion protection is enabled for the profile.</p>"""
    execution_role_arn: "capo_wellarchitected.types.role_arn.RoleArn"
    """<p>The ARN of the IAM execution role used for recommendation actions.</p>"""
    aggregation_configuration: "capo_wellarchitected.types.aggregation_configurations.AggregationConfigurations"
    """<p>The aggregation configuration that defines which Amazon Web Services accounts and Regions to analyze.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["capo_wellarchitected.types.tags.Tags"]
    """<p>The tags to associate with the profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentProfileRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "business_overview" in value:
        out["businessOverview"] = value["business_overview"]
    import capo_wellarchitected.types.pillars

    out["pillars"] = capo_wellarchitected.types.pillars.serialize_json(value["pillars"])
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    out["executionRoleArn"] = value["execution_role_arn"]
    import capo_wellarchitected.types.aggregation_configurations

    out["aggregationConfiguration"] = (
        capo_wellarchitected.types.aggregation_configurations.serialize_json(
            value["aggregation_configuration"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_wellarchitected.types.tags

        out["tags"] = capo_wellarchitected.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAgentProfileRequest:
    out: CreateAgentProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAgentProfileRequest.name required")
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("businessOverview") is not None:
        out["business_overview"] = data["businessOverview"]
    if data.get("pillars") is not None:
        import capo_wellarchitected.types.pillars

        out["pillars"] = capo_wellarchitected.types.pillars.deserialize_json(
            data["pillars"]
        )
    else:
        raise DeserializationError("CreateAgentProfileRequest.pillars required")
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError(
            "CreateAgentProfileRequest.execution_role_arn required"
        )
    if data.get("aggregationConfiguration") is not None:
        import capo_wellarchitected.types.aggregation_configurations

        out["aggregation_configuration"] = (
            capo_wellarchitected.types.aggregation_configurations.deserialize_json(
                data["aggregationConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAgentProfileRequest.aggregation_configuration required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_wellarchitected.types.tags

        out["tags"] = capo_wellarchitected.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateAgentProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "business_overview" in value:
        out["business_overview"] = "*** Sensitive Data Redacted ***"
    return out

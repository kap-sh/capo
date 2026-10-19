"""Generated from Smithy shape ``com.amazonaws.wellarchitected#GetAgentProfileResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.aggregation_configurations
    import capo_wellarchitected.types.field_errors
    import capo_wellarchitected.types.pillars
    import capo_wellarchitected.types.role_arn
    import capo_wellarchitected.types.sensitive_string
    import capo_wellarchitected.types.tags


class GetAgentProfileResponse(TypedDict, closed=True):
    name: "str"
    """<p>The system name of the profile.</p>"""
    display_name: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>The display name of the profile.</p>"""
    description: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>A description of the profile.</p>"""
    business_overview: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>The business overview of the profile.</p>"""
    pillars: "capo_wellarchitected.types.pillars.Pillars"
    """<p>The Well-Architected Tool Framework pillars associated with the profile.</p>"""
    deletion_protection: "bool"
    """<p>Indicates whether deletion protection is enabled.</p>"""
    execution_role_arn: "capo_wellarchitected.types.role_arn.RoleArn"
    """<p>The ARN of the IAM execution role.</p>"""
    aggregation_configuration: "capo_wellarchitected.types.aggregation_configurations.AggregationConfigurations"
    """<p>The aggregation configuration.</p>"""
    arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the profile.</p>"""
    eligible_for_scheduled_generation: NotRequired["bool"]
    """<p>Indicates whether the profile is valid for scheduled recommendation generation.</p>"""
    eligible_for_architecture_generation: NotRequired["bool"]
    """<p>Indicates whether the profile is valid for manual architecture generation.</p>"""
    field_errors: NotRequired["capo_wellarchitected.types.field_errors.FieldErrors"]
    """<p>A map of field paths to error messages for invalid or missing input fields.</p>"""
    tags: NotRequired["capo_wellarchitected.types.tags.Tags"]
    """<p>The tags associated with the profile.</p>"""
    created_by: "str"
    """<p>The identifier of the user or system that created this profile.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the profile was created.</p>"""
    last_modified_by: NotRequired["str"]
    """<p>The identifier of the user or system that last modified this profile.</p>"""
    last_modified_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the profile was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentProfileResponse) -> dict:
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
    out["deletionProtection"] = value.get("deletion_protection", True)
    out["executionRoleArn"] = value["execution_role_arn"]
    import capo_wellarchitected.types.aggregation_configurations

    out["aggregationConfiguration"] = (
        capo_wellarchitected.types.aggregation_configurations.serialize_json(
            value["aggregation_configuration"]
        )
    )
    out["arn"] = value["arn"]
    if "eligible_for_scheduled_generation" in value:
        out["eligibleForScheduledGeneration"] = value[
            "eligible_for_scheduled_generation"
        ]
    if "eligible_for_architecture_generation" in value:
        out["eligibleForArchitectureGeneration"] = value[
            "eligible_for_architecture_generation"
        ]
    if "field_errors" in value:
        import capo_wellarchitected.types.field_errors

        out["fieldErrors"] = capo_wellarchitected.types.field_errors.serialize_json(
            value["field_errors"]
        )
    if "tags" in value:
        import capo_wellarchitected.types.tags

        out["tags"] = capo_wellarchitected.types.tags.serialize_json(value["tags"])
    out["createdBy"] = value["created_by"]
    import capo_wellarchitected._protocol.serialize

    out["createdAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "last_modified_by" in value:
        out["lastModifiedBy"] = value["last_modified_by"]
    if "last_modified_at" in value:
        import capo_wellarchitected._protocol.serialize

        out["lastModifiedAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
            value["last_modified_at"]
        )
    return out


def deserialize_json(data: dict) -> GetAgentProfileResponse:
    out: GetAgentProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
        out["pillars"] = []
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    else:
        out["deletion_protection"] = True
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        out["execution_role_arn"] = ""
    if data.get("aggregationConfiguration") is not None:
        import capo_wellarchitected.types.aggregation_configurations

        out["aggregation_configuration"] = (
            capo_wellarchitected.types.aggregation_configurations.deserialize_json(
                data["aggregationConfiguration"]
            )
        )
    else:
        out["aggregation_configuration"] = []
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("eligibleForScheduledGeneration") is not None:
        out["eligible_for_scheduled_generation"] = data[
            "eligibleForScheduledGeneration"
        ]
    if data.get("eligibleForArchitectureGeneration") is not None:
        out["eligible_for_architecture_generation"] = data[
            "eligibleForArchitectureGeneration"
        ]
    if data.get("fieldErrors") is not None:
        import capo_wellarchitected.types.field_errors

        out["field_errors"] = capo_wellarchitected.types.field_errors.deserialize_json(
            data["fieldErrors"]
        )
    if data.get("tags") is not None:
        import capo_wellarchitected.types.tags

        out["tags"] = capo_wellarchitected.types.tags.deserialize_json(data["tags"])
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastModifiedBy") is not None:
        out["last_modified_by"] = data["lastModifiedBy"]
    if data.get("lastModifiedAt") is not None:
        import datetime

        out["last_modified_at"] = datetime.datetime.fromisoformat(
            data["lastModifiedAt"].replace("Z", "+00:00")
        )
    return out


def redact_sensitive(value: GetAgentProfileResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "business_overview" in value:
        out["business_overview"] = "*** Sensitive Data Redacted ***"
    return out

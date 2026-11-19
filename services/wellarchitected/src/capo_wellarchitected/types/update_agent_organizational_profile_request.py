"""Generated from Smithy shape ``com.amazonaws.wellarchitected#UpdateAgentOrganizationalProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.organizational_aggregation_configuration
    import capo_wellarchitected.types.pillars
    import capo_wellarchitected.types.sensitive_string


class UpdateAgentOrganizationalProfileRequest(TypedDict, closed=True):
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the organizational profile to update.</p>"""
    display_name: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>The updated display name of the organizational profile. Omit this field to keep the current display name. A display name is required, so it cannot be cleared.</p>"""
    description: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>The updated description of the organizational profile. Omit this field to keep the current description, or supply an empty string to clear it; a cleared description is read back as absent rather than as an empty string.</p>"""
    business_overview: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>The updated business overview for the organizational profile. Omit this field to keep the current business overview, or supply an empty string to clear it; a cleared business overview is read back as absent rather than as an empty string.</p>"""
    pillars: NotRequired["capo_wellarchitected.types.pillars.Pillars"]
    """<p>The updated Amazon Web Services Well-Architected Framework pillars for the organizational profile. Omit this field to keep the current pillars. A profile must target at least one pillar, so an empty list is rejected.</p>"""
    deletion_protection: NotRequired["bool"]
    """<p>Indicates whether deletion protection is enabled for the organizational profile.</p>"""
    organizational_aggregation_configuration: NotRequired[
        "capo_wellarchitected.types.organizational_aggregation_configuration.OrganizationalAggregationConfiguration"
    ]
    """<p>The organizational monitoring boundary. Contains organizational unit or root entries and individual account entries that define the scope for the profile. Omit this field to keep the current boundary, or supply this structure with both its <code>organizationalUnits</code> and <code>accounts</code> lists empty to remove every monitored organizational unit and account. The field remains set either way — an emptied boundary is read back as a structure with two empty lists, not as an absent field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentOrganizationalProfileRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "business_overview" in value:
        out["businessOverview"] = value["business_overview"]
    if "pillars" in value:
        import capo_wellarchitected.types.pillars

        out["pillars"] = capo_wellarchitected.types.pillars.serialize_json(
            value["pillars"]
        )
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    if "organizational_aggregation_configuration" in value:
        import capo_wellarchitected.types.organizational_aggregation_configuration

        out["organizationalAggregationConfiguration"] = (
            capo_wellarchitected.types.organizational_aggregation_configuration.serialize_json(
                value["organizational_aggregation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAgentOrganizationalProfileRequest:
    out: UpdateAgentOrganizationalProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
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
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    if data.get("organizationalAggregationConfiguration") is not None:
        import capo_wellarchitected.types.organizational_aggregation_configuration

        out["organizational_aggregation_configuration"] = (
            capo_wellarchitected.types.organizational_aggregation_configuration.deserialize_json(
                data["organizationalAggregationConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdateAgentOrganizationalProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "business_overview" in value:
        out["business_overview"] = "*** Sensitive Data Redacted ***"
    return out

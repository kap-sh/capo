"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateAgentOrganizationalProfileRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.organizational_aggregation_configuration
    import capo_wellarchitected.types.pillars
    import capo_wellarchitected.types.sensitive_string
    import capo_wellarchitected.types.tags


class CreateAgentOrganizationalProfileRequest(TypedDict, closed=True):
    name: "str"
    """<p>The system name of the organizational profile.</p>"""
    display_name: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>The display name of the organizational profile shown to users.</p>"""
    description: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>A description of the organizational profile.</p>"""
    business_overview: NotRequired[
        "capo_wellarchitected.types.sensitive_string.SensitiveString"
    ]
    """<p>The business overview for this organizational profile.</p>"""
    pillars: "capo_wellarchitected.types.pillars.Pillars"
    """<p>The Amazon Web Services Well-Architected Framework pillars to associate with this organizational profile.</p>"""
    deletion_protection: NotRequired["bool"]
    """<p>Indicates whether deletion protection is enabled for the organizational profile.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    organizational_aggregation_configuration: NotRequired[
        "capo_wellarchitected.types.organizational_aggregation_configuration.OrganizationalAggregationConfiguration"
    ]
    """<p>The organizational monitoring boundary. Contains organizational unit or root entries and individual account entries that define the scope for the profile.</p>"""
    tags: NotRequired["capo_wellarchitected.types.tags.Tags"]
    """<p>The tags to associate with the organizational profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentOrganizationalProfileRequest) -> dict:
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "organizational_aggregation_configuration" in value:
        import capo_wellarchitected.types.organizational_aggregation_configuration

        out["organizationalAggregationConfiguration"] = (
            capo_wellarchitected.types.organizational_aggregation_configuration.serialize_json(
                value["organizational_aggregation_configuration"]
            )
        )
    if "tags" in value:
        import capo_wellarchitected.types.tags

        out["tags"] = capo_wellarchitected.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAgentOrganizationalProfileRequest:
    out: CreateAgentOrganizationalProfileRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("organizationalAggregationConfiguration") is not None:
        import capo_wellarchitected.types.organizational_aggregation_configuration

        out["organizational_aggregation_configuration"] = (
            capo_wellarchitected.types.organizational_aggregation_configuration.deserialize_json(
                data["organizationalAggregationConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_wellarchitected.types.tags

        out["tags"] = capo_wellarchitected.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateAgentOrganizationalProfileRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "business_overview" in value:
        out["business_overview"] = "*** Sensitive Data Redacted ***"
    return out

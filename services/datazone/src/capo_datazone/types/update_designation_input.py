"""Generated from Smithy shape ``com.amazonaws.datazone#UpdateDesignationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.cedar_designation_policy
    import capo_datazone.types.description
    import capo_datazone.types.designation_id
    import capo_datazone.types.designation_name
    import capo_datazone.types.domain_id


class UpdateDesignationInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain that contains the designation to update.</p>"""
    identifier: "capo_datazone.types.designation_id.DesignationId"
    """<p>The unique ID of the designation to update.</p>"""
    name: NotRequired["capo_datazone.types.designation_name.DesignationName"]
    """<p>The updated name of the designation. The name must be unique within the domain.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>The updated human-readable description of the designation and its intended use.</p>"""
    policy: NotRequired[
        "capo_datazone.types.cedar_designation_policy.CedarDesignationPolicy"
    ]
    """The updated Cedar permit policy."""
    deletion_protection: NotRequired["bool"]
    """Whether deletion protection is enabled for this designation. Omit to keep the existing value."""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDesignationInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "policy" in value:
        out["policy"] = value["policy"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    return out


def deserialize_json(data: dict) -> UpdateDesignationInput:
    out: UpdateDesignationInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    return out


def redact_sensitive(value: UpdateDesignationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out

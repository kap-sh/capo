"""Generated from Smithy shape ``com.amazonaws.datazone#CreateDesignationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.cedar_designation_policy
    import capo_datazone.types.description
    import capo_datazone.types.designation_name
    import capo_datazone.types.domain_id


class CreateDesignationInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon DataZone domain in which the designation is created.</p>"""
    name: "capo_datazone.types.designation_name.DesignationName"
    """<p>The name of the designation. The name must be unique within the domain.</p>"""
    description: NotRequired["capo_datazone.types.description.Description"]
    """<p>A human-readable description of the designation and its intended use.</p>"""
    policy: "capo_datazone.types.cedar_designation_policy.CedarDesignationPolicy"
    """The Cedar permit policy that defines what actions holders of this designation are allowed to perform."""
    deletion_protection: NotRequired["bool"]
    """Whether deletion protection is enabled for this designation. Defaults to true when omitted."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDesignationInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["policy"] = value["policy"]
    if "deletion_protection" in value:
        out["deletionProtection"] = value["deletion_protection"]
    return out


def deserialize_json(data: dict) -> CreateDesignationInput:
    out: CreateDesignationInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    if data.get("deletionProtection") is not None:
        out["deletion_protection"] = data["deletionProtection"]
    return out


def redact_sensitive(value: CreateDesignationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out

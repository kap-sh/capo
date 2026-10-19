"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateSecurityRequirementEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.security_requirement_name


class UpdateSecurityRequirementEntry(TypedDict, closed=True):
    name: "capo_securityagent.types.security_requirement_name.SecurityRequirementName"
    """<p>The name of the security requirement to update. This is an immutable identifier and cannot be changed once the requirement is created.</p>"""
    description: NotRequired["str"]
    """<p>The updated description of the security requirement.</p>"""
    domain: NotRequired["str"]
    """<p>The updated security domain the requirement belongs to.</p>"""
    evaluation: NotRequired["str"]
    """<p>The updated evaluation criteria used to assess compliance with this requirement.</p>"""
    remediation: NotRequired["str"]
    """<p>The updated remediation steps when the requirement is not met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSecurityRequirementEntry) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "domain" in value:
        out["domain"] = value["domain"]
    if "evaluation" in value:
        out["evaluation"] = value["evaluation"]
    if "remediation" in value:
        out["remediation"] = value["remediation"]
    return out


def deserialize_json(data: dict) -> UpdateSecurityRequirementEntry:
    out: UpdateSecurityRequirementEntry = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    if data.get("evaluation") is not None:
        out["evaluation"] = data["evaluation"]
    if data.get("remediation") is not None:
        out["remediation"] = data["remediation"]
    return out

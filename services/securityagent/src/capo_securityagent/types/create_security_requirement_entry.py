"""Generated from Smithy shape ``com.amazonaws.securityagent#CreateSecurityRequirementEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.security_requirement_name


class CreateSecurityRequirementEntry(TypedDict, closed=True):
    name: "capo_securityagent.types.security_requirement_name.SecurityRequirementName"
    """<p>The name of the security requirement.</p>"""
    description: "str"
    """<p>A description of the security requirement.</p>"""
    domain: "str"
    """<p>The security domain the requirement belongs to.</p>"""
    evaluation: "str"
    """<p>The evaluation criteria used to assess compliance with this requirement.</p>"""
    remediation: NotRequired["str"]
    """<p>The recommended remediation steps when the requirement is not met.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSecurityRequirementEntry) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["description"] = value["description"]
    out["domain"] = value["domain"]
    out["evaluation"] = value["evaluation"]
    if "remediation" in value:
        out["remediation"] = value["remediation"]
    return out


def deserialize_json(data: dict) -> CreateSecurityRequirementEntry:
    out: CreateSecurityRequirementEntry = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("domain") is not None:
        out["domain"] = data["domain"]
    else:
        out["domain"] = ""
    if data.get("evaluation") is not None:
        out["evaluation"] = data["evaluation"]
    else:
        out["evaluation"] = ""
    if data.get("remediation") is not None:
        out["remediation"] = data["remediation"]
    return out

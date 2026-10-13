"""Generated from Smithy shape ``com.amazonaws.auditmanager#FrameworkMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.assessment_framework_description
    import capo_auditmanager.types.assessment_name
    import capo_auditmanager.types.compliance_type
    import capo_auditmanager.types.filename


class FrameworkMetadata(TypedDict, closed=True):
    name: NotRequired["capo_auditmanager.types.assessment_name.AssessmentName"]
    """<p> The name of the framework. </p>"""
    description: NotRequired[
        "capo_auditmanager.types.assessment_framework_description.AssessmentFrameworkDescription"
    ]
    """<p> The description of the framework. </p>"""
    logo: NotRequired["capo_auditmanager.types.filename.Filename"]
    """<p> The logo that's associated with the framework. </p>"""
    compliance_type: NotRequired[
        "capo_auditmanager.types.compliance_type.ComplianceType"
    ]
    """<p> The compliance standard that's associated with the framework. For example, this could be PCI DSS or HIPAA. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrameworkMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "logo" in value:
        out["logo"] = value["logo"]
    if "compliance_type" in value:
        out["complianceType"] = value["compliance_type"]
    return out


def deserialize_json(data: dict) -> FrameworkMetadata:
    out: FrameworkMetadata = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("logo") is not None:
        out["logo"] = data["logo"]
    if data.get("complianceType") is not None:
        out["compliance_type"] = data["complianceType"]
    return out


def redact_sensitive(value: FrameworkMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "compliance_type" in value:
        out["compliance_type"] = "*** Sensitive Data Redacted ***"
    return out

"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentFrameworkRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.compliance_type
    import capo_auditmanager.types.framework_description
    import capo_auditmanager.types.framework_name
    import capo_auditmanager.types.update_assessment_framework_control_sets
    import capo_auditmanager.types.uuid


class UpdateAssessmentFrameworkRequest(TypedDict, closed=True):
    framework_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the framework. </p>"""
    name: "capo_auditmanager.types.framework_name.FrameworkName"
    """<p> The name of the framework to be updated. </p>"""
    description: NotRequired[
        "capo_auditmanager.types.framework_description.FrameworkDescription"
    ]
    """<p> The description of the updated framework. </p>"""
    compliance_type: NotRequired[
        "capo_auditmanager.types.compliance_type.ComplianceType"
    ]
    """<p> The compliance type that the new custom framework supports, such as CIS or HIPAA. </p>"""
    control_sets: "capo_auditmanager.types.update_assessment_framework_control_sets.UpdateAssessmentFrameworkControlSets"
    """<p> The control sets that are associated with the framework. </p> <note> <p>The <code>Controls</code> object returns a partial response when called through Framework APIs. For a complete <code>Controls</code> object, use <code>GetControl</code>.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentFrameworkRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "compliance_type" in value:
        out["complianceType"] = value["compliance_type"]
    import capo_auditmanager.types.update_assessment_framework_control_sets

    out["controlSets"] = (
        capo_auditmanager.types.update_assessment_framework_control_sets.serialize_json(
            value["control_sets"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentFrameworkRequest:
    out: UpdateAssessmentFrameworkRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("complianceType") is not None:
        out["compliance_type"] = data["complianceType"]
    if data.get("controlSets") is not None:
        import capo_auditmanager.types.update_assessment_framework_control_sets

        out["control_sets"] = (
            capo_auditmanager.types.update_assessment_framework_control_sets.deserialize_json(
                data["controlSets"]
            )
        )
    else:
        out["control_sets"] = []
    return out


def redact_sensitive(value: UpdateAssessmentFrameworkRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "compliance_type" in value:
        out["compliance_type"] = "*** Sensitive Data Redacted ***"
    return out

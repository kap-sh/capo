"""Generated from Smithy shape ``com.amazonaws.auditmanager#CreateAssessmentFrameworkRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.compliance_type
    import capo_auditmanager.types.create_assessment_framework_control_sets
    import capo_auditmanager.types.framework_description
    import capo_auditmanager.types.framework_name
    import capo_auditmanager.types.tag_map


class CreateAssessmentFrameworkRequest(TypedDict, closed=True):
    name: "capo_auditmanager.types.framework_name.FrameworkName"
    """<p> The name of the new custom framework. </p>"""
    description: NotRequired[
        "capo_auditmanager.types.framework_description.FrameworkDescription"
    ]
    """<p> An optional description for the new custom framework. </p>"""
    compliance_type: NotRequired[
        "capo_auditmanager.types.compliance_type.ComplianceType"
    ]
    """<p> The compliance type that the new custom framework supports, such as CIS or HIPAA. </p>"""
    control_sets: "capo_auditmanager.types.create_assessment_framework_control_sets.CreateAssessmentFrameworkControlSets"
    """<p> The control sets that are associated with the framework. </p> <note> <p>The <code>Controls</code> object returns a partial response when called through Framework APIs. For a complete <code>Controls</code> object, use <code>GetControl</code>.</p> </note>"""
    tags: NotRequired["capo_auditmanager.types.tag_map.TagMap"]
    """<p> The tags that are associated with the framework. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssessmentFrameworkRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "compliance_type" in value:
        out["complianceType"] = value["compliance_type"]
    import capo_auditmanager.types.create_assessment_framework_control_sets

    out["controlSets"] = (
        capo_auditmanager.types.create_assessment_framework_control_sets.serialize_json(
            value["control_sets"]
        )
    )
    if "tags" in value:
        import capo_auditmanager.types.tag_map

        out["tags"] = capo_auditmanager.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAssessmentFrameworkRequest:
    out: CreateAssessmentFrameworkRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("complianceType") is not None:
        out["compliance_type"] = data["complianceType"]
    if data.get("controlSets") is not None:
        import capo_auditmanager.types.create_assessment_framework_control_sets

        out["control_sets"] = (
            capo_auditmanager.types.create_assessment_framework_control_sets.deserialize_json(
                data["controlSets"]
            )
        )
    else:
        out["control_sets"] = []
    if data.get("tags") is not None:
        import capo_auditmanager.types.tag_map

        out["tags"] = capo_auditmanager.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateAssessmentFrameworkRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "compliance_type" in value:
        out["compliance_type"] = "*** Sensitive Data Redacted ***"
    return out

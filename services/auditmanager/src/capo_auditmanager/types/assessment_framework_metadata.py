"""Generated from Smithy shape ``com.amazonaws.auditmanager#AssessmentFrameworkMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.audit_manager_arn
    import capo_auditmanager.types.compliance_type
    import capo_auditmanager.types.control_sets_count
    import capo_auditmanager.types.controls_count
    import capo_auditmanager.types.filename
    import capo_auditmanager.types.framework_description
    import capo_auditmanager.types.framework_name
    import capo_auditmanager.types.framework_type
    import capo_auditmanager.types.timestamp
    import capo_auditmanager.types.uuid


class AssessmentFrameworkMetadata(TypedDict, closed=True):
    arn: NotRequired["capo_auditmanager.types.audit_manager_arn.AuditManagerArn"]
    """<p> The Amazon Resource Name (ARN) of the framework. </p>"""
    id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the framework. </p>"""
    type: NotRequired["capo_auditmanager.types.framework_type.FrameworkType"]
    """<p> The framework type, such as a standard framework or a custom framework. </p>"""
    name: NotRequired["capo_auditmanager.types.framework_name.FrameworkName"]
    """<p> The name of the framework. </p>"""
    description: NotRequired[
        "capo_auditmanager.types.framework_description.FrameworkDescription"
    ]
    """<p> The description of the framework. </p>"""
    logo: NotRequired["capo_auditmanager.types.filename.Filename"]
    """<p> The logo that's associated with the framework. </p>"""
    compliance_type: NotRequired[
        "capo_auditmanager.types.compliance_type.ComplianceType"
    ]
    """<p> The compliance type that the new custom framework supports, such as CIS or HIPAA. </p>"""
    controls_count: "capo_auditmanager.types.controls_count.ControlsCount"
    """<p> The number of controls that are associated with the framework. </p>"""
    control_sets_count: "capo_auditmanager.types.control_sets_count.ControlSetsCount"
    """<p> The number of control sets that are associated with the framework. </p>"""
    created_at: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the framework was created. </p>"""
    last_updated_at: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the framework was most recently updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssessmentFrameworkMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "type" in value:
        import capo_auditmanager.types.framework_type

        out["type"] = capo_auditmanager.types.framework_type.serialize_json(
            value["type"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "logo" in value:
        out["logo"] = value["logo"]
    if "compliance_type" in value:
        out["complianceType"] = value["compliance_type"]
    out["controlsCount"] = value.get("controls_count", 0)
    out["controlSetsCount"] = value.get("control_sets_count", 0)
    if "created_at" in value:
        import capo_auditmanager.types.timestamp

        out["createdAt"] = capo_auditmanager.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_auditmanager.types.timestamp

        out["lastUpdatedAt"] = capo_auditmanager.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> AssessmentFrameworkMetadata:
    out: AssessmentFrameworkMetadata = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("type") is not None:
        import capo_auditmanager.types.framework_type

        out["type"] = capo_auditmanager.types.framework_type.deserialize_json(
            data["type"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("logo") is not None:
        out["logo"] = data["logo"]
    if data.get("complianceType") is not None:
        out["compliance_type"] = data["complianceType"]
    if data.get("controlsCount") is not None:
        out["controls_count"] = data["controlsCount"]
    else:
        out["controls_count"] = 0
    if data.get("controlSetsCount") is not None:
        out["control_sets_count"] = data["controlSetsCount"]
    else:
        out["control_sets_count"] = 0
    if data.get("createdAt") is not None:
        import capo_auditmanager.types.timestamp

        out["created_at"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_auditmanager.types.timestamp

        out["last_updated_at"] = capo_auditmanager.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out


def redact_sensitive(value: AssessmentFrameworkMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "compliance_type" in value:
        out["compliance_type"] = "*** Sensitive Data Redacted ***"
    return out

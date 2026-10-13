"""Generated from Smithy shape ``com.amazonaws.auditmanager#Framework``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_auditmanager.types.audit_manager_arn
    import capo_auditmanager.types.compliance_type
    import capo_auditmanager.types.control_sets
    import capo_auditmanager.types.control_sources
    import capo_auditmanager.types.created_by
    import capo_auditmanager.types.filename
    import capo_auditmanager.types.framework_description
    import capo_auditmanager.types.framework_name
    import capo_auditmanager.types.framework_type
    import capo_auditmanager.types.last_updated_by
    import capo_auditmanager.types.tag_map
    import capo_auditmanager.types.timestamp
    import capo_auditmanager.types.uuid


class Framework(TypedDict, closed=True):
    arn: NotRequired["capo_auditmanager.types.audit_manager_arn.AuditManagerArn"]
    """<p> The Amazon Resource Name (ARN) of the framework. </p>"""
    id: NotRequired["capo_auditmanager.types.uuid.UUID"]
    """<p> The unique identifier for the framework. </p>"""
    name: NotRequired["capo_auditmanager.types.framework_name.FrameworkName"]
    """<p> The name of the framework. </p>"""
    type: NotRequired["capo_auditmanager.types.framework_type.FrameworkType"]
    """<p> Specifies whether the framework is a standard framework or a custom framework.</p>"""
    compliance_type: NotRequired[
        "capo_auditmanager.types.compliance_type.ComplianceType"
    ]
    """<p> The compliance type that the framework supports, such as CIS or HIPAA. </p>"""
    description: NotRequired[
        "capo_auditmanager.types.framework_description.FrameworkDescription"
    ]
    """<p> The description of the framework. </p>"""
    logo: NotRequired["capo_auditmanager.types.filename.Filename"]
    """<p> The logo that's associated with the framework. </p>"""
    control_sources: NotRequired[
        "capo_auditmanager.types.control_sources.ControlSources"
    ]
    """<p> The control data sources where Audit Manager collects evidence from.</p> <important> <p>This API parameter is no longer supported.</p> </important>"""
    control_sets: NotRequired["capo_auditmanager.types.control_sets.ControlSets"]
    """<p> The control sets that are associated with the framework. </p> <note> <p>The <code>Controls</code> object returns a partial response when called through Framework APIs. For a complete <code>Controls</code> object, use <code>GetControl</code>.</p> </note>"""
    created_at: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the framework was created. </p>"""
    last_updated_at: NotRequired["capo_auditmanager.types.timestamp.Timestamp"]
    """<p> The time when the framework was most recently updated. </p>"""
    created_by: NotRequired["capo_auditmanager.types.created_by.CreatedBy"]
    """<p> The user or role that created the framework. </p>"""
    last_updated_by: NotRequired[
        "capo_auditmanager.types.last_updated_by.LastUpdatedBy"
    ]
    """<p> The user or role that most recently updated the framework. </p>"""
    tags: NotRequired["capo_auditmanager.types.tag_map.TagMap"]
    """<p> The tags that are associated with the framework. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Framework) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "type" in value:
        import capo_auditmanager.types.framework_type

        out["type"] = capo_auditmanager.types.framework_type.serialize_json(
            value["type"]
        )
    if "compliance_type" in value:
        out["complianceType"] = value["compliance_type"]
    if "description" in value:
        out["description"] = value["description"]
    if "logo" in value:
        out["logo"] = value["logo"]
    if "control_sources" in value:
        out["controlSources"] = value["control_sources"]
    if "control_sets" in value:
        import capo_auditmanager.types.control_sets

        out["controlSets"] = capo_auditmanager.types.control_sets.serialize_json(
            value["control_sets"]
        )
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
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "last_updated_by" in value:
        out["lastUpdatedBy"] = value["last_updated_by"]
    if "tags" in value:
        import capo_auditmanager.types.tag_map

        out["tags"] = capo_auditmanager.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> Framework:
    out: Framework = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("type") is not None:
        import capo_auditmanager.types.framework_type

        out["type"] = capo_auditmanager.types.framework_type.deserialize_json(
            data["type"]
        )
    if data.get("complianceType") is not None:
        out["compliance_type"] = data["complianceType"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("logo") is not None:
        out["logo"] = data["logo"]
    if data.get("controlSources") is not None:
        out["control_sources"] = data["controlSources"]
    if data.get("controlSets") is not None:
        import capo_auditmanager.types.control_sets

        out["control_sets"] = capo_auditmanager.types.control_sets.deserialize_json(
            data["controlSets"]
        )
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
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("lastUpdatedBy") is not None:
        out["last_updated_by"] = data["lastUpdatedBy"]
    if data.get("tags") is not None:
        import capo_auditmanager.types.tag_map

        out["tags"] = capo_auditmanager.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: Framework) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "compliance_type" in value:
        out["compliance_type"] = "*** Sensitive Data Redacted ***"
    if "control_sets" in value:
        out["control_sets"] = "*** Sensitive Data Redacted ***"
    if "created_by" in value:
        out["created_by"] = "*** Sensitive Data Redacted ***"
    if "last_updated_by" in value:
        out["last_updated_by"] = "*** Sensitive Data Redacted ***"
    return out

"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#TemplateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.date_timestamp
    import capo_network_security_manager.types.entity_status
    import capo_network_security_manager.types.entity_version
    import capo_network_security_manager.types.has_published_version
    import capo_network_security_manager.types.template_arn
    import capo_network_security_manager.types.template_firewall_type
    import capo_network_security_manager.types.template_id
    import capo_network_security_manager.types.template_name


class TemplateSummary(TypedDict, closed=True):
    template_id: "capo_network_security_manager.types.template_id.TemplateId"
    """<p>The service-generated id of the template.</p>"""
    template_arn: "capo_network_security_manager.types.template_arn.TemplateArn"
    """<p>The Amazon Resource Name (ARN) of the template.</p>"""
    template_name: "capo_network_security_manager.types.template_name.TemplateName"
    """<p>The name of the template.</p>"""
    status: NotRequired[
        "capo_network_security_manager.types.entity_status.EntityStatus"
    ]
    """<p>The current status of the resource: <code>DRAFT</code> (unpublished, editable) or <code>ACTIVE</code> (published, in use).</p>"""
    version: NotRequired[
        "capo_network_security_manager.types.entity_version.EntityVersion"
    ]
    """<p>The version of the resource.</p>"""
    has_published_version: NotRequired[
        "capo_network_security_manager.types.has_published_version.HasPublishedVersion"
    ]
    """<p>Specifies whether a published version of the resource exists.</p>"""
    firewall_type: NotRequired[
        "capo_network_security_manager.types.template_firewall_type.TemplateFirewallType"
    ]
    """<p>The firewall type associated with the resource.</p>"""
    updated_at: NotRequired[
        "capo_network_security_manager.types.date_timestamp.DateTimestamp"
    ]
    """<p>The time when the resource was last updated. For a snapshot, this is the time when the snapshot was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSummary) -> dict:
    out: dict = {}
    out["templateId"] = value["template_id"]
    out["templateArn"] = value["template_arn"]
    out["templateName"] = value["template_name"]
    if "status" in value:
        import capo_network_security_manager.types.entity_status

        out["status"] = (
            capo_network_security_manager.types.entity_status.serialize_json(
                value["status"]
            )
        )
    if "version" in value:
        out["version"] = value["version"]
    if "has_published_version" in value:
        out["hasPublishedVersion"] = value["has_published_version"]
    if "firewall_type" in value:
        import capo_network_security_manager.types.template_firewall_type

        out["firewallType"] = (
            capo_network_security_manager.types.template_firewall_type.serialize_json(
                value["firewall_type"]
            )
        )
    if "updated_at" in value:
        import capo_network_security_manager.types.date_timestamp

        out["updatedAt"] = (
            capo_network_security_manager.types.date_timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> TemplateSummary:
    out: TemplateSummary = {}  # type: ignore[typeddict-item]
    if data.get("templateId") is not None:
        out["template_id"] = data["templateId"]
    else:
        raise DeserializationError("TemplateSummary.template_id required")
    if data.get("templateArn") is not None:
        out["template_arn"] = data["templateArn"]
    else:
        raise DeserializationError("TemplateSummary.template_arn required")
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("TemplateSummary.template_name required")
    if data.get("status") is not None:
        import capo_network_security_manager.types.entity_status

        out["status"] = (
            capo_network_security_manager.types.entity_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("hasPublishedVersion") is not None:
        out["has_published_version"] = data["hasPublishedVersion"]
    if data.get("firewallType") is not None:
        import capo_network_security_manager.types.template_firewall_type

        out["firewall_type"] = (
            capo_network_security_manager.types.template_firewall_type.deserialize_json(
                data["firewallType"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_network_security_manager.types.date_timestamp

        out["updated_at"] = (
            capo_network_security_manager.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#CreateTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.associated_rule_list
    import capo_network_security_manager.types.date_timestamp
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.entity_status
    import capo_network_security_manager.types.entity_version
    import capo_network_security_manager.types.has_published_version
    import capo_network_security_manager.types.is_snapshot
    import capo_network_security_manager.types.template_arn
    import capo_network_security_manager.types.template_firewall_type
    import capo_network_security_manager.types.template_id
    import capo_network_security_manager.types.template_name
    import capo_network_security_manager.types.update_token


class CreateTemplateOutput(TypedDict, closed=True):
    template_id: "capo_network_security_manager.types.template_id.TemplateId"
    """<p>The service-generated id of the template.</p>"""
    template_arn: "capo_network_security_manager.types.template_arn.TemplateArn"
    """<p>The Amazon Resource Name (ARN) of the template.</p>"""
    template_name: "capo_network_security_manager.types.template_name.TemplateName"
    """<p>The name of the template.</p>"""
    template_description: NotRequired[
        "capo_network_security_manager.types.description.Description"
    ]
    """<p>A description of the template.</p>"""
    status: "capo_network_security_manager.types.entity_status.EntityStatus"
    """<p>The current status of the resource: <code>DRAFT</code> (unpublished, editable) or <code>ACTIVE</code> (published, in use).</p>"""
    version: "capo_network_security_manager.types.entity_version.EntityVersion"
    """<p>The version of the resource.</p>"""
    associated_rule_list: (
        "capo_network_security_manager.types.associated_rule_list.AssociatedRuleList"
    )
    """<p>The rules associated with the template.</p>"""
    update_token: NotRequired[
        "capo_network_security_manager.types.update_token.UpdateToken"
    ]
    """<p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>"""
    is_snapshot: NotRequired[
        "capo_network_security_manager.types.is_snapshot.IsSnapshot"
    ]
    """<p>Specifies whether the resource is a snapshot of a published version.</p>"""
    has_published_version: NotRequired[
        "capo_network_security_manager.types.has_published_version.HasPublishedVersion"
    ]
    """<p>Specifies whether a published version of the resource exists.</p>"""
    firewall_type: "capo_network_security_manager.types.template_firewall_type.TemplateFirewallType"
    """<p>The firewall type associated with the resource.</p>"""
    updated_at: NotRequired[
        "capo_network_security_manager.types.date_timestamp.DateTimestamp"
    ]
    """<p>The time when the resource was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateOutput) -> dict:
    out: dict = {}
    out["templateId"] = value["template_id"]
    out["templateArn"] = value["template_arn"]
    out["templateName"] = value["template_name"]
    if "template_description" in value:
        out["templateDescription"] = value["template_description"]
    import capo_network_security_manager.types.entity_status

    out["status"] = capo_network_security_manager.types.entity_status.serialize_json(
        value["status"]
    )
    out["version"] = value["version"]
    import capo_network_security_manager.types.associated_rule_list

    out["associatedRuleList"] = (
        capo_network_security_manager.types.associated_rule_list.serialize_json(
            value["associated_rule_list"]
        )
    )
    if "update_token" in value:
        out["updateToken"] = value["update_token"]
    if "is_snapshot" in value:
        out["isSnapshot"] = value["is_snapshot"]
    if "has_published_version" in value:
        out["hasPublishedVersion"] = value["has_published_version"]
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


def deserialize_json(data: dict) -> CreateTemplateOutput:
    out: CreateTemplateOutput = {}  # type: ignore[typeddict-item]
    if data.get("templateId") is not None:
        out["template_id"] = data["templateId"]
    else:
        raise DeserializationError("CreateTemplateOutput.template_id required")
    if data.get("templateArn") is not None:
        out["template_arn"] = data["templateArn"]
    else:
        raise DeserializationError("CreateTemplateOutput.template_arn required")
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("CreateTemplateOutput.template_name required")
    if data.get("templateDescription") is not None:
        out["template_description"] = data["templateDescription"]
    if data.get("status") is not None:
        import capo_network_security_manager.types.entity_status

        out["status"] = (
            capo_network_security_manager.types.entity_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateTemplateOutput.status required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CreateTemplateOutput.version required")
    if data.get("associatedRuleList") is not None:
        import capo_network_security_manager.types.associated_rule_list

        out["associated_rule_list"] = (
            capo_network_security_manager.types.associated_rule_list.deserialize_json(
                data["associatedRuleList"]
            )
        )
    else:
        raise DeserializationError("CreateTemplateOutput.associated_rule_list required")
    if data.get("updateToken") is not None:
        out["update_token"] = data["updateToken"]
    if data.get("isSnapshot") is not None:
        out["is_snapshot"] = data["isSnapshot"]
    if data.get("hasPublishedVersion") is not None:
        out["has_published_version"] = data["hasPublishedVersion"]
    if data.get("firewallType") is not None:
        import capo_network_security_manager.types.template_firewall_type

        out["firewall_type"] = (
            capo_network_security_manager.types.template_firewall_type.deserialize_json(
                data["firewallType"]
            )
        )
    else:
        raise DeserializationError("CreateTemplateOutput.firewall_type required")
    if data.get("updatedAt") is not None:
        import capo_network_security_manager.types.date_timestamp

        out["updated_at"] = (
            capo_network_security_manager.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out

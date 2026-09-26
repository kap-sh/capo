"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#CreateTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.rule_reference_list
    import capo_network_security_manager.types.tag_map
    import capo_network_security_manager.types.template_firewall_type
    import capo_network_security_manager.types.template_name


class CreateTemplateInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>"""
    template_name: "capo_network_security_manager.types.template_name.TemplateName"
    """<p>The name of the template.</p>"""
    template_description: NotRequired[
        "capo_network_security_manager.types.description.Description"
    ]
    """<p>A description of the template.</p>"""
    associated_rule_list: (
        "capo_network_security_manager.types.rule_reference_list.RuleReferenceList"
    )
    """<p>The rules associated with the template.</p>"""
    firewall_type: "capo_network_security_manager.types.template_firewall_type.TemplateFirewallType"
    """<p>The firewall type associated with the resource.</p>"""
    is_published: "capo_network_security_manager.types.is_published.IsPublished"
    """<p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>). Default: <code>true</code>.</p>"""
    tags: NotRequired["capo_network_security_manager.types.tag_map.TagMap"]
    """<p>The tags to add to the resource when it is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["templateName"] = value["template_name"]
    if "template_description" in value:
        out["templateDescription"] = value["template_description"]
    import capo_network_security_manager.types.rule_reference_list

    out["associatedRuleList"] = (
        capo_network_security_manager.types.rule_reference_list.serialize_json(
            value["associated_rule_list"]
        )
    )
    import capo_network_security_manager.types.template_firewall_type

    out["firewallType"] = (
        capo_network_security_manager.types.template_firewall_type.serialize_json(
            value["firewall_type"]
        )
    )
    out["isPublished"] = value.get("is_published", True)
    if "tags" in value:
        import capo_network_security_manager.types.tag_map

        out["tags"] = capo_network_security_manager.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateTemplateInput:
    out: CreateTemplateInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("CreateTemplateInput.template_name required")
    if data.get("templateDescription") is not None:
        out["template_description"] = data["templateDescription"]
    if data.get("associatedRuleList") is not None:
        import capo_network_security_manager.types.rule_reference_list

        out["associated_rule_list"] = (
            capo_network_security_manager.types.rule_reference_list.deserialize_json(
                data["associatedRuleList"]
            )
        )
    else:
        raise DeserializationError("CreateTemplateInput.associated_rule_list required")
    if data.get("firewallType") is not None:
        import capo_network_security_manager.types.template_firewall_type

        out["firewall_type"] = (
            capo_network_security_manager.types.template_firewall_type.deserialize_json(
                data["firewallType"]
            )
        )
    else:
        raise DeserializationError("CreateTemplateInput.firewall_type required")
    if data.get("isPublished") is not None:
        out["is_published"] = data["isPublished"]
    else:
        out["is_published"] = True
    if data.get("tags") is not None:
        import capo_network_security_manager.types.tag_map

        out["tags"] = capo_network_security_manager.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#UpdateTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.rule_reference_list
    import capo_network_security_manager.types.template_identifier
    import capo_network_security_manager.types.update_token


class UpdateTemplateInput(TypedDict, closed=True):
    template_identifier: (
        "capo_network_security_manager.types.template_identifier.TemplateIdentifier"
    )
    """<p>The identifier of the template. This is the template's Amazon Resource Name (ARN).</p>"""
    update_token: "capo_network_security_manager.types.update_token.UpdateToken"
    """<p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>"""
    template_description: NotRequired[
        "capo_network_security_manager.types.description.Description"
    ]
    """<p>A description of the template.</p>"""
    associated_rule_list: NotRequired[
        "capo_network_security_manager.types.rule_reference_list.RuleReferenceList"
    ]
    """<p>The rules associated with the template.</p>"""
    is_published: "capo_network_security_manager.types.is_published.IsPublished"
    """<p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>).</p>"""
    client_token: NotRequired[
        "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTemplateInput) -> dict:
    out: dict = {}
    out["updateToken"] = value["update_token"]
    if "template_description" in value:
        out["templateDescription"] = value["template_description"]
    if "associated_rule_list" in value:
        import capo_network_security_manager.types.rule_reference_list

        out["associatedRuleList"] = (
            capo_network_security_manager.types.rule_reference_list.serialize_json(
                value["associated_rule_list"]
            )
        )
    out["isPublished"] = value["is_published"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateTemplateInput:
    out: UpdateTemplateInput = {}  # type: ignore[typeddict-item]
    if data.get("updateToken") is not None:
        out["update_token"] = data["updateToken"]
    else:
        raise DeserializationError("UpdateTemplateInput.update_token required")
    if data.get("templateDescription") is not None:
        out["template_description"] = data["templateDescription"]
    if data.get("associatedRuleList") is not None:
        import capo_network_security_manager.types.rule_reference_list

        out["associated_rule_list"] = (
            capo_network_security_manager.types.rule_reference_list.deserialize_json(
                data["associatedRuleList"]
            )
        )
    if data.get("isPublished") is not None:
        out["is_published"] = data["isPublished"]
    else:
        raise DeserializationError("UpdateTemplateInput.is_published required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out

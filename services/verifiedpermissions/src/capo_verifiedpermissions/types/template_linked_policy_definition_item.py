"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#TemplateLinkedPolicyDefinitionItem``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.entity_identifier
    import capo_verifiedpermissions.types.policy_template_id


class TemplateLinkedPolicyDefinitionItem(TypedDict, closed=True):
    policy_template_id: (
        "capo_verifiedpermissions.types.policy_template_id.PolicyTemplateId"
    )
    """<p>The unique identifier of the policy template used to create this policy.</p>"""
    principal: NotRequired[
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>The principal associated with this template-linked policy. Verified Permissions substitutes this principal for the <code>?principal</code> placeholder in the policy template when it evaluates an authorization request.</p>"""
    resource: NotRequired[
        "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"
    ]
    """<p>The resource associated with this template-linked policy. Verified Permissions substitutes this resource for the <code>?resource</code> placeholder in the policy template when it evaluates an authorization request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TemplateLinkedPolicyDefinitionItem) -> dict:
    out: dict = {}
    out["policyTemplateId"] = value["policy_template_id"]
    if "principal" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["principal"]
            )
        )
    if "resource" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["resource"] = (
            capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["resource"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TemplateLinkedPolicyDefinitionItem:
    out: TemplateLinkedPolicyDefinitionItem = {}  # type: ignore[typeddict-item]
    if data.get("policyTemplateId") is not None:
        out["policy_template_id"] = data["policyTemplateId"]
    else:
        out["policy_template_id"] = ""
    if data.get("principal") is not None:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["principal"]
            )
        )
    if data.get("resource") is not None:
        import capo_verifiedpermissions.types.entity_identifier

        out["resource"] = (
            capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["resource"]
            )
        )
    return out


def redact_sensitive(value: TemplateLinkedPolicyDefinitionItem) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "principal" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["principal"] = (
            capo_verifiedpermissions.types.entity_identifier.redact_sensitive(
                value["principal"]
            )
        )
    if "resource" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["resource"] = (
            capo_verifiedpermissions.types.entity_identifier.redact_sensitive(
                value["resource"]
            )
        )
    return out

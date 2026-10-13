"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#PolicyFilter``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.entity_reference
    import capo_verifiedpermissions.types.policy_template_id
    import capo_verifiedpermissions.types.policy_type


class PolicyFilter(TypedDict, closed=True):
    principal: NotRequired[
        "capo_verifiedpermissions.types.entity_reference.EntityReference"
    ]
    """<p>Filters the output to only policies that reference the specified principal.</p>"""
    resource: NotRequired[
        "capo_verifiedpermissions.types.entity_reference.EntityReference"
    ]
    """<p>Filters the output to only policies that reference the specified resource.</p>"""
    policy_type: NotRequired["capo_verifiedpermissions.types.policy_type.PolicyType"]
    """<p>Filters the output to only policies of the specified type.</p>"""
    policy_template_id: NotRequired[
        "capo_verifiedpermissions.types.policy_template_id.PolicyTemplateId"
    ]
    """<p>Filters the output to only template-linked policies that were instantiated from the specified policy template.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PolicyFilter) -> dict:
    out: dict = {}
    if "principal" in value:
        import capo_verifiedpermissions.types.entity_reference

        out["principal"] = (
            capo_verifiedpermissions.types.entity_reference.serialize_aws_json_1_0(
                value["principal"]
            )
        )
    if "resource" in value:
        import capo_verifiedpermissions.types.entity_reference

        out["resource"] = (
            capo_verifiedpermissions.types.entity_reference.serialize_aws_json_1_0(
                value["resource"]
            )
        )
    if "policy_type" in value:
        import capo_verifiedpermissions.types.policy_type

        out["policyType"] = (
            capo_verifiedpermissions.types.policy_type.serialize_aws_json_1_0(
                value["policy_type"]
            )
        )
    if "policy_template_id" in value:
        out["policyTemplateId"] = value["policy_template_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PolicyFilter:
    out: PolicyFilter = {}  # type: ignore[typeddict-item]
    if data.get("principal") is not None:
        import capo_verifiedpermissions.types.entity_reference

        out["principal"] = (
            capo_verifiedpermissions.types.entity_reference.deserialize_aws_json_1_0(
                data["principal"]
            )
        )
    if data.get("resource") is not None:
        import capo_verifiedpermissions.types.entity_reference

        out["resource"] = (
            capo_verifiedpermissions.types.entity_reference.deserialize_aws_json_1_0(
                data["resource"]
            )
        )
    if data.get("policyType") is not None:
        import capo_verifiedpermissions.types.policy_type

        out["policy_type"] = (
            capo_verifiedpermissions.types.policy_type.deserialize_aws_json_1_0(
                data["policyType"]
            )
        )
    if data.get("policyTemplateId") is not None:
        out["policy_template_id"] = data["policyTemplateId"]
    return out


def redact_sensitive(value: PolicyFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "principal" in value:
        import capo_verifiedpermissions.types.entity_reference

        out["principal"] = (
            capo_verifiedpermissions.types.entity_reference.redact_sensitive(
                value["principal"]
            )
        )
    if "resource" in value:
        import capo_verifiedpermissions.types.entity_reference

        out["resource"] = (
            capo_verifiedpermissions.types.entity_reference.redact_sensitive(
                value["resource"]
            )
        )
    return out

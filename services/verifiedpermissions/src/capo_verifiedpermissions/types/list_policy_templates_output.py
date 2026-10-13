"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ListPolicyTemplatesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.next_token
    import capo_verifiedpermissions.types.policy_templates_list


class ListPolicyTemplatesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_verifiedpermissions.types.next_token.NextToken"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""
    policy_templates: (
        "capo_verifiedpermissions.types.policy_templates_list.PolicyTemplatesList"
    )
    """<p>The list of the policy templates in the specified policy store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPolicyTemplatesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_verifiedpermissions.types.policy_templates_list

    out["policyTemplates"] = (
        capo_verifiedpermissions.types.policy_templates_list.serialize_aws_json_1_0(
            value["policy_templates"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPolicyTemplatesOutput:
    out: ListPolicyTemplatesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("policyTemplates") is not None:
        import capo_verifiedpermissions.types.policy_templates_list

        out["policy_templates"] = (
            capo_verifiedpermissions.types.policy_templates_list.deserialize_aws_json_1_0(
                data["policyTemplates"]
            )
        )
    else:
        raise DeserializationError(
            "ListPolicyTemplatesOutput.policy_templates required"
        )
    return out


def redact_sensitive(value: ListPolicyTemplatesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy_templates" in value:
        import capo_verifiedpermissions.types.policy_templates_list

        out["policy_templates"] = (
            capo_verifiedpermissions.types.policy_templates_list.redact_sensitive(
                value["policy_templates"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ListPoliciesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.next_token
    import capo_verifiedpermissions.types.policy_list


class ListPoliciesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_verifiedpermissions.types.next_token.NextToken"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""
    policies: "capo_verifiedpermissions.types.policy_list.PolicyList"
    """<p>Lists all policies that are available in the specified policy store.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPoliciesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_verifiedpermissions.types.policy_list

    out["policies"] = capo_verifiedpermissions.types.policy_list.serialize_aws_json_1_0(
        value["policies"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPoliciesOutput:
    out: ListPoliciesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("policies") is not None:
        import capo_verifiedpermissions.types.policy_list

        out["policies"] = (
            capo_verifiedpermissions.types.policy_list.deserialize_aws_json_1_0(
                data["policies"]
            )
        )
    else:
        out["policies"] = []
    return out


def redact_sensitive(value: ListPoliciesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policies" in value:
        import capo_verifiedpermissions.types.policy_list

        out["policies"] = capo_verifiedpermissions.types.policy_list.redact_sensitive(
            value["policies"]
        )
    return out

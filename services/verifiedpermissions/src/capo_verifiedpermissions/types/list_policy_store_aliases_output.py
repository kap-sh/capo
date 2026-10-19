"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ListPolicyStoreAliasesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.next_token
    import capo_verifiedpermissions.types.policy_store_alias_list


class ListPolicyStoreAliasesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_verifiedpermissions.types.next_token.NextToken"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""
    policy_store_aliases: (
        "capo_verifiedpermissions.types.policy_store_alias_list.PolicyStoreAliasList"
    )
    """<p>The list of policy store aliases in the account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPolicyStoreAliasesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_verifiedpermissions.types.policy_store_alias_list

    out["policyStoreAliases"] = (
        capo_verifiedpermissions.types.policy_store_alias_list.serialize_aws_json_1_0(
            value["policy_store_aliases"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPolicyStoreAliasesOutput:
    out: ListPolicyStoreAliasesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("policyStoreAliases") is not None:
        import capo_verifiedpermissions.types.policy_store_alias_list

        out["policy_store_aliases"] = (
            capo_verifiedpermissions.types.policy_store_alias_list.deserialize_aws_json_1_0(
                data["policyStoreAliases"]
            )
        )
    else:
        out["policy_store_aliases"] = []
    return out

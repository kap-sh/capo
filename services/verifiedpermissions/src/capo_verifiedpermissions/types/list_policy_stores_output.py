"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#ListPolicyStoresOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.next_token
    import capo_verifiedpermissions.types.policy_store_list


class ListPolicyStoresOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_verifiedpermissions.types.next_token.NextToken"]
    """<p>If present, this value indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. This indicates that this is the last page of results.</p>"""
    policy_stores: "capo_verifiedpermissions.types.policy_store_list.PolicyStoreList"
    """<p>The list of policy stores in the account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPolicyStoresOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_verifiedpermissions.types.policy_store_list

    out["policyStores"] = (
        capo_verifiedpermissions.types.policy_store_list.serialize_aws_json_1_0(
            value["policy_stores"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPolicyStoresOutput:
    out: ListPolicyStoresOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("policyStores") is not None:
        import capo_verifiedpermissions.types.policy_store_list

        out["policy_stores"] = (
            capo_verifiedpermissions.types.policy_store_list.deserialize_aws_json_1_0(
                data["policyStores"]
            )
        )
    else:
        raise DeserializationError("ListPolicyStoresOutput.policy_stores required")
    return out


def redact_sensitive(value: ListPolicyStoresOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "policy_stores" in value:
        import capo_verifiedpermissions.types.policy_store_list

        out["policy_stores"] = (
            capo_verifiedpermissions.types.policy_store_list.redact_sensitive(
                value["policy_stores"]
            )
        )
    return out

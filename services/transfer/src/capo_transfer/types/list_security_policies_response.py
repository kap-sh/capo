"""Generated from Smithy shape ``com.amazonaws.transfer#ListSecurityPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.next_token
    import capo_transfer.types.security_policy_names


class ListSecurityPoliciesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_transfer.types.next_token.NextToken"]
    """<p>When you can get additional results from the <code>ListSecurityPolicies</code> operation, a <code>NextToken</code> parameter is returned in the output. In a following command, you can pass in the <code>NextToken</code> parameter to continue listing security policies.</p>"""
    security_policy_names: (
        "capo_transfer.types.security_policy_names.SecurityPolicyNames"
    )
    """<p>An array of security policies that were listed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSecurityPoliciesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_transfer.types.security_policy_names

    out["SecurityPolicyNames"] = (
        capo_transfer.types.security_policy_names.serialize_aws_json_1_1(
            value["security_policy_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSecurityPoliciesResponse:
    out: ListSecurityPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("SecurityPolicyNames") is not None:
        import capo_transfer.types.security_policy_names

        out["security_policy_names"] = (
            capo_transfer.types.security_policy_names.deserialize_aws_json_1_1(
                data["SecurityPolicyNames"]
            )
        )
    else:
        out["security_policy_names"] = []
    return out

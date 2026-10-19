"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateFirewallPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall_policy_response
    import capo_network_firewall.types.update_token


class CreateFirewallPolicyResponse(TypedDict, closed=True):
    update_token: "capo_network_firewall.types.update_token.UpdateToken"
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the firewall policy. The token marks the state of the policy resource at the time of the request. </p> <p>To make changes to the policy, you provide the token in your request. Network Firewall uses the token to ensure that the policy hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the firewall policy again to get a current copy of it with current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""
    firewall_policy_response: (
        "capo_network_firewall.types.firewall_policy_response.FirewallPolicyResponse"
    )
    """<p>The high-level properties of a firewall policy. This, along with the <a>FirewallPolicy</a>, define the policy. You can retrieve all objects for a firewall policy by calling <a>DescribeFirewallPolicy</a>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateFirewallPolicyResponse) -> dict:
    out: dict = {}
    out["UpdateToken"] = value["update_token"]
    import capo_network_firewall.types.firewall_policy_response

    out["FirewallPolicyResponse"] = (
        capo_network_firewall.types.firewall_policy_response.serialize_aws_json_1_0(
            value["firewall_policy_response"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateFirewallPolicyResponse:
    out: CreateFirewallPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    else:
        out["update_token"] = ""
    if data.get("FirewallPolicyResponse") is not None:
        import capo_network_firewall.types.firewall_policy_response

        out["firewall_policy_response"] = (
            capo_network_firewall.types.firewall_policy_response.deserialize_aws_json_1_0(
                data["FirewallPolicyResponse"]
            )
        )
    else:
        raise DeserializationError(
            "CreateFirewallPolicyResponse.firewall_policy_response required"
        )
    return out

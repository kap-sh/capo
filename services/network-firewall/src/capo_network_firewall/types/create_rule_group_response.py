"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateRuleGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.rule_group_response
    import capo_network_firewall.types.update_token


class CreateRuleGroupResponse(TypedDict, closed=True):
    update_token: "capo_network_firewall.types.update_token.UpdateToken"
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the rule group. The token marks the state of the rule group resource at the time of the request. </p> <p>To make changes to the rule group, you provide the token in your request. Network Firewall uses the token to ensure that the rule group hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""
    rule_group_response: (
        "capo_network_firewall.types.rule_group_response.RuleGroupResponse"
    )
    """<p>The high-level properties of a rule group. This, along with the <a>RuleGroup</a>, define the rule group. You can retrieve all objects for a rule group by calling <a>DescribeRuleGroup</a>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRuleGroupResponse) -> dict:
    out: dict = {}
    out["UpdateToken"] = value["update_token"]
    import capo_network_firewall.types.rule_group_response

    out["RuleGroupResponse"] = (
        capo_network_firewall.types.rule_group_response.serialize_aws_json_1_0(
            value["rule_group_response"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRuleGroupResponse:
    out: CreateRuleGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    else:
        out["update_token"] = ""
    if data.get("RuleGroupResponse") is not None:
        import capo_network_firewall.types.rule_group_response

        out["rule_group_response"] = (
            capo_network_firewall.types.rule_group_response.deserialize_aws_json_1_0(
                data["RuleGroupResponse"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRuleGroupResponse.rule_group_response required"
        )
    return out

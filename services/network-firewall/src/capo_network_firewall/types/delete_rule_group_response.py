"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteRuleGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.rule_group_response


class DeleteRuleGroupResponse(TypedDict, closed=True):
    rule_group_response: (
        "capo_network_firewall.types.rule_group_response.RuleGroupResponse"
    )
    """<p>The high-level properties of a rule group. This, along with the <a>RuleGroup</a>, define the rule group. You can retrieve all objects for a rule group by calling <a>DescribeRuleGroup</a>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRuleGroupResponse) -> dict:
    out: dict = {}
    import capo_network_firewall.types.rule_group_response

    out["RuleGroupResponse"] = (
        capo_network_firewall.types.rule_group_response.serialize_aws_json_1_0(
            value["rule_group_response"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRuleGroupResponse:
    out: DeleteRuleGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("RuleGroupResponse") is not None:
        import capo_network_firewall.types.rule_group_response

        out["rule_group_response"] = (
            capo_network_firewall.types.rule_group_response.deserialize_aws_json_1_0(
                data["RuleGroupResponse"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteRuleGroupResponse.rule_group_response required"
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteRuleGroupResponse) -> dict:
    out: dict = {}
    import capo_network_firewall.types.rule_group_response

    out["RuleGroupResponse"] = (
        capo_network_firewall.types.rule_group_response.serialize_cbor(
            value["rule_group_response"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> DeleteRuleGroupResponse:
    out: DeleteRuleGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("RuleGroupResponse") is not None:
        import capo_network_firewall.types.rule_group_response

        out["rule_group_response"] = (
            capo_network_firewall.types.rule_group_response.deserialize_cbor(
                data["RuleGroupResponse"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteRuleGroupResponse.rule_group_response required"
        )
    return out

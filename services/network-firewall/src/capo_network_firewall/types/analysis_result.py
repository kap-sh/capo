"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AnalysisResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.collection_member_string
    import capo_network_firewall.types.identified_type
    import capo_network_firewall.types.rule_id_list


class AnalysisResult(TypedDict, closed=True):
    identified_rule_ids: NotRequired[
        "capo_network_firewall.types.rule_id_list.RuleIdList"
    ]
    """<p>The priority number of the stateless rules identified in the analysis.</p>"""
    identified_type: NotRequired[
        "capo_network_firewall.types.identified_type.IdentifiedType"
    ]
    """<p>The types of rule configurations that Network Firewall analyzes your rule groups for. Network Firewall analyzes stateless rule groups for the following types of rule configurations:</p> <ul> <li> <p> <code>STATELESS_RULE_FORWARDING_ASYMMETRICALLY</code> </p> <p>Cause: One or more stateless rules with the action <code>pass</code> or <code>forward</code> are forwarding traffic asymmetrically. Specifically, the rule's set of source IP addresses or their associated port numbers, don't match the set of destination IP addresses or their associated port numbers.</p> <p>To mitigate: Make sure that there's an existing return path. For example, if the rule allows traffic from source 10.1.0.0/24 to destination 20.1.0.0/24, you should allow return traffic from source 20.1.0.0/24 to destination 10.1.0.0/24.</p> </li> <li> <p> <code>STATELESS_RULE_CONTAINS_TCP_FLAGS</code> </p> <p>Cause: At least one stateless rule with the action <code>pass</code> or<code>forward</code> contains TCP flags that are inconsistent in the forward and return directions.</p> <p>To mitigate: Prevent asymmetric routing issues caused by TCP flags by following these actions:</p> <ul> <li> <p>Remove unnecessary TCP flag inspections from the rules.</p> </li> <li> <p>If you need to inspect TCP flags, check that the rules correctly account for changes in TCP flags throughout the TCP connection cycle, for example <code>SYN</code> and <code>ACK</code> flags used in a 3-way TCP handshake.</p> </li> </ul> </li> </ul>"""
    analysis_detail: NotRequired[
        "capo_network_firewall.types.collection_member_string.CollectionMember_String"
    ]
    """<p>Provides analysis details for the identified rule.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AnalysisResult) -> dict:
    out: dict = {}
    if "identified_rule_ids" in value:
        import capo_network_firewall.types.rule_id_list

        out["IdentifiedRuleIds"] = (
            capo_network_firewall.types.rule_id_list.serialize_aws_json_1_0(
                value["identified_rule_ids"]
            )
        )
    if "identified_type" in value:
        import capo_network_firewall.types.identified_type

        out["IdentifiedType"] = (
            capo_network_firewall.types.identified_type.serialize_aws_json_1_0(
                value["identified_type"]
            )
        )
    if "analysis_detail" in value:
        out["AnalysisDetail"] = value["analysis_detail"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AnalysisResult:
    out: AnalysisResult = {}  # type: ignore[typeddict-item]
    if data.get("IdentifiedRuleIds") is not None:
        import capo_network_firewall.types.rule_id_list

        out["identified_rule_ids"] = (
            capo_network_firewall.types.rule_id_list.deserialize_aws_json_1_0(
                data["IdentifiedRuleIds"]
            )
        )
    if data.get("IdentifiedType") is not None:
        import capo_network_firewall.types.identified_type

        out["identified_type"] = (
            capo_network_firewall.types.identified_type.deserialize_aws_json_1_0(
                data["IdentifiedType"]
            )
        )
    if data.get("AnalysisDetail") is not None:
        out["analysis_detail"] = data["AnalysisDetail"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AnalysisResult) -> dict:
    out: dict = {}
    if "identified_rule_ids" in value:
        import capo_network_firewall.types.rule_id_list

        out["IdentifiedRuleIds"] = (
            capo_network_firewall.types.rule_id_list.serialize_cbor(
                value["identified_rule_ids"]
            )
        )
    if "identified_type" in value:
        import capo_network_firewall.types.identified_type

        out["IdentifiedType"] = (
            capo_network_firewall.types.identified_type.serialize_cbor(
                value["identified_type"]
            )
        )
    if "analysis_detail" in value:
        out["AnalysisDetail"] = value["analysis_detail"]
    return out


def deserialize_cbor(data: dict) -> AnalysisResult:
    out: AnalysisResult = {}  # type: ignore[typeddict-item]
    if data.get("IdentifiedRuleIds") is not None:
        import capo_network_firewall.types.rule_id_list

        out["identified_rule_ids"] = (
            capo_network_firewall.types.rule_id_list.deserialize_cbor(
                data["IdentifiedRuleIds"]
            )
        )
    if data.get("IdentifiedType") is not None:
        import capo_network_firewall.types.identified_type

        out["identified_type"] = (
            capo_network_firewall.types.identified_type.deserialize_cbor(
                data["IdentifiedType"]
            )
        )
    if data.get("AnalysisDetail") is not None:
        out["analysis_detail"] = data["AnalysisDetail"]
    return out

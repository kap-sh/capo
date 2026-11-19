"""Generated from Smithy shape ``com.amazonaws.networkfirewall#SummaryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.summary_rule_options


class SummaryConfiguration(TypedDict, closed=True):
    rule_options: NotRequired[
        "capo_network_firewall.types.summary_rule_options.SummaryRuleOptions"
    ]
    """<p>Specifies the selected rule options returned by <a>DescribeRuleGroupSummary</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SummaryConfiguration) -> dict:
    out: dict = {}
    if "rule_options" in value:
        import capo_network_firewall.types.summary_rule_options

        out["RuleOptions"] = (
            capo_network_firewall.types.summary_rule_options.serialize_aws_json_1_0(
                value["rule_options"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SummaryConfiguration:
    out: SummaryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RuleOptions") is not None:
        import capo_network_firewall.types.summary_rule_options

        out["rule_options"] = (
            capo_network_firewall.types.summary_rule_options.deserialize_aws_json_1_0(
                data["RuleOptions"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SummaryConfiguration) -> dict:
    out: dict = {}
    if "rule_options" in value:
        import capo_network_firewall.types.summary_rule_options

        out["RuleOptions"] = (
            capo_network_firewall.types.summary_rule_options.serialize_cbor(
                value["rule_options"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> SummaryConfiguration:
    out: SummaryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RuleOptions") is not None:
        import capo_network_firewall.types.summary_rule_options

        out["rule_options"] = (
            capo_network_firewall.types.summary_rule_options.deserialize_cbor(
                data["RuleOptions"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Summary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.rule_summaries


class Summary(TypedDict, closed=True):
    rule_summaries: NotRequired[
        "capo_network_firewall.types.rule_summaries.RuleSummaries"
    ]
    """<p>An array of <a>RuleSummary</a> objects containing individual rule details that had been configured by the rulegroup's SummaryConfiguration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Summary) -> dict:
    out: dict = {}
    if "rule_summaries" in value:
        import capo_network_firewall.types.rule_summaries

        out["RuleSummaries"] = (
            capo_network_firewall.types.rule_summaries.serialize_aws_json_1_0(
                value["rule_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Summary:
    out: Summary = {}  # type: ignore[typeddict-item]
    if data.get("RuleSummaries") is not None:
        import capo_network_firewall.types.rule_summaries

        out["rule_summaries"] = (
            capo_network_firewall.types.rule_summaries.deserialize_aws_json_1_0(
                data["RuleSummaries"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Summary) -> dict:
    out: dict = {}
    if "rule_summaries" in value:
        import capo_network_firewall.types.rule_summaries

        out["RuleSummaries"] = (
            capo_network_firewall.types.rule_summaries.serialize_cbor(
                value["rule_summaries"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Summary:
    out: Summary = {}  # type: ignore[typeddict-item]
    if data.get("RuleSummaries") is not None:
        import capo_network_firewall.types.rule_summaries

        out["rule_summaries"] = (
            capo_network_firewall.types.rule_summaries.deserialize_cbor(
                data["RuleSummaries"]
            )
        )
    return out

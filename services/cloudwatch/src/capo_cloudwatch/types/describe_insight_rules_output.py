"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeInsightRulesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.insight_rules
    import capo_cloudwatch.types.next_token


class DescribeInsightRulesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>If this parameter is present, it is a token that marks the start of the next batch of returned results. </p>"""
    insight_rules: NotRequired["capo_cloudwatch.types.insight_rules.InsightRules"]
    """<p>The rules returned by the operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeInsightRulesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "insight_rules" in value:
        import capo_cloudwatch.types.insight_rules

        out["InsightRules"] = (
            capo_cloudwatch.types.insight_rules.serialize_aws_json_1_0(
                value["insight_rules"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeInsightRulesOutput:
    out: DescribeInsightRulesOutput = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("InsightRules") is not None:
        import capo_cloudwatch.types.insight_rules

        out["insight_rules"] = (
            capo_cloudwatch.types.insight_rules.deserialize_aws_json_1_0(
                data["InsightRules"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeInsightRulesOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "insight_rules" in value:
        import capo_cloudwatch.types.insight_rules

        capo_cloudwatch.types.insight_rules.serialize_query(
            value["insight_rules"], pairs, f"{key_prefix}InsightRules"
        )


def deserialize_query(el: Element) -> DescribeInsightRulesOutput:
    out: DescribeInsightRulesOutput = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_insight_rules = el.find("InsightRules")
    if child_insight_rules is not None:
        import capo_cloudwatch.types.insight_rules

        out["insight_rules"] = capo_cloudwatch.types.insight_rules.deserialize_query(
            child_insight_rules
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeInsightRulesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "insight_rules" in value:
        import capo_cloudwatch.types.insight_rules

        out["InsightRules"] = capo_cloudwatch.types.insight_rules.serialize_cbor(
            value["insight_rules"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeInsightRulesOutput:
    out: DescribeInsightRulesOutput = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("InsightRules") is not None:
        import capo_cloudwatch.types.insight_rules

        out["insight_rules"] = capo_cloudwatch.types.insight_rules.deserialize_cbor(
            data["InsightRules"]
        )
    return out

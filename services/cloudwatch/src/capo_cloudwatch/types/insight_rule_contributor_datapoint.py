"""Generated from Smithy shape ``com.amazonaws.cloudwatch#InsightRuleContributorDatapoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.insight_rule_unbound_double
    import capo_cloudwatch.types.timestamp


class InsightRuleContributorDatapoint(TypedDict, closed=True):
    timestamp: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The timestamp of the data point.</p>"""
    approximate_value: NotRequired[
        "capo_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The approximate value that this contributor added during this timestamp.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InsightRuleContributorDatapoint) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["Timestamp"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["timestamp"]
        )
    if "approximate_value" in value:
        out["ApproximateValue"] = (
            "NaN"
            if value["approximate_value"] != value["approximate_value"]
            else "Infinity"
            if value["approximate_value"] == float("inf")
            else "-Infinity"
            if value["approximate_value"] == float("-inf")
            else value["approximate_value"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InsightRuleContributorDatapoint:
    out: InsightRuleContributorDatapoint = {}  # type: ignore[typeddict-item]
    if data.get("Timestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["timestamp"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["Timestamp"]
        )
    if data.get("ApproximateValue") is not None:
        out["approximate_value"] = float(data["ApproximateValue"])
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: InsightRuleContributorDatapoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "timestamp" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["timestamp"], pairs, f"{key_prefix}Timestamp"
        )
    if "approximate_value" in value:
        pairs.append(
            (
                f"{key_prefix}ApproximateValue",
                (
                    "NaN"
                    if value["approximate_value"] != value["approximate_value"]
                    else "Infinity"
                    if value["approximate_value"] == float("inf")
                    else "-Infinity"
                    if value["approximate_value"] == float("-inf")
                    else str(value["approximate_value"])
                ),
            )
        )


def deserialize_query(el: Element) -> InsightRuleContributorDatapoint:
    out: InsightRuleContributorDatapoint = {}  # type: ignore[typeddict-item]
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import capo_cloudwatch.types.timestamp

        out["timestamp"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_timestamp
        )
    child_approximate_value = el.find("ApproximateValue")
    if child_approximate_value is not None:
        out["approximate_value"] = float(child_approximate_value.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InsightRuleContributorDatapoint) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["Timestamp"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["timestamp"]
        )
    if "approximate_value" in value:
        out["ApproximateValue"] = value["approximate_value"]
    return out


def deserialize_cbor(data: dict) -> InsightRuleContributorDatapoint:
    out: InsightRuleContributorDatapoint = {}  # type: ignore[typeddict-item]
    if data.get("Timestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["timestamp"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["Timestamp"]
        )
    if data.get("ApproximateValue") is not None:
        out["approximate_value"] = float(data["ApproximateValue"])
    return out

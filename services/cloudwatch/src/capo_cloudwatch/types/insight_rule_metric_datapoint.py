"""Generated from Smithy shape ``com.amazonaws.cloudwatch#InsightRuleMetricDatapoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.insight_rule_unbound_double
    import capo_cloudwatch.types.timestamp


class InsightRuleMetricDatapoint(TypedDict, closed=True):
    timestamp: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The timestamp of the data point.</p>"""
    unique_contributors: NotRequired[
        "capo_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The number of unique contributors who published data during this timestamp.</p> <p>This statistic is returned only if you included it in the <code>Metrics</code> array in your request.</p>"""
    max_contributor_value: NotRequired[
        "capo_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The maximum value provided by one contributor during this timestamp. Each timestamp is evaluated separately, so the identity of the max contributor could be different for each timestamp.</p> <p>This statistic is returned only if you included it in the <code>Metrics</code> array in your request.</p>"""
    sample_count: NotRequired[
        "capo_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The number of occurrences that matched the rule during this data point.</p> <p>This statistic is returned only if you included it in the <code>Metrics</code> array in your request.</p>"""
    average: NotRequired[
        "capo_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The average value from all contributors during the time period represented by that data point.</p> <p>This statistic is returned only if you included it in the <code>Metrics</code> array in your request.</p>"""
    sum: NotRequired[
        "capo_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The sum of the values from all contributors during the time period represented by that data point.</p> <p>This statistic is returned only if you included it in the <code>Metrics</code> array in your request.</p>"""
    minimum: NotRequired[
        "capo_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The minimum value from a single contributor during the time period represented by that data point.</p> <p>This statistic is returned only if you included it in the <code>Metrics</code> array in your request.</p>"""
    maximum: NotRequired[
        "capo_cloudwatch.types.insight_rule_unbound_double.InsightRuleUnboundDouble"
    ]
    """<p>The maximum value from a single occurence from a single contributor during the time period represented by that data point.</p> <p>This statistic is returned only if you included it in the <code>Metrics</code> array in your request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InsightRuleMetricDatapoint) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["Timestamp"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["timestamp"]
        )
    if "unique_contributors" in value:
        out["UniqueContributors"] = (
            "NaN"
            if value["unique_contributors"] != value["unique_contributors"]
            else "Infinity"
            if value["unique_contributors"] == float("inf")
            else "-Infinity"
            if value["unique_contributors"] == float("-inf")
            else value["unique_contributors"]
        )
    if "max_contributor_value" in value:
        out["MaxContributorValue"] = (
            "NaN"
            if value["max_contributor_value"] != value["max_contributor_value"]
            else "Infinity"
            if value["max_contributor_value"] == float("inf")
            else "-Infinity"
            if value["max_contributor_value"] == float("-inf")
            else value["max_contributor_value"]
        )
    if "sample_count" in value:
        out["SampleCount"] = (
            "NaN"
            if value["sample_count"] != value["sample_count"]
            else "Infinity"
            if value["sample_count"] == float("inf")
            else "-Infinity"
            if value["sample_count"] == float("-inf")
            else value["sample_count"]
        )
    if "average" in value:
        out["Average"] = (
            "NaN"
            if value["average"] != value["average"]
            else "Infinity"
            if value["average"] == float("inf")
            else "-Infinity"
            if value["average"] == float("-inf")
            else value["average"]
        )
    if "sum" in value:
        out["Sum"] = (
            "NaN"
            if value["sum"] != value["sum"]
            else "Infinity"
            if value["sum"] == float("inf")
            else "-Infinity"
            if value["sum"] == float("-inf")
            else value["sum"]
        )
    if "minimum" in value:
        out["Minimum"] = (
            "NaN"
            if value["minimum"] != value["minimum"]
            else "Infinity"
            if value["minimum"] == float("inf")
            else "-Infinity"
            if value["minimum"] == float("-inf")
            else value["minimum"]
        )
    if "maximum" in value:
        out["Maximum"] = (
            "NaN"
            if value["maximum"] != value["maximum"]
            else "Infinity"
            if value["maximum"] == float("inf")
            else "-Infinity"
            if value["maximum"] == float("-inf")
            else value["maximum"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InsightRuleMetricDatapoint:
    out: InsightRuleMetricDatapoint = {}  # type: ignore[typeddict-item]
    if data.get("Timestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["timestamp"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["Timestamp"]
        )
    if data.get("UniqueContributors") is not None:
        out["unique_contributors"] = float(data["UniqueContributors"])
    if data.get("MaxContributorValue") is not None:
        out["max_contributor_value"] = float(data["MaxContributorValue"])
    if data.get("SampleCount") is not None:
        out["sample_count"] = float(data["SampleCount"])
    if data.get("Average") is not None:
        out["average"] = float(data["Average"])
    if data.get("Sum") is not None:
        out["sum"] = float(data["Sum"])
    if data.get("Minimum") is not None:
        out["minimum"] = float(data["Minimum"])
    if data.get("Maximum") is not None:
        out["maximum"] = float(data["Maximum"])
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: InsightRuleMetricDatapoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "timestamp" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["timestamp"], pairs, f"{key_prefix}Timestamp"
        )
    if "unique_contributors" in value:
        pairs.append(
            (
                f"{key_prefix}UniqueContributors",
                (
                    "NaN"
                    if value["unique_contributors"] != value["unique_contributors"]
                    else "Infinity"
                    if value["unique_contributors"] == float("inf")
                    else "-Infinity"
                    if value["unique_contributors"] == float("-inf")
                    else str(value["unique_contributors"])
                ),
            )
        )
    if "max_contributor_value" in value:
        pairs.append(
            (
                f"{key_prefix}MaxContributorValue",
                (
                    "NaN"
                    if value["max_contributor_value"] != value["max_contributor_value"]
                    else "Infinity"
                    if value["max_contributor_value"] == float("inf")
                    else "-Infinity"
                    if value["max_contributor_value"] == float("-inf")
                    else str(value["max_contributor_value"])
                ),
            )
        )
    if "sample_count" in value:
        pairs.append(
            (
                f"{key_prefix}SampleCount",
                (
                    "NaN"
                    if value["sample_count"] != value["sample_count"]
                    else "Infinity"
                    if value["sample_count"] == float("inf")
                    else "-Infinity"
                    if value["sample_count"] == float("-inf")
                    else str(value["sample_count"])
                ),
            )
        )
    if "average" in value:
        pairs.append(
            (
                f"{key_prefix}Average",
                (
                    "NaN"
                    if value["average"] != value["average"]
                    else "Infinity"
                    if value["average"] == float("inf")
                    else "-Infinity"
                    if value["average"] == float("-inf")
                    else str(value["average"])
                ),
            )
        )
    if "sum" in value:
        pairs.append(
            (
                f"{key_prefix}Sum",
                (
                    "NaN"
                    if value["sum"] != value["sum"]
                    else "Infinity"
                    if value["sum"] == float("inf")
                    else "-Infinity"
                    if value["sum"] == float("-inf")
                    else str(value["sum"])
                ),
            )
        )
    if "minimum" in value:
        pairs.append(
            (
                f"{key_prefix}Minimum",
                (
                    "NaN"
                    if value["minimum"] != value["minimum"]
                    else "Infinity"
                    if value["minimum"] == float("inf")
                    else "-Infinity"
                    if value["minimum"] == float("-inf")
                    else str(value["minimum"])
                ),
            )
        )
    if "maximum" in value:
        pairs.append(
            (
                f"{key_prefix}Maximum",
                (
                    "NaN"
                    if value["maximum"] != value["maximum"]
                    else "Infinity"
                    if value["maximum"] == float("inf")
                    else "-Infinity"
                    if value["maximum"] == float("-inf")
                    else str(value["maximum"])
                ),
            )
        )


def deserialize_query(el: Element) -> InsightRuleMetricDatapoint:
    out: InsightRuleMetricDatapoint = {}  # type: ignore[typeddict-item]
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import capo_cloudwatch.types.timestamp

        out["timestamp"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_timestamp
        )
    child_unique_contributors = el.find("UniqueContributors")
    if child_unique_contributors is not None:
        out["unique_contributors"] = float(child_unique_contributors.text or "")
    child_max_contributor_value = el.find("MaxContributorValue")
    if child_max_contributor_value is not None:
        out["max_contributor_value"] = float(child_max_contributor_value.text or "")
    child_sample_count = el.find("SampleCount")
    if child_sample_count is not None:
        out["sample_count"] = float(child_sample_count.text or "")
    child_average = el.find("Average")
    if child_average is not None:
        out["average"] = float(child_average.text or "")
    child_sum = el.find("Sum")
    if child_sum is not None:
        out["sum"] = float(child_sum.text or "")
    child_minimum = el.find("Minimum")
    if child_minimum is not None:
        out["minimum"] = float(child_minimum.text or "")
    child_maximum = el.find("Maximum")
    if child_maximum is not None:
        out["maximum"] = float(child_maximum.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InsightRuleMetricDatapoint) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["Timestamp"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["timestamp"]
        )
    if "unique_contributors" in value:
        out["UniqueContributors"] = value["unique_contributors"]
    if "max_contributor_value" in value:
        out["MaxContributorValue"] = value["max_contributor_value"]
    if "sample_count" in value:
        out["SampleCount"] = value["sample_count"]
    if "average" in value:
        out["Average"] = value["average"]
    if "sum" in value:
        out["Sum"] = value["sum"]
    if "minimum" in value:
        out["Minimum"] = value["minimum"]
    if "maximum" in value:
        out["Maximum"] = value["maximum"]
    return out


def deserialize_cbor(data: dict) -> InsightRuleMetricDatapoint:
    out: InsightRuleMetricDatapoint = {}  # type: ignore[typeddict-item]
    if data.get("Timestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["timestamp"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["Timestamp"]
        )
    if data.get("UniqueContributors") is not None:
        out["unique_contributors"] = float(data["UniqueContributors"])
    if data.get("MaxContributorValue") is not None:
        out["max_contributor_value"] = float(data["MaxContributorValue"])
    if data.get("SampleCount") is not None:
        out["sample_count"] = float(data["SampleCount"])
    if data.get("Average") is not None:
        out["average"] = float(data["Average"])
    if data.get("Sum") is not None:
        out["sum"] = float(data["Sum"])
    if data.get("Minimum") is not None:
        out["minimum"] = float(data["Minimum"])
    if data.get("Maximum") is not None:
        out["maximum"] = float(data["Maximum"])
    return out

"""Generated from Smithy shape ``com.amazonaws.cloudwatch#StatisticSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.datapoint_value


class StatisticSet(TypedDict, closed=True):
    sample_count: NotRequired["capo_cloudwatch.types.datapoint_value.DatapointValue"]
    """<p>The number of samples used for the statistic set.</p>"""
    sum: NotRequired["capo_cloudwatch.types.datapoint_value.DatapointValue"]
    """<p>The sum of values for the sample set.</p>"""
    minimum: NotRequired["capo_cloudwatch.types.datapoint_value.DatapointValue"]
    """<p>The minimum value of the sample set.</p>"""
    maximum: NotRequired["capo_cloudwatch.types.datapoint_value.DatapointValue"]
    """<p>The maximum value of the sample set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatisticSet) -> dict:
    out: dict = {}
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


def deserialize_aws_json_1_0(data: dict) -> StatisticSet:
    out: StatisticSet = {}  # type: ignore[typeddict-item]
    if data.get("SampleCount") is not None:
        out["sample_count"] = float(data["SampleCount"])
    if data.get("Sum") is not None:
        out["sum"] = float(data["Sum"])
    if data.get("Minimum") is not None:
        out["minimum"] = float(data["Minimum"])
    if data.get("Maximum") is not None:
        out["maximum"] = float(data["Maximum"])
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: StatisticSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
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


def deserialize_query(el: Element) -> StatisticSet:
    out: StatisticSet = {}  # type: ignore[typeddict-item]
    child_sample_count = el.find("SampleCount")
    if child_sample_count is not None:
        out["sample_count"] = float(child_sample_count.text or "")
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
def serialize_cbor(value: StatisticSet) -> dict:
    out: dict = {}
    if "sample_count" in value:
        out["SampleCount"] = value["sample_count"]
    if "sum" in value:
        out["Sum"] = value["sum"]
    if "minimum" in value:
        out["Minimum"] = value["minimum"]
    if "maximum" in value:
        out["Maximum"] = value["maximum"]
    return out


def deserialize_cbor(data: dict) -> StatisticSet:
    out: StatisticSet = {}  # type: ignore[typeddict-item]
    if data.get("SampleCount") is not None:
        out["sample_count"] = float(data["SampleCount"])
    if data.get("Sum") is not None:
        out["sum"] = float(data["Sum"])
    if data.get("Minimum") is not None:
        out["minimum"] = float(data["Minimum"])
    if data.get("Maximum") is not None:
        out["maximum"] = float(data["Maximum"])
    return out

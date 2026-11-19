"""Generated from Smithy shape ``com.amazonaws.cloudwatch#Datapoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.datapoint_value
    import capo_cloudwatch.types.datapoint_value_map
    import capo_cloudwatch.types.standard_unit
    import capo_cloudwatch.types.timestamp


class Datapoint(TypedDict, closed=True):
    timestamp: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The time stamp used for the data point.</p>"""
    sample_count: NotRequired["capo_cloudwatch.types.datapoint_value.DatapointValue"]
    """<p>The number of metric values that contributed to the aggregate value of this data point.</p>"""
    average: NotRequired["capo_cloudwatch.types.datapoint_value.DatapointValue"]
    """<p>The average of the metric values that correspond to the data point.</p>"""
    sum: NotRequired["capo_cloudwatch.types.datapoint_value.DatapointValue"]
    """<p>The sum of the metric values for the data point.</p>"""
    minimum: NotRequired["capo_cloudwatch.types.datapoint_value.DatapointValue"]
    """<p>The minimum metric value for the data point.</p>"""
    maximum: NotRequired["capo_cloudwatch.types.datapoint_value.DatapointValue"]
    """<p>The maximum metric value for the data point.</p>"""
    unit: NotRequired["capo_cloudwatch.types.standard_unit.StandardUnit"]
    """<p>The standard unit for the data point.</p>"""
    extended_statistics: NotRequired[
        "capo_cloudwatch.types.datapoint_value_map.DatapointValueMap"
    ]
    """<p>The percentile statistic for the data point.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Datapoint) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["Timestamp"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["timestamp"]
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
    if "unit" in value:
        import capo_cloudwatch.types.standard_unit

        out["Unit"] = capo_cloudwatch.types.standard_unit.serialize_aws_json_1_0(
            value["unit"]
        )
    if "extended_statistics" in value:
        import capo_cloudwatch.types.datapoint_value_map

        out["ExtendedStatistics"] = (
            capo_cloudwatch.types.datapoint_value_map.serialize_aws_json_1_0(
                value["extended_statistics"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Datapoint:
    out: Datapoint = {}  # type: ignore[typeddict-item]
    if data.get("Timestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["timestamp"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["Timestamp"]
        )
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
    if data.get("Unit") is not None:
        import capo_cloudwatch.types.standard_unit

        out["unit"] = capo_cloudwatch.types.standard_unit.deserialize_aws_json_1_0(
            data["Unit"]
        )
    if data.get("ExtendedStatistics") is not None:
        import capo_cloudwatch.types.datapoint_value_map

        out["extended_statistics"] = (
            capo_cloudwatch.types.datapoint_value_map.deserialize_aws_json_1_0(
                data["ExtendedStatistics"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: Datapoint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "timestamp" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["timestamp"], pairs, f"{key_prefix}Timestamp"
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
    if "unit" in value:
        import capo_cloudwatch.types.standard_unit

        capo_cloudwatch.types.standard_unit.serialize_query(
            value["unit"], pairs, f"{key_prefix}Unit"
        )
    if "extended_statistics" in value:
        import capo_cloudwatch.types.datapoint_value_map

        capo_cloudwatch.types.datapoint_value_map.serialize_query(
            value["extended_statistics"], pairs, f"{key_prefix}ExtendedStatistics"
        )


def deserialize_query(el: Element) -> Datapoint:
    out: Datapoint = {}  # type: ignore[typeddict-item]
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import capo_cloudwatch.types.timestamp

        out["timestamp"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_timestamp
        )
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
    child_unit = el.find("Unit")
    if child_unit is not None:
        import capo_cloudwatch.types.standard_unit

        out["unit"] = capo_cloudwatch.types.standard_unit.deserialize_query(child_unit)
    child_extended_statistics = el.find("ExtendedStatistics")
    if child_extended_statistics is not None:
        import capo_cloudwatch.types.datapoint_value_map

        out["extended_statistics"] = (
            capo_cloudwatch.types.datapoint_value_map.deserialize_query(
                child_extended_statistics
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Datapoint) -> dict:
    out: dict = {}
    if "timestamp" in value:
        import capo_cloudwatch.types.timestamp

        out["Timestamp"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["timestamp"]
        )
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
    if "unit" in value:
        import capo_cloudwatch.types.standard_unit

        out["Unit"] = capo_cloudwatch.types.standard_unit.serialize_cbor(value["unit"])
    if "extended_statistics" in value:
        import capo_cloudwatch.types.datapoint_value_map

        out["ExtendedStatistics"] = (
            capo_cloudwatch.types.datapoint_value_map.serialize_cbor(
                value["extended_statistics"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Datapoint:
    out: Datapoint = {}  # type: ignore[typeddict-item]
    if data.get("Timestamp") is not None:
        import capo_cloudwatch.types.timestamp

        out["timestamp"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["Timestamp"]
        )
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
    if data.get("Unit") is not None:
        import capo_cloudwatch.types.standard_unit

        out["unit"] = capo_cloudwatch.types.standard_unit.deserialize_cbor(data["Unit"])
    if data.get("ExtendedStatistics") is not None:
        import capo_cloudwatch.types.datapoint_value_map

        out["extended_statistics"] = (
            capo_cloudwatch.types.datapoint_value_map.deserialize_cbor(
                data["ExtendedStatistics"]
            )
        )
    return out

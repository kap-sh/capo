"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetObjectTypeAttributeStatisticsStats``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.double
    import capo_customer_profiles.types.get_object_type_attribute_statistics_percentiles


class GetObjectTypeAttributeStatisticsStats(TypedDict, closed=True):
    maximum: "capo_customer_profiles.types.double.Double"
    """<p>The maximum value found in the attribute dataset.</p>"""
    minimum: "capo_customer_profiles.types.double.Double"
    """<p>The minimum value found in the attribute dataset.</p>"""
    average: "capo_customer_profiles.types.double.Double"
    """<p>The arithmetic mean of the attribute values.</p>"""
    standard_deviation: "capo_customer_profiles.types.double.Double"
    """<p>The standard deviation of the attribute values, measuring their spread around the mean.</p>"""
    percentiles: "capo_customer_profiles.types.get_object_type_attribute_statistics_percentiles.GetObjectTypeAttributeStatisticsPercentiles"
    """<p>Percentile distribution statistics for the attribute values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetObjectTypeAttributeStatisticsStats) -> dict:
    out: dict = {}
    out["Maximum"] = (
        "NaN"
        if value["maximum"] != value["maximum"]
        else "Infinity"
        if value["maximum"] == float("inf")
        else "-Infinity"
        if value["maximum"] == float("-inf")
        else value["maximum"]
    )
    out["Minimum"] = (
        "NaN"
        if value["minimum"] != value["minimum"]
        else "Infinity"
        if value["minimum"] == float("inf")
        else "-Infinity"
        if value["minimum"] == float("-inf")
        else value["minimum"]
    )
    out["Average"] = (
        "NaN"
        if value["average"] != value["average"]
        else "Infinity"
        if value["average"] == float("inf")
        else "-Infinity"
        if value["average"] == float("-inf")
        else value["average"]
    )
    out["StandardDeviation"] = (
        "NaN"
        if value["standard_deviation"] != value["standard_deviation"]
        else "Infinity"
        if value["standard_deviation"] == float("inf")
        else "-Infinity"
        if value["standard_deviation"] == float("-inf")
        else value["standard_deviation"]
    )
    import capo_customer_profiles.types.get_object_type_attribute_statistics_percentiles

    out["Percentiles"] = (
        capo_customer_profiles.types.get_object_type_attribute_statistics_percentiles.serialize_json(
            value["percentiles"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetObjectTypeAttributeStatisticsStats:
    out: GetObjectTypeAttributeStatisticsStats = {}  # type: ignore[typeddict-item]
    if data.get("Maximum") is not None:
        out["maximum"] = float(data["Maximum"])
    else:
        out["maximum"] = 0.0
    if data.get("Minimum") is not None:
        out["minimum"] = float(data["Minimum"])
    else:
        out["minimum"] = 0.0
    if data.get("Average") is not None:
        out["average"] = float(data["Average"])
    else:
        out["average"] = 0.0
    if data.get("StandardDeviation") is not None:
        out["standard_deviation"] = float(data["StandardDeviation"])
    else:
        out["standard_deviation"] = 0.0
    if data.get("Percentiles") is not None:
        import capo_customer_profiles.types.get_object_type_attribute_statistics_percentiles

        out["percentiles"] = (
            capo_customer_profiles.types.get_object_type_attribute_statistics_percentiles.deserialize_json(
                data["Percentiles"]
            )
        )
    else:
        raise DeserializationError(
            "GetObjectTypeAttributeStatisticsStats.percentiles required"
        )
    return out

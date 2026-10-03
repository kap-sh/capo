"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PropertyType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.attribute
    import capo_iotsitewise.types.measurement
    import capo_iotsitewise.types.metric
    import capo_iotsitewise.types.transform


class PropertyType(TypedDict, closed=True):
    attribute: NotRequired["capo_iotsitewise.types.attribute.Attribute"]
    """<p>Specifies an asset attribute property. An attribute generally contains static information, such as the serial number of an <a href="https://en.wikipedia.org/wiki/Internet_of_things#Industrial_applications">IIoT</a> wind turbine.</p>"""
    measurement: NotRequired["capo_iotsitewise.types.measurement.Measurement"]
    """<p>Specifies an asset measurement property. A measurement represents a device's raw sensor data stream, such as timestamped temperature values or timestamped power values.</p>"""
    transform: NotRequired["capo_iotsitewise.types.transform.Transform"]
    """<p>Specifies an asset transform property. A transform contains a mathematical expression that maps a property's data points from one form to another, such as a unit conversion from Celsius to Fahrenheit.</p>"""
    metric: NotRequired["capo_iotsitewise.types.metric.Metric"]
    """<p>Specifies an asset metric property. A metric contains a mathematical expression that uses aggregate functions to process all input data points over a time interval and output a single data point, such as to calculate the average hourly temperature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyType) -> dict:
    out: dict = {}
    if "attribute" in value:
        import capo_iotsitewise.types.attribute

        out["attribute"] = capo_iotsitewise.types.attribute.serialize_json(
            value["attribute"]
        )
    if "measurement" in value:
        import capo_iotsitewise.types.measurement

        out["measurement"] = capo_iotsitewise.types.measurement.serialize_json(
            value["measurement"]
        )
    if "transform" in value:
        import capo_iotsitewise.types.transform

        out["transform"] = capo_iotsitewise.types.transform.serialize_json(
            value["transform"]
        )
    if "metric" in value:
        import capo_iotsitewise.types.metric

        out["metric"] = capo_iotsitewise.types.metric.serialize_json(value["metric"])
    return out


def deserialize_json(data: dict) -> PropertyType:
    out: PropertyType = {}  # type: ignore[typeddict-item]
    if data.get("attribute") is not None:
        import capo_iotsitewise.types.attribute

        out["attribute"] = capo_iotsitewise.types.attribute.deserialize_json(
            data["attribute"]
        )
    if data.get("measurement") is not None:
        import capo_iotsitewise.types.measurement

        out["measurement"] = capo_iotsitewise.types.measurement.deserialize_json(
            data["measurement"]
        )
    if data.get("transform") is not None:
        import capo_iotsitewise.types.transform

        out["transform"] = capo_iotsitewise.types.transform.deserialize_json(
            data["transform"]
        )
    if data.get("metric") is not None:
        import capo_iotsitewise.types.metric

        out["metric"] = capo_iotsitewise.types.metric.deserialize_json(data["metric"])
    return out

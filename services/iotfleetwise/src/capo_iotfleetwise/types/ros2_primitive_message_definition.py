"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ROS2PrimitiveMessageDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.double
    import capo_iotfleetwise.types.max_string_size
    import capo_iotfleetwise.types.ros2_primitive_type


class ROS2PrimitiveMessageDefinition(TypedDict, closed=True):
    primitive_type: "capo_iotfleetwise.types.ros2_primitive_type.ROS2PrimitiveType"
    """<p>The primitive type (integer, floating point, boolean, etc.) for the ROS 2 primitive message definition.</p>"""
    offset: NotRequired["capo_iotfleetwise.types.double.double"]
    """<p>The offset used to calculate the signal value. Combined with scaling, the calculation is <code>value = raw_value * scaling + offset</code>.</p>"""
    scaling: NotRequired["capo_iotfleetwise.types.double.double"]
    """<p>A multiplier used to decode the message.</p>"""
    upper_bound: NotRequired["capo_iotfleetwise.types.max_string_size.maxStringSize"]
    """<p>An optional attribute specifying the upper bound for <code>STRING</code> and <code>WSTRING</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ROS2PrimitiveMessageDefinition) -> dict:
    out: dict = {}
    import capo_iotfleetwise.types.ros2_primitive_type

    out["primitiveType"] = (
        capo_iotfleetwise.types.ros2_primitive_type.serialize_aws_json_1_0(
            value["primitive_type"]
        )
    )
    if "offset" in value:
        out["offset"] = (
            "NaN"
            if value["offset"] != value["offset"]
            else "Infinity"
            if value["offset"] == float("inf")
            else "-Infinity"
            if value["offset"] == float("-inf")
            else value["offset"]
        )
    if "scaling" in value:
        out["scaling"] = (
            "NaN"
            if value["scaling"] != value["scaling"]
            else "Infinity"
            if value["scaling"] == float("inf")
            else "-Infinity"
            if value["scaling"] == float("-inf")
            else value["scaling"]
        )
    if "upper_bound" in value:
        out["upperBound"] = value["upper_bound"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ROS2PrimitiveMessageDefinition:
    out: ROS2PrimitiveMessageDefinition = {}  # type: ignore[typeddict-item]
    if data.get("primitiveType") is not None:
        import capo_iotfleetwise.types.ros2_primitive_type

        out["primitive_type"] = (
            capo_iotfleetwise.types.ros2_primitive_type.deserialize_aws_json_1_0(
                data["primitiveType"]
            )
        )
    else:
        import typing

        out["primitive_type"] = typing.cast(
            "capo_iotfleetwise.types.ros2_primitive_type.ROS2PrimitiveType", ""
        )
    if data.get("offset") is not None:
        out["offset"] = float(data["offset"])
    if data.get("scaling") is not None:
        out["scaling"] = float(data["scaling"])
    if data.get("upperBound") is not None:
        out["upper_bound"] = data["upperBound"]
    return out

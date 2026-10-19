"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ObdSignal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.double
    import capo_iotfleetwise.types.non_negative_integer
    import capo_iotfleetwise.types.obd_bitmask_length
    import capo_iotfleetwise.types.obd_byte_length
    import capo_iotfleetwise.types.positive_integer
    import capo_iotfleetwise.types.signal_value_type


class ObdSignal(TypedDict, closed=True):
    pid_response_length: "capo_iotfleetwise.types.positive_integer.positiveInteger"
    """<p>The length of the requested data.</p>"""
    service_mode: "capo_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    """<p>The mode of operation (diagnostic service) in a message.</p>"""
    pid: "capo_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    """<p>The diagnostic code used to request data from a vehicle for this signal.</p>"""
    scaling: "capo_iotfleetwise.types.double.double"
    """<p>A multiplier used to decode the message.</p>"""
    offset: "capo_iotfleetwise.types.double.double"
    """<p>The offset used to calculate the signal value. Combined with scaling, the calculation is <code>value = raw_value * scaling + offset</code>.</p>"""
    start_byte: "capo_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    """<p>Indicates the beginning of the message.</p>"""
    byte_length: "capo_iotfleetwise.types.obd_byte_length.ObdByteLength"
    """<p>The length of a message.</p>"""
    bit_right_shift: "capo_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    """<p>The number of positions to shift bits in the message.</p>"""
    bit_mask_length: NotRequired[
        "capo_iotfleetwise.types.obd_bitmask_length.ObdBitmaskLength"
    ]
    """<p>The number of bits to mask in a message.</p>"""
    is_signed: NotRequired["bool"]
    """<p>Determines whether the message is signed (<code>true</code>) or not (<code>false</code>). If it's signed, the message can represent both positive and negative numbers. The <code>isSigned</code> parameter only applies to the <code>INTEGER</code> raw signal type, and it doesn't affect the <code>FLOATING_POINT</code> raw signal type. The default value is <code>false</code>.</p>"""
    signal_value_type: NotRequired[
        "capo_iotfleetwise.types.signal_value_type.SignalValueType"
    ]
    """<p>The value type of the signal. The default value is <code>INTEGER</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ObdSignal) -> dict:
    out: dict = {}
    out["pidResponseLength"] = value["pid_response_length"]
    out["serviceMode"] = value.get("service_mode", 0)
    out["pid"] = value.get("pid", 0)
    out["scaling"] = (
        "NaN"
        if value["scaling"] != value["scaling"]
        else "Infinity"
        if value["scaling"] == float("inf")
        else "-Infinity"
        if value["scaling"] == float("-inf")
        else value["scaling"]
    )
    out["offset"] = (
        "NaN"
        if value["offset"] != value["offset"]
        else "Infinity"
        if value["offset"] == float("inf")
        else "-Infinity"
        if value["offset"] == float("-inf")
        else value["offset"]
    )
    out["startByte"] = value.get("start_byte", 0)
    out["byteLength"] = value["byte_length"]
    out["bitRightShift"] = value.get("bit_right_shift", 0)
    if "bit_mask_length" in value:
        out["bitMaskLength"] = value["bit_mask_length"]
    if "is_signed" in value:
        out["isSigned"] = value["is_signed"]
    if "signal_value_type" in value:
        import capo_iotfleetwise.types.signal_value_type

        out["signalValueType"] = (
            capo_iotfleetwise.types.signal_value_type.serialize_aws_json_1_0(
                value["signal_value_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ObdSignal:
    out: ObdSignal = {}  # type: ignore[typeddict-item]
    if data.get("pidResponseLength") is not None:
        out["pid_response_length"] = data["pidResponseLength"]
    else:
        out["pid_response_length"] = 0
    if data.get("serviceMode") is not None:
        out["service_mode"] = data["serviceMode"]
    else:
        out["service_mode"] = 0
    if data.get("pid") is not None:
        out["pid"] = data["pid"]
    else:
        out["pid"] = 0
    if data.get("scaling") is not None:
        out["scaling"] = float(data["scaling"])
    else:
        out["scaling"] = 0.0
    if data.get("offset") is not None:
        out["offset"] = float(data["offset"])
    else:
        out["offset"] = 0.0
    if data.get("startByte") is not None:
        out["start_byte"] = data["startByte"]
    else:
        out["start_byte"] = 0
    if data.get("byteLength") is not None:
        out["byte_length"] = data["byteLength"]
    else:
        out["byte_length"] = 0
    if data.get("bitRightShift") is not None:
        out["bit_right_shift"] = data["bitRightShift"]
    else:
        out["bit_right_shift"] = 0
    if data.get("bitMaskLength") is not None:
        out["bit_mask_length"] = data["bitMaskLength"]
    if data.get("isSigned") is not None:
        out["is_signed"] = data["isSigned"]
    if data.get("signalValueType") is not None:
        import capo_iotfleetwise.types.signal_value_type

        out["signal_value_type"] = (
            capo_iotfleetwise.types.signal_value_type.deserialize_aws_json_1_0(
                data["signalValueType"]
            )
        )
    return out

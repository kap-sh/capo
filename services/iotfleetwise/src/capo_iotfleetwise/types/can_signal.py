"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CanSignal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.can_signal_name
    import capo_iotfleetwise.types.double
    import capo_iotfleetwise.types.non_negative_integer
    import capo_iotfleetwise.types.signal_value_type


class CanSignal(TypedDict, closed=True):
    message_id: "capo_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    """<p>The ID of the message.</p>"""
    is_big_endian: "bool"
    """<p>Whether the byte ordering of a CAN message is big-endian.</p>"""
    is_signed: "bool"
    """<p>Determines whether the message is signed (<code>true</code>) or not (<code>false</code>). If it's signed, the message can represent both positive and negative numbers. The <code>isSigned</code> parameter only applies to the <code>INTEGER</code> raw signal type, and it doesn't affect the <code>FLOATING_POINT</code> raw signal type.</p>"""
    start_bit: "capo_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    """<p>Indicates the beginning of the CAN signal. This should always be the least significant bit (LSB).</p> <p>This value might be different from the value in a DBC file. For little endian signals, <code>startBit</code> is the same value as in the DBC file. For big endian signals in a DBC file, the start bit is the most significant bit (MSB). You will have to calculate the LSB instead and pass it as the <code>startBit</code>.</p>"""
    offset: "capo_iotfleetwise.types.double.double"
    """<p>The offset used to calculate the signal value. Combined with factor, the calculation is <code>value = raw_value * factor + offset</code>.</p>"""
    factor: "capo_iotfleetwise.types.double.double"
    """<p>A multiplier used to decode the CAN message.</p>"""
    length: "capo_iotfleetwise.types.non_negative_integer.nonNegativeInteger"
    """<p>How many bytes of data are in the message.</p>"""
    name: NotRequired["capo_iotfleetwise.types.can_signal_name.CanSignalName"]
    """<p>The name of the signal.</p>"""
    signal_value_type: NotRequired[
        "capo_iotfleetwise.types.signal_value_type.SignalValueType"
    ]
    """<p>The value type of the signal. The default value is <code>INTEGER</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CanSignal) -> dict:
    out: dict = {}
    out["messageId"] = value.get("message_id", 0)
    out["isBigEndian"] = value.get("is_big_endian", False)
    out["isSigned"] = value.get("is_signed", False)
    out["startBit"] = value.get("start_bit", 0)
    out["offset"] = (
        "NaN"
        if value["offset"] != value["offset"]
        else "Infinity"
        if value["offset"] == float("inf")
        else "-Infinity"
        if value["offset"] == float("-inf")
        else value["offset"]
    )
    out["factor"] = (
        "NaN"
        if value["factor"] != value["factor"]
        else "Infinity"
        if value["factor"] == float("inf")
        else "-Infinity"
        if value["factor"] == float("-inf")
        else value["factor"]
    )
    out["length"] = value.get("length", 0)
    if "name" in value:
        out["name"] = value["name"]
    if "signal_value_type" in value:
        import capo_iotfleetwise.types.signal_value_type

        out["signalValueType"] = (
            capo_iotfleetwise.types.signal_value_type.serialize_aws_json_1_0(
                value["signal_value_type"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CanSignal:
    out: CanSignal = {}  # type: ignore[typeddict-item]
    if data.get("messageId") is not None:
        out["message_id"] = data["messageId"]
    else:
        out["message_id"] = 0
    if data.get("isBigEndian") is not None:
        out["is_big_endian"] = data["isBigEndian"]
    else:
        out["is_big_endian"] = False
    if data.get("isSigned") is not None:
        out["is_signed"] = data["isSigned"]
    else:
        out["is_signed"] = False
    if data.get("startBit") is not None:
        out["start_bit"] = data["startBit"]
    else:
        out["start_bit"] = 0
    if data.get("offset") is not None:
        out["offset"] = float(data["offset"])
    else:
        out["offset"] = 0.0
    if data.get("factor") is not None:
        out["factor"] = float(data["factor"])
    else:
        out["factor"] = 0.0
    if data.get("length") is not None:
        out["length"] = data["length"]
    else:
        out["length"] = 0
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("signalValueType") is not None:
        import capo_iotfleetwise.types.signal_value_type

        out["signal_value_type"] = (
            capo_iotfleetwise.types.signal_value_type.deserialize_aws_json_1_0(
                data["signalValueType"]
            )
        )
    return out

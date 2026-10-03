"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalDecoder``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.can_signal
    import capo_iotfleetwise.types.custom_decoding_signal
    import capo_iotfleetwise.types.fully_qualified_name
    import capo_iotfleetwise.types.interface_id
    import capo_iotfleetwise.types.message_signal
    import capo_iotfleetwise.types.obd_signal
    import capo_iotfleetwise.types.signal_decoder_type


class SignalDecoder(TypedDict, closed=True):
    fully_qualified_name: (
        "capo_iotfleetwise.types.fully_qualified_name.FullyQualifiedName"
    )
    """<p>The fully qualified name of a signal decoder as defined in a vehicle model.</p>"""
    type: "capo_iotfleetwise.types.signal_decoder_type.SignalDecoderType"
    """<p>The network protocol for the vehicle. For example, <code>CAN_SIGNAL</code> specifies a protocol that defines how data is communicated between electronic control units (ECUs). <code>OBD_SIGNAL</code> specifies a protocol that defines how self-diagnostic data is communicated between ECUs.</p>"""
    interface_id: "capo_iotfleetwise.types.interface_id.InterfaceId"
    """<p>The ID of a network interface that specifies what network protocol a vehicle follows.</p>"""
    can_signal: NotRequired["capo_iotfleetwise.types.can_signal.CanSignal"]
    """<p>Information about signal decoder using the Controller Area Network (CAN) protocol.</p>"""
    obd_signal: NotRequired["capo_iotfleetwise.types.obd_signal.ObdSignal"]
    """<p>Information about signal decoder using the on-board diagnostic (OBD) II protocol.</p>"""
    message_signal: NotRequired["capo_iotfleetwise.types.message_signal.MessageSignal"]
    """<p>The decoding information for a specific message which supports higher order data types. </p>"""
    custom_decoding_signal: NotRequired[
        "capo_iotfleetwise.types.custom_decoding_signal.CustomDecodingSignal"
    ]
    """<p>Information about a <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CustomDecodingSignal.html">custom signal decoder</a>.</p> <important> <p>Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html">Amazon Web Services Region and feature availability</a> in the <i>Amazon Web Services IoT FleetWise Developer Guide</i>.</p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalDecoder) -> dict:
    out: dict = {}
    out["fullyQualifiedName"] = value["fully_qualified_name"]
    import capo_iotfleetwise.types.signal_decoder_type

    out["type"] = capo_iotfleetwise.types.signal_decoder_type.serialize_aws_json_1_0(
        value["type"]
    )
    out["interfaceId"] = value["interface_id"]
    if "can_signal" in value:
        import capo_iotfleetwise.types.can_signal

        out["canSignal"] = capo_iotfleetwise.types.can_signal.serialize_aws_json_1_0(
            value["can_signal"]
        )
    if "obd_signal" in value:
        import capo_iotfleetwise.types.obd_signal

        out["obdSignal"] = capo_iotfleetwise.types.obd_signal.serialize_aws_json_1_0(
            value["obd_signal"]
        )
    if "message_signal" in value:
        import capo_iotfleetwise.types.message_signal

        out["messageSignal"] = (
            capo_iotfleetwise.types.message_signal.serialize_aws_json_1_0(
                value["message_signal"]
            )
        )
    if "custom_decoding_signal" in value:
        import capo_iotfleetwise.types.custom_decoding_signal

        out["customDecodingSignal"] = (
            capo_iotfleetwise.types.custom_decoding_signal.serialize_aws_json_1_0(
                value["custom_decoding_signal"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SignalDecoder:
    out: SignalDecoder = {}  # type: ignore[typeddict-item]
    if data.get("fullyQualifiedName") is not None:
        out["fully_qualified_name"] = data["fullyQualifiedName"]
    else:
        raise DeserializationError("SignalDecoder.fully_qualified_name required")
    if data.get("type") is not None:
        import capo_iotfleetwise.types.signal_decoder_type

        out["type"] = (
            capo_iotfleetwise.types.signal_decoder_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    else:
        raise DeserializationError("SignalDecoder.type required")
    if data.get("interfaceId") is not None:
        out["interface_id"] = data["interfaceId"]
    else:
        raise DeserializationError("SignalDecoder.interface_id required")
    if data.get("canSignal") is not None:
        import capo_iotfleetwise.types.can_signal

        out["can_signal"] = capo_iotfleetwise.types.can_signal.deserialize_aws_json_1_0(
            data["canSignal"]
        )
    if data.get("obdSignal") is not None:
        import capo_iotfleetwise.types.obd_signal

        out["obd_signal"] = capo_iotfleetwise.types.obd_signal.deserialize_aws_json_1_0(
            data["obdSignal"]
        )
    if data.get("messageSignal") is not None:
        import capo_iotfleetwise.types.message_signal

        out["message_signal"] = (
            capo_iotfleetwise.types.message_signal.deserialize_aws_json_1_0(
                data["messageSignal"]
            )
        )
    if data.get("customDecodingSignal") is not None:
        import capo_iotfleetwise.types.custom_decoding_signal

        out["custom_decoding_signal"] = (
            capo_iotfleetwise.types.custom_decoding_signal.deserialize_aws_json_1_0(
                data["customDecodingSignal"]
            )
        )
    return out

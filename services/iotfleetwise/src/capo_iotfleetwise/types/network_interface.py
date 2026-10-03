"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#NetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.can_interface
    import capo_iotfleetwise.types.custom_decoding_interface
    import capo_iotfleetwise.types.interface_id
    import capo_iotfleetwise.types.network_interface_type
    import capo_iotfleetwise.types.obd_interface
    import capo_iotfleetwise.types.vehicle_middleware


class NetworkInterface(TypedDict, closed=True):
    interface_id: "capo_iotfleetwise.types.interface_id.InterfaceId"
    """<p>The ID of the network interface.</p>"""
    type: "capo_iotfleetwise.types.network_interface_type.NetworkInterfaceType"
    """<p>The network protocol for the vehicle. For example, <code>CAN_SIGNAL</code> specifies a protocol that defines how data is communicated between electronic control units (ECUs). <code>OBD_SIGNAL</code> specifies a protocol that defines how self-diagnostic data is communicated between ECUs.</p>"""
    can_interface: NotRequired["capo_iotfleetwise.types.can_interface.CanInterface"]
    """<p>Information about a network interface specified by the Controller Area Network (CAN) protocol.</p>"""
    obd_interface: NotRequired["capo_iotfleetwise.types.obd_interface.ObdInterface"]
    """<p>Information about a network interface specified by the on-board diagnostic (OBD) II protocol.</p>"""
    vehicle_middleware: NotRequired[
        "capo_iotfleetwise.types.vehicle_middleware.VehicleMiddleware"
    ]
    """<p>The vehicle middleware defined as a type of network interface. Examples of vehicle middleware include <code>ROS2</code> and <code>SOME/IP</code>.</p>"""
    custom_decoding_interface: NotRequired[
        "capo_iotfleetwise.types.custom_decoding_interface.CustomDecodingInterface"
    ]
    """<p>Information about a <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CustomDecodingInterface.html">custom network interface</a>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkInterface) -> dict:
    out: dict = {}
    out["interfaceId"] = value["interface_id"]
    import capo_iotfleetwise.types.network_interface_type

    out["type"] = capo_iotfleetwise.types.network_interface_type.serialize_aws_json_1_0(
        value["type"]
    )
    if "can_interface" in value:
        import capo_iotfleetwise.types.can_interface

        out["canInterface"] = (
            capo_iotfleetwise.types.can_interface.serialize_aws_json_1_0(
                value["can_interface"]
            )
        )
    if "obd_interface" in value:
        import capo_iotfleetwise.types.obd_interface

        out["obdInterface"] = (
            capo_iotfleetwise.types.obd_interface.serialize_aws_json_1_0(
                value["obd_interface"]
            )
        )
    if "vehicle_middleware" in value:
        import capo_iotfleetwise.types.vehicle_middleware

        out["vehicleMiddleware"] = (
            capo_iotfleetwise.types.vehicle_middleware.serialize_aws_json_1_0(
                value["vehicle_middleware"]
            )
        )
    if "custom_decoding_interface" in value:
        import capo_iotfleetwise.types.custom_decoding_interface

        out["customDecodingInterface"] = (
            capo_iotfleetwise.types.custom_decoding_interface.serialize_aws_json_1_0(
                value["custom_decoding_interface"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> NetworkInterface:
    out: NetworkInterface = {}  # type: ignore[typeddict-item]
    if data.get("interfaceId") is not None:
        out["interface_id"] = data["interfaceId"]
    else:
        raise DeserializationError("NetworkInterface.interface_id required")
    if data.get("type") is not None:
        import capo_iotfleetwise.types.network_interface_type

        out["type"] = (
            capo_iotfleetwise.types.network_interface_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    else:
        raise DeserializationError("NetworkInterface.type required")
    if data.get("canInterface") is not None:
        import capo_iotfleetwise.types.can_interface

        out["can_interface"] = (
            capo_iotfleetwise.types.can_interface.deserialize_aws_json_1_0(
                data["canInterface"]
            )
        )
    if data.get("obdInterface") is not None:
        import capo_iotfleetwise.types.obd_interface

        out["obd_interface"] = (
            capo_iotfleetwise.types.obd_interface.deserialize_aws_json_1_0(
                data["obdInterface"]
            )
        )
    if data.get("vehicleMiddleware") is not None:
        import capo_iotfleetwise.types.vehicle_middleware

        out["vehicle_middleware"] = (
            capo_iotfleetwise.types.vehicle_middleware.deserialize_aws_json_1_0(
                data["vehicleMiddleware"]
            )
        )
    if data.get("customDecodingInterface") is not None:
        import capo_iotfleetwise.types.custom_decoding_interface

        out["custom_decoding_interface"] = (
            capo_iotfleetwise.types.custom_decoding_interface.deserialize_aws_json_1_0(
                data["customDecodingInterface"]
            )
        )
    return out

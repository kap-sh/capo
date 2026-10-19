"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#VehicleMiddleware``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.vehicle_middleware_name
    import capo_iotfleetwise.types.vehicle_middleware_protocol


class VehicleMiddleware(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.vehicle_middleware_name.VehicleMiddlewareName"
    """<p>The name of the vehicle middleware. </p>"""
    protocol_name: (
        "capo_iotfleetwise.types.vehicle_middleware_protocol.VehicleMiddlewareProtocol"
    )
    """<p>The protocol name of the vehicle middleware. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VehicleMiddleware) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_iotfleetwise.types.vehicle_middleware_protocol

    out["protocolName"] = (
        capo_iotfleetwise.types.vehicle_middleware_protocol.serialize_aws_json_1_0(
            value["protocol_name"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> VehicleMiddleware:
    out: VehicleMiddleware = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("protocolName") is not None:
        import capo_iotfleetwise.types.vehicle_middleware_protocol

        out["protocol_name"] = (
            capo_iotfleetwise.types.vehicle_middleware_protocol.deserialize_aws_json_1_0(
                data["protocolName"]
            )
        )
    else:
        import typing

        out["protocol_name"] = typing.cast(
            "capo_iotfleetwise.types.vehicle_middleware_protocol.VehicleMiddlewareProtocol",
            "",
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateVTLDeviceTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.device_type
    import capo_storage_gateway.types.vtl_device_arn


class UpdateVTLDeviceTypeInput(TypedDict, closed=True):
    vtl_device_arn: "capo_storage_gateway.types.vtl_device_arn.VTLDeviceARN"
    """<p>The Amazon Resource Name (ARN) of the medium changer you want to select.</p>"""
    device_type: "capo_storage_gateway.types.device_type.DeviceType"
    """<p>The type of medium changer you want to select.</p> <p>Valid Values: <code>STK-L700</code> | <code>AWS-Gateway-VTL</code> | <code>IBM-03584L32-0402</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateVTLDeviceTypeInput) -> dict:
    out: dict = {}
    out["VTLDeviceARN"] = value["vtl_device_arn"]
    out["DeviceType"] = value["device_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateVTLDeviceTypeInput:
    out: UpdateVTLDeviceTypeInput = {}  # type: ignore[typeddict-item]
    if data.get("VTLDeviceARN") is not None:
        out["vtl_device_arn"] = data["VTLDeviceARN"]
    else:
        out["vtl_device_arn"] = ""
    if data.get("DeviceType") is not None:
        out["device_type"] = data["DeviceType"]
    else:
        out["device_type"] = ""
    return out

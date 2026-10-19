"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeVTLDevicesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.marker
    import capo_storage_gateway.types.positive_int_object
    import capo_storage_gateway.types.vtl_device_ar_ns


class DescribeVTLDevicesInput(TypedDict, closed=True):
    gateway_arn: "capo_storage_gateway.types.gateway_arn.GatewayARN"
    vtl_device_ar_ns: NotRequired[
        "capo_storage_gateway.types.vtl_device_ar_ns.VTLDeviceARNs"
    ]
    """<p>An array of strings, where each string represents the Amazon Resource Name (ARN) of a VTL device.</p> <note> <p>All of the specified VTL devices must be from the same gateway. If no VTL devices are specified, the result will contain all devices on the specified gateway.</p> </note>"""
    marker: NotRequired["capo_storage_gateway.types.marker.Marker"]
    """<p>An opaque string that indicates the position at which to begin describing the VTL devices.</p>"""
    limit: NotRequired[
        "capo_storage_gateway.types.positive_int_object.PositiveIntObject"
    ]
    """<p>Specifies that the number of VTL devices described be limited to the specified number.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeVTLDevicesInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    if "vtl_device_ar_ns" in value:
        import capo_storage_gateway.types.vtl_device_ar_ns

        out["VTLDeviceARNs"] = (
            capo_storage_gateway.types.vtl_device_ar_ns.serialize_aws_json_1_1(
                value["vtl_device_ar_ns"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeVTLDevicesInput:
    out: DescribeVTLDevicesInput = {}  # type: ignore[typeddict-item]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        out["gateway_arn"] = ""
    if data.get("VTLDeviceARNs") is not None:
        import capo_storage_gateway.types.vtl_device_ar_ns

        out["vtl_device_ar_ns"] = (
            capo_storage_gateway.types.vtl_device_ar_ns.deserialize_aws_json_1_1(
                data["VTLDeviceARNs"]
            )
        )
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out

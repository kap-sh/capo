"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ListCoreDevicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.core_device_runtime_string
    import capo_greengrassv2.types.core_device_status
    import capo_greengrassv2.types.default_max_results
    import capo_greengrassv2.types.next_token_string
    import capo_greengrassv2.types.thing_group_arn


class ListCoreDevicesRequest(TypedDict, closed=True):
    thing_group_arn: NotRequired[
        "capo_greengrassv2.types.thing_group_arn.ThingGroupARN"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the IoT thing group by which to filter. If you specify this parameter, the list includes only core devices that have successfully deployed a deployment that targets the thing group. When you remove a core device from a thing group, the list continues to include that core device.</p>"""
    status: NotRequired["capo_greengrassv2.types.core_device_status.CoreDeviceStatus"]
    """<p>The core device status by which to filter. If you specify this parameter, the list includes only core devices that have this status. Choose one of the following options:</p> <ul> <li> <p> <code>HEALTHY</code> – The IoT Greengrass Core software and all components run on the core device without issue.</p> </li> <li> <p> <code>UNHEALTHY</code> – The IoT Greengrass Core software or a component is in a failed state on the core device.</p> </li> </ul>"""
    max_results: NotRequired[
        "capo_greengrassv2.types.default_max_results.DefaultMaxResults"
    ]
    """<p>The maximum number of results to be returned per paginated request.</p>"""
    next_token: NotRequired["capo_greengrassv2.types.next_token_string.NextTokenString"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    runtime: NotRequired[
        "capo_greengrassv2.types.core_device_runtime_string.CoreDeviceRuntimeString"
    ]
    """<p>The runtime to be used by the core device. The runtime can be:</p> <ul> <li> <p> <code>aws_nucleus_classic</code> </p> </li> <li> <p> <code>aws_nucleus_lite</code> </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoreDevicesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListCoreDevicesRequest:
    out: ListCoreDevicesRequest = {}  # type: ignore[typeddict-item]
    return out

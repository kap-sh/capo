"""Generated from Smithy shape ``com.amazonaws.iotevents#RoutedResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.amazon_resource_name
    import capo_iot_events.types.resource_name


class RoutedResource(TypedDict, closed=True):
    name: NotRequired["capo_iot_events.types.resource_name.ResourceName"]
    """<p> The name of the routed resource. </p>"""
    arn: NotRequired["capo_iot_events.types.amazon_resource_name.AmazonResourceName"]
    """<p> The ARN of the routed resource. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs)</a> in the <i>AWS General Reference</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutedResource) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> RoutedResource:
    out: RoutedResource = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out

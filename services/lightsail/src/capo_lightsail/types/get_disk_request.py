"""Generated from Smithy shape ``com.amazonaws.lightsail#GetDiskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class GetDiskRequest(TypedDict, closed=True):
    disk_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the disk (<code>my-disk</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDiskRequest) -> dict:
    out: dict = {}
    out["diskName"] = value["disk_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDiskRequest:
    out: GetDiskRequest = {}  # type: ignore[typeddict-item]
    if data.get("diskName") is not None:
        out["disk_name"] = data["diskName"]
    else:
        out["disk_name"] = ""
    return out

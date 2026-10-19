"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteDiskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.boolean
    import capo_lightsail.types.resource_name


class DeleteDiskRequest(TypedDict, closed=True):
    disk_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The unique name of the disk you want to delete (<code>my-disk</code>).</p>"""
    force_delete_add_ons: NotRequired["capo_lightsail.types.boolean.boolean"]
    """<p>A Boolean value to indicate whether to delete all add-ons for the disk.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDiskRequest) -> dict:
    out: dict = {}
    out["diskName"] = value["disk_name"]
    if "force_delete_add_ons" in value:
        out["forceDeleteAddOns"] = value["force_delete_add_ons"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDiskRequest:
    out: DeleteDiskRequest = {}  # type: ignore[typeddict-item]
    if data.get("diskName") is not None:
        out["disk_name"] = data["diskName"]
    else:
        out["disk_name"] = ""
    if data.get("forceDeleteAddOns") is not None:
        out["force_delete_add_ons"] = data["forceDeleteAddOns"]
    return out

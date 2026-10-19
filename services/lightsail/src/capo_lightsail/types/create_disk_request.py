"""Generated from Smithy shape ``com.amazonaws.lightsail#CreateDiskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.add_on_request_list
    import capo_lightsail.types.integer
    import capo_lightsail.types.non_empty_string
    import capo_lightsail.types.resource_name
    import capo_lightsail.types.tag_list


class CreateDiskRequest(TypedDict, closed=True):
    disk_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The unique Lightsail disk name (<code>my-disk</code>).</p>"""
    availability_zone: "capo_lightsail.types.non_empty_string.NonEmptyString"
    """<p>The Availability Zone where you want to create the disk (<code>us-east-2a</code>). Use the same Availability Zone as the Lightsail instance to which you want to attach the disk.</p> <p>Use the <code>get regions</code> operation to list the Availability Zones where Lightsail is currently available.</p>"""
    size_in_gb: "capo_lightsail.types.integer.integer"
    """<p>The size of the disk in GB (<code>32</code>).</p>"""
    tags: NotRequired["capo_lightsail.types.tag_list.TagList"]
    """<p>The tag keys and optional values to add to the resource during create.</p> <p>Use the <code>TagResource</code> action to tag a resource after it's created.</p>"""
    add_ons: NotRequired["capo_lightsail.types.add_on_request_list.AddOnRequestList"]
    """<p>An array of objects that represent the add-ons to enable for the new disk.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDiskRequest) -> dict:
    out: dict = {}
    out["diskName"] = value["disk_name"]
    out["availabilityZone"] = value["availability_zone"]
    out["sizeInGb"] = value["size_in_gb"]
    if "tags" in value:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "add_ons" in value:
        import capo_lightsail.types.add_on_request_list

        out["addOns"] = capo_lightsail.types.add_on_request_list.serialize_aws_json_1_1(
            value["add_ons"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDiskRequest:
    out: CreateDiskRequest = {}  # type: ignore[typeddict-item]
    if data.get("diskName") is not None:
        out["disk_name"] = data["diskName"]
    else:
        out["disk_name"] = ""
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    else:
        out["availability_zone"] = ""
    if data.get("sizeInGb") is not None:
        out["size_in_gb"] = data["sizeInGb"]
    else:
        out["size_in_gb"] = 0
    if data.get("tags") is not None:
        import capo_lightsail.types.tag_list

        out["tags"] = capo_lightsail.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("addOns") is not None:
        import capo_lightsail.types.add_on_request_list

        out["add_ons"] = (
            capo_lightsail.types.add_on_request_list.deserialize_aws_json_1_1(
                data["addOns"]
            )
        )
    return out

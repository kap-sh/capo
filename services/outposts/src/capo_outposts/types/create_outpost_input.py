"""Generated from Smithy shape ``com.amazonaws.outposts#CreateOutpostInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.availability_zone
    import capo_outposts.types.availability_zone_id
    import capo_outposts.types.outpost_description
    import capo_outposts.types.outpost_name
    import capo_outposts.types.site_id
    import capo_outposts.types.supported_hardware_type
    import capo_outposts.types.tag_map


class CreateOutpostInput(TypedDict, closed=True):
    name: "capo_outposts.types.outpost_name.OutpostName"
    description: NotRequired[
        "capo_outposts.types.outpost_description.OutpostDescription"
    ]
    site_id: "capo_outposts.types.site_id.SiteId"
    """<p> The ID or the Amazon Resource Name (ARN) of the site. </p>"""
    availability_zone: NotRequired[
        "capo_outposts.types.availability_zone.AvailabilityZone"
    ]
    availability_zone_id: NotRequired[
        "capo_outposts.types.availability_zone_id.AvailabilityZoneId"
    ]
    tags: NotRequired["capo_outposts.types.tag_map.TagMap"]
    """<p>The tags to apply to the Outpost.</p>"""
    supported_hardware_type: NotRequired[
        "capo_outposts.types.supported_hardware_type.SupportedHardwareType"
    ]
    """<p> The type of hardware for this Outpost. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateOutpostInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["SiteId"] = value["site_id"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["AvailabilityZoneId"] = value["availability_zone_id"]
    if "tags" in value:
        import capo_outposts.types.tag_map

        out["Tags"] = capo_outposts.types.tag_map.serialize_json(value["tags"])
    if "supported_hardware_type" in value:
        import capo_outposts.types.supported_hardware_type

        out["SupportedHardwareType"] = (
            capo_outposts.types.supported_hardware_type.serialize_json(
                value["supported_hardware_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateOutpostInput:
    out: CreateOutpostInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SiteId") is not None:
        out["site_id"] = data["SiteId"]
    else:
        out["site_id"] = ""
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("AvailabilityZoneId") is not None:
        out["availability_zone_id"] = data["AvailabilityZoneId"]
    if data.get("Tags") is not None:
        import capo_outposts.types.tag_map

        out["tags"] = capo_outposts.types.tag_map.deserialize_json(data["Tags"])
    if data.get("SupportedHardwareType") is not None:
        import capo_outposts.types.supported_hardware_type

        out["supported_hardware_type"] = (
            capo_outposts.types.supported_hardware_type.deserialize_json(
                data["SupportedHardwareType"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.outposts#CreateSiteInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_outposts.errors import DeserializationError

if TYPE_CHECKING:
    import capo_outposts.types.address
    import capo_outposts.types.rack_physical_properties
    import capo_outposts.types.site_description
    import capo_outposts.types.site_name
    import capo_outposts.types.site_notes
    import capo_outposts.types.tag_map


class CreateSiteInput(TypedDict, closed=True):
    name: "capo_outposts.types.site_name.SiteName"
    description: NotRequired["capo_outposts.types.site_description.SiteDescription"]
    notes: NotRequired["capo_outposts.types.site_notes.SiteNotes"]
    """<p>Additional information that you provide about site access requirements, electrician scheduling, personal protective equipment, or regulation of equipment materials that could affect your installation process. </p>"""
    tags: NotRequired["capo_outposts.types.tag_map.TagMap"]
    """<p> The tags to apply to a site. </p>"""
    operating_address: NotRequired["capo_outposts.types.address.Address"]
    """<p> The location to install and power on the hardware. This address might be different from the shipping address. </p>"""
    shipping_address: NotRequired["capo_outposts.types.address.Address"]
    """<p> The location to ship the hardware. This address might be different from the operating address. </p>"""
    rack_physical_properties: NotRequired[
        "capo_outposts.types.rack_physical_properties.RackPhysicalProperties"
    ]
    """<p> Information about the physical and logistical details for the rack at this site. For more information about hardware requirements for racks, see <a href="https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#checklist">Network readiness checklist</a> in the Amazon Web Services Outposts User Guide. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSiteInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "notes" in value:
        out["Notes"] = value["notes"]
    if "tags" in value:
        import capo_outposts.types.tag_map

        out["Tags"] = capo_outposts.types.tag_map.serialize_json(value["tags"])
    if "operating_address" in value:
        import capo_outposts.types.address

        out["OperatingAddress"] = capo_outposts.types.address.serialize_json(
            value["operating_address"]
        )
    if "shipping_address" in value:
        import capo_outposts.types.address

        out["ShippingAddress"] = capo_outposts.types.address.serialize_json(
            value["shipping_address"]
        )
    if "rack_physical_properties" in value:
        import capo_outposts.types.rack_physical_properties

        out["RackPhysicalProperties"] = (
            capo_outposts.types.rack_physical_properties.serialize_json(
                value["rack_physical_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateSiteInput:
    out: CreateSiteInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateSiteInput.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Notes") is not None:
        out["notes"] = data["Notes"]
    if data.get("Tags") is not None:
        import capo_outposts.types.tag_map

        out["tags"] = capo_outposts.types.tag_map.deserialize_json(data["Tags"])
    if data.get("OperatingAddress") is not None:
        import capo_outposts.types.address

        out["operating_address"] = capo_outposts.types.address.deserialize_json(
            data["OperatingAddress"]
        )
    if data.get("ShippingAddress") is not None:
        import capo_outposts.types.address

        out["shipping_address"] = capo_outposts.types.address.deserialize_json(
            data["ShippingAddress"]
        )
    if data.get("RackPhysicalProperties") is not None:
        import capo_outposts.types.rack_physical_properties

        out["rack_physical_properties"] = (
            capo_outposts.types.rack_physical_properties.deserialize_json(
                data["RackPhysicalProperties"]
            )
        )
    return out

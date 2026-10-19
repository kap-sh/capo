"""Generated from Smithy shape ``com.amazonaws.s3control#CreateMultiRegionAccessPointInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.multi_region_access_point_name
    import capo_s3_control.types.public_access_block_configuration
    import capo_s3_control.types.region_creation_list


class CreateMultiRegionAccessPointInput(TypedDict, closed=True):
    name: "capo_s3_control.types.multi_region_access_point_name.MultiRegionAccessPointName"
    """<p>The name of the Multi-Region Access Point associated with this request.</p>"""
    public_access_block: NotRequired[
        "capo_s3_control.types.public_access_block_configuration.PublicAccessBlockConfiguration"
    ]
    regions: "capo_s3_control.types.region_creation_list.RegionCreationList"
    """<p>The buckets in different Regions that are associated with the Multi-Region Access Point.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateMultiRegionAccessPointInput, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Name").text = str(value["name"])
    if "public_access_block" in value:
        import capo_s3_control.types.public_access_block_configuration

        capo_s3_control.types.public_access_block_configuration.serialize_xml(
            value["public_access_block"], el, "PublicAccessBlock"
        )
    import capo_s3_control.types.region_creation_list

    capo_s3_control.types.region_creation_list.serialize_xml(
        value["regions"], el, "Regions"
    )


def deserialize_xml(el: Element) -> CreateMultiRegionAccessPointInput:
    out: CreateMultiRegionAccessPointInput = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        out["name"] = ""
    child_public_access_block = el.find("PublicAccessBlock")
    if child_public_access_block is not None:
        import capo_s3_control.types.public_access_block_configuration

        out["public_access_block"] = (
            capo_s3_control.types.public_access_block_configuration.deserialize_xml(
                child_public_access_block
            )
        )
    child_regions = el.find("Regions")
    if child_regions is not None:
        import capo_s3_control.types.region_creation_list

        out["regions"] = capo_s3_control.types.region_creation_list.deserialize_xml(
            child_regions
        )
    else:
        out["regions"] = []
    return out

"""Generated from Smithy shape ``com.amazonaws.s3control#MultiRegionAccessPointReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.creation_timestamp
    import capo_s3_control.types.multi_region_access_point_alias
    import capo_s3_control.types.multi_region_access_point_name
    import capo_s3_control.types.multi_region_access_point_status
    import capo_s3_control.types.public_access_block_configuration
    import capo_s3_control.types.region_report_list


class MultiRegionAccessPointReport(TypedDict, closed=True):
    name: NotRequired[
        "capo_s3_control.types.multi_region_access_point_name.MultiRegionAccessPointName"
    ]
    """<p>The name of the Multi-Region Access Point.</p>"""
    alias: NotRequired[
        "capo_s3_control.types.multi_region_access_point_alias.MultiRegionAccessPointAlias"
    ]
    """<p>The alias for the Multi-Region Access Point. For more information about the distinction between the name and the alias of an Multi-Region Access Point, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/CreatingMultiRegionAccessPoints.html#multi-region-access-point-naming">Rules for naming Amazon S3 Multi-Region Access Points</a>.</p>"""
    created_at: NotRequired[
        "capo_s3_control.types.creation_timestamp.CreationTimestamp"
    ]
    """<p>When the Multi-Region Access Point create request was received.</p>"""
    public_access_block: NotRequired[
        "capo_s3_control.types.public_access_block_configuration.PublicAccessBlockConfiguration"
    ]
    status: NotRequired[
        "capo_s3_control.types.multi_region_access_point_status.MultiRegionAccessPointStatus"
    ]
    """<p>The current status of the Multi-Region Access Point.</p> <p> <code>CREATING</code> and <code>DELETING</code> are temporary states that exist while the request is propagating and being completed. If a Multi-Region Access Point has a status of <code>PARTIALLY_CREATED</code>, you can retry creation or send a request to delete the Multi-Region Access Point. If a Multi-Region Access Point has a status of <code>PARTIALLY_DELETED</code>, you can retry a delete request to finish the deletion of the Multi-Region Access Point.</p>"""
    regions: NotRequired["capo_s3_control.types.region_report_list.RegionReportList"]
    """<p>A collection of the Regions and buckets associated with the Multi-Region Access Point.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: MultiRegionAccessPointReport, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "name" in value:
        SubElement(el, "Name").text = str(value["name"])
    if "alias" in value:
        SubElement(el, "Alias").text = str(value["alias"])
    if "created_at" in value:
        import capo_s3_control.types.creation_timestamp

        capo_s3_control.types.creation_timestamp.serialize_xml(
            value["created_at"], el, "CreatedAt"
        )
    if "public_access_block" in value:
        import capo_s3_control.types.public_access_block_configuration

        capo_s3_control.types.public_access_block_configuration.serialize_xml(
            value["public_access_block"], el, "PublicAccessBlock"
        )
    if "status" in value:
        import capo_s3_control.types.multi_region_access_point_status

        capo_s3_control.types.multi_region_access_point_status.serialize_xml(
            value["status"], el, "Status"
        )
    if "regions" in value:
        import capo_s3_control.types.region_report_list

        capo_s3_control.types.region_report_list.serialize_xml(
            value["regions"], el, "Regions"
        )


def deserialize_xml(el: Element) -> MultiRegionAccessPointReport:
    out: MultiRegionAccessPointReport = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_alias = el.find("Alias")
    if child_alias is not None:
        out["alias"] = str(child_alias.text or "")
    child_created_at = el.find("CreatedAt")
    if child_created_at is not None:
        import capo_s3_control.types.creation_timestamp

        out["created_at"] = capo_s3_control.types.creation_timestamp.deserialize_xml(
            child_created_at
        )
    child_public_access_block = el.find("PublicAccessBlock")
    if child_public_access_block is not None:
        import capo_s3_control.types.public_access_block_configuration

        out["public_access_block"] = (
            capo_s3_control.types.public_access_block_configuration.deserialize_xml(
                child_public_access_block
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        import capo_s3_control.types.multi_region_access_point_status

        out["status"] = (
            capo_s3_control.types.multi_region_access_point_status.deserialize_xml(
                child_status
            )
        )
    child_regions = el.find("Regions")
    if child_regions is not None:
        import capo_s3_control.types.region_report_list

        out["regions"] = capo_s3_control.types.region_report_list.deserialize_xml(
            child_regions
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.s3control#MultiRegionAccessPointRoute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.bucket_name
    import capo_s3_control.types.region_name
    import capo_s3_control.types.traffic_dial_percentage


class MultiRegionAccessPointRoute(TypedDict, closed=True):
    bucket: NotRequired["capo_s3_control.types.bucket_name.BucketName"]
    """<p>The name of the Amazon S3 bucket for which you'll submit a routing configuration change. Either the <code>Bucket</code> or the <code>Region</code> value must be provided. If both are provided, the bucket must be in the specified Region.</p>"""
    region: NotRequired["capo_s3_control.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region to which you'll be submitting a routing configuration change. Either the <code>Bucket</code> or the <code>Region</code> value must be provided. If both are provided, the bucket must be in the specified Region.</p>"""
    traffic_dial_percentage: (
        "capo_s3_control.types.traffic_dial_percentage.TrafficDialPercentage"
    )
    """<p>The traffic state for the specified bucket or Amazon Web Services Region. </p> <p>A value of <code>0</code> indicates a passive state, which means that no new traffic will be routed to the Region. </p> <p>A value of <code>100</code> indicates an active state, which means that traffic will be routed to the specified Region. </p> <p>When the routing configuration for a Region is changed from active to passive, any in-progress operations (uploads, copies, deletes, and so on) to the formerly active Region will continue to run to until a final success or failure status is reached.</p> <p>If all Regions in the routing configuration are designated as passive, you'll receive an <code>InvalidRequest</code> error.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: MultiRegionAccessPointRoute, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "bucket" in value:
        SubElement(el, "Bucket").text = str(value["bucket"])
    if "region" in value:
        SubElement(el, "Region").text = str(value["region"])
    SubElement(el, "TrafficDialPercentage").text = str(value["traffic_dial_percentage"])


def deserialize_xml(el: Element) -> MultiRegionAccessPointRoute:
    out: MultiRegionAccessPointRoute = {}  # type: ignore[typeddict-item]
    child_bucket = el.find("Bucket")
    if child_bucket is not None:
        out["bucket"] = str(child_bucket.text or "")
    child_region = el.find("Region")
    if child_region is not None:
        out["region"] = str(child_region.text or "")
    child_traffic_dial_percentage = el.find("TrafficDialPercentage")
    if child_traffic_dial_percentage is not None:
        out["traffic_dial_percentage"] = int(child_traffic_dial_percentage.text or "")
    else:
        out["traffic_dial_percentage"] = 0
    return out

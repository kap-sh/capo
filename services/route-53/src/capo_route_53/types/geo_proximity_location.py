"""Generated from Smithy shape ``com.amazonaws.route53#GeoProximityLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.aws_region
    import capo_route_53.types.bias
    import capo_route_53.types.coordinates
    import capo_route_53.types.local_zone_group


class GeoProximityLocation(TypedDict, closed=True):
    aws_region: NotRequired["capo_route_53.types.aws_region.AWSRegion"]
    """<p> The Amazon Web Services Region the resource you are directing DNS traffic to, is in. </p>"""
    local_zone_group: NotRequired["capo_route_53.types.local_zone_group.LocalZoneGroup"]
    """<p> Specifies an Amazon Web Services Local Zone Group. </p> <p>A local Zone Group is usually the Local Zone code without the ending character. For example, if the Local Zone is <code>us-east-1-bue-1a</code> the Local Zone Group is <code>us-east-1-bue-1</code>.</p> <p>You can identify the Local Zones Group for a specific Local Zone by using the <a href="https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html">describe-availability-zones</a> CLI command:</p> <p>This command returns: <code>"GroupName": "us-west-2-den-1"</code>, specifying that the Local Zone <code>us-west-2-den-1a</code> belongs to the Local Zone Group <code>us-west-2-den-1</code>.</p>"""
    coordinates: NotRequired["capo_route_53.types.coordinates.Coordinates"]
    """<p> Contains the longitude and latitude for a geographic region. </p>"""
    bias: NotRequired["capo_route_53.types.bias.Bias"]
    """<p> The bias increases or decreases the size of the geographic region from which Route 53 routes traffic to a resource. </p> <p>To use <code>Bias</code> to change the size of the geographic region, specify the applicable value for the bias:</p> <ul> <li> <p>To expand the size of the geographic region from which Route 53 routes traffic to a resource, specify a positive integer from 1 to 99 for the bias. Route 53 shrinks the size of adjacent regions. </p> </li> <li> <p>To shrink the size of the geographic region from which Route 53 routes traffic to a resource, specify a negative bias of -1 to -99. Route 53 expands the size of adjacent regions. </p> </li> </ul>"""


# --- restXml ser/de ---
def serialize_xml(value: GeoProximityLocation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "aws_region" in value:
        SubElement(el, "AWSRegion").text = str(value["aws_region"])
    if "local_zone_group" in value:
        SubElement(el, "LocalZoneGroup").text = str(value["local_zone_group"])
    if "coordinates" in value:
        import capo_route_53.types.coordinates

        capo_route_53.types.coordinates.serialize_xml(
            value["coordinates"], el, "Coordinates"
        )
    if "bias" in value:
        SubElement(el, "Bias").text = str(value["bias"])


def deserialize_xml(el: Element) -> GeoProximityLocation:
    out: GeoProximityLocation = {}  # type: ignore[typeddict-item]
    child_aws_region = el.find("AWSRegion")
    if child_aws_region is not None:
        out["aws_region"] = str(child_aws_region.text or "")
    child_local_zone_group = el.find("LocalZoneGroup")
    if child_local_zone_group is not None:
        out["local_zone_group"] = str(child_local_zone_group.text or "")
    child_coordinates = el.find("Coordinates")
    if child_coordinates is not None:
        import capo_route_53.types.coordinates

        out["coordinates"] = capo_route_53.types.coordinates.deserialize_xml(
            child_coordinates
        )
    child_bias = el.find("Bias")
    if child_bias is not None:
        out["bias"] = int(child_bias.text or "")
    return out

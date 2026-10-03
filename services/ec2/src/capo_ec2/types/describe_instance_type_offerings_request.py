"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceTypeOfferingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.dito_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.location_type
    import capo_ec2.types.next_token


class DescribeInstanceTypeOfferingsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    location_type: NotRequired["capo_ec2.types.location_type.LocationType"]
    """<p>The location type.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone. When you specify a location filter, it must be an Availability Zone for the current Region.</p> </li> <li> <p> <code>availability-zone-id</code> - The AZ ID. When you specify a location filter, it must be an AZ ID for the current Region.</p> </li> <li> <p> <code>outpost</code> - The Outpost ARN. When you specify a location filter, it must be an Outpost ARN for the current Region.</p> </li> <li> <p> <code>region</code> - The current Region. If you specify a location filter, it must match the current Region.</p> </li> </ul>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>One or more filters. Filter names and values are case-sensitive.</p> <ul> <li> <p> <code>instance-type</code> - The instance type. For a list of possible values, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Instance.html">Instance</a>.</p> </li> <li> <p> <code>location</code> - The location. For a list of possible identifiers, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html">Regions and Zones</a>.</p> </li> </ul>"""
    max_results: NotRequired["capo_ec2.types.dito_max_results.DITOMaxResults"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    next_token: NotRequired["capo_ec2.types.next_token.NextToken"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceTypeOfferingsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "location_type" in value:
        import capo_ec2.types.location_type

        capo_ec2.types.location_type.serialize_ec2_query(
            value["location_type"], pairs, f"{key_prefix}LocationType"
        )
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_ec2_query(el: Element) -> DescribeInstanceTypeOfferingsRequest:
    out: DescribeInstanceTypeOfferingsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_location_type = el.find("LocationType")
    if child_location_type is not None:
        import capo_ec2.types.location_type

        out["location_type"] = capo_ec2.types.location_type.deserialize_ec2_query(
            child_location_type
        )
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out

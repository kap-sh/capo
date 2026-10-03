"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.fleet_id_set
    import capo_ec2.types.integer
    import capo_ec2.types.string


class DescribeFleetsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    max_results: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    fleet_ids: NotRequired["capo_ec2.types.fleet_id_set.FleetIdSet"]
    """<p>The IDs of the EC2 Fleets.</p> <note> <p>If a fleet is of type <code>instant</code>, you must specify the fleet ID, otherwise it does not appear in the response.</p> </note>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>activity-status</code> - The progress of the EC2 Fleet ( <code>error</code> | <code>pending-fulfillment</code> | <code>pending-termination</code> | <code>fulfilled</code>).</p> </li> <li> <p> <code>excess-capacity-termination-policy</code> - Indicates whether to terminate running instances if the target capacity is decreased below the current EC2 Fleet size (<code>true</code> | <code>false</code>).</p> </li> <li> <p> <code>fleet-state</code> - The state of the EC2 Fleet (<code>submitted</code> | <code>active</code> | <code>deleted</code> | <code>failed</code> | <code>deleted-running</code> | <code>deleted-terminating</code> | <code>modifying</code>).</p> </li> <li> <p> <code>replace-unhealthy-instances</code> - Indicates whether EC2 Fleet should replace unhealthy instances (<code>true</code> | <code>false</code>).</p> </li> <li> <p> <code>type</code> - The type of request (<code>instant</code> | <code>request</code> | <code>maintain</code>).</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFleetsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "fleet_ids" in value:
        import capo_ec2.types.fleet_id_set

        capo_ec2.types.fleet_id_set.serialize_ec2_query(
            value["fleet_ids"], pairs, f"{key_prefix}FleetId"
        )
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )


def deserialize_ec2_query(el: Element) -> DescribeFleetsRequest:
    out: DescribeFleetsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_fleet_ids = el.find("FleetId")
    if child_fleet_ids is not None:
        import capo_ec2.types.fleet_id_set

        out["fleet_ids"] = capo_ec2.types.fleet_id_set.deserialize_ec2_query(
            child_fleet_ids
        )
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    return out

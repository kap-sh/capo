"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceTopologyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_instance_topology_group_name_set
    import capo_ec2.types.describe_instance_topology_instance_id_set
    import capo_ec2.types.describe_instance_topology_max_results
    import capo_ec2.types.filter_list
    import capo_ec2.types.string


class DescribeInstanceTopologyRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_instance_topology_max_results.DescribeInstanceTopologyMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p> <p>You can't specify this parameter and the instance IDs parameter in the same request.</p> <p>Default: <code>20</code> </p>"""
    instance_ids: NotRequired[
        "capo_ec2.types.describe_instance_topology_instance_id_set.DescribeInstanceTopologyInstanceIdSet"
    ]
    """<p>The instance IDs.</p> <p>Default: Describes all your instances.</p> <p>Constraints: Maximum 100 explicitly specified instance IDs.</p>"""
    group_names: NotRequired[
        "capo_ec2.types.describe_instance_topology_group_name_set.DescribeInstanceTopologyGroupNameSet"
    ]
    """<p>The name of the placement group that each instance is in.</p> <p>Constraints: Maximum 100 explicitly specified placement group names.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The name of the Availability Zone (for example, <code>us-west-2a</code>) or Local Zone (for example, <code>us-west-2-lax-1b</code>) that the instance is in.</p> </li> <li> <p> <code>instance-type</code> - The instance type (for example, <code>p4d.24xlarge</code>) or instance family (for example, <code>p4d*</code>). You can use the <code>*</code> wildcard to match zero or more characters, or the <code>?</code> wildcard to match zero or one character.</p> </li> <li> <p> <code>zone-id</code> - The ID of the Availability Zone (for example, <code>usw2-az2</code>) or Local Zone (for example, <code>usw2-lax1-az1</code>) that the instance is in.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceTopologyRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "instance_ids" in value:
        import capo_ec2.types.describe_instance_topology_instance_id_set

        capo_ec2.types.describe_instance_topology_instance_id_set.serialize_ec2_query(
            value["instance_ids"], pairs, f"{key_prefix}InstanceId"
        )
    if "group_names" in value:
        import capo_ec2.types.describe_instance_topology_group_name_set

        capo_ec2.types.describe_instance_topology_group_name_set.serialize_ec2_query(
            value["group_names"], pairs, f"{key_prefix}GroupName"
        )
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )


def deserialize_ec2_query(el: Element) -> DescribeInstanceTopologyRequest:
    out: DescribeInstanceTopologyRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_instance_ids = el.find("InstanceId")
    if child_instance_ids is not None:
        import capo_ec2.types.describe_instance_topology_instance_id_set

        out["instance_ids"] = (
            capo_ec2.types.describe_instance_topology_instance_id_set.deserialize_ec2_query(
                child_instance_ids
            )
        )
    child_group_names = el.find("GroupName")
    if child_group_names is not None:
        import capo_ec2.types.describe_instance_topology_group_name_set

        out["group_names"] = (
            capo_ec2.types.describe_instance_topology_group_name_set.deserialize_ec2_query(
                child_group_names
            )
        )
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    return out

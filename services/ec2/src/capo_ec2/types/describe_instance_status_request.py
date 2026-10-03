"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.instance_id_string_list
    import capo_ec2.types.integer
    import capo_ec2.types.string


class DescribeInstanceStatusRequest(TypedDict, closed=True):
    instance_ids: NotRequired[
        "capo_ec2.types.instance_id_string_list.InstanceIdStringList"
    ]
    """<p>The instance IDs.</p> <p>Default: Describes all your instances.</p> <p>Constraints: Maximum 100 explicitly specified instance IDs.</p>"""
    max_results: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p> <p>You cannot specify this parameter and the instance IDs parameter in the same request.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    include_managed_resources: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to include managed resources in the output. If this parameter is set to <code>true</code>, the output includes resources that are managed by Amazon Web Services services, even if managed resource visibility is set to hidden.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone</code> - The Availability Zone of the instance.</p> </li> <li> <p> <code>availability-zone-id</code> - The ID of the Availability Zone of the instance.</p> </li> <li> <p> <code>event.code</code> - The code for the scheduled event (<code>instance-reboot</code> | <code>system-reboot</code> | <code>system-maintenance</code> | <code>instance-retirement</code> | <code>instance-stop</code>).</p> </li> <li> <p> <code>event.description</code> - A description of the event.</p> </li> <li> <p> <code>event.instance-event-id</code> - The ID of the event whose date and time you are modifying.</p> </li> <li> <p> <code>event.not-after</code> - The latest end time for the scheduled event (for example, <code>2014-09-15T17:15:20.000Z</code>).</p> </li> <li> <p> <code>event.not-before</code> - The earliest start time for the scheduled event (for example, <code>2014-09-15T17:15:20.000Z</code>).</p> </li> <li> <p> <code>event.not-before-deadline</code> - The deadline for starting the event (for example, <code>2014-09-15T17:15:20.000Z</code>).</p> </li> <li> <p> <code>instance-state-code</code> - The code for the instance state, as a 16-bit unsigned integer. The high byte is used for internal purposes and should be ignored. The low byte is set based on the state represented. The valid values are 0 (pending), 16 (running), 32 (shutting-down), 48 (terminated), 64 (stopping), and 80 (stopped).</p> </li> <li> <p> <code>instance-state-name</code> - The state of the instance (<code>pending</code> | <code>running</code> | <code>shutting-down</code> | <code>terminated</code> | <code>stopping</code> | <code>stopped</code>).</p> </li> <li> <p> <code>instance-status.reachability</code> - Filters on instance status where the name is <code>reachability</code> (<code>passed</code> | <code>failed</code> | <code>initializing</code> | <code>insufficient-data</code>).</p> </li> <li> <p> <code>instance-status.status</code> - The status of the instance (<code>ok</code> | <code>impaired</code> | <code>initializing</code> | <code>insufficient-data</code> | <code>not-applicable</code>).</p> </li> <li> <p> <code>operator.managed</code> - A Boolean that indicates whether this is a managed instance.</p> </li> <li> <p> <code>operator.principal</code> - The principal that manages the instance. Only valid for managed instances, where <code>managed</code> is <code>true</code>.</p> </li> <li> <p> <code>system-status.reachability</code> - Filters on system status where the name is <code>reachability</code> (<code>passed</code> | <code>failed</code> | <code>initializing</code> | <code>insufficient-data</code>).</p> </li> <li> <p> <code>system-status.status</code> - The system status of the instance (<code>ok</code> | <code>impaired</code> | <code>initializing</code> | <code>insufficient-data</code> | <code>not-applicable</code>).</p> </li> <li> <p> <code>attached-ebs-status.status</code> - The status of the attached EBS volume for the instance (<code>ok</code> | <code>impaired</code> | <code>initializing</code> | <code>insufficient-data</code> | <code>not-applicable</code>).</p> </li> <li> <p> <code>application-status.status</code> - The application status of the instance (<code>ok</code> | <code>impaired</code> | <code>initializing</code> | <code>insufficient-data</code> | <code>not-applicable</code>).</p> </li> </ul>"""
    include_all_instances: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>When <code>true</code>, includes the health status for all instances. When <code>false</code>, includes the health status for running instances only.</p> <p>Default: <code>false</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeInstanceStatusRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_ids" in value:
        import capo_ec2.types.instance_id_string_list

        capo_ec2.types.instance_id_string_list.serialize_ec2_query(
            value["instance_ids"], pairs, f"{key_prefix}InstanceId"
        )
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "include_managed_resources" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeManagedResources",
                "true" if value["include_managed_resources"] else "false",
            )
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )
    if "include_all_instances" in value:
        pairs.append(
            (
                f"{key_prefix}IncludeAllInstances",
                "true" if value["include_all_instances"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> DescribeInstanceStatusRequest:
    out: DescribeInstanceStatusRequest = {}  # type: ignore[typeddict-item]
    child_instance_ids = el.find("InstanceId")
    if child_instance_ids is not None:
        import capo_ec2.types.instance_id_string_list

        out["instance_ids"] = (
            capo_ec2.types.instance_id_string_list.deserialize_ec2_query(
                child_instance_ids
            )
        )
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_include_managed_resources = el.find("IncludeManagedResources")
    if child_include_managed_resources is not None:
        out["include_managed_resources"] = (
            child_include_managed_resources.text or ""
        ).lower() == "true"
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    child_include_all_instances = el.find("includeAllInstances")
    if child_include_all_instances is not None:
        out["include_all_instances"] = (
            child_include_all_instances.text or ""
        ).lower() == "true"
    return out

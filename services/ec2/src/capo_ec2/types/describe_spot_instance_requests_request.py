"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSpotInstanceRequestsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.filter_list
    import capo_ec2.types.integer
    import capo_ec2.types.spot_instance_request_id_list
    import capo_ec2.types.string


class DescribeSpotInstanceRequestsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    max_results: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    spot_instance_request_ids: NotRequired[
        "capo_ec2.types.spot_instance_request_id_list.SpotInstanceRequestIdList"
    ]
    """<p>The IDs of the Spot Instance requests.</p>"""
    filters: NotRequired["capo_ec2.types.filter_list.FilterList"]
    """<p>The filters.</p> <ul> <li> <p> <code>availability-zone-group</code> - The Availability Zone group.</p> </li> <li> <p> <code>create-time</code> - The time stamp when the Spot Instance request was created.</p> </li> <li> <p> <code>fault-code</code> - The fault code related to the request.</p> </li> <li> <p> <code>fault-message</code> - The fault message related to the request.</p> </li> <li> <p> <code>instance-id</code> - The ID of the instance that fulfilled the request.</p> </li> <li> <p> <code>launch-group</code> - The Spot Instance launch group.</p> </li> <li> <p> <code>launch.block-device-mapping.delete-on-termination</code> - Indicates whether the EBS volume is deleted on instance termination.</p> </li> <li> <p> <code>launch.block-device-mapping.device-name</code> - The device name for the volume in the block device mapping (for example, <code>/dev/sdh</code> or <code>xvdh</code>).</p> </li> <li> <p> <code>launch.block-device-mapping.snapshot-id</code> - The ID of the snapshot for the EBS volume.</p> </li> <li> <p> <code>launch.block-device-mapping.volume-size</code> - The size of the EBS volume, in GiB.</p> </li> <li> <p> <code>launch.block-device-mapping.volume-type</code> - The type of EBS volume: <code>gp2</code> or <code>gp3</code> for General Purpose SSD, <code>io1</code> or <code>io2</code> for Provisioned IOPS SSD, <code>st1</code> for Throughput Optimized HDD, <code>sc1</code> for Cold HDD, or <code>standard</code> for Magnetic.</p> </li> <li> <p> <code>launch.group-id</code> - The ID of the security group for the instance.</p> </li> <li> <p> <code>launch.group-name</code> - The name of the security group for the instance.</p> </li> <li> <p> <code>launch.image-id</code> - The ID of the AMI.</p> </li> <li> <p> <code>launch.instance-type</code> - The type of instance (for example, <code>m3.medium</code>).</p> </li> <li> <p> <code>launch.kernel-id</code> - The kernel ID.</p> </li> <li> <p> <code>launch.key-name</code> - The name of the key pair the instance launched with.</p> </li> <li> <p> <code>launch.monitoring-enabled</code> - Whether detailed monitoring is enabled for the Spot Instance.</p> </li> <li> <p> <code>launch.ramdisk-id</code> - The RAM disk ID.</p> </li> <li> <p> <code>launched-availability-zone</code> - The Availability Zone in which the request is launched.</p> </li> <li> <p> <code>launched-availability-zone-id</code> - The ID of the Availability Zone in which the request is launched.</p> </li> <li> <p> <code>network-interface.addresses.primary</code> - Indicates whether the IP address is the primary private IP address.</p> </li> <li> <p> <code>network-interface.delete-on-termination</code> - Indicates whether the network interface is deleted when the instance is terminated.</p> </li> <li> <p> <code>network-interface.description</code> - A description of the network interface.</p> </li> <li> <p> <code>network-interface.device-index</code> - The index of the device for the network interface attachment on the instance.</p> </li> <li> <p> <code>network-interface.group-id</code> - The ID of the security group associated with the network interface.</p> </li> <li> <p> <code>network-interface.network-interface-id</code> - The ID of the network interface.</p> </li> <li> <p> <code>network-interface.private-ip-address</code> - The primary private IP address of the network interface.</p> </li> <li> <p> <code>network-interface.subnet-id</code> - The ID of the subnet for the instance.</p> </li> <li> <p> <code>product-description</code> - The product description associated with the instance (<code>Linux/UNIX</code> | <code>Windows</code>).</p> </li> <li> <p> <code>spot-instance-request-id</code> - The Spot Instance request ID.</p> </li> <li> <p> <code>spot-price</code> - The maximum hourly price for any Spot Instance launched to fulfill the request.</p> </li> <li> <p> <code>state</code> - The state of the Spot Instance request (<code>open</code> | <code>active</code> | <code>closed</code> | <code>cancelled</code> | <code>failed</code>). Spot request status information can help you track your Amazon EC2 Spot Instance requests. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-request-status.html">Spot request status</a> in the <i>Amazon EC2 User Guide</i>.</p> </li> <li> <p> <code>status-code</code> - The short code describing the most recent evaluation of your Spot Instance request.</p> </li> <li> <p> <code>status-message</code> - The message explaining the status of the Spot Instance request.</p> </li> <li> <p> <code>tag:<key></code> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key <code>Owner</code> and the value <code>TeamA</code>, specify <code>tag:Owner</code> for the filter name and <code>TeamA</code> for the filter value.</p> </li> <li> <p> <code>tag-key</code> - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.</p> </li> <li> <p> <code>type</code> - The type of Spot Instance request (<code>one-time</code> | <code>persistent</code>).</p> </li> <li> <p> <code>valid-from</code> - The start date of the request.</p> </li> <li> <p> <code>valid-until</code> - The end date of the request.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeSpotInstanceRequestsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "spot_instance_request_ids" in value:
        import capo_ec2.types.spot_instance_request_id_list

        capo_ec2.types.spot_instance_request_id_list.serialize_ec2_query(
            value["spot_instance_request_ids"],
            pairs,
            f"{key_prefix}SpotInstanceRequestId",
        )
    if "filters" in value:
        import capo_ec2.types.filter_list

        capo_ec2.types.filter_list.serialize_ec2_query(
            value["filters"], pairs, f"{key_prefix}Filter"
        )


def deserialize_ec2_query(el: Element) -> DescribeSpotInstanceRequestsRequest:
    out: DescribeSpotInstanceRequestsRequest = {}  # type: ignore[typeddict-item]
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_spot_instance_request_ids = el.find("SpotInstanceRequestId")
    if child_spot_instance_request_ids is not None:
        import capo_ec2.types.spot_instance_request_id_list

        out["spot_instance_request_ids"] = (
            capo_ec2.types.spot_instance_request_id_list.deserialize_ec2_query(
                child_spot_instance_request_ids
            )
        )
    child_filters = el.find("Filter")
    if child_filters is not None:
        import capo_ec2.types.filter_list

        out["filters"] = capo_ec2.types.filter_list.deserialize_ec2_query(child_filters)
    return out

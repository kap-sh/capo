"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeCapacityBlockOfferingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.describe_capacity_block_offerings_max_results
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string


class DescribeCapacityBlockOfferingsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of instance for which the Capacity Block offering reserves capacity.</p>"""
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of instances for which to reserve capacity. Each Capacity Block can have up to 64 instances, and you can have up to 256 instances across Capacity Blocks.</p>"""
    start_date_range: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The earliest start date for the Capacity Block offering.</p>"""
    end_date_range: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The latest end date for the Capacity Block offering.</p>"""
    capacity_duration_hours: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The reservation duration for the Capacity Block, in hours. You must specify the duration in 1-day increments up 14 days, and in 7-day increments up to 182 days.</p>"""
    next_token: NotRequired["capo_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""
    max_results: NotRequired[
        "capo_ec2.types.describe_capacity_block_offerings_max_results.DescribeCapacityBlockOfferingsMaxResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination">Pagination</a>.</p>"""
    ultraserver_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The EC2 UltraServer type of the Capacity Block offerings.</p>"""
    ultraserver_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of EC2 UltraServers in the offerings.</p>"""
    all_availability_zones: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p> Include all Availability Zones and Local Zones, regardless of your opt-in status. If you do not use this parameter, the results include available offerings from all Availability Zones in the Amazon Web Services Region and Local Zones you are opted into. </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeCapacityBlockOfferingsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "instance_count" in value:
        pairs.append((f"{key_prefix}InstanceCount", str(value["instance_count"])))
    if "start_date_range" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_date_range"], pairs, f"{key_prefix}StartDateRange"
        )
    if "end_date_range" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["end_date_range"], pairs, f"{key_prefix}EndDateRange"
        )
    if "capacity_duration_hours" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityDurationHours",
                str(value["capacity_duration_hours"]),
            )
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "max_results" in value:
        pairs.append((f"{key_prefix}MaxResults", str(value["max_results"])))
    if "ultraserver_type" in value:
        pairs.append((f"{key_prefix}UltraserverType", str(value["ultraserver_type"])))
    if "ultraserver_count" in value:
        pairs.append((f"{key_prefix}UltraserverCount", str(value["ultraserver_count"])))
    if "all_availability_zones" in value:
        pairs.append(
            (
                f"{key_prefix}AllAvailabilityZones",
                "true" if value["all_availability_zones"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> DescribeCapacityBlockOfferingsRequest:
    out: DescribeCapacityBlockOfferingsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_start_date_range = el.find("StartDateRange")
    if child_start_date_range is not None:
        import capo_ec2.types.millisecond_date_time

        out["start_date_range"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_start_date_range
            )
        )
    child_end_date_range = el.find("EndDateRange")
    if child_end_date_range is not None:
        import capo_ec2.types.millisecond_date_time

        out["end_date_range"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_end_date_range
            )
        )
    child_capacity_duration_hours = el.find("CapacityDurationHours")
    if child_capacity_duration_hours is not None:
        out["capacity_duration_hours"] = int(child_capacity_duration_hours.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_results = el.find("MaxResults")
    if child_max_results is not None:
        out["max_results"] = int(child_max_results.text or "")
    child_ultraserver_type = el.find("UltraserverType")
    if child_ultraserver_type is not None:
        out["ultraserver_type"] = str(child_ultraserver_type.text or "")
    child_ultraserver_count = el.find("UltraserverCount")
    if child_ultraserver_count is not None:
        out["ultraserver_count"] = int(child_ultraserver_count.text or "")
    child_all_availability_zones = el.find("AllAvailabilityZones")
    if child_all_availability_zones is not None:
        out["all_availability_zones"] = (
            child_all_availability_zones.text or ""
        ).lower() == "true"
    return out

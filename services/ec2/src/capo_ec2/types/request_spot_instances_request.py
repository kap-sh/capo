"""Generated from Smithy shape ``com.amazonaws.ec2#RequestSpotInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.instance_interruption_behavior
    import capo_ec2.types.integer
    import capo_ec2.types.request_spot_launch_specification
    import capo_ec2.types.spot_instance_type
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class RequestSpotInstancesRequest(TypedDict, closed=True):
    launch_specification: NotRequired[
        "capo_ec2.types.request_spot_launch_specification.RequestSpotLaunchSpecification"
    ]
    """<p>The launch specification.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The key-value pair for tagging the Spot Instance request on creation. The value for <code>ResourceType</code> must be <code>spot-instances-request</code>, otherwise the Spot Instance request fails. To tag the Spot Instance request after it has been created, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html">CreateTags</a>. </p>"""
    instance_interruption_behavior: NotRequired[
        "capo_ec2.types.instance_interruption_behavior.InstanceInterruptionBehavior"
    ]
    """<p>The behavior when a Spot Instance is interrupted. The default is <code>terminate</code>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    spot_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.</p> <important> <p>If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.</p> </important>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Run_Instance_Idempotency.html">Ensuring idempotency in Amazon EC2 API requests</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The maximum number of Spot Instances to launch.</p> <p>Default: 1</p>"""
    type: NotRequired["capo_ec2.types.spot_instance_type.SpotInstanceType"]
    """<p>The Spot Instance request type.</p> <p>Default: <code>one-time</code> </p>"""
    valid_from: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The start date of the request. If this is a one-time request, the request becomes active at this date and time and remains active until all instances launch, the request expires, or the request is canceled. If the request is persistent, the request becomes active at this date and time and remains active until it expires or is canceled.</p> <p>The specified start date and time cannot be equal to the current date and time. You must specify a start date and time that occurs after the current date and time.</p>"""
    valid_until: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The end date of the request, in UTC format (<i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p> <ul> <li> <p>For a persistent request, the request remains active until the <code>ValidUntil</code> date and time is reached. Otherwise, the request remains active until you cancel it. </p> </li> <li> <p>For a one-time request, the request remains active until all instances launch, the request is canceled, or the <code>ValidUntil</code> date and time is reached. By default, the request is valid for 7 days from the date the request was created.</p> </li> </ul>"""
    launch_group: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance launch group. Launch groups are Spot Instances that launch together and terminate together.</p> <p>Default: Instances are launched and terminated individually</p>"""
    availability_zone_group: NotRequired["capo_ec2.types.string.String"]
    """<p>The user-specified name for a logical grouping of requests.</p> <p>When you specify an Availability Zone group in a Spot Instance request, all Spot Instances in the request are launched in the same Availability Zone. Instance proximity is maintained with this parameter, but the choice of Availability Zone is not. The group applies only to requests for Spot Instances of the same instance type. Any additional Spot Instance requests that are specified with the same Availability Zone group name are launched in that same Availability Zone, as long as at least one instance from the group is still active.</p> <p>If there is no active instance running in the Availability Zone group that you specify for a new Spot Instance request (all instances are terminated, the request is expired, or the maximum price you specified falls below current Spot price), then Amazon EC2 launches the instance in any Availability Zone where the constraint can be met. Consequently, the subsequent set of Spot Instances could be placed in a different zone from the original request, even if you specified the same Availability Zone group.</p> <p>Default: Instances are launched in any available Availability Zone.</p>"""
    block_duration_minutes: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>Deprecated.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RequestSpotInstancesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "launch_specification" in value:
        import capo_ec2.types.request_spot_launch_specification

        capo_ec2.types.request_spot_launch_specification.serialize_ec2_query(
            value["launch_specification"], pairs, f"{key_prefix}LaunchSpecification"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "instance_interruption_behavior" in value:
        import capo_ec2.types.instance_interruption_behavior

        capo_ec2.types.instance_interruption_behavior.serialize_ec2_query(
            value["instance_interruption_behavior"],
            pairs,
            f"{key_prefix}InstanceInterruptionBehavior",
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "spot_price" in value:
        pairs.append((f"{key_prefix}SpotPrice", str(value["spot_price"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "instance_count" in value:
        pairs.append((f"{key_prefix}InstanceCount", str(value["instance_count"])))
    if "type" in value:
        import capo_ec2.types.spot_instance_type

        capo_ec2.types.spot_instance_type.serialize_ec2_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "valid_from" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["valid_from"], pairs, f"{key_prefix}ValidFrom"
        )
    if "valid_until" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["valid_until"], pairs, f"{key_prefix}ValidUntil"
        )
    if "launch_group" in value:
        pairs.append((f"{key_prefix}LaunchGroup", str(value["launch_group"])))
    if "availability_zone_group" in value:
        pairs.append(
            (
                f"{key_prefix}AvailabilityZoneGroup",
                str(value["availability_zone_group"]),
            )
        )
    if "block_duration_minutes" in value:
        pairs.append(
            (f"{key_prefix}BlockDurationMinutes", str(value["block_duration_minutes"]))
        )


def deserialize_ec2_query(el: Element) -> RequestSpotInstancesRequest:
    out: RequestSpotInstancesRequest = {}  # type: ignore[typeddict-item]
    child_launch_specification = el.find("LaunchSpecification")
    if child_launch_specification is not None:
        import capo_ec2.types.request_spot_launch_specification

        out["launch_specification"] = (
            capo_ec2.types.request_spot_launch_specification.deserialize_ec2_query(
                child_launch_specification
            )
        )
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_instance_interruption_behavior = el.find("InstanceInterruptionBehavior")
    if child_instance_interruption_behavior is not None:
        import capo_ec2.types.instance_interruption_behavior

        out["instance_interruption_behavior"] = (
            capo_ec2.types.instance_interruption_behavior.deserialize_ec2_query(
                child_instance_interruption_behavior
            )
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_spot_price = el.find("spotPrice")
    if child_spot_price is not None:
        out["spot_price"] = str(child_spot_price.text or "")
    child_client_token = el.find("clientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_instance_count = el.find("instanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_type = el.find("type")
    if child_type is not None:
        import capo_ec2.types.spot_instance_type

        out["type"] = capo_ec2.types.spot_instance_type.deserialize_ec2_query(
            child_type
        )
    child_valid_from = el.find("validFrom")
    if child_valid_from is not None:
        import capo_ec2.types.date_time

        out["valid_from"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_valid_from
        )
    child_valid_until = el.find("validUntil")
    if child_valid_until is not None:
        import capo_ec2.types.date_time

        out["valid_until"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_valid_until
        )
    child_launch_group = el.find("launchGroup")
    if child_launch_group is not None:
        out["launch_group"] = str(child_launch_group.text or "")
    child_availability_zone_group = el.find("availabilityZoneGroup")
    if child_availability_zone_group is not None:
        out["availability_zone_group"] = str(child_availability_zone_group.text or "")
    child_block_duration_minutes = el.find("blockDurationMinutes")
    if child_block_duration_minutes is not None:
        out["block_duration_minutes"] = int(child_block_duration_minutes.text or "")
    return out

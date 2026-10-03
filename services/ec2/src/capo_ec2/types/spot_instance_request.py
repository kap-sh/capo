"""Generated from Smithy shape ``com.amazonaws.ec2#SpotInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.instance_id
    import capo_ec2.types.instance_interruption_behavior
    import capo_ec2.types.integer
    import capo_ec2.types.launch_specification
    import capo_ec2.types.ri_product_description
    import capo_ec2.types.spot_instance_state
    import capo_ec2.types.spot_instance_state_fault
    import capo_ec2.types.spot_instance_status
    import capo_ec2.types.spot_instance_type
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class SpotInstanceRequest(TypedDict, closed=True):
    actual_block_hourly_price: NotRequired["capo_ec2.types.string.String"]
    """<p>Deprecated.</p>"""
    availability_zone_group: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone group. If you specify the same Availability Zone group for all Spot Instance requests, all Spot Instances are launched in the same Availability Zone.</p>"""
    block_duration_minutes: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>Deprecated.</p>"""
    create_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time when the Spot Instance request was created, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p>"""
    fault: NotRequired[
        "capo_ec2.types.spot_instance_state_fault.SpotInstanceStateFault"
    ]
    """<p>The fault codes for the Spot Instance request, if any.</p>"""
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The instance ID, if an instance has been launched to fulfill the Spot Instance request.</p>"""
    launch_group: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance launch group. Launch groups are Spot Instances that launch together and terminate together.</p>"""
    launch_specification: NotRequired[
        "capo_ec2.types.launch_specification.LaunchSpecification"
    ]
    """<p>Additional information for launching instances.</p>"""
    launched_availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone in which the request is launched.</p> <p>Either <code>launchedAvailabilityZone</code> or <code>launchedAvailabilityZoneId</code> can be specified, but not both</p>"""
    launched_availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone in which the request is launched.</p> <p>Either <code>launchedAvailabilityZone</code> or <code>launchedAvailabilityZoneId</code> can be specified, but not both</p>"""
    product_description: NotRequired[
        "capo_ec2.types.ri_product_description.RIProductDescription"
    ]
    """<p>The product description associated with the Spot Instance.</p>"""
    spot_instance_request_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Spot Instance request.</p>"""
    spot_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.</p> <important> <p>If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.</p> </important>"""
    state: NotRequired["capo_ec2.types.spot_instance_state.SpotInstanceState"]
    """<p>The state of the Spot Instance request. Spot request status information helps track your Spot Instance requests. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-request-status.html">Spot request status</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    status: NotRequired["capo_ec2.types.spot_instance_status.SpotInstanceStatus"]
    """<p>The status code and status message describing the Spot Instance request.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the resource.</p>"""
    type: NotRequired["capo_ec2.types.spot_instance_type.SpotInstanceType"]
    """<p>The Spot Instance request type.</p>"""
    valid_from: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The start date of the request, in UTC format (for example, <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). The request becomes active at this date and time.</p>"""
    valid_until: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The end date of the request, in UTC format (<i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z).</p> <ul> <li> <p>For a persistent request, the request remains active until the <code>validUntil</code> date and time is reached. Otherwise, the request remains active until you cancel it. </p> </li> <li> <p>For a one-time request, the request remains active until all instances launch, the request is canceled, or the <code>validUntil</code> date and time is reached. By default, the request is valid for 7 days from the date the request was created.</p> </li> </ul>"""
    instance_interruption_behavior: NotRequired[
        "capo_ec2.types.instance_interruption_behavior.InstanceInterruptionBehavior"
    ]
    """<p>The behavior when a Spot Instance is interrupted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotInstanceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "actual_block_hourly_price" in value:
        pairs.append(
            (
                f"{key_prefix}ActualBlockHourlyPrice",
                str(value["actual_block_hourly_price"]),
            )
        )
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
    if "create_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["create_time"], pairs, f"{key_prefix}CreateTime"
        )
    if "fault" in value:
        import capo_ec2.types.spot_instance_state_fault

        capo_ec2.types.spot_instance_state_fault.serialize_ec2_query(
            value["fault"], pairs, f"{key_prefix}Fault"
        )
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "launch_group" in value:
        pairs.append((f"{key_prefix}LaunchGroup", str(value["launch_group"])))
    if "launch_specification" in value:
        import capo_ec2.types.launch_specification

        capo_ec2.types.launch_specification.serialize_ec2_query(
            value["launch_specification"], pairs, f"{key_prefix}LaunchSpecification"
        )
    if "launched_availability_zone" in value:
        pairs.append(
            (
                f"{key_prefix}LaunchedAvailabilityZone",
                str(value["launched_availability_zone"]),
            )
        )
    if "launched_availability_zone_id" in value:
        pairs.append(
            (
                f"{key_prefix}LaunchedAvailabilityZoneId",
                str(value["launched_availability_zone_id"]),
            )
        )
    if "product_description" in value:
        import capo_ec2.types.ri_product_description

        capo_ec2.types.ri_product_description.serialize_ec2_query(
            value["product_description"], pairs, f"{key_prefix}ProductDescription"
        )
    if "spot_instance_request_id" in value:
        pairs.append(
            (
                f"{key_prefix}SpotInstanceRequestId",
                str(value["spot_instance_request_id"]),
            )
        )
    if "spot_price" in value:
        pairs.append((f"{key_prefix}SpotPrice", str(value["spot_price"])))
    if "state" in value:
        import capo_ec2.types.spot_instance_state

        capo_ec2.types.spot_instance_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "status" in value:
        import capo_ec2.types.spot_instance_status

        capo_ec2.types.spot_instance_status.serialize_ec2_query(
            value["status"], pairs, f"{key_prefix}Status"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
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
    if "instance_interruption_behavior" in value:
        import capo_ec2.types.instance_interruption_behavior

        capo_ec2.types.instance_interruption_behavior.serialize_ec2_query(
            value["instance_interruption_behavior"],
            pairs,
            f"{key_prefix}InstanceInterruptionBehavior",
        )


def deserialize_ec2_query(el: Element) -> SpotInstanceRequest:
    out: SpotInstanceRequest = {}  # type: ignore[typeddict-item]
    child_actual_block_hourly_price = el.find("actualBlockHourlyPrice")
    if child_actual_block_hourly_price is not None:
        out["actual_block_hourly_price"] = str(
            child_actual_block_hourly_price.text or ""
        )
    child_availability_zone_group = el.find("availabilityZoneGroup")
    if child_availability_zone_group is not None:
        out["availability_zone_group"] = str(child_availability_zone_group.text or "")
    child_block_duration_minutes = el.find("blockDurationMinutes")
    if child_block_duration_minutes is not None:
        out["block_duration_minutes"] = int(child_block_duration_minutes.text or "")
    child_create_time = el.find("createTime")
    if child_create_time is not None:
        import capo_ec2.types.date_time

        out["create_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_create_time
        )
    child_fault = el.find("fault")
    if child_fault is not None:
        import capo_ec2.types.spot_instance_state_fault

        out["fault"] = capo_ec2.types.spot_instance_state_fault.deserialize_ec2_query(
            child_fault
        )
    child_instance_id = el.find("instanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_launch_group = el.find("launchGroup")
    if child_launch_group is not None:
        out["launch_group"] = str(child_launch_group.text or "")
    child_launch_specification = el.find("launchSpecification")
    if child_launch_specification is not None:
        import capo_ec2.types.launch_specification

        out["launch_specification"] = (
            capo_ec2.types.launch_specification.deserialize_ec2_query(
                child_launch_specification
            )
        )
    child_launched_availability_zone = el.find("launchedAvailabilityZone")
    if child_launched_availability_zone is not None:
        out["launched_availability_zone"] = str(
            child_launched_availability_zone.text or ""
        )
    child_launched_availability_zone_id = el.find("launchedAvailabilityZoneId")
    if child_launched_availability_zone_id is not None:
        out["launched_availability_zone_id"] = str(
            child_launched_availability_zone_id.text or ""
        )
    child_product_description = el.find("productDescription")
    if child_product_description is not None:
        import capo_ec2.types.ri_product_description

        out["product_description"] = (
            capo_ec2.types.ri_product_description.deserialize_ec2_query(
                child_product_description
            )
        )
    child_spot_instance_request_id = el.find("spotInstanceRequestId")
    if child_spot_instance_request_id is not None:
        out["spot_instance_request_id"] = str(child_spot_instance_request_id.text or "")
    child_spot_price = el.find("spotPrice")
    if child_spot_price is not None:
        out["spot_price"] = str(child_spot_price.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.spot_instance_state

        out["state"] = capo_ec2.types.spot_instance_state.deserialize_ec2_query(
            child_state
        )
    child_status = el.find("status")
    if child_status is not None:
        import capo_ec2.types.spot_instance_status

        out["status"] = capo_ec2.types.spot_instance_status.deserialize_ec2_query(
            child_status
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
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
    child_instance_interruption_behavior = el.find("instanceInterruptionBehavior")
    if child_instance_interruption_behavior is not None:
        import capo_ec2.types.instance_interruption_behavior

        out["instance_interruption_behavior"] = (
            capo_ec2.types.instance_interruption_behavior.deserialize_ec2_query(
                child_instance_interruption_behavior
            )
        )
    return out

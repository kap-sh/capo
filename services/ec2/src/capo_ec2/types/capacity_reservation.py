"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityReservation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.account_id
    import capo_ec2.types.boolean
    import capo_ec2.types.boxed_boolean
    import capo_ec2.types.capacity_allocations
    import capo_ec2.types.capacity_block_id
    import capo_ec2.types.capacity_reservation_adjustment_details
    import capo_ec2.types.capacity_reservation_adjustment_status
    import capo_ec2.types.capacity_reservation_commitment_info
    import capo_ec2.types.capacity_reservation_delivery_preference
    import capo_ec2.types.capacity_reservation_instance_platform
    import capo_ec2.types.capacity_reservation_launch_status
    import capo_ec2.types.capacity_reservation_state
    import capo_ec2.types.capacity_reservation_tenancy
    import capo_ec2.types.capacity_reservation_type
    import capo_ec2.types.date_time
    import capo_ec2.types.end_date_type
    import capo_ec2.types.instance_match_criteria
    import capo_ec2.types.integer
    import capo_ec2.types.interruptible_capacity_allocation
    import capo_ec2.types.interruption_info
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.outpost_arn
    import capo_ec2.types.placement_group_arn
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.zero_size_preference


class CapacityReservation(TypedDict, closed=True):
    capacity_reservation_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Capacity Reservation.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the Capacity Reservation.</p>"""
    capacity_reservation_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Capacity Reservation.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone in which the capacity is reserved.</p>"""
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The type of instance for which the Capacity Reservation reserves capacity.</p>"""
    instance_platform: NotRequired[
        "capo_ec2.types.capacity_reservation_instance_platform.CapacityReservationInstancePlatform"
    ]
    """<p>The type of operating system for which the Capacity Reservation reserves capacity.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone in which the capacity is reserved.</p>"""
    tenancy: NotRequired[
        "capo_ec2.types.capacity_reservation_tenancy.CapacityReservationTenancy"
    ]
    """<p>Indicates the tenancy of the Capacity Reservation. A Capacity Reservation can have one of the following tenancy settings:</p> <ul> <li> <p> <code>default</code> - The Capacity Reservation is created on hardware that is shared with other Amazon Web Services accounts.</p> </li> <li> <p> <code>dedicated</code> - The Capacity Reservation is created on single-tenant hardware that is dedicated to a single Amazon Web Services account.</p> </li> </ul>"""
    total_instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The total number of instances for which the Capacity Reservation reserves capacity.</p>"""
    available_instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The remaining capacity. Indicates the number of instances that can be launched in the Capacity Reservation.</p>"""
    ebs_optimized: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the Capacity Reservation supports EBS-optimized instances. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS- optimized instance.</p>"""
    ephemeral_storage: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p> <i>Deprecated.</i> </p>"""
    state: NotRequired[
        "capo_ec2.types.capacity_reservation_state.CapacityReservationState"
    ]
    """<p>The current state of the Capacity Reservation. A Capacity Reservation can be in one of the following states:</p> <ul> <li> <p> <code>active</code> - The capacity is available for use.</p> </li> <li> <p> <code>expired</code> - The Capacity Reservation expired automatically at the date and time specified in your reservation request. The reserved capacity is no longer available for your use.</p> </li> <li> <p> <code>cancelled</code> - The Capacity Reservation was canceled. The reserved capacity is no longer available for your use.</p> </li> <li> <p> <code>pending</code> - The Capacity Reservation request was successful but the capacity provisioning is still pending.</p> </li> <li> <p> <code>failed</code> - The Capacity Reservation request has failed. A request can fail due to request parameters that are not valid, capacity constraints, or instance limit constraints. You can view a failed request for 60 minutes.</p> </li> <li> <p> <code>scheduled</code> - (<i>Future-dated Capacity Reservations</i>) The future-dated Capacity Reservation request was approved and the Capacity Reservation is scheduled for delivery on the requested start date.</p> </li> <li> <p> <code>payment-pending</code> - (<i>Capacity Blocks</i>) The upfront payment has not been processed yet.</p> </li> <li> <p> <code>payment-failed</code> - (<i>Capacity Blocks</i>) The upfront payment was not processed in the 12-hour time frame. Your Capacity Block was released.</p> </li> <li> <p> <code>assessing</code> - (<i>Future-dated Capacity Reservations</i>) Amazon EC2 is assessing your request for a future-dated Capacity Reservation.</p> </li> <li> <p> <code>delayed</code> - (<i>Future-dated Capacity Reservations</i>) Amazon EC2 encountered a delay in provisioning the requested future-dated Capacity Reservation. Amazon EC2 is unable to deliver the requested capacity by the requested start date and time.</p> </li> <li> <p> <code>unsupported</code> - (<i>Future-dated Capacity Reservations</i>) Amazon EC2 can't support the future-dated Capacity Reservation request due to capacity constraints. You can view unsupported requests for 30 days. The Capacity Reservation will not be delivered.</p> </li> <li> <p> <code>cancelling</code> - (<i>Future-dated Capacity Reservations</i>) The Capacity Reservation is being cancelled. Capacity has been released but charges continue for the commitment wind-down period. The reservation transitions to <code>cancelled</code> when the wind-down completes.</p> </li> </ul>"""
    start_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time the Capacity Reservation was started.</p>"""
    end_date: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to <code>expired</code> when it reaches its end date and time.</p>"""
    end_date_type: NotRequired["capo_ec2.types.end_date_type.EndDateType"]
    """<p>Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types:</p> <ul> <li> <p> <code>unlimited</code> - The Capacity Reservation remains active until you explicitly cancel it.</p> </li> <li> <p> <code>limited</code> - The Capacity Reservation expires automatically at a specified date and time.</p> </li> </ul>"""
    instance_match_criteria: NotRequired[
        "capo_ec2.types.instance_match_criteria.InstanceMatchCriteria"
    ]
    """<p>Indicates the type of instance launches that the Capacity Reservation accepts. The options include:</p> <ul> <li> <p> <code>open</code> - The Capacity Reservation accepts all instances that have matching attributes (instance type, platform, and Availability Zone). Instances that have matching attributes launch into the Capacity Reservation automatically without specifying any additional parameters.</p> </li> <li> <p> <code>targeted</code> - The Capacity Reservation only accepts instances that have matching attributes (instance type, platform, and Availability Zone), and explicitly target the Capacity Reservation. This ensures that only permitted instances can use the reserved capacity. </p> </li> </ul>"""
    create_date: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time the Capacity Reservation was created.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the Capacity Reservation.</p>"""
    outpost_arn: NotRequired["capo_ec2.types.outpost_arn.OutpostArn"]
    """<p>The Amazon Resource Name (ARN) of the Outpost on which the Capacity Reservation was created.</p>"""
    capacity_reservation_fleet_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Capacity Reservation Fleet to which the Capacity Reservation belongs. Only valid for Capacity Reservations that were created by a Capacity Reservation Fleet.</p>"""
    placement_group_arn: NotRequired[
        "capo_ec2.types.placement_group_arn.PlacementGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the cluster placement group in which the Capacity Reservation was created. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-cpg.html"> Capacity Reservations for cluster placement groups</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    capacity_allocations: NotRequired[
        "capo_ec2.types.capacity_allocations.CapacityAllocations"
    ]
    """<p>Information about instance capacity usage.</p>"""
    reservation_type: NotRequired[
        "capo_ec2.types.capacity_reservation_type.CapacityReservationType"
    ]
    """<p>The type of Capacity Reservation.</p>"""
    unused_reservation_billing_owner_id: NotRequired[
        "capo_ec2.types.account_id.AccountID"
    ]
    """<p>The ID of the Amazon Web Services account to which billing of the unused capacity of the Capacity Reservation is assigned.</p>"""
    commitment_info: NotRequired[
        "capo_ec2.types.capacity_reservation_commitment_info.CapacityReservationCommitmentInfo"
    ]
    """<p>Information about your commitment for a future-dated Capacity Reservation.</p>"""
    delivery_preference: NotRequired[
        "capo_ec2.types.capacity_reservation_delivery_preference.CapacityReservationDeliveryPreference"
    ]
    """<p>The delivery method for a future-dated Capacity Reservation. <code>incremental</code> indicates that the requested capacity is delivered in addition to any running instances and reserved capacity that you have in your account at the requested date and time.</p>"""
    capacity_block_id: NotRequired["capo_ec2.types.capacity_block_id.CapacityBlockId"]
    """<p>The ID of the Capacity Block.</p>"""
    interruptible: NotRequired["capo_ec2.types.boxed_boolean.BoxedBoolean"]
    """<p> Indicates whether this Capacity Reservation is interruptible, meaning instances may be terminated when the owner reclaims capacity. </p>"""
    interruptible_capacity_allocation: NotRequired[
        "capo_ec2.types.interruptible_capacity_allocation.InterruptibleCapacityAllocation"
    ]
    """<p> Contains allocation details for interruptible reservations, including current allocated instances and target instance counts within the interruptibleCapacityAllocation object. </p>"""
    interruption_info: NotRequired["capo_ec2.types.interruption_info.InterruptionInfo"]
    """<p> Information about the interruption configuration and association with the source reservation for interruptible Capacity Reservations. </p>"""
    adjustment_status: NotRequired[
        "capo_ec2.types.capacity_reservation_adjustment_status.CapacityReservationAdjustmentStatus"
    ]
    """<p>The status of the most recent modification to the Capacity Reservation. A Capacity Reservation can have one of the following adjustment statuses:</p> <ul> <li> <p> <code>requested</code> - The modification was requested and is being processed.</p> </li> <li> <p> <code>applied</code> - The modification was applied to the Capacity Reservation.</p> </li> <li> <p> <code>rejected</code> - The modification was not applied and the Capacity Reservation keeps its existing configuration.</p> </li> </ul> <p>This field is not returned if the Capacity Reservation has never been modified.</p>"""
    adjustment_details: NotRequired[
        "capo_ec2.types.capacity_reservation_adjustment_details.CapacityReservationAdjustmentDetails"
    ]
    """<p>The configuration that the Capacity Reservation will have after the requested adjustment is applied.</p>"""
    original_start_date: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The start date that you originally requested for the Capacity Reservation, in the ISO8601 format in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>). This value doesn't change when you push out the start date.</p>"""
    zero_size_preference: NotRequired[
        "capo_ec2.types.zero_size_preference.ZeroSizePreference"
    ]
    """<p> The zero-size preference configured for the interruptible Capacity Reservation. A value of <code>retain</code> keeps the interruptible Capacity Reservation active at zero capacity when you reduce its allocation to zero. A value of <code>default</code> cancels the interruptible Capacity Reservation when you reduce its allocation to zero. </p>"""
    launch_status: NotRequired[
        "capo_ec2.types.capacity_reservation_launch_status.CapacityReservationLaunchStatus"
    ]
    """<note> <p>Only supported for UltraServers.</p> </note> <p>Indicates whether you can launch instances into the Capacity Reservation. A Capacity Reservation can have the following launch statuses:</p> <ul> <li> <p> <code>launchable</code> - You can launch instances into the Capacity Reservation.</p> </li> <li> <p> <code>unlaunchable</code> - You can't launch instances into the Capacity Reservation. For example, the Capacity Reservation is not active.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityReservation, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "capacity_reservation_id" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityReservationId",
                str(value["capacity_reservation_id"]),
            )
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "capacity_reservation_arn" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityReservationArn",
                str(value["capacity_reservation_arn"]),
            )
        )
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "instance_platform" in value:
        import capo_ec2.types.capacity_reservation_instance_platform

        capo_ec2.types.capacity_reservation_instance_platform.serialize_ec2_query(
            value["instance_platform"], pairs, f"{key_prefix}InstancePlatform"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "tenancy" in value:
        import capo_ec2.types.capacity_reservation_tenancy

        capo_ec2.types.capacity_reservation_tenancy.serialize_ec2_query(
            value["tenancy"], pairs, f"{key_prefix}Tenancy"
        )
    if "total_instance_count" in value:
        pairs.append(
            (f"{key_prefix}TotalInstanceCount", str(value["total_instance_count"]))
        )
    if "available_instance_count" in value:
        pairs.append(
            (
                f"{key_prefix}AvailableInstanceCount",
                str(value["available_instance_count"]),
            )
        )
    if "ebs_optimized" in value:
        pairs.append(
            (f"{key_prefix}EbsOptimized", "true" if value["ebs_optimized"] else "false")
        )
    if "ephemeral_storage" in value:
        pairs.append(
            (
                f"{key_prefix}EphemeralStorage",
                "true" if value["ephemeral_storage"] else "false",
            )
        )
    if "state" in value:
        import capo_ec2.types.capacity_reservation_state

        capo_ec2.types.capacity_reservation_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "start_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_date"], pairs, f"{key_prefix}StartDate"
        )
    if "end_date" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["end_date"], pairs, f"{key_prefix}EndDate"
        )
    if "end_date_type" in value:
        import capo_ec2.types.end_date_type

        capo_ec2.types.end_date_type.serialize_ec2_query(
            value["end_date_type"], pairs, f"{key_prefix}EndDateType"
        )
    if "instance_match_criteria" in value:
        import capo_ec2.types.instance_match_criteria

        capo_ec2.types.instance_match_criteria.serialize_ec2_query(
            value["instance_match_criteria"],
            pairs,
            f"{key_prefix}InstanceMatchCriteria",
        )
    if "create_date" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["create_date"], pairs, f"{key_prefix}CreateDate"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "outpost_arn" in value:
        pairs.append((f"{key_prefix}OutpostArn", str(value["outpost_arn"])))
    if "capacity_reservation_fleet_id" in value:
        pairs.append(
            (
                f"{key_prefix}CapacityReservationFleetId",
                str(value["capacity_reservation_fleet_id"]),
            )
        )
    if "placement_group_arn" in value:
        pairs.append(
            (f"{key_prefix}PlacementGroupArn", str(value["placement_group_arn"]))
        )
    if "capacity_allocations" in value:
        import capo_ec2.types.capacity_allocations

        capo_ec2.types.capacity_allocations.serialize_ec2_query(
            value["capacity_allocations"], pairs, f"{key_prefix}CapacityAllocationSet"
        )
    if "reservation_type" in value:
        import capo_ec2.types.capacity_reservation_type

        capo_ec2.types.capacity_reservation_type.serialize_ec2_query(
            value["reservation_type"], pairs, f"{key_prefix}ReservationType"
        )
    if "unused_reservation_billing_owner_id" in value:
        pairs.append(
            (
                f"{key_prefix}UnusedReservationBillingOwnerId",
                str(value["unused_reservation_billing_owner_id"]),
            )
        )
    if "commitment_info" in value:
        import capo_ec2.types.capacity_reservation_commitment_info

        capo_ec2.types.capacity_reservation_commitment_info.serialize_ec2_query(
            value["commitment_info"], pairs, f"{key_prefix}CommitmentInfo"
        )
    if "delivery_preference" in value:
        import capo_ec2.types.capacity_reservation_delivery_preference

        capo_ec2.types.capacity_reservation_delivery_preference.serialize_ec2_query(
            value["delivery_preference"], pairs, f"{key_prefix}DeliveryPreference"
        )
    if "capacity_block_id" in value:
        pairs.append((f"{key_prefix}CapacityBlockId", str(value["capacity_block_id"])))
    if "interruptible" in value:
        pairs.append(
            (
                f"{key_prefix}Interruptible",
                "true" if value["interruptible"] else "false",
            )
        )
    if "interruptible_capacity_allocation" in value:
        import capo_ec2.types.interruptible_capacity_allocation

        capo_ec2.types.interruptible_capacity_allocation.serialize_ec2_query(
            value["interruptible_capacity_allocation"],
            pairs,
            f"{key_prefix}InterruptibleCapacityAllocation",
        )
    if "interruption_info" in value:
        import capo_ec2.types.interruption_info

        capo_ec2.types.interruption_info.serialize_ec2_query(
            value["interruption_info"], pairs, f"{key_prefix}InterruptionInfo"
        )
    if "adjustment_status" in value:
        import capo_ec2.types.capacity_reservation_adjustment_status

        capo_ec2.types.capacity_reservation_adjustment_status.serialize_ec2_query(
            value["adjustment_status"], pairs, f"{key_prefix}AdjustmentStatus"
        )
    if "adjustment_details" in value:
        import capo_ec2.types.capacity_reservation_adjustment_details

        capo_ec2.types.capacity_reservation_adjustment_details.serialize_ec2_query(
            value["adjustment_details"], pairs, f"{key_prefix}AdjustmentDetails"
        )
    if "original_start_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["original_start_date"], pairs, f"{key_prefix}OriginalStartDate"
        )
    if "zero_size_preference" in value:
        import capo_ec2.types.zero_size_preference

        capo_ec2.types.zero_size_preference.serialize_ec2_query(
            value["zero_size_preference"], pairs, f"{key_prefix}ZeroSizePreference"
        )
    if "launch_status" in value:
        import capo_ec2.types.capacity_reservation_launch_status

        capo_ec2.types.capacity_reservation_launch_status.serialize_ec2_query(
            value["launch_status"], pairs, f"{key_prefix}LaunchStatus"
        )


def deserialize_ec2_query(el: Element) -> CapacityReservation:
    out: CapacityReservation = {}  # type: ignore[typeddict-item]
    child_capacity_reservation_id = el.find("capacityReservationId")
    if child_capacity_reservation_id is not None:
        out["capacity_reservation_id"] = str(child_capacity_reservation_id.text or "")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_capacity_reservation_arn = el.find("capacityReservationArn")
    if child_capacity_reservation_arn is not None:
        out["capacity_reservation_arn"] = str(child_capacity_reservation_arn.text or "")
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_instance_type = el.find("instanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_instance_platform = el.find("instancePlatform")
    if child_instance_platform is not None:
        import capo_ec2.types.capacity_reservation_instance_platform

        out["instance_platform"] = (
            capo_ec2.types.capacity_reservation_instance_platform.deserialize_ec2_query(
                child_instance_platform
            )
        )
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_tenancy = el.find("tenancy")
    if child_tenancy is not None:
        import capo_ec2.types.capacity_reservation_tenancy

        out["tenancy"] = (
            capo_ec2.types.capacity_reservation_tenancy.deserialize_ec2_query(
                child_tenancy
            )
        )
    child_total_instance_count = el.find("totalInstanceCount")
    if child_total_instance_count is not None:
        out["total_instance_count"] = int(child_total_instance_count.text or "")
    child_available_instance_count = el.find("availableInstanceCount")
    if child_available_instance_count is not None:
        out["available_instance_count"] = int(child_available_instance_count.text or "")
    child_ebs_optimized = el.find("ebsOptimized")
    if child_ebs_optimized is not None:
        out["ebs_optimized"] = (child_ebs_optimized.text or "").lower() == "true"
    child_ephemeral_storage = el.find("ephemeralStorage")
    if child_ephemeral_storage is not None:
        out["ephemeral_storage"] = (
            child_ephemeral_storage.text or ""
        ).lower() == "true"
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.capacity_reservation_state

        out["state"] = capo_ec2.types.capacity_reservation_state.deserialize_ec2_query(
            child_state
        )
    child_start_date = el.find("startDate")
    if child_start_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["start_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_start_date
        )
    child_end_date = el.find("endDate")
    if child_end_date is not None:
        import capo_ec2.types.date_time

        out["end_date"] = capo_ec2.types.date_time.deserialize_ec2_query(child_end_date)
    child_end_date_type = el.find("endDateType")
    if child_end_date_type is not None:
        import capo_ec2.types.end_date_type

        out["end_date_type"] = capo_ec2.types.end_date_type.deserialize_ec2_query(
            child_end_date_type
        )
    child_instance_match_criteria = el.find("instanceMatchCriteria")
    if child_instance_match_criteria is not None:
        import capo_ec2.types.instance_match_criteria

        out["instance_match_criteria"] = (
            capo_ec2.types.instance_match_criteria.deserialize_ec2_query(
                child_instance_match_criteria
            )
        )
    child_create_date = el.find("createDate")
    if child_create_date is not None:
        import capo_ec2.types.date_time

        out["create_date"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_create_date
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_outpost_arn = el.find("outpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_capacity_reservation_fleet_id = el.find("capacityReservationFleetId")
    if child_capacity_reservation_fleet_id is not None:
        out["capacity_reservation_fleet_id"] = str(
            child_capacity_reservation_fleet_id.text or ""
        )
    child_placement_group_arn = el.find("placementGroupArn")
    if child_placement_group_arn is not None:
        out["placement_group_arn"] = str(child_placement_group_arn.text or "")
    child_capacity_allocations = el.find("capacityAllocationSet")
    if child_capacity_allocations is not None:
        import capo_ec2.types.capacity_allocations

        out["capacity_allocations"] = (
            capo_ec2.types.capacity_allocations.deserialize_ec2_query(
                child_capacity_allocations
            )
        )
    child_reservation_type = el.find("reservationType")
    if child_reservation_type is not None:
        import capo_ec2.types.capacity_reservation_type

        out["reservation_type"] = (
            capo_ec2.types.capacity_reservation_type.deserialize_ec2_query(
                child_reservation_type
            )
        )
    child_unused_reservation_billing_owner_id = el.find(
        "unusedReservationBillingOwnerId"
    )
    if child_unused_reservation_billing_owner_id is not None:
        out["unused_reservation_billing_owner_id"] = str(
            child_unused_reservation_billing_owner_id.text or ""
        )
    child_commitment_info = el.find("commitmentInfo")
    if child_commitment_info is not None:
        import capo_ec2.types.capacity_reservation_commitment_info

        out["commitment_info"] = (
            capo_ec2.types.capacity_reservation_commitment_info.deserialize_ec2_query(
                child_commitment_info
            )
        )
    child_delivery_preference = el.find("deliveryPreference")
    if child_delivery_preference is not None:
        import capo_ec2.types.capacity_reservation_delivery_preference

        out["delivery_preference"] = (
            capo_ec2.types.capacity_reservation_delivery_preference.deserialize_ec2_query(
                child_delivery_preference
            )
        )
    child_capacity_block_id = el.find("capacityBlockId")
    if child_capacity_block_id is not None:
        out["capacity_block_id"] = str(child_capacity_block_id.text or "")
    child_interruptible = el.find("interruptible")
    if child_interruptible is not None:
        out["interruptible"] = (child_interruptible.text or "").lower() == "true"
    child_interruptible_capacity_allocation = el.find("interruptibleCapacityAllocation")
    if child_interruptible_capacity_allocation is not None:
        import capo_ec2.types.interruptible_capacity_allocation

        out["interruptible_capacity_allocation"] = (
            capo_ec2.types.interruptible_capacity_allocation.deserialize_ec2_query(
                child_interruptible_capacity_allocation
            )
        )
    child_interruption_info = el.find("interruptionInfo")
    if child_interruption_info is not None:
        import capo_ec2.types.interruption_info

        out["interruption_info"] = (
            capo_ec2.types.interruption_info.deserialize_ec2_query(
                child_interruption_info
            )
        )
    child_adjustment_status = el.find("adjustmentStatus")
    if child_adjustment_status is not None:
        import capo_ec2.types.capacity_reservation_adjustment_status

        out["adjustment_status"] = (
            capo_ec2.types.capacity_reservation_adjustment_status.deserialize_ec2_query(
                child_adjustment_status
            )
        )
    child_adjustment_details = el.find("adjustmentDetails")
    if child_adjustment_details is not None:
        import capo_ec2.types.capacity_reservation_adjustment_details

        out["adjustment_details"] = (
            capo_ec2.types.capacity_reservation_adjustment_details.deserialize_ec2_query(
                child_adjustment_details
            )
        )
    child_original_start_date = el.find("originalStartDate")
    if child_original_start_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["original_start_date"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_original_start_date
            )
        )
    child_zero_size_preference = el.find("zeroSizePreference")
    if child_zero_size_preference is not None:
        import capo_ec2.types.zero_size_preference

        out["zero_size_preference"] = (
            capo_ec2.types.zero_size_preference.deserialize_ec2_query(
                child_zero_size_preference
            )
        )
    child_launch_status = el.find("launchStatus")
    if child_launch_status is not None:
        import capo_ec2.types.capacity_reservation_launch_status

        out["launch_status"] = (
            capo_ec2.types.capacity_reservation_launch_status.deserialize_ec2_query(
                child_launch_status
            )
        )
    return out

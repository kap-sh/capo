"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityReservationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_id
    import capo_ec2.types.availability_zone_name
    import capo_ec2.types.boolean
    import capo_ec2.types.capacity_reservation_commitment_duration
    import capo_ec2.types.capacity_reservation_delivery_preference
    import capo_ec2.types.capacity_reservation_instance_platform
    import capo_ec2.types.capacity_reservation_tenancy
    import capo_ec2.types.date_time
    import capo_ec2.types.end_date_type
    import capo_ec2.types.instance_match_criteria
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.outpost_arn
    import capo_ec2.types.placement_group_arn
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateCapacityReservationRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensure Idempotency</a>.</p>"""
    instance_type: NotRequired["capo_ec2.types.string.String"]
    """<p>The instance type for which to reserve capacity.</p> <note> <p>You can request future-dated Capacity Reservations for instance types in the C, M, R, I, T, and G instance families only.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html">Instance types</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    instance_platform: NotRequired[
        "capo_ec2.types.capacity_reservation_instance_platform.CapacityReservationInstancePlatform"
    ]
    """<p>The type of operating system for which to reserve capacity.</p>"""
    availability_zone: NotRequired[
        "capo_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The Availability Zone in which to create the Capacity Reservation.</p>"""
    availability_zone_id: NotRequired[
        "capo_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone in which to create the Capacity Reservation.</p>"""
    tenancy: NotRequired[
        "capo_ec2.types.capacity_reservation_tenancy.CapacityReservationTenancy"
    ]
    """<p>Indicates the tenancy of the Capacity Reservation. A Capacity Reservation can have one of the following tenancy settings:</p> <ul> <li> <p> <code>default</code> - The Capacity Reservation is created on hardware that is shared with other Amazon Web Services accounts.</p> </li> <li> <p> <code>dedicated</code> - The Capacity Reservation is created on single-tenant hardware that is dedicated to a single Amazon Web Services account.</p> </li> </ul>"""
    instance_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of instances for which to reserve capacity.</p> <note> <p>You can request future-dated Capacity Reservations for an instance count with a minimum of 32 vCPUs. For example, if you request a future-dated Capacity Reservation for <code>m5.xlarge</code> instances, you must request at least 8 instances (<i>8 * m5.xlarge = 32 vCPUs</i>).</p> </note> <p>Valid range: 1 - 1000</p>"""
    ebs_optimized: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the Capacity Reservation supports EBS-optimized instances. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isn't available with all instance types. Additional usage charges apply when using an EBS- optimized instance.</p>"""
    ephemeral_storage: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p> <i>Deprecated.</i> </p>"""
    end_date: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservation's state changes to <code>expired</code> when it reaches its end date and time.</p> <p>You must provide an <code>EndDate</code> value if <code>EndDateType</code> is <code>limited</code>. Omit <code>EndDate</code> if <code>EndDateType</code> is <code>unlimited</code>.</p> <p>If the <code>EndDateType</code> is <code>limited</code>, the Capacity Reservation is cancelled within an hour from the specified time. For example, if you specify 5/31/2019, 13:30:55, the Capacity Reservation is guaranteed to end between 13:30:55 and 14:30:55 on 5/31/2019.</p> <p>If you are requesting a future-dated Capacity Reservation, you can't specify an end date and time that is within the commitment duration.</p>"""
    end_date_type: NotRequired["capo_ec2.types.end_date_type.EndDateType"]
    """<p>Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types:</p> <ul> <li> <p> <code>unlimited</code> - The Capacity Reservation remains active until you explicitly cancel it. Do not provide an <code>EndDate</code> if the <code>EndDateType</code> is <code>unlimited</code>.</p> </li> <li> <p> <code>limited</code> - The Capacity Reservation expires automatically at a specified date and time. You must provide an <code>EndDate</code> value if the <code>EndDateType</code> value is <code>limited</code>.</p> </li> </ul>"""
    instance_match_criteria: NotRequired[
        "capo_ec2.types.instance_match_criteria.InstanceMatchCriteria"
    ]
    """<p>Indicates the type of instance launches that the Capacity Reservation accepts. The options include:</p> <ul> <li> <p> <code>open</code> - The Capacity Reservation automatically matches all instances that have matching attributes (instance type, platform, and Availability Zone). Instances that have matching attributes run in the Capacity Reservation automatically without specifying any additional parameters.</p> </li> <li> <p> <code>targeted</code> - The Capacity Reservation only accepts instances that have matching attributes (instance type, platform, and Availability Zone), and explicitly target the Capacity Reservation. This ensures that only permitted instances can use the reserved capacity. </p> </li> </ul> <note> <p>If you are requesting a future-dated Capacity Reservation, you must specify <code>targeted</code>.</p> </note> <p>Default: <code>open</code> </p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the Capacity Reservation during launch.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    outpost_arn: NotRequired["capo_ec2.types.outpost_arn.OutpostArn"]
    """<note> <p>Not supported for future-dated Capacity Reservations.</p> </note> <p>The Amazon Resource Name (ARN) of the Outpost on which to create the Capacity Reservation.</p>"""
    placement_group_arn: NotRequired[
        "capo_ec2.types.placement_group_arn.PlacementGroupArn"
    ]
    """<note> <p>Not supported for future-dated Capacity Reservations.</p> </note> <p>The Amazon Resource Name (ARN) of the cluster placement group in which to create the Capacity Reservation. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-cpg.html"> Capacity Reservations for cluster placement groups</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    start_date: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<note> <p>Required for future-dated Capacity Reservations only. To create a Capacity Reservation for immediate use, omit this parameter. </p> </note> <p>The date and time at which the future-dated Capacity Reservation should become available for use, in the ISO8601 format in the UTC time zone (<code>YYYY-MM-DDThh:mm:ss.sssZ</code>).</p> <p>You can request a future-dated Capacity Reservation between 5 and 120 days in advance.</p>"""
    commitment_duration: NotRequired[
        "capo_ec2.types.capacity_reservation_commitment_duration.CapacityReservationCommitmentDuration"
    ]
    """<note> <p>Required for future-dated Capacity Reservations only. To create a Capacity Reservation for immediate use, omit this parameter. </p> </note> <p>Specify a commitment duration, in seconds, for the future-dated Capacity Reservation.</p> <p>The commitment duration is a minimum duration for which you commit to having the future-dated Capacity Reservation in the <code>active</code> state in your account after it has been delivered.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-concepts.html#cr-commitment-duration"> Commitment duration</a>.</p>"""
    delivery_preference: NotRequired[
        "capo_ec2.types.capacity_reservation_delivery_preference.CapacityReservationDeliveryPreference"
    ]
    """<note> <p>Required for future-dated Capacity Reservations only. To create a Capacity Reservation for immediate use, omit this parameter. </p> </note> <p>Indicates that the requested capacity will be delivered in addition to any running instances or reserved capacity that you have in your account at the requested date and time.</p> <p>The only supported value is <code>incremental</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateCapacityReservationRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "instance_type" in value:
        pairs.append((f"{key_prefix}InstanceType", str(value["instance_type"])))
    if "instance_platform" in value:
        import capo_ec2.types.capacity_reservation_instance_platform

        capo_ec2.types.capacity_reservation_instance_platform.serialize_ec2_query(
            value["instance_platform"], pairs, f"{key_prefix}InstancePlatform"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "tenancy" in value:
        import capo_ec2.types.capacity_reservation_tenancy

        capo_ec2.types.capacity_reservation_tenancy.serialize_ec2_query(
            value["tenancy"], pairs, f"{key_prefix}Tenancy"
        )
    if "instance_count" in value:
        pairs.append((f"{key_prefix}InstanceCount", str(value["instance_count"])))
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
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecifications"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "outpost_arn" in value:
        pairs.append((f"{key_prefix}OutpostArn", str(value["outpost_arn"])))
    if "placement_group_arn" in value:
        pairs.append(
            (f"{key_prefix}PlacementGroupArn", str(value["placement_group_arn"]))
        )
    if "start_date" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_date"], pairs, f"{key_prefix}StartDate"
        )
    if "commitment_duration" in value:
        pairs.append(
            (f"{key_prefix}CommitmentDuration", str(value["commitment_duration"]))
        )
    if "delivery_preference" in value:
        import capo_ec2.types.capacity_reservation_delivery_preference

        capo_ec2.types.capacity_reservation_delivery_preference.serialize_ec2_query(
            value["delivery_preference"], pairs, f"{key_prefix}DeliveryPreference"
        )


def deserialize_ec2_query(el: Element) -> CreateCapacityReservationRequest:
    out: CreateCapacityReservationRequest = {}  # type: ignore[typeddict-item]
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_instance_type = el.find("InstanceType")
    if child_instance_type is not None:
        out["instance_type"] = str(child_instance_type.text or "")
    child_instance_platform = el.find("InstancePlatform")
    if child_instance_platform is not None:
        import capo_ec2.types.capacity_reservation_instance_platform

        out["instance_platform"] = (
            capo_ec2.types.capacity_reservation_instance_platform.deserialize_ec2_query(
                child_instance_platform
            )
        )
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_tenancy = el.find("Tenancy")
    if child_tenancy is not None:
        import capo_ec2.types.capacity_reservation_tenancy

        out["tenancy"] = (
            capo_ec2.types.capacity_reservation_tenancy.deserialize_ec2_query(
                child_tenancy
            )
        )
    child_instance_count = el.find("InstanceCount")
    if child_instance_count is not None:
        out["instance_count"] = int(child_instance_count.text or "")
    child_ebs_optimized = el.find("EbsOptimized")
    if child_ebs_optimized is not None:
        out["ebs_optimized"] = (child_ebs_optimized.text or "").lower() == "true"
    child_ephemeral_storage = el.find("EphemeralStorage")
    if child_ephemeral_storage is not None:
        out["ephemeral_storage"] = (
            child_ephemeral_storage.text or ""
        ).lower() == "true"
    child_end_date = el.find("EndDate")
    if child_end_date is not None:
        import capo_ec2.types.date_time

        out["end_date"] = capo_ec2.types.date_time.deserialize_ec2_query(child_end_date)
    child_end_date_type = el.find("EndDateType")
    if child_end_date_type is not None:
        import capo_ec2.types.end_date_type

        out["end_date_type"] = capo_ec2.types.end_date_type.deserialize_ec2_query(
            child_end_date_type
        )
    child_instance_match_criteria = el.find("InstanceMatchCriteria")
    if child_instance_match_criteria is not None:
        import capo_ec2.types.instance_match_criteria

        out["instance_match_criteria"] = (
            capo_ec2.types.instance_match_criteria.deserialize_ec2_query(
                child_instance_match_criteria
            )
        )
    child_tag_specifications = el.find("TagSpecifications")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_outpost_arn = el.find("OutpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_placement_group_arn = el.find("PlacementGroupArn")
    if child_placement_group_arn is not None:
        out["placement_group_arn"] = str(child_placement_group_arn.text or "")
    child_start_date = el.find("StartDate")
    if child_start_date is not None:
        import capo_ec2.types.millisecond_date_time

        out["start_date"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_start_date
        )
    child_commitment_duration = el.find("CommitmentDuration")
    if child_commitment_duration is not None:
        out["commitment_duration"] = int(child_commitment_duration.text or "")
    child_delivery_preference = el.find("DeliveryPreference")
    if child_delivery_preference is not None:
        import capo_ec2.types.capacity_reservation_delivery_preference

        out["delivery_preference"] = (
            capo_ec2.types.capacity_reservation_delivery_preference.deserialize_ec2_query(
                child_delivery_preference
            )
        )
    return out

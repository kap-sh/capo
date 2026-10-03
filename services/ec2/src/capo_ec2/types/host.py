"""Generated from Smithy shape ``com.amazonaws.ec2#Host``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.allocation_state
    import capo_ec2.types.allows_multiple_instance_types
    import capo_ec2.types.asset_id
    import capo_ec2.types.auto_placement
    import capo_ec2.types.available_capacity
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.host_cpu_options
    import capo_ec2.types.host_instance_list
    import capo_ec2.types.host_maintenance
    import capo_ec2.types.host_properties
    import capo_ec2.types.host_recovery
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class Host(TypedDict, closed=True):
    auto_placement: NotRequired["capo_ec2.types.auto_placement.AutoPlacement"]
    """<p>Whether auto-placement is on or off.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone of the Dedicated Host.</p>"""
    available_capacity: NotRequired[
        "capo_ec2.types.available_capacity.AvailableCapacity"
    ]
    """<p>Information about the instances running on the Dedicated Host.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring Idempotency</a>.</p>"""
    host_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Dedicated Host.</p>"""
    host_properties: NotRequired["capo_ec2.types.host_properties.HostProperties"]
    """<p>The hardware specifications of the Dedicated Host.</p>"""
    host_reservation_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The reservation ID of the Dedicated Host. This returns a <code>null</code> response if the Dedicated Host doesn't have an associated reservation.</p>"""
    instances: NotRequired["capo_ec2.types.host_instance_list.HostInstanceList"]
    """<p>The IDs and instance type that are currently running on the Dedicated Host.</p>"""
    state: NotRequired["capo_ec2.types.allocation_state.AllocationState"]
    """<p>The Dedicated Host's state.</p>"""
    allocation_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time that the Dedicated Host was allocated.</p>"""
    release_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time that the Dedicated Host was released.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the Dedicated Host.</p>"""
    host_recovery: NotRequired["capo_ec2.types.host_recovery.HostRecovery"]
    """<p>Indicates whether host recovery is enabled or disabled for the Dedicated Host.</p>"""
    allows_multiple_instance_types: NotRequired[
        "capo_ec2.types.allows_multiple_instance_types.AllowsMultipleInstanceTypes"
    ]
    """<p>Indicates whether the Dedicated Host supports multiple instance types of the same instance family. If the value is <code>on</code>, the Dedicated Host supports multiple instance types in the instance family. If the value is <code>off</code>, the Dedicated Host supports a single instance type only.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the Dedicated Host.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone in which the Dedicated Host is allocated.</p>"""
    member_of_service_linked_resource_group: NotRequired[
        "capo_ec2.types.boolean.Boolean"
    ]
    """<p>Indicates whether the Dedicated Host is in a host resource group. If <b>memberOfServiceLinkedResourceGroup</b> is <code>true</code>, the host is in a host resource group; otherwise, it is not.</p>"""
    outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Outpost on which the Dedicated Host is allocated.</p>"""
    host_maintenance: NotRequired["capo_ec2.types.host_maintenance.HostMaintenance"]
    """<p>Indicates whether host maintenance is enabled or disabled for the Dedicated Host.</p>"""
    asset_id: NotRequired["capo_ec2.types.asset_id.AssetId"]
    """<p>The ID of the Outpost hardware asset on which the Dedicated Host is allocated.</p>"""
    cpu_options: NotRequired["capo_ec2.types.host_cpu_options.HostCpuOptions"]
    """<p>The CPU options for the Dedicated Host, including AMD Secure Encrypted Virtualization-Secure Nested Paging (AMD SEV-SNP) settings.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(value: Host, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "auto_placement" in value:
        import capo_ec2.types.auto_placement

        capo_ec2.types.auto_placement.serialize_ec2_query(
            value["auto_placement"], pairs, f"{key_prefix}AutoPlacement"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "available_capacity" in value:
        import capo_ec2.types.available_capacity

        capo_ec2.types.available_capacity.serialize_ec2_query(
            value["available_capacity"], pairs, f"{key_prefix}AvailableCapacity"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "host_id" in value:
        pairs.append((f"{key_prefix}HostId", str(value["host_id"])))
    if "host_properties" in value:
        import capo_ec2.types.host_properties

        capo_ec2.types.host_properties.serialize_ec2_query(
            value["host_properties"], pairs, f"{key_prefix}HostProperties"
        )
    if "host_reservation_id" in value:
        pairs.append(
            (f"{key_prefix}HostReservationId", str(value["host_reservation_id"]))
        )
    if "instances" in value:
        import capo_ec2.types.host_instance_list

        capo_ec2.types.host_instance_list.serialize_ec2_query(
            value["instances"], pairs, f"{key_prefix}Instances"
        )
    if "state" in value:
        import capo_ec2.types.allocation_state

        capo_ec2.types.allocation_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "allocation_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["allocation_time"], pairs, f"{key_prefix}AllocationTime"
        )
    if "release_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["release_time"], pairs, f"{key_prefix}ReleaseTime"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "host_recovery" in value:
        import capo_ec2.types.host_recovery

        capo_ec2.types.host_recovery.serialize_ec2_query(
            value["host_recovery"], pairs, f"{key_prefix}HostRecovery"
        )
    if "allows_multiple_instance_types" in value:
        import capo_ec2.types.allows_multiple_instance_types

        capo_ec2.types.allows_multiple_instance_types.serialize_ec2_query(
            value["allows_multiple_instance_types"],
            pairs,
            f"{key_prefix}AllowsMultipleInstanceTypes",
        )
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "member_of_service_linked_resource_group" in value:
        pairs.append(
            (
                f"{key_prefix}MemberOfServiceLinkedResourceGroup",
                "true" if value["member_of_service_linked_resource_group"] else "false",
            )
        )
    if "outpost_arn" in value:
        pairs.append((f"{key_prefix}OutpostArn", str(value["outpost_arn"])))
    if "host_maintenance" in value:
        import capo_ec2.types.host_maintenance

        capo_ec2.types.host_maintenance.serialize_ec2_query(
            value["host_maintenance"], pairs, f"{key_prefix}HostMaintenance"
        )
    if "asset_id" in value:
        pairs.append((f"{key_prefix}AssetId", str(value["asset_id"])))
    if "cpu_options" in value:
        import capo_ec2.types.host_cpu_options

        capo_ec2.types.host_cpu_options.serialize_ec2_query(
            value["cpu_options"], pairs, f"{key_prefix}CpuOptions"
        )


def deserialize_ec2_query(el: Element) -> Host:
    out: Host = {}  # type: ignore[typeddict-item]
    child_auto_placement = el.find("autoPlacement")
    if child_auto_placement is not None:
        import capo_ec2.types.auto_placement

        out["auto_placement"] = capo_ec2.types.auto_placement.deserialize_ec2_query(
            child_auto_placement
        )
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_available_capacity = el.find("availableCapacity")
    if child_available_capacity is not None:
        import capo_ec2.types.available_capacity

        out["available_capacity"] = (
            capo_ec2.types.available_capacity.deserialize_ec2_query(
                child_available_capacity
            )
        )
    child_client_token = el.find("clientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_host_id = el.find("hostId")
    if child_host_id is not None:
        out["host_id"] = str(child_host_id.text or "")
    child_host_properties = el.find("hostProperties")
    if child_host_properties is not None:
        import capo_ec2.types.host_properties

        out["host_properties"] = capo_ec2.types.host_properties.deserialize_ec2_query(
            child_host_properties
        )
    child_host_reservation_id = el.find("hostReservationId")
    if child_host_reservation_id is not None:
        out["host_reservation_id"] = str(child_host_reservation_id.text or "")
    child_instances = el.find("instances")
    if child_instances is not None:
        import capo_ec2.types.host_instance_list

        out["instances"] = capo_ec2.types.host_instance_list.deserialize_ec2_query(
            child_instances
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.allocation_state

        out["state"] = capo_ec2.types.allocation_state.deserialize_ec2_query(
            child_state
        )
    child_allocation_time = el.find("allocationTime")
    if child_allocation_time is not None:
        import capo_ec2.types.date_time

        out["allocation_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_allocation_time
        )
    child_release_time = el.find("releaseTime")
    if child_release_time is not None:
        import capo_ec2.types.date_time

        out["release_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_release_time
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_host_recovery = el.find("hostRecovery")
    if child_host_recovery is not None:
        import capo_ec2.types.host_recovery

        out["host_recovery"] = capo_ec2.types.host_recovery.deserialize_ec2_query(
            child_host_recovery
        )
    child_allows_multiple_instance_types = el.find("allowsMultipleInstanceTypes")
    if child_allows_multiple_instance_types is not None:
        import capo_ec2.types.allows_multiple_instance_types

        out["allows_multiple_instance_types"] = (
            capo_ec2.types.allows_multiple_instance_types.deserialize_ec2_query(
                child_allows_multiple_instance_types
            )
        )
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_member_of_service_linked_resource_group = el.find(
        "memberOfServiceLinkedResourceGroup"
    )
    if child_member_of_service_linked_resource_group is not None:
        out["member_of_service_linked_resource_group"] = (
            child_member_of_service_linked_resource_group.text or ""
        ).lower() == "true"
    child_outpost_arn = el.find("outpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_host_maintenance = el.find("hostMaintenance")
    if child_host_maintenance is not None:
        import capo_ec2.types.host_maintenance

        out["host_maintenance"] = capo_ec2.types.host_maintenance.deserialize_ec2_query(
            child_host_maintenance
        )
    child_asset_id = el.find("assetId")
    if child_asset_id is not None:
        out["asset_id"] = str(child_asset_id.text or "")
    child_cpu_options = el.find("cpuOptions")
    if child_cpu_options is not None:
        import capo_ec2.types.host_cpu_options

        out["cpu_options"] = capo_ec2.types.host_cpu_options.deserialize_ec2_query(
            child_cpu_options
        )
    return out

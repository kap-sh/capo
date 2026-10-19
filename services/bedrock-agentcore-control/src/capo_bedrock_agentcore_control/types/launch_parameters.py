"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LaunchParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.capacity_reservation_specification
    import capo_bedrock_agentcore_control.types.ephemeral_block_device_mapping_list
    import capo_bedrock_agentcore_control.types.instance_profile_arn
    import capo_bedrock_agentcore_control.types.instance_requirements
    import capo_bedrock_agentcore_control.types.license_specification_list
    import capo_bedrock_agentcore_control.types.monitoring
    import capo_bedrock_agentcore_control.types.operating_system
    import capo_bedrock_agentcore_control.types.ssh_key_name
    import capo_bedrock_agentcore_control.types.tags_map


class LaunchParameters(TypedDict, closed=True):
    operating_system: (
        "capo_bedrock_agentcore_control.types.operating_system.OperatingSystem"
    )
    """<p>The operating system and CPU architecture for the instances.</p>"""
    instance_requirements: "capo_bedrock_agentcore_control.types.instance_requirements.InstanceRequirements"
    """<p>The requirements that determine which instance types can be launched.</p>"""
    ephemeral_volumes: NotRequired[
        "capo_bedrock_agentcore_control.types.ephemeral_block_device_mapping_list.EphemeralBlockDeviceMappingList"
    ]
    """<p>The block device mappings for instance store (ephemeral) volumes. You can specify up to five mappings.</p>"""
    monitoring: NotRequired[
        "capo_bedrock_agentcore_control.types.monitoring.Monitoring"
    ]
    """<p>The monitoring level for the instances.</p>"""
    license_specifications: NotRequired[
        "capo_bedrock_agentcore_control.types.license_specification_list.LicenseSpecificationList"
    ]
    """<p>The license configurations to associate with the instances. You can specify up to five configurations.</p>"""
    capacity_reservation_specification: NotRequired[
        "capo_bedrock_agentcore_control.types.capacity_reservation_specification.CapacityReservationSpecification"
    ]
    """<p>The Capacity Reservation targeting option for the instances.</p>"""
    ssh_key_name: NotRequired[
        "capo_bedrock_agentcore_control.types.ssh_key_name.SSHKeyName"
    ]
    """<p>The name of the SSH key pair to configure on the instances for SSH connectivity.</p>"""
    instance_profile_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.instance_profile_arn.InstanceProfileArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM instance profile to associate with launched instances. If provided, this overrides the default instance profile.</p>"""
    propagated_tags: NotRequired[
        "capo_bedrock_agentcore_control.types.tags_map.TagsMap"
    ]
    """<p>The tags to propagate to all Amazon EC2 resources (instances, volumes, and network interfaces) that the capacity provider creates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LaunchParameters) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.operating_system

    out["operatingSystem"] = (
        capo_bedrock_agentcore_control.types.operating_system.serialize_json(
            value["operating_system"]
        )
    )
    import capo_bedrock_agentcore_control.types.instance_requirements

    out["instanceRequirements"] = (
        capo_bedrock_agentcore_control.types.instance_requirements.serialize_json(
            value["instance_requirements"]
        )
    )
    if "ephemeral_volumes" in value:
        import capo_bedrock_agentcore_control.types.ephemeral_block_device_mapping_list

        out["ephemeralVolumes"] = (
            capo_bedrock_agentcore_control.types.ephemeral_block_device_mapping_list.serialize_json(
                value["ephemeral_volumes"]
            )
        )
    if "monitoring" in value:
        import capo_bedrock_agentcore_control.types.monitoring

        out["monitoring"] = (
            capo_bedrock_agentcore_control.types.monitoring.serialize_json(
                value["monitoring"]
            )
        )
    if "license_specifications" in value:
        import capo_bedrock_agentcore_control.types.license_specification_list

        out["licenseSpecifications"] = (
            capo_bedrock_agentcore_control.types.license_specification_list.serialize_json(
                value["license_specifications"]
            )
        )
    if "capacity_reservation_specification" in value:
        import capo_bedrock_agentcore_control.types.capacity_reservation_specification

        out["capacityReservationSpecification"] = (
            capo_bedrock_agentcore_control.types.capacity_reservation_specification.serialize_json(
                value["capacity_reservation_specification"]
            )
        )
    if "ssh_key_name" in value:
        out["sshKeyName"] = value["ssh_key_name"]
    if "instance_profile_arn" in value:
        out["instanceProfileArn"] = value["instance_profile_arn"]
    if "propagated_tags" in value:
        import capo_bedrock_agentcore_control.types.tags_map

        out["propagatedTags"] = (
            capo_bedrock_agentcore_control.types.tags_map.serialize_json(
                value["propagated_tags"]
            )
        )
    return out


def deserialize_json(data: dict) -> LaunchParameters:
    out: LaunchParameters = {}  # type: ignore[typeddict-item]
    if data.get("operatingSystem") is not None:
        import capo_bedrock_agentcore_control.types.operating_system

        out["operating_system"] = (
            capo_bedrock_agentcore_control.types.operating_system.deserialize_json(
                data["operatingSystem"]
            )
        )
    else:
        import typing

        out["operating_system"] = typing.cast(
            "capo_bedrock_agentcore_control.types.operating_system.OperatingSystem", ""
        )
    if data.get("instanceRequirements") is not None:
        import capo_bedrock_agentcore_control.types.instance_requirements

        out["instance_requirements"] = (
            capo_bedrock_agentcore_control.types.instance_requirements.deserialize_json(
                data["instanceRequirements"]
            )
        )
    else:
        raise DeserializationError("LaunchParameters.instance_requirements required")
    if data.get("ephemeralVolumes") is not None:
        import capo_bedrock_agentcore_control.types.ephemeral_block_device_mapping_list

        out["ephemeral_volumes"] = (
            capo_bedrock_agentcore_control.types.ephemeral_block_device_mapping_list.deserialize_json(
                data["ephemeralVolumes"]
            )
        )
    if data.get("monitoring") is not None:
        import capo_bedrock_agentcore_control.types.monitoring

        out["monitoring"] = (
            capo_bedrock_agentcore_control.types.monitoring.deserialize_json(
                data["monitoring"]
            )
        )
    if data.get("licenseSpecifications") is not None:
        import capo_bedrock_agentcore_control.types.license_specification_list

        out["license_specifications"] = (
            capo_bedrock_agentcore_control.types.license_specification_list.deserialize_json(
                data["licenseSpecifications"]
            )
        )
    if data.get("capacityReservationSpecification") is not None:
        import capo_bedrock_agentcore_control.types.capacity_reservation_specification

        out["capacity_reservation_specification"] = (
            capo_bedrock_agentcore_control.types.capacity_reservation_specification.deserialize_json(
                data["capacityReservationSpecification"]
            )
        )
    if data.get("sshKeyName") is not None:
        out["ssh_key_name"] = data["sshKeyName"]
    if data.get("instanceProfileArn") is not None:
        out["instance_profile_arn"] = data["instanceProfileArn"]
    if data.get("propagatedTags") is not None:
        import capo_bedrock_agentcore_control.types.tags_map

        out["propagated_tags"] = (
            capo_bedrock_agentcore_control.types.tags_map.deserialize_json(
                data["propagatedTags"]
            )
        )
    return out

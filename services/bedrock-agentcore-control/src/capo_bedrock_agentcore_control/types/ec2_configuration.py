"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Ec2Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.instance_lifecycle_configuration
    import capo_bedrock_agentcore_control.types.launch_template_source
    import capo_bedrock_agentcore_control.types.root_volume_configuration
    import capo_bedrock_agentcore_control.types.volume_configuration_list
    import capo_bedrock_agentcore_control.types.vpc_configuration


class Ec2Configuration(TypedDict, closed=True):
    launch_template_source: "capo_bedrock_agentcore_control.types.launch_template_source.LaunchTemplateSource"
    """<p>The source of the launch template configuration that defines how instances are launched.</p>"""
    vpc_configuration: (
        "capo_bedrock_agentcore_control.types.vpc_configuration.VpcConfiguration"
    )
    """<p>The VPC configuration for launching instances, including subnets and security groups.</p>"""
    volumes: NotRequired[
        "capo_bedrock_agentcore_control.types.volume_configuration_list.VolumeConfigurationList"
    ]
    """<p>The named persistent Amazon EBS volumes for the capacity provider. A capacity provider can define up to five volumes.</p>"""
    lifecycle_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.instance_lifecycle_configuration.InstanceLifecycleConfiguration"
    ]
    """<p>The lifecycle configuration for instances in the capacity provider.</p>"""
    root_volume: NotRequired[
        "capo_bedrock_agentcore_control.types.root_volume_configuration.RootVolumeConfiguration"
    ]
    """<p>The configuration for the instance root volume. Specify the amount of free space to guarantee and, optionally, the Amazon EBS performance and encryption settings. The device name and delete-on-termination behavior are not configurable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2Configuration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.launch_template_source

    out["launchTemplateSource"] = (
        capo_bedrock_agentcore_control.types.launch_template_source.serialize_json(
            value["launch_template_source"]
        )
    )
    import capo_bedrock_agentcore_control.types.vpc_configuration

    out["vpcConfiguration"] = (
        capo_bedrock_agentcore_control.types.vpc_configuration.serialize_json(
            value["vpc_configuration"]
        )
    )
    if "volumes" in value:
        import capo_bedrock_agentcore_control.types.volume_configuration_list

        out["volumes"] = (
            capo_bedrock_agentcore_control.types.volume_configuration_list.serialize_json(
                value["volumes"]
            )
        )
    if "lifecycle_configuration" in value:
        import capo_bedrock_agentcore_control.types.instance_lifecycle_configuration

        out["lifecycleConfiguration"] = (
            capo_bedrock_agentcore_control.types.instance_lifecycle_configuration.serialize_json(
                value["lifecycle_configuration"]
            )
        )
    if "root_volume" in value:
        import capo_bedrock_agentcore_control.types.root_volume_configuration

        out["rootVolume"] = (
            capo_bedrock_agentcore_control.types.root_volume_configuration.serialize_json(
                value["root_volume"]
            )
        )
    return out


def deserialize_json(data: dict) -> Ec2Configuration:
    out: Ec2Configuration = {}  # type: ignore[typeddict-item]
    if data.get("launchTemplateSource") is not None:
        import capo_bedrock_agentcore_control.types.launch_template_source

        out["launch_template_source"] = (
            capo_bedrock_agentcore_control.types.launch_template_source.deserialize_json(
                data["launchTemplateSource"]
            )
        )
    else:
        import capo_bedrock_agentcore_control.types._unknown

        out["launch_template_source"] = (
            capo_bedrock_agentcore_control.types._unknown.UnknownUnionMember("")
        )
    if data.get("vpcConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.vpc_configuration

        out["vpc_configuration"] = (
            capo_bedrock_agentcore_control.types.vpc_configuration.deserialize_json(
                data["vpcConfiguration"]
            )
        )
    else:
        raise DeserializationError("Ec2Configuration.vpc_configuration required")
    if data.get("volumes") is not None:
        import capo_bedrock_agentcore_control.types.volume_configuration_list

        out["volumes"] = (
            capo_bedrock_agentcore_control.types.volume_configuration_list.deserialize_json(
                data["volumes"]
            )
        )
    if data.get("lifecycleConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.instance_lifecycle_configuration

        out["lifecycle_configuration"] = (
            capo_bedrock_agentcore_control.types.instance_lifecycle_configuration.deserialize_json(
                data["lifecycleConfiguration"]
            )
        )
    if data.get("rootVolume") is not None:
        import capo_bedrock_agentcore_control.types.root_volume_configuration

        out["root_volume"] = (
            capo_bedrock_agentcore_control.types.root_volume_configuration.deserialize_json(
                data["rootVolume"]
            )
        )
    return out

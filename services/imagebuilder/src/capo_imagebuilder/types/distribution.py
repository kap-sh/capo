"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Distribution``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.ami_distribution_configuration
    import capo_imagebuilder.types.container_distribution_configuration
    import capo_imagebuilder.types.fast_launch_configuration_list
    import capo_imagebuilder.types.launch_template_configuration_list
    import capo_imagebuilder.types.license_configuration_arn_list
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.s3_export_configuration
    import capo_imagebuilder.types.ssm_parameter_configuration_list


class Distribution(TypedDict, closed=True):
    region: "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The target Region.</p>"""
    ami_distribution_configuration: NotRequired[
        "capo_imagebuilder.types.ami_distribution_configuration.AmiDistributionConfiguration"
    ]
    """<p>The specific AMI settings; for example, launch permissions or AMI tags.</p>"""
    container_distribution_configuration: NotRequired[
        "capo_imagebuilder.types.container_distribution_configuration.ContainerDistributionConfiguration"
    ]
    """<p>Container distribution settings for encryption, licensing, and sharing in a specific Region.</p>"""
    license_configuration_arns: NotRequired[
        "capo_imagebuilder.types.license_configuration_arn_list.LicenseConfigurationArnList"
    ]
    """<p>The License Manager Configuration to associate with the AMI in the specified Region.</p>"""
    launch_template_configurations: NotRequired[
        "capo_imagebuilder.types.launch_template_configuration_list.LaunchTemplateConfigurationList"
    ]
    """<p>A group of launchTemplateConfiguration settings that apply to image distribution for specified accounts.</p>"""
    s3_export_configuration: NotRequired[
        "capo_imagebuilder.types.s3_export_configuration.S3ExportConfiguration"
    ]
    """<p>Configure export settings to deliver disk images created from your image build, using a file format that is compatible with your VMs in that Region.</p>"""
    fast_launch_configurations: NotRequired[
        "capo_imagebuilder.types.fast_launch_configuration_list.FastLaunchConfigurationList"
    ]
    """<p>The Windows faster-launching configurations to use for AMI distribution.</p>"""
    ssm_parameter_configurations: NotRequired[
        "capo_imagebuilder.types.ssm_parameter_configuration_list.SsmParameterConfigurationList"
    ]
    """<p>Contains settings to update Amazon Web Services Systems Manager (SSM) Parameter Store Parameters with output AMI IDs from the build by target Region.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Distribution) -> dict:
    out: dict = {}
    out["region"] = value["region"]
    if "ami_distribution_configuration" in value:
        import capo_imagebuilder.types.ami_distribution_configuration

        out["amiDistributionConfiguration"] = (
            capo_imagebuilder.types.ami_distribution_configuration.serialize_json(
                value["ami_distribution_configuration"]
            )
        )
    if "container_distribution_configuration" in value:
        import capo_imagebuilder.types.container_distribution_configuration

        out["containerDistributionConfiguration"] = (
            capo_imagebuilder.types.container_distribution_configuration.serialize_json(
                value["container_distribution_configuration"]
            )
        )
    if "license_configuration_arns" in value:
        import capo_imagebuilder.types.license_configuration_arn_list

        out["licenseConfigurationArns"] = (
            capo_imagebuilder.types.license_configuration_arn_list.serialize_json(
                value["license_configuration_arns"]
            )
        )
    if "launch_template_configurations" in value:
        import capo_imagebuilder.types.launch_template_configuration_list

        out["launchTemplateConfigurations"] = (
            capo_imagebuilder.types.launch_template_configuration_list.serialize_json(
                value["launch_template_configurations"]
            )
        )
    if "s3_export_configuration" in value:
        import capo_imagebuilder.types.s3_export_configuration

        out["s3ExportConfiguration"] = (
            capo_imagebuilder.types.s3_export_configuration.serialize_json(
                value["s3_export_configuration"]
            )
        )
    if "fast_launch_configurations" in value:
        import capo_imagebuilder.types.fast_launch_configuration_list

        out["fastLaunchConfigurations"] = (
            capo_imagebuilder.types.fast_launch_configuration_list.serialize_json(
                value["fast_launch_configurations"]
            )
        )
    if "ssm_parameter_configurations" in value:
        import capo_imagebuilder.types.ssm_parameter_configuration_list

        out["ssmParameterConfigurations"] = (
            capo_imagebuilder.types.ssm_parameter_configuration_list.serialize_json(
                value["ssm_parameter_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> Distribution:
    out: Distribution = {}  # type: ignore[typeddict-item]
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        out["region"] = ""
    if data.get("amiDistributionConfiguration") is not None:
        import capo_imagebuilder.types.ami_distribution_configuration

        out["ami_distribution_configuration"] = (
            capo_imagebuilder.types.ami_distribution_configuration.deserialize_json(
                data["amiDistributionConfiguration"]
            )
        )
    if data.get("containerDistributionConfiguration") is not None:
        import capo_imagebuilder.types.container_distribution_configuration

        out["container_distribution_configuration"] = (
            capo_imagebuilder.types.container_distribution_configuration.deserialize_json(
                data["containerDistributionConfiguration"]
            )
        )
    if data.get("licenseConfigurationArns") is not None:
        import capo_imagebuilder.types.license_configuration_arn_list

        out["license_configuration_arns"] = (
            capo_imagebuilder.types.license_configuration_arn_list.deserialize_json(
                data["licenseConfigurationArns"]
            )
        )
    if data.get("launchTemplateConfigurations") is not None:
        import capo_imagebuilder.types.launch_template_configuration_list

        out["launch_template_configurations"] = (
            capo_imagebuilder.types.launch_template_configuration_list.deserialize_json(
                data["launchTemplateConfigurations"]
            )
        )
    if data.get("s3ExportConfiguration") is not None:
        import capo_imagebuilder.types.s3_export_configuration

        out["s3_export_configuration"] = (
            capo_imagebuilder.types.s3_export_configuration.deserialize_json(
                data["s3ExportConfiguration"]
            )
        )
    if data.get("fastLaunchConfigurations") is not None:
        import capo_imagebuilder.types.fast_launch_configuration_list

        out["fast_launch_configurations"] = (
            capo_imagebuilder.types.fast_launch_configuration_list.deserialize_json(
                data["fastLaunchConfigurations"]
            )
        )
    if data.get("ssmParameterConfigurations") is not None:
        import capo_imagebuilder.types.ssm_parameter_configuration_list

        out["ssm_parameter_configurations"] = (
            capo_imagebuilder.types.ssm_parameter_configuration_list.deserialize_json(
                data["ssmParameterConfigurations"]
            )
        )
    return out

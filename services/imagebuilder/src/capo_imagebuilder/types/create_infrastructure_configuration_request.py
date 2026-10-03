"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateInfrastructureConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.boolean
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.instance_metadata_options
    import capo_imagebuilder.types.instance_profile_name_type
    import capo_imagebuilder.types.instance_type_list
    import capo_imagebuilder.types.logging
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.nullable_boolean
    import capo_imagebuilder.types.placement
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.resource_tag_map
    import capo_imagebuilder.types.security_group_ids
    import capo_imagebuilder.types.sns_topic_arn
    import capo_imagebuilder.types.tag_map


class CreateInfrastructureConfigurationRequest(TypedDict, closed=True):
    name: "capo_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the infrastructure configuration. Infrastructure configuration names must be unique to your account in each Amazon Web Services Region. Image Builder generates the infrastructure configuration ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the infrastructure configuration.</p>"""
    instance_types: NotRequired[
        "capo_imagebuilder.types.instance_type_list.InstanceTypeList"
    ]
    """<p>The instance types of the infrastructure configuration. You can specify one or more instance types to use for this build. Image Builder picks one of these instance types based on availability. If you don't specify instance types, Image Builder selects compatible instance types automatically. If you specify a Dedicated Host, Image Builder uses only instance types that the host supports.</p>"""
    instance_profile_name: (
        "capo_imagebuilder.types.instance_profile_name_type.InstanceProfileNameType"
    )
    """<p>The instance profile to associate with the instance used to customize your Amazon EC2 AMI. The instance profile must exist in your account.</p>"""
    security_group_ids: NotRequired[
        "capo_imagebuilder.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The security group IDs to associate with the instance used to customize your Amazon EC2 AMI.</p>"""
    subnet_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The subnet ID in which to place the instance used to customize your Amazon EC2 AMI. If you specify <code>subnetId</code>, you must also specify one or more security group IDs in <code>securityGroupIds</code>. Otherwise, the request fails.</p>"""
    logging: NotRequired["capo_imagebuilder.types.logging.Logging"]
    """<p>The logging configuration of the infrastructure configuration. When you configure S3 logs, Image Builder writes logs from the build and test process to the specified bucket under the key prefix.</p>"""
    key_pair: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The key pair of the infrastructure configuration. You can use this to log on to and debug the instance used to create your image.</p>"""
    terminate_instance_on_failure: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Specifies whether to terminate the instance on failure. Set to false if you want Image Builder to retain the instance used to configure your AMI if the build or test phase of your workflow fails. Defaults to <code>true</code>.</p>"""
    sns_topic_arn: NotRequired["capo_imagebuilder.types.sns_topic_arn.SnsTopicArn"]
    """<p>The Amazon Resource Name (ARN) of the SNS topic to which Image Builder sends image build event notifications. Specify a standard topic. Image Builder doesn't support FIFO topics. Image Builder validates the topic when you create or update the configuration. You must have permission to publish to the topic.</p> <note> <p>EC2 Image Builder can't send notifications to SNS topics that are encrypted using keys from other accounts. If your SNS topic is encrypted, the key must be owned by the same account that owns your Image Builder resources.</p> </note>"""
    resource_tags: NotRequired[
        "capo_imagebuilder.types.resource_tag_map.ResourceTagMap"
    ]
    """<p>The metadata tags to assign to the Amazon EC2 instance that Image Builder launches during the build process. Tags are formatted as key value pairs. Tag keys can't begin with <code>aws:</code> or match one of the following reserved keys: <code>CreatedBy</code>, <code>Ec2ImageBuilderArn</code>, <code>Name</code>, or <code>Tags</code>.</p>"""
    instance_metadata_options: NotRequired[
        "capo_imagebuilder.types.instance_metadata_options.InstanceMetadataOptions"
    ]
    """<p>The instance metadata service (IMDS) settings that Image Builder applies to the EC2 build and test instances it launches during image creation. If you don't set these options, the EC2 launch defaults for the instance apply. For more information about instance metadata options, see one of the following links:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html">Configure the instance metadata options</a> in the <i> <i>Amazon EC2 User Guide</i> </i> for Linux instances.</p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/configuring-instance-metadata-options.html">Configure the instance metadata options</a> in the <i> <i>Amazon EC2 Windows Guide</i> </i> for Windows instances.</p> </li> </ul>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The metadata tags to assign to the infrastructure configuration resource that Image Builder creates as output. Tags are formatted as key value pairs.</p>"""
    placement: NotRequired["capo_imagebuilder.types.placement.Placement"]
    """<p>The instance placement settings that define where the build and test instances that Image Builder launches during image creation run. These settings don't affect instances that you launch from the output image.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    dry_run: "capo_imagebuilder.types.boolean.Boolean"
    """<p>Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a <code>DryRunOperationException</code> error response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateInfrastructureConfigurationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "instance_types" in value:
        import capo_imagebuilder.types.instance_type_list

        out["instanceTypes"] = (
            capo_imagebuilder.types.instance_type_list.serialize_json(
                value["instance_types"]
            )
        )
    out["instanceProfileName"] = value["instance_profile_name"]
    if "security_group_ids" in value:
        import capo_imagebuilder.types.security_group_ids

        out["securityGroupIds"] = (
            capo_imagebuilder.types.security_group_ids.serialize_json(
                value["security_group_ids"]
            )
        )
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    if "logging" in value:
        import capo_imagebuilder.types.logging

        out["logging"] = capo_imagebuilder.types.logging.serialize_json(
            value["logging"]
        )
    if "key_pair" in value:
        out["keyPair"] = value["key_pair"]
    if "terminate_instance_on_failure" in value:
        out["terminateInstanceOnFailure"] = value["terminate_instance_on_failure"]
    if "sns_topic_arn" in value:
        out["snsTopicArn"] = value["sns_topic_arn"]
    if "resource_tags" in value:
        import capo_imagebuilder.types.resource_tag_map

        out["resourceTags"] = capo_imagebuilder.types.resource_tag_map.serialize_json(
            value["resource_tags"]
        )
    if "instance_metadata_options" in value:
        import capo_imagebuilder.types.instance_metadata_options

        out["instanceMetadataOptions"] = (
            capo_imagebuilder.types.instance_metadata_options.serialize_json(
                value["instance_metadata_options"]
            )
        )
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "placement" in value:
        import capo_imagebuilder.types.placement

        out["placement"] = capo_imagebuilder.types.placement.serialize_json(
            value["placement"]
        )
    out["clientToken"] = value["client_token"]
    out["dryRun"] = value.get("dry_run", False)
    return out


def deserialize_json(data: dict) -> CreateInfrastructureConfigurationRequest:
    out: CreateInfrastructureConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateInfrastructureConfigurationRequest.name required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("instanceTypes") is not None:
        import capo_imagebuilder.types.instance_type_list

        out["instance_types"] = (
            capo_imagebuilder.types.instance_type_list.deserialize_json(
                data["instanceTypes"]
            )
        )
    if data.get("instanceProfileName") is not None:
        out["instance_profile_name"] = data["instanceProfileName"]
    else:
        raise DeserializationError(
            "CreateInfrastructureConfigurationRequest.instance_profile_name required"
        )
    if data.get("securityGroupIds") is not None:
        import capo_imagebuilder.types.security_group_ids

        out["security_group_ids"] = (
            capo_imagebuilder.types.security_group_ids.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if data.get("subnetId") is not None:
        out["subnet_id"] = data["subnetId"]
    if data.get("logging") is not None:
        import capo_imagebuilder.types.logging

        out["logging"] = capo_imagebuilder.types.logging.deserialize_json(
            data["logging"]
        )
    if data.get("keyPair") is not None:
        out["key_pair"] = data["keyPair"]
    if data.get("terminateInstanceOnFailure") is not None:
        out["terminate_instance_on_failure"] = data["terminateInstanceOnFailure"]
    if data.get("snsTopicArn") is not None:
        out["sns_topic_arn"] = data["snsTopicArn"]
    if data.get("resourceTags") is not None:
        import capo_imagebuilder.types.resource_tag_map

        out["resource_tags"] = (
            capo_imagebuilder.types.resource_tag_map.deserialize_json(
                data["resourceTags"]
            )
        )
    if data.get("instanceMetadataOptions") is not None:
        import capo_imagebuilder.types.instance_metadata_options

        out["instance_metadata_options"] = (
            capo_imagebuilder.types.instance_metadata_options.deserialize_json(
                data["instanceMetadataOptions"]
            )
        )
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if data.get("placement") is not None:
        import capo_imagebuilder.types.placement

        out["placement"] = capo_imagebuilder.types.placement.deserialize_json(
            data["placement"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "CreateInfrastructureConfigurationRequest.client_token required"
        )
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    else:
        out["dry_run"] = False
    return out

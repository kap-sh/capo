"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateImageRecipeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.additional_instance_configuration
    import capo_imagebuilder.types.ami_watermarks_list
    import capo_imagebuilder.types.boolean
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.component_configuration_list
    import capo_imagebuilder.types.instance_block_device_mappings
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.wildcard_version_number


class CreateImageRecipeRequest(TypedDict, closed=True):
    name: "capo_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the image recipe. The recipe name, combined with the semantic version, must be unique to your account in each Amazon Web Services Region. Image Builder generates the image recipe ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the image recipe.</p>"""
    semantic_version: (
        "capo_imagebuilder.types.wildcard_version_number.WildcardVersionNumber"
    )
    """<p>The semantic version of the image recipe. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>"""
    components: NotRequired[
        "capo_imagebuilder.types.component_configuration_list.ComponentConfigurationList"
    ]
    """<p>The components included in the image recipe. Components are optional. A recipe with no components bakes the base image without additional customization. You can specify each component only one time in a recipe. Components with a status of <code>DEPRECATED</code> or <code>DISABLED</code> can't be added to new recipes.</p>"""
    parent_image: "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The base image for customizations specified in the image recipe. You can specify the parent image using one of the following options:</p> <ul> <li> <p>AMI ID</p> </li> <li> <p>Image Builder image Amazon Resource Name (ARN)</p> </li> <li> <p>Amazon Web Services Systems Manager (SSM) Parameter Store Parameter, prefixed by <code>ssm:</code>, followed by the parameter name or ARN.</p> </li> <li> <p>Amazon Web Services Marketplace product ID</p> </li> </ul> <p>If you enter an AMI ID or an SSM parameter that contains the AMI ID, you must have access to the AMI. The AMI must also be in the Region where you're creating the recipe.</p>"""
    block_device_mappings: NotRequired[
        "capo_imagebuilder.types.instance_block_device_mappings.InstanceBlockDeviceMappings"
    ]
    """<p>The block device mappings that Image Builder applies to the build instance and the output AMI. For example, you can override the size of the base image's root volume or attach additional EBS volumes.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>The tags of the image recipe.</p>"""
    working_directory: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The working directory used during build and test workflows. If you don't specify a working directory, Image Builder uses <code>/tmp</code> for Linux and macOS build instances, and <code>C:/</code> for Windows build instances.</p>"""
    additional_instance_configuration: NotRequired[
        "capo_imagebuilder.types.additional_instance_configuration.AdditionalInstanceConfiguration"
    ]
    """<p>The additional settings and launch scripts for your build instances.</p>"""
    ami_tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags that are applied to the AMI that Image Builder creates during the Build phase prior to image distribution.</p>"""
    ami_watermarks: NotRequired[
        "capo_imagebuilder.types.ami_watermarks_list.AmiWatermarksList"
    ]
    """<p>The AMI watermark names to attach to the output AMI from this recipe. AMI watermarks are lineage markers. They automatically propagate to derivative AMIs when the source AMI is copied or distributed across Regions or accounts.</p> <note> <p>AMI watermarks are supported only for image recipes. AMIs with watermarks cannot be made public.</p> </note>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    dry_run: "capo_imagebuilder.types.boolean.Boolean"
    """<p>Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a <code>DryRunOperationException</code> error response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateImageRecipeRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["semanticVersion"] = value["semantic_version"]
    if "components" in value:
        import capo_imagebuilder.types.component_configuration_list

        out["components"] = (
            capo_imagebuilder.types.component_configuration_list.serialize_json(
                value["components"]
            )
        )
    out["parentImage"] = value["parent_image"]
    if "block_device_mappings" in value:
        import capo_imagebuilder.types.instance_block_device_mappings

        out["blockDeviceMappings"] = (
            capo_imagebuilder.types.instance_block_device_mappings.serialize_json(
                value["block_device_mappings"]
            )
        )
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "working_directory" in value:
        out["workingDirectory"] = value["working_directory"]
    if "additional_instance_configuration" in value:
        import capo_imagebuilder.types.additional_instance_configuration

        out["additionalInstanceConfiguration"] = (
            capo_imagebuilder.types.additional_instance_configuration.serialize_json(
                value["additional_instance_configuration"]
            )
        )
    if "ami_tags" in value:
        import capo_imagebuilder.types.tag_map

        out["amiTags"] = capo_imagebuilder.types.tag_map.serialize_json(
            value["ami_tags"]
        )
    if "ami_watermarks" in value:
        import capo_imagebuilder.types.ami_watermarks_list

        out["amiWatermarks"] = (
            capo_imagebuilder.types.ami_watermarks_list.serialize_json(
                value["ami_watermarks"]
            )
        )
    out["clientToken"] = value["client_token"]
    out["dryRun"] = value.get("dry_run", False)
    return out


def deserialize_json(data: dict) -> CreateImageRecipeRequest:
    out: CreateImageRecipeRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateImageRecipeRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("semanticVersion") is not None:
        out["semantic_version"] = data["semanticVersion"]
    else:
        raise DeserializationError("CreateImageRecipeRequest.semantic_version required")
    if data.get("components") is not None:
        import capo_imagebuilder.types.component_configuration_list

        out["components"] = (
            capo_imagebuilder.types.component_configuration_list.deserialize_json(
                data["components"]
            )
        )
    if data.get("parentImage") is not None:
        out["parent_image"] = data["parentImage"]
    else:
        raise DeserializationError("CreateImageRecipeRequest.parent_image required")
    if data.get("blockDeviceMappings") is not None:
        import capo_imagebuilder.types.instance_block_device_mappings

        out["block_device_mappings"] = (
            capo_imagebuilder.types.instance_block_device_mappings.deserialize_json(
                data["blockDeviceMappings"]
            )
        )
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if data.get("workingDirectory") is not None:
        out["working_directory"] = data["workingDirectory"]
    if data.get("additionalInstanceConfiguration") is not None:
        import capo_imagebuilder.types.additional_instance_configuration

        out["additional_instance_configuration"] = (
            capo_imagebuilder.types.additional_instance_configuration.deserialize_json(
                data["additionalInstanceConfiguration"]
            )
        )
    if data.get("amiTags") is not None:
        import capo_imagebuilder.types.tag_map

        out["ami_tags"] = capo_imagebuilder.types.tag_map.deserialize_json(
            data["amiTags"]
        )
    if data.get("amiWatermarks") is not None:
        import capo_imagebuilder.types.ami_watermarks_list

        out["ami_watermarks"] = (
            capo_imagebuilder.types.ami_watermarks_list.deserialize_json(
                data["amiWatermarks"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateImageRecipeRequest.client_token required")
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    else:
        out["dry_run"] = False
    return out

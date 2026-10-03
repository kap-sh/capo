"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateContainerRecipeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_imagebuilder.errors import DeserializationError

if TYPE_CHECKING:
    import capo_imagebuilder.types.boolean
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.component_configuration_list
    import capo_imagebuilder.types.container_type
    import capo_imagebuilder.types.inline_docker_file_template
    import capo_imagebuilder.types.instance_configuration
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.platform
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.target_container_repository
    import capo_imagebuilder.types.uri
    import capo_imagebuilder.types.wildcard_version_number


class CreateContainerRecipeRequest(TypedDict, closed=True):
    container_type: "capo_imagebuilder.types.container_type.ContainerType"
    """<p>The type of container to create.</p>"""
    name: "capo_imagebuilder.types.resource_name.ResourceName"
    """<p>The name of the container recipe. The recipe name, combined with the semantic version, must be unique to your account in each Amazon Web Services Region. Image Builder generates the container recipe ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the container recipe.</p>"""
    semantic_version: (
        "capo_imagebuilder.types.wildcard_version_number.WildcardVersionNumber"
    )
    """<p>The semantic version of the container recipe. This version follows the semantic version syntax.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> </note>"""
    components: NotRequired[
        "capo_imagebuilder.types.component_configuration_list.ComponentConfigurationList"
    ]
    """<p>The components included in the container recipe. You can specify each component only one time in a recipe.</p>"""
    instance_configuration: NotRequired[
        "capo_imagebuilder.types.instance_configuration.InstanceConfiguration"
    ]
    """<p>A group of options that can be used to configure an instance for building and testing container images.</p>"""
    dockerfile_template_data: NotRequired[
        "capo_imagebuilder.types.inline_docker_file_template.InlineDockerFileTemplate"
    ]
    """<p>The Dockerfile template used to build your image, as an inline data blob. You must specify exactly one of the <code>dockerfileTemplateData</code> or <code>dockerfileTemplateUri</code> properties. For the contextual variables that the template can include, see <a href="https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-container-recipes.html">Create a new version of a container recipe</a> in the <i>EC2 Image Builder User Guide</i>.</p>"""
    dockerfile_template_uri: NotRequired["capo_imagebuilder.types.uri.Uri"]
    """<p>The Amazon S3 URI for the Dockerfile template that is used to build your container image. You must have permission to read the object. Image Builder reads the object once, when it creates the recipe, and stores its content in the recipe. Later changes to the S3 object don't affect the recipe. You must specify exactly one of the <code>dockerfileTemplateData</code> or <code>dockerfileTemplateUri</code> properties.</p>"""
    platform_override: NotRequired["capo_imagebuilder.types.platform.Platform"]
    """<p>Specifies the operating system platform when you use a custom base image. Container recipes support only the Linux and Windows platforms.</p>"""
    image_os_version_override: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>Specifies the operating system version for the base image. Use this property only when the base image is a container image from a registry. When the base image is an Image Builder image, the operating system version comes from the parent image.</p>"""
    parent_image: "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    """<p>The base image for the container recipe. This can be an Image Builder image resource ARN or a container image URI from a registry, for example <code>amazonlinux:latest</code>.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags that are attached to the container recipe.</p>"""
    working_directory: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The working directory for use during build and test workflows.</p>"""
    target_repository: (
        "capo_imagebuilder.types.target_container_repository.TargetContainerRepository"
    )
    """<p>The destination repository for the container image. The Amazon ECR repository must already exist in the Amazon Web Services Region where the build runs.</p>"""
    kms_key_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies which KMS key is used to encrypt the Dockerfile template. This can be either the Key ARN or the Alias ARN. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    client_token: "capo_imagebuilder.types.client_token.ClientToken"
    """<p>A unique, case-sensitive identifier you provide to ensure that the operation runs no more than one time. If you retry a request with the same client token, Image Builder returns the original response without running the operation again. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    dry_run: "capo_imagebuilder.types.boolean.Boolean"
    """<p>Validates the required permissions and request parameters without performing the operation. If validation succeeds, the operation returns a <code>DryRunOperationException</code> error response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContainerRecipeRequest) -> dict:
    out: dict = {}
    import capo_imagebuilder.types.container_type

    out["containerType"] = capo_imagebuilder.types.container_type.serialize_json(
        value["container_type"]
    )
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
    if "instance_configuration" in value:
        import capo_imagebuilder.types.instance_configuration

        out["instanceConfiguration"] = (
            capo_imagebuilder.types.instance_configuration.serialize_json(
                value["instance_configuration"]
            )
        )
    if "dockerfile_template_data" in value:
        out["dockerfileTemplateData"] = value["dockerfile_template_data"]
    if "dockerfile_template_uri" in value:
        out["dockerfileTemplateUri"] = value["dockerfile_template_uri"]
    if "platform_override" in value:
        import capo_imagebuilder.types.platform

        out["platformOverride"] = capo_imagebuilder.types.platform.serialize_json(
            value["platform_override"]
        )
    if "image_os_version_override" in value:
        out["imageOsVersionOverride"] = value["image_os_version_override"]
    out["parentImage"] = value["parent_image"]
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "working_directory" in value:
        out["workingDirectory"] = value["working_directory"]
    import capo_imagebuilder.types.target_container_repository

    out["targetRepository"] = (
        capo_imagebuilder.types.target_container_repository.serialize_json(
            value["target_repository"]
        )
    )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    out["clientToken"] = value["client_token"]
    out["dryRun"] = value.get("dry_run", False)
    return out


def deserialize_json(data: dict) -> CreateContainerRecipeRequest:
    out: CreateContainerRecipeRequest = {}  # type: ignore[typeddict-item]
    if data.get("containerType") is not None:
        import capo_imagebuilder.types.container_type

        out["container_type"] = capo_imagebuilder.types.container_type.deserialize_json(
            data["containerType"]
        )
    else:
        raise DeserializationError(
            "CreateContainerRecipeRequest.container_type required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateContainerRecipeRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("semanticVersion") is not None:
        out["semantic_version"] = data["semanticVersion"]
    else:
        raise DeserializationError(
            "CreateContainerRecipeRequest.semantic_version required"
        )
    if data.get("components") is not None:
        import capo_imagebuilder.types.component_configuration_list

        out["components"] = (
            capo_imagebuilder.types.component_configuration_list.deserialize_json(
                data["components"]
            )
        )
    if data.get("instanceConfiguration") is not None:
        import capo_imagebuilder.types.instance_configuration

        out["instance_configuration"] = (
            capo_imagebuilder.types.instance_configuration.deserialize_json(
                data["instanceConfiguration"]
            )
        )
    if data.get("dockerfileTemplateData") is not None:
        out["dockerfile_template_data"] = data["dockerfileTemplateData"]
    if data.get("dockerfileTemplateUri") is not None:
        out["dockerfile_template_uri"] = data["dockerfileTemplateUri"]
    if data.get("platformOverride") is not None:
        import capo_imagebuilder.types.platform

        out["platform_override"] = capo_imagebuilder.types.platform.deserialize_json(
            data["platformOverride"]
        )
    if data.get("imageOsVersionOverride") is not None:
        out["image_os_version_override"] = data["imageOsVersionOverride"]
    if data.get("parentImage") is not None:
        out["parent_image"] = data["parentImage"]
    else:
        raise DeserializationError("CreateContainerRecipeRequest.parent_image required")
    if data.get("tags") is not None:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.deserialize_json(data["tags"])
    if data.get("workingDirectory") is not None:
        out["working_directory"] = data["workingDirectory"]
    if data.get("targetRepository") is not None:
        import capo_imagebuilder.types.target_container_repository

        out["target_repository"] = (
            capo_imagebuilder.types.target_container_repository.deserialize_json(
                data["targetRepository"]
            )
        )
    else:
        raise DeserializationError(
            "CreateContainerRecipeRequest.target_repository required"
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateContainerRecipeRequest.client_token required")
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    else:
        out["dry_run"] = False
    return out

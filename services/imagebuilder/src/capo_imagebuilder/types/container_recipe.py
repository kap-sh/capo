"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ContainerRecipe``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.component_configuration_list
    import capo_imagebuilder.types.container_type
    import capo_imagebuilder.types.date_time
    import capo_imagebuilder.types.docker_file_template
    import capo_imagebuilder.types.image_builder_arn
    import capo_imagebuilder.types.instance_configuration
    import capo_imagebuilder.types.non_empty_string
    import capo_imagebuilder.types.nullable_boolean
    import capo_imagebuilder.types.platform
    import capo_imagebuilder.types.resource_name
    import capo_imagebuilder.types.tag_map
    import capo_imagebuilder.types.target_container_repository
    import capo_imagebuilder.types.version_number


class ContainerRecipe(TypedDict, closed=True):
    arn: NotRequired["capo_imagebuilder.types.image_builder_arn.ImageBuilderArn"]
    """<p>The Amazon Resource Name (ARN) of the container recipe.</p> <note> <p>Semantic versioning is included in each object's Amazon Resource Name (ARN), at the level that applies to that object as follows:</p> <ol> <li> <p>Versionless ARNs and Name ARNs do not include specific values in any of the nodes. The nodes are either left off entirely, or they are specified as wildcards, for example: x.x.x.</p> </li> <li> <p>Version ARNs have only the first three nodes: <major>.<minor>.<patch></p> </li> <li> <p>Build version ARNs have all four nodes, and point to a specific build for a specific version of an object.</p> </li> </ol> </note>"""
    container_type: NotRequired["capo_imagebuilder.types.container_type.ContainerType"]
    """<p>Specifies the type of container, such as Docker.</p>"""
    name: NotRequired["capo_imagebuilder.types.resource_name.ResourceName"]
    """<p>The name of the container recipe.</p>"""
    description: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The description of the container recipe.</p>"""
    platform: NotRequired["capo_imagebuilder.types.platform.Platform"]
    """<p>The system platform for the container. Container recipes support only the Linux and Windows platforms.</p>"""
    owner: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The owner of the container recipe.</p>"""
    version: NotRequired["capo_imagebuilder.types.version_number.VersionNumber"]
    """<p>The semantic version of the container recipe.</p> <note> <p>The semantic version has four nodes: <major>.<minor>.<patch>/<build>. You can assign values for the first three, and can filter on all of them.</p> <p> <b>Assignment:</b> For the first three nodes, you can assign any positive integer value, including zero. The upper limit is 2^30-1, or 1073741823, for each node. Image Builder automatically assigns the build number to the fourth node.</p> <p> <b>Patterns:</b> You can use any numeric pattern that adheres to the assignment requirements for the nodes that you can assign. For example, you might choose a software version pattern, such as 1.0.0, or a date, such as 2021.01.01.</p> <p> <b>Filtering:</b> You can use wildcards (x) to specify the most recent versions or nodes when selecting the base image or components for your recipe. When you use a wildcard in any node, all nodes to the right of the first wildcard must also be wildcards.</p> </note>"""
    components: NotRequired[
        "capo_imagebuilder.types.component_configuration_list.ComponentConfigurationList"
    ]
    """<p>Build and test components that are included in the container recipe. A recipe can contain a maximum of 20 build and test components in any combination, by default. This maximum is an adjustable quota. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/imagebuilder.html">EC2 Image Builder endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    instance_configuration: NotRequired[
        "capo_imagebuilder.types.instance_configuration.InstanceConfiguration"
    ]
    """<p>A group of options that can be used to configure an instance for building and testing container images.</p>"""
    dockerfile_template_data: NotRequired[
        "capo_imagebuilder.types.docker_file_template.DockerFileTemplate"
    ]
    """<p>The Dockerfile template that Image Builder uses to build the container image. The template can include contextual variables that Image Builder replaces with build information at build time. For the contextual variables that the template can include, see <a href="https://docs.aws.amazon.com/imagebuilder/latest/userguide/create-container-recipes.html">Create a new version of a container recipe</a> in the <i>EC2 Image Builder User Guide</i>.</p>"""
    kms_key_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The KMS key that Image Builder uses to encrypt the recipe's Dockerfile template data at rest. This can be either the Key ARN or the Alias ARN. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN">Key identifiers (KeyId)</a> in the <i>Key Management Service Developer Guide</i>. If you don't specify a key, Image Builder encrypts the template data with a KMS key that Image Builder owns. This key isn't used to encrypt the output container image.</p>"""
    encrypted: NotRequired["capo_imagebuilder.types.nullable_boolean.NullableBoolean"]
    """<p>Specifies whether the recipe's Dockerfile template data is encrypted at rest. Image Builder encrypts all Dockerfile template data at rest, so this value is always <code>true</code>. This field is retained for backward compatibility, and doesn't describe encryption of the output container image.</p>"""
    parent_image: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The base image for customizations specified in the container recipe. This can contain an Image Builder image resource ARN or a container image URI, for example <code>amazonlinux:latest</code>.</p>"""
    date_created: NotRequired["capo_imagebuilder.types.date_time.DateTime"]
    """<p>The date when this container recipe was created.</p>"""
    tags: NotRequired["capo_imagebuilder.types.tag_map.TagMap"]
    """<p>Tags that are attached to the container recipe.</p>"""
    working_directory: NotRequired[
        "capo_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The working directory for use during build and test workflows.</p>"""
    target_repository: NotRequired[
        "capo_imagebuilder.types.target_container_repository.TargetContainerRepository"
    ]
    """<p>The destination repository for the container image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerRecipe) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "container_type" in value:
        import capo_imagebuilder.types.container_type

        out["containerType"] = capo_imagebuilder.types.container_type.serialize_json(
            value["container_type"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "platform" in value:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.serialize_json(
            value["platform"]
        )
    if "owner" in value:
        out["owner"] = value["owner"]
    if "version" in value:
        out["version"] = value["version"]
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
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "encrypted" in value:
        out["encrypted"] = value["encrypted"]
    if "parent_image" in value:
        out["parentImage"] = value["parent_image"]
    if "date_created" in value:
        out["dateCreated"] = value["date_created"]
    if "tags" in value:
        import capo_imagebuilder.types.tag_map

        out["tags"] = capo_imagebuilder.types.tag_map.serialize_json(value["tags"])
    if "working_directory" in value:
        out["workingDirectory"] = value["working_directory"]
    if "target_repository" in value:
        import capo_imagebuilder.types.target_container_repository

        out["targetRepository"] = (
            capo_imagebuilder.types.target_container_repository.serialize_json(
                value["target_repository"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContainerRecipe:
    out: ContainerRecipe = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("containerType") is not None:
        import capo_imagebuilder.types.container_type

        out["container_type"] = capo_imagebuilder.types.container_type.deserialize_json(
            data["containerType"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("platform") is not None:
        import capo_imagebuilder.types.platform

        out["platform"] = capo_imagebuilder.types.platform.deserialize_json(
            data["platform"]
        )
    if data.get("owner") is not None:
        out["owner"] = data["owner"]
    if data.get("version") is not None:
        out["version"] = data["version"]
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
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("encrypted") is not None:
        out["encrypted"] = data["encrypted"]
    if data.get("parentImage") is not None:
        out["parent_image"] = data["parentImage"]
    if data.get("dateCreated") is not None:
        out["date_created"] = data["dateCreated"]
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
    return out

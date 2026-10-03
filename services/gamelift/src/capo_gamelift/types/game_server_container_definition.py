"""Generated from Smithy shape ``com.amazonaws.gamelift#GameServerContainerDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_dependency_list
    import capo_gamelift.types.container_environment_list
    import capo_gamelift.types.container_mount_point_list
    import capo_gamelift.types.container_port_configuration
    import capo_gamelift.types.image_uri_string
    import capo_gamelift.types.linux_capabilities
    import capo_gamelift.types.non_zero_and128_max_ascii_string
    import capo_gamelift.types.server_sdk_version
    import capo_gamelift.types.sha256


class GameServerContainerDefinition(TypedDict, closed=True):
    container_name: NotRequired[
        "capo_gamelift.types.non_zero_and128_max_ascii_string.NonZeroAnd128MaxAsciiString"
    ]
    """<p>The container definition identifier. Container names are unique within a container group definition.</p>"""
    depends_on: NotRequired[
        "capo_gamelift.types.container_dependency_list.ContainerDependencyList"
    ]
    """<p>Indicates that the container relies on the status of other containers in the same container group during startup and shutdown sequences. A container might have dependencies on multiple containers.</p>"""
    mount_points: NotRequired[
        "capo_gamelift.types.container_mount_point_list.ContainerMountPointList"
    ]
    """<p>A mount point that binds a path inside the container to a file or directory on the host system and lets it access the file or directory.</p>"""
    environment_override: NotRequired[
        "capo_gamelift.types.container_environment_list.ContainerEnvironmentList"
    ]
    """<p>A set of environment variables that's passed to the container on startup. See the <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment">ContainerDefinition::environment</a> parameter in the <i>Amazon Elastic Container Service API Reference</i>.</p>"""
    image_uri: NotRequired["capo_gamelift.types.image_uri_string.ImageUriString"]
    """<p>The URI to the image that Amazon GameLift Servers uses when deploying this container to a container fleet. For a more specific identifier, see <code>ResolvedImageDigest</code>. </p>"""
    port_configuration: NotRequired[
        "capo_gamelift.types.container_port_configuration.ContainerPortConfiguration"
    ]
    """<p>The set of ports that are available to bind to processes in the container. For example, a game server process requires a container port to allow game clients to connect to it. Container ports aren't directly accessed by inbound traffic. Amazon GameLift Servers maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleet's <code>ConnectionPortRange</code>. </p>"""
    resolved_image_digest: NotRequired["capo_gamelift.types.sha256.Sha256"]
    """<p>A unique and immutable identifier for the container image. The digest is a SHA 256 hash of the container image manifest. </p>"""
    server_sdk_version: NotRequired[
        "capo_gamelift.types.server_sdk_version.ServerSdkVersion"
    ]
    """<p>The Amazon GameLift Servers server SDK version that the game server is integrated with. Only game servers using 5.2.0 or higher are compatible with container fleets.</p>"""
    linux_capabilities: NotRequired[
        "capo_gamelift.types.linux_capabilities.LinuxCapabilities"
    ]
    """<p>Linux-specific modifications that are applied to the default Docker container configuration, such as Linux capabilities. For more information see <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_LinuxCapabilities.html">LinuxCapabilities</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameServerContainerDefinition) -> dict:
    out: dict = {}
    if "container_name" in value:
        out["ContainerName"] = value["container_name"]
    if "depends_on" in value:
        import capo_gamelift.types.container_dependency_list

        out["DependsOn"] = (
            capo_gamelift.types.container_dependency_list.serialize_aws_json_1_1(
                value["depends_on"]
            )
        )
    if "mount_points" in value:
        import capo_gamelift.types.container_mount_point_list

        out["MountPoints"] = (
            capo_gamelift.types.container_mount_point_list.serialize_aws_json_1_1(
                value["mount_points"]
            )
        )
    if "environment_override" in value:
        import capo_gamelift.types.container_environment_list

        out["EnvironmentOverride"] = (
            capo_gamelift.types.container_environment_list.serialize_aws_json_1_1(
                value["environment_override"]
            )
        )
    if "image_uri" in value:
        out["ImageUri"] = value["image_uri"]
    if "port_configuration" in value:
        import capo_gamelift.types.container_port_configuration

        out["PortConfiguration"] = (
            capo_gamelift.types.container_port_configuration.serialize_aws_json_1_1(
                value["port_configuration"]
            )
        )
    if "resolved_image_digest" in value:
        out["ResolvedImageDigest"] = value["resolved_image_digest"]
    if "server_sdk_version" in value:
        out["ServerSdkVersion"] = value["server_sdk_version"]
    if "linux_capabilities" in value:
        import capo_gamelift.types.linux_capabilities

        out["LinuxCapabilities"] = (
            capo_gamelift.types.linux_capabilities.serialize_aws_json_1_1(
                value["linux_capabilities"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GameServerContainerDefinition:
    out: GameServerContainerDefinition = {}  # type: ignore[typeddict-item]
    if data.get("ContainerName") is not None:
        out["container_name"] = data["ContainerName"]
    if data.get("DependsOn") is not None:
        import capo_gamelift.types.container_dependency_list

        out["depends_on"] = (
            capo_gamelift.types.container_dependency_list.deserialize_aws_json_1_1(
                data["DependsOn"]
            )
        )
    if data.get("MountPoints") is not None:
        import capo_gamelift.types.container_mount_point_list

        out["mount_points"] = (
            capo_gamelift.types.container_mount_point_list.deserialize_aws_json_1_1(
                data["MountPoints"]
            )
        )
    if data.get("EnvironmentOverride") is not None:
        import capo_gamelift.types.container_environment_list

        out["environment_override"] = (
            capo_gamelift.types.container_environment_list.deserialize_aws_json_1_1(
                data["EnvironmentOverride"]
            )
        )
    if data.get("ImageUri") is not None:
        out["image_uri"] = data["ImageUri"]
    if data.get("PortConfiguration") is not None:
        import capo_gamelift.types.container_port_configuration

        out["port_configuration"] = (
            capo_gamelift.types.container_port_configuration.deserialize_aws_json_1_1(
                data["PortConfiguration"]
            )
        )
    if data.get("ResolvedImageDigest") is not None:
        out["resolved_image_digest"] = data["ResolvedImageDigest"]
    if data.get("ServerSdkVersion") is not None:
        out["server_sdk_version"] = data["ServerSdkVersion"]
    if data.get("LinuxCapabilities") is not None:
        import capo_gamelift.types.linux_capabilities

        out["linux_capabilities"] = (
            capo_gamelift.types.linux_capabilities.deserialize_aws_json_1_1(
                data["LinuxCapabilities"]
            )
        )
    return out

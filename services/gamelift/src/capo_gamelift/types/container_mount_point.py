"""Generated from Smithy shape ``com.amazonaws.gamelift#ContainerMountPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.container_mount_point_access_level
    import capo_gamelift.types.container_path_string
    import capo_gamelift.types.instance_path_string


class ContainerMountPoint(TypedDict, closed=True):
    instance_path: NotRequired[
        "capo_gamelift.types.instance_path_string.InstancePathString"
    ]
    """<p>The path to the source file or directory. </p>"""
    container_path: NotRequired[
        "capo_gamelift.types.container_path_string.ContainerPathString"
    ]
    """<p>The mount path on the container. If this property isn't set, the instance path is used.</p>"""
    access_level: NotRequired[
        "capo_gamelift.types.container_mount_point_access_level.ContainerMountPointAccessLevel"
    ]
    """<p>The type of access for the container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContainerMountPoint) -> dict:
    out: dict = {}
    if "instance_path" in value:
        out["InstancePath"] = value["instance_path"]
    if "container_path" in value:
        out["ContainerPath"] = value["container_path"]
    if "access_level" in value:
        import capo_gamelift.types.container_mount_point_access_level

        out["AccessLevel"] = (
            capo_gamelift.types.container_mount_point_access_level.serialize_aws_json_1_1(
                value["access_level"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContainerMountPoint:
    out: ContainerMountPoint = {}  # type: ignore[typeddict-item]
    if data.get("InstancePath") is not None:
        out["instance_path"] = data["InstancePath"]
    if data.get("ContainerPath") is not None:
        out["container_path"] = data["ContainerPath"]
    if data.get("AccessLevel") is not None:
        import capo_gamelift.types.container_mount_point_access_level

        out["access_level"] = (
            capo_gamelift.types.container_mount_point_access_level.deserialize_aws_json_1_1(
                data["AccessLevel"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ContainerMountPoint) -> dict:
    out: dict = {}
    if "instance_path" in value:
        out["InstancePath"] = value["instance_path"]
    if "container_path" in value:
        out["ContainerPath"] = value["container_path"]
    if "access_level" in value:
        import capo_gamelift.types.container_mount_point_access_level

        out["AccessLevel"] = (
            capo_gamelift.types.container_mount_point_access_level.serialize_cbor(
                value["access_level"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ContainerMountPoint:
    out: ContainerMountPoint = {}  # type: ignore[typeddict-item]
    if data.get("InstancePath") is not None:
        out["instance_path"] = data["InstancePath"]
    if data.get("ContainerPath") is not None:
        out["container_path"] = data["ContainerPath"]
    if data.get("AccessLevel") is not None:
        import capo_gamelift.types.container_mount_point_access_level

        out["access_level"] = (
            capo_gamelift.types.container_mount_point_access_level.deserialize_cbor(
                data["AccessLevel"]
            )
        )
    return out

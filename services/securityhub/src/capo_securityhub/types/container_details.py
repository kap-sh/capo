"""Generated from Smithy shape ``com.amazonaws.securityhub#ContainerDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.volume_mount_list


class ContainerDetails(TypedDict, closed=True):
    container_runtime: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The runtime of the container. </p>"""
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the container related to a finding.</p>"""
    image_id: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the container image related to a finding.</p>"""
    image_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the container image related to a finding.</p>"""
    launched_at: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates when the container started.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    volume_mounts: NotRequired[
        "capo_securityhub.types.volume_mount_list.VolumeMountList"
    ]
    """<p>Provides information about the mounting of a volume in a container. </p>"""
    privileged: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>When this parameter is <code>true</code>, the container is given elevated privileges on the host container instance (similar to the root user). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerDetails) -> dict:
    out: dict = {}
    if "container_runtime" in value:
        out["ContainerRuntime"] = value["container_runtime"]
    if "name" in value:
        out["Name"] = value["name"]
    if "image_id" in value:
        out["ImageId"] = value["image_id"]
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    if "launched_at" in value:
        out["LaunchedAt"] = value["launched_at"]
    if "volume_mounts" in value:
        import capo_securityhub.types.volume_mount_list

        out["VolumeMounts"] = capo_securityhub.types.volume_mount_list.serialize_json(
            value["volume_mounts"]
        )
    if "privileged" in value:
        out["Privileged"] = value["privileged"]
    return out


def deserialize_json(data: dict) -> ContainerDetails:
    out: ContainerDetails = {}  # type: ignore[typeddict-item]
    if data.get("ContainerRuntime") is not None:
        out["container_runtime"] = data["ContainerRuntime"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("ImageId") is not None:
        out["image_id"] = data["ImageId"]
    if data.get("ImageName") is not None:
        out["image_name"] = data["ImageName"]
    if data.get("LaunchedAt") is not None:
        out["launched_at"] = data["LaunchedAt"]
    if data.get("VolumeMounts") is not None:
        import capo_securityhub.types.volume_mount_list

        out["volume_mounts"] = (
            capo_securityhub.types.volume_mount_list.deserialize_json(
                data["VolumeMounts"]
            )
        )
    if data.get("Privileged") is not None:
        out["privileged"] = data["Privileged"]
    return out

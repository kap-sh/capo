"""Generated from Smithy shape ``com.amazonaws.mgn#GetLaunchConfigurationDefaultsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.positive_integer
    import capo_mgn.types.source_server_id
    import capo_mgn.types.source_server_volume_configuration


class GetLaunchConfigurationDefaultsResponse(TypedDict, closed=True):
    source_server_id: NotRequired["capo_mgn.types.source_server_id.SourceServerID"]
    """<p>Source Server ID of the launch configuration defaults.</p>"""
    small_volume_max_size: "capo_mgn.types.positive_integer.PositiveInteger"
    """<p>Disks up to this size, in GiB, use the small volume configuration, and larger disks use the large one. <code>0</code> means every disk uses the large one.</p>"""
    small_volume_configuration: NotRequired[
        "capo_mgn.types.source_server_volume_configuration.SourceServerVolumeConfiguration"
    ]
    """<p>Volume configuration for disks up to <code>smallVolumeMaxSize</code>. Omitted when none of its fields is set.</p>"""
    large_volume_configuration: NotRequired[
        "capo_mgn.types.source_server_volume_configuration.SourceServerVolumeConfiguration"
    ]
    """<p>Volume configuration for disks larger than <code>smallVolumeMaxSize</code>. Omitted when none of its fields is set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLaunchConfigurationDefaultsResponse) -> dict:
    out: dict = {}
    if "source_server_id" in value:
        out["sourceServerID"] = value["source_server_id"]
    out["smallVolumeMaxSize"] = value.get("small_volume_max_size", 0)
    if "small_volume_configuration" in value:
        import capo_mgn.types.source_server_volume_configuration

        out["smallVolumeConfiguration"] = (
            capo_mgn.types.source_server_volume_configuration.serialize_json(
                value["small_volume_configuration"]
            )
        )
    if "large_volume_configuration" in value:
        import capo_mgn.types.source_server_volume_configuration

        out["largeVolumeConfiguration"] = (
            capo_mgn.types.source_server_volume_configuration.serialize_json(
                value["large_volume_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetLaunchConfigurationDefaultsResponse:
    out: GetLaunchConfigurationDefaultsResponse = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    if data.get("smallVolumeMaxSize") is not None:
        out["small_volume_max_size"] = data["smallVolumeMaxSize"]
    else:
        out["small_volume_max_size"] = 0
    if data.get("smallVolumeConfiguration") is not None:
        import capo_mgn.types.source_server_volume_configuration

        out["small_volume_configuration"] = (
            capo_mgn.types.source_server_volume_configuration.deserialize_json(
                data["smallVolumeConfiguration"]
            )
        )
    if data.get("largeVolumeConfiguration") is not None:
        import capo_mgn.types.source_server_volume_configuration

        out["large_volume_configuration"] = (
            capo_mgn.types.source_server_volume_configuration.deserialize_json(
                data["largeVolumeConfiguration"]
            )
        )
    return out

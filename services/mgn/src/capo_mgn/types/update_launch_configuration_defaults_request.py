"""Generated from Smithy shape ``com.amazonaws.mgn#UpdateLaunchConfigurationDefaultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.positive_integer
    import capo_mgn.types.source_server_id
    import capo_mgn.types.source_server_volume_configuration


class UpdateLaunchConfigurationDefaultsRequest(TypedDict, closed=True):
    source_server_id: "capo_mgn.types.source_server_id.SourceServerID"
    """<p>Request to update the launch configuration defaults by Source Server ID.</p>"""
    account_id: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>Request to update the launch configuration defaults by Account ID.</p>"""
    small_volume_max_size: NotRequired[
        "capo_mgn.types.positive_integer.PositiveInteger"
    ]
    """<p>Disks up to this size, in GiB, use the small volume configuration, and larger disks use the large one. <code>0</code> means every disk uses the large one. If you omit it, the current value is kept.</p>"""
    small_volume_configuration: NotRequired[
        "capo_mgn.types.source_server_volume_configuration.SourceServerVolumeConfiguration"
    ]
    """<p>Volume configuration for disks up to <code>smallVolumeMaxSize</code>. If you omit it, the current one is kept. If you send it, it replaces the current one: fields you omit are cleared, and an empty configuration, <code>{}</code>, clears all of them.</p>"""
    large_volume_configuration: NotRequired[
        "capo_mgn.types.source_server_volume_configuration.SourceServerVolumeConfiguration"
    ]
    """<p>Volume configuration for disks larger than <code>smallVolumeMaxSize</code>. If you omit it, the current one is kept. If you send it, it replaces the current one: fields you omit are cleared, and an empty configuration, <code>{}</code>, clears all of them.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateLaunchConfigurationDefaultsRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    if "small_volume_max_size" in value:
        out["smallVolumeMaxSize"] = value["small_volume_max_size"]
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


def deserialize_json(data: dict) -> UpdateLaunchConfigurationDefaultsRequest:
    out: UpdateLaunchConfigurationDefaultsRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    else:
        out["source_server_id"] = ""
    if data.get("accountID") is not None:
        out["account_id"] = data["accountID"]
    if data.get("smallVolumeMaxSize") is not None:
        out["small_volume_max_size"] = data["smallVolumeMaxSize"]
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

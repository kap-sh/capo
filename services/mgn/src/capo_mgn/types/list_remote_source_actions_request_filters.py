"""Generated from Smithy shape ``com.amazonaws.mgn#ListRemoteSourceActionsRequestFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.remote_source_action_i_ds_filter


class ListRemoteSourceActionsRequestFilters(TypedDict, closed=True):
    remote_source_action_i_ds: NotRequired[
        "capo_mgn.types.remote_source_action_i_ds_filter.RemoteSourceActionIDsFilter"
    ]
    """<p>A list of source action IDs to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRemoteSourceActionsRequestFilters) -> dict:
    out: dict = {}
    if "remote_source_action_i_ds" in value:
        import capo_mgn.types.remote_source_action_i_ds_filter

        out["remoteSourceActionIDs"] = (
            capo_mgn.types.remote_source_action_i_ds_filter.serialize_json(
                value["remote_source_action_i_ds"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRemoteSourceActionsRequestFilters:
    out: ListRemoteSourceActionsRequestFilters = {}  # type: ignore[typeddict-item]
    if data.get("remoteSourceActionIDs") is not None:
        import capo_mgn.types.remote_source_action_i_ds_filter

        out["remote_source_action_i_ds"] = (
            capo_mgn.types.remote_source_action_i_ds_filter.deserialize_json(
                data["remoteSourceActionIDs"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.mgn#ListRemoteSourceActionJobsRequestFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.remote_source_action_job_i_ds_filter


class ListRemoteSourceActionJobsRequestFilters(TypedDict, closed=True):
    remote_source_action_job_i_ds: NotRequired[
        "capo_mgn.types.remote_source_action_job_i_ds_filter.RemoteSourceActionJobIDsFilter"
    ]
    """<p>A list of job IDs to filter by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRemoteSourceActionJobsRequestFilters) -> dict:
    out: dict = {}
    if "remote_source_action_job_i_ds" in value:
        import capo_mgn.types.remote_source_action_job_i_ds_filter

        out["remoteSourceActionJobIDs"] = (
            capo_mgn.types.remote_source_action_job_i_ds_filter.serialize_json(
                value["remote_source_action_job_i_ds"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListRemoteSourceActionJobsRequestFilters:
    out: ListRemoteSourceActionJobsRequestFilters = {}  # type: ignore[typeddict-item]
    if data.get("remoteSourceActionJobIDs") is not None:
        import capo_mgn.types.remote_source_action_job_i_ds_filter

        out["remote_source_action_job_i_ds"] = (
            capo_mgn.types.remote_source_action_job_i_ds_filter.deserialize_json(
                data["remoteSourceActionJobIDs"]
            )
        )
    return out

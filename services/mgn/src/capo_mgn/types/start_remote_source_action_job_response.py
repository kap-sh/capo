"""Generated from Smithy shape ``com.amazonaws.mgn#StartRemoteSourceActionJobResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.remote_source_action_job


class StartRemoteSourceActionJobResponse(TypedDict, closed=True):
    remote_source_action_job: NotRequired[
        "capo_mgn.types.remote_source_action_job.RemoteSourceActionJob"
    ]
    """<p>The job that was started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartRemoteSourceActionJobResponse) -> dict:
    out: dict = {}
    if "remote_source_action_job" in value:
        import capo_mgn.types.remote_source_action_job

        out["remoteSourceActionJob"] = (
            capo_mgn.types.remote_source_action_job.serialize_json(
                value["remote_source_action_job"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartRemoteSourceActionJobResponse:
    out: StartRemoteSourceActionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("remoteSourceActionJob") is not None:
        import capo_mgn.types.remote_source_action_job

        out["remote_source_action_job"] = (
            capo_mgn.types.remote_source_action_job.deserialize_json(
                data["remoteSourceActionJob"]
            )
        )
    return out


def redact_sensitive(value: StartRemoteSourceActionJobResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "remote_source_action_job" in value:
        import capo_mgn.types.remote_source_action_job

        out["remote_source_action_job"] = (
            capo_mgn.types.remote_source_action_job.redact_sensitive(
                value["remote_source_action_job"]
            )
        )
    return out

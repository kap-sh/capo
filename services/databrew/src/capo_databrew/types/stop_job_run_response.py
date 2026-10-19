"""Generated from Smithy shape ``com.amazonaws.databrew#StopJobRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.job_run_id


class StopJobRunResponse(TypedDict, closed=True):
    run_id: "capo_databrew.types.job_run_id.JobRunId"
    """<p>The ID of the job run that you stopped.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopJobRunResponse) -> dict:
    out: dict = {}
    out["RunId"] = value["run_id"]
    return out


def deserialize_json(data: dict) -> StopJobRunResponse:
    out: StopJobRunResponse = {}  # type: ignore[typeddict-item]
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    else:
        out["run_id"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.databrew#StartJobRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.job_run_id


class StartJobRunResponse(TypedDict, closed=True):
    run_id: "capo_databrew.types.job_run_id.JobRunId"
    """<p>A system-generated identifier for this particular job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartJobRunResponse) -> dict:
    out: dict = {}
    out["RunId"] = value["run_id"]
    return out


def deserialize_json(data: dict) -> StartJobRunResponse:
    out: StartJobRunResponse = {}  # type: ignore[typeddict-item]
    if data.get("RunId") is not None:
        out["run_id"] = data["RunId"]
    else:
        out["run_id"] = ""
    return out

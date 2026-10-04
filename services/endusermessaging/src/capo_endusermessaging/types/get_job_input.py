"""Generated from Smithy shape ``com.amazonaws.endusermessaging#GetJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_endusermessaging.types.job_id


class GetJobInput(TypedDict, closed=True):
    job_id: "capo_endusermessaging.types.job_id.JobId"
    """<p>The unique identifier of the asynchronous job. Use the GetJob operation to check the status of the job and to retrieve its results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetJobInput:
    out: GetJobInput = {}  # type: ignore[typeddict-item]
    return out

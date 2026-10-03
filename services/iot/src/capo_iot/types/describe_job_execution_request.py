"""Generated from Smithy shape ``com.amazonaws.iot#DescribeJobExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.execution_number
    import capo_iot.types.job_id
    import capo_iot.types.thing_name


class DescribeJobExecutionRequest(TypedDict, closed=True):
    job_id: "capo_iot.types.job_id.JobId"
    """<p>The unique identifier you assigned to this job when it was created.</p>"""
    thing_name: "capo_iot.types.thing_name.ThingName"
    """<p>The name of the thing on which the job execution is running.</p>"""
    execution_number: NotRequired["capo_iot.types.execution_number.ExecutionNumber"]
    """<p>A string (consisting of the digits "0" through "9" which is used to specify a particular job execution on a particular device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeJobExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeJobExecutionRequest:
    out: DescribeJobExecutionRequest = {}  # type: ignore[typeddict-item]
    return out

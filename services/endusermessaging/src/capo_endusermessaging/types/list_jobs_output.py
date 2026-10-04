"""Generated from Smithy shape ``com.amazonaws.endusermessaging#ListJobsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.job_summary_list
    import capo_endusermessaging.types.next_token


class ListJobsOutput(TypedDict, closed=True):
    jobs: "capo_endusermessaging.types.job_summary_list.JobSummaryList"
    """<p>The list of asynchronous jobs.</p>"""
    next_token: NotRequired["capo_endusermessaging.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsOutput) -> dict:
    out: dict = {}
    import capo_endusermessaging.types.job_summary_list

    out["jobs"] = capo_endusermessaging.types.job_summary_list.serialize_json(
        value["jobs"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobsOutput:
    out: ListJobsOutput = {}  # type: ignore[typeddict-item]
    if data.get("jobs") is not None:
        import capo_endusermessaging.types.job_summary_list

        out["jobs"] = capo_endusermessaging.types.job_summary_list.deserialize_json(
            data["jobs"]
        )
    else:
        raise DeserializationError("ListJobsOutput.jobs required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

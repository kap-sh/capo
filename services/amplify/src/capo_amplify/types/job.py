"""Generated from Smithy shape ``com.amazonaws.amplify#Job``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.job_summary
    import capo_amplify.types.steps


class Job(TypedDict, closed=True):
    summary: "capo_amplify.types.job_summary.JobSummary"
    """<p> Describes the summary for an execution job for an Amplify app. </p>"""
    steps: "capo_amplify.types.steps.Steps"
    """<p> The execution steps for an execution job, for an Amplify app. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Job) -> dict:
    out: dict = {}
    import capo_amplify.types.job_summary

    out["summary"] = capo_amplify.types.job_summary.serialize_json(value["summary"])
    import capo_amplify.types.steps

    out["steps"] = capo_amplify.types.steps.serialize_json(value["steps"])
    return out


def deserialize_json(data: dict) -> Job:
    out: Job = {}  # type: ignore[typeddict-item]
    if data.get("summary") is not None:
        import capo_amplify.types.job_summary

        out["summary"] = capo_amplify.types.job_summary.deserialize_json(
            data["summary"]
        )
    else:
        raise DeserializationError("Job.summary required")
    if data.get("steps") is not None:
        import capo_amplify.types.steps

        out["steps"] = capo_amplify.types.steps.deserialize_json(data["steps"])
    else:
        out["steps"] = []
    return out

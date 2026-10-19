"""Generated from Smithy shape ``com.amazonaws.deadline#ListJobParameterDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.job_parameter_definitions
    import capo_deadline.types.next_token


class ListJobParameterDefinitionsResponse(TypedDict, closed=True):
    job_parameter_definitions: (
        "capo_deadline.types.job_parameter_definitions.JobParameterDefinitions"
    )
    """<p>Lists parameter definitions of a job.</p>"""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """<p>If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobParameterDefinitionsResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.job_parameter_definitions

    out["jobParameterDefinitions"] = (
        capo_deadline.types.job_parameter_definitions.serialize_json(
            value["job_parameter_definitions"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobParameterDefinitionsResponse:
    out: ListJobParameterDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobParameterDefinitions") is not None:
        import capo_deadline.types.job_parameter_definitions

        out["job_parameter_definitions"] = (
            capo_deadline.types.job_parameter_definitions.deserialize_json(
                data["jobParameterDefinitions"]
            )
        )
    else:
        out["job_parameter_definitions"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

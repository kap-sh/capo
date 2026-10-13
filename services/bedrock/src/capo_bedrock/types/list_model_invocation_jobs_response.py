"""Generated from Smithy shape ``com.amazonaws.bedrock#ListModelInvocationJobsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.model_invocation_job_summaries
    import capo_bedrock.types.pagination_token


class ListModelInvocationJobsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>If there are more results than can fit in the response, a <code>nextToken</code> is returned. Use the <code>nextToken</code> in a request to return the next batch of results.</p>"""
    invocation_job_summaries: NotRequired[
        "capo_bedrock.types.model_invocation_job_summaries.ModelInvocationJobSummaries"
    ]
    """<p>A list of items, each of which contains a summary about a batch inference job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListModelInvocationJobsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "invocation_job_summaries" in value:
        import capo_bedrock.types.model_invocation_job_summaries

        out["invocationJobSummaries"] = (
            capo_bedrock.types.model_invocation_job_summaries.serialize_json(
                value["invocation_job_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListModelInvocationJobsResponse:
    out: ListModelInvocationJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("invocationJobSummaries") is not None:
        import capo_bedrock.types.model_invocation_job_summaries

        out["invocation_job_summaries"] = (
            capo_bedrock.types.model_invocation_job_summaries.deserialize_json(
                data["invocationJobSummaries"]
            )
        )
    return out


def redact_sensitive(value: ListModelInvocationJobsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "invocation_job_summaries" in value:
        import capo_bedrock.types.model_invocation_job_summaries

        out["invocation_job_summaries"] = (
            capo_bedrock.types.model_invocation_job_summaries.redact_sensitive(
                value["invocation_job_summaries"]
            )
        )
    return out

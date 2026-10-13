"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ListAsyncInvokesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.async_invoke_summaries
    import capo_bedrock_runtime.types.pagination_token


class ListAsyncInvokesResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_bedrock_runtime.types.pagination_token.PaginationToken"
    ]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    async_invoke_summaries: NotRequired[
        "capo_bedrock_runtime.types.async_invoke_summaries.AsyncInvokeSummaries"
    ]
    """<p>A list of invocation summaries.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAsyncInvokesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "async_invoke_summaries" in value:
        import capo_bedrock_runtime.types.async_invoke_summaries

        out["asyncInvokeSummaries"] = (
            capo_bedrock_runtime.types.async_invoke_summaries.serialize_json(
                value["async_invoke_summaries"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListAsyncInvokesResponse:
    out: ListAsyncInvokesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("asyncInvokeSummaries") is not None:
        import capo_bedrock_runtime.types.async_invoke_summaries

        out["async_invoke_summaries"] = (
            capo_bedrock_runtime.types.async_invoke_summaries.deserialize_json(
                data["asyncInvokeSummaries"]
            )
        )
    return out


def redact_sensitive(value: ListAsyncInvokesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "async_invoke_summaries" in value:
        import capo_bedrock_runtime.types.async_invoke_summaries

        out["async_invoke_summaries"] = (
            capo_bedrock_runtime.types.async_invoke_summaries.redact_sensitive(
                value["async_invoke_summaries"]
            )
        )
    return out

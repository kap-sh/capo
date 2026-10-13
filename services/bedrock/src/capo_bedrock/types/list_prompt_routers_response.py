"""Generated from Smithy shape ``com.amazonaws.bedrock#ListPromptRoutersResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.prompt_router_summaries


class ListPromptRoutersResponse(TypedDict, closed=True):
    prompt_router_summaries: NotRequired[
        "capo_bedrock.types.prompt_router_summaries.PromptRouterSummaries"
    ]
    """<p>A list of prompt router summaries.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPromptRoutersResponse) -> dict:
    out: dict = {}
    if "prompt_router_summaries" in value:
        import capo_bedrock.types.prompt_router_summaries

        out["promptRouterSummaries"] = (
            capo_bedrock.types.prompt_router_summaries.serialize_json(
                value["prompt_router_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPromptRoutersResponse:
    out: ListPromptRoutersResponse = {}  # type: ignore[typeddict-item]
    if data.get("promptRouterSummaries") is not None:
        import capo_bedrock.types.prompt_router_summaries

        out["prompt_router_summaries"] = (
            capo_bedrock.types.prompt_router_summaries.deserialize_json(
                data["promptRouterSummaries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListPromptRoutersResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "prompt_router_summaries" in value:
        import capo_bedrock.types.prompt_router_summaries

        out["prompt_router_summaries"] = (
            capo_bedrock.types.prompt_router_summaries.redact_sensitive(
                value["prompt_router_summaries"]
            )
        )
    return out

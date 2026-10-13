"""Generated from Smithy shape ``com.amazonaws.bedrock#ListInferenceProfilesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.inference_profile_summaries
    import capo_bedrock.types.pagination_token


class ListInferenceProfilesResponse(TypedDict, closed=True):
    inference_profile_summaries: NotRequired[
        "capo_bedrock.types.inference_profile_summaries.InferenceProfileSummaries"
    ]
    """<p>A list of information about each inference profile that you can use.</p>"""
    next_token: NotRequired["capo_bedrock.types.pagination_token.PaginationToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInferenceProfilesResponse) -> dict:
    out: dict = {}
    if "inference_profile_summaries" in value:
        import capo_bedrock.types.inference_profile_summaries

        out["inferenceProfileSummaries"] = (
            capo_bedrock.types.inference_profile_summaries.serialize_json(
                value["inference_profile_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInferenceProfilesResponse:
    out: ListInferenceProfilesResponse = {}  # type: ignore[typeddict-item]
    if data.get("inferenceProfileSummaries") is not None:
        import capo_bedrock.types.inference_profile_summaries

        out["inference_profile_summaries"] = (
            capo_bedrock.types.inference_profile_summaries.deserialize_json(
                data["inferenceProfileSummaries"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListInferenceProfilesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inference_profile_summaries" in value:
        import capo_bedrock.types.inference_profile_summaries

        out["inference_profile_summaries"] = (
            capo_bedrock.types.inference_profile_summaries.redact_sensitive(
                value["inference_profile_summaries"]
            )
        )
    return out

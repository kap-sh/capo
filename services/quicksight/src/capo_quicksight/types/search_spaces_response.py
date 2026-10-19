"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchSpacesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.next_token
    import capo_quicksight.types.public_space_arn
    import capo_quicksight.types.public_space_id
    import capo_quicksight.types.space_summaries


class SearchSpacesResponse(TypedDict, closed=True):
    space_id: "capo_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space.</p>"""
    space_arn: NotRequired["capo_quicksight.types.public_space_arn.PublicSpaceArn"]
    """<p>The ARN of the space.</p>"""
    space_summaries: "capo_quicksight.types.space_summaries.SpaceSummaries"
    """<p>A list of space summaries that match the search criteria.</p>"""
    next_token: NotRequired["capo_quicksight.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSpacesResponse) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "space_arn" in value:
        out["spaceArn"] = value["space_arn"]
    import capo_quicksight.types.space_summaries

    out["SpaceSummaries"] = capo_quicksight.types.space_summaries.serialize_json(
        value["space_summaries"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> SearchSpacesResponse:
    out: SearchSpacesResponse = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("spaceArn") is not None:
        out["space_arn"] = data["spaceArn"]
    if data.get("SpaceSummaries") is not None:
        import capo_quicksight.types.space_summaries

        out["space_summaries"] = capo_quicksight.types.space_summaries.deserialize_json(
            data["SpaceSummaries"]
        )
    else:
        out["space_summaries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(value: SearchSpacesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "space_summaries" in value:
        import capo_quicksight.types.space_summaries

        out["space_summaries"] = capo_quicksight.types.space_summaries.redact_sensitive(
            value["space_summaries"]
        )
    return out

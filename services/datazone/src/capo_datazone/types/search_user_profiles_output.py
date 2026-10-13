"""Generated from Smithy shape ``com.amazonaws.datazone#SearchUserProfilesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.pagination_token
    import capo_datazone.types.user_profile_summaries


class SearchUserProfilesOutput(TypedDict, closed=True):
    items: NotRequired[
        "capo_datazone.types.user_profile_summaries.UserProfileSummaries"
    ]
    """<p>The results of the <code>SearchUserProfiles</code> action.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of results is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of results, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>SearchUserProfiles</code> to list the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchUserProfilesOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_datazone.types.user_profile_summaries

        out["items"] = capo_datazone.types.user_profile_summaries.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchUserProfilesOutput:
    out: SearchUserProfilesOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_datazone.types.user_profile_summaries

        out["items"] = capo_datazone.types.user_profile_summaries.deserialize_json(
            data["items"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: SearchUserProfilesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_datazone.types.user_profile_summaries

        out["items"] = capo_datazone.types.user_profile_summaries.redact_sensitive(
            value["items"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.deadline#ListStorageProfilesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.next_token
    import capo_deadline.types.storage_profile_summaries


class ListStorageProfilesResponse(TypedDict, closed=True):
    storage_profiles: (
        "capo_deadline.types.storage_profile_summaries.StorageProfileSummaries"
    )
    """The storage profiles."""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error."""


# --- restJson1 ser/de ---
def serialize_json(value: ListStorageProfilesResponse) -> dict:
    out: dict = {}
    import capo_deadline.types.storage_profile_summaries

    out["storageProfiles"] = (
        capo_deadline.types.storage_profile_summaries.serialize_json(
            value["storage_profiles"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListStorageProfilesResponse:
    out: ListStorageProfilesResponse = {}  # type: ignore[typeddict-item]
    if data.get("storageProfiles") is not None:
        import capo_deadline.types.storage_profile_summaries

        out["storage_profiles"] = (
            capo_deadline.types.storage_profile_summaries.deserialize_json(
                data["storageProfiles"]
            )
        )
    else:
        out["storage_profiles"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

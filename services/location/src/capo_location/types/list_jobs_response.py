"""Generated from Smithy shape ``com.amazonaws.location#ListJobsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.large_token
    import capo_location.types.list_jobs_response_entry_list


class ListJobsResponse(TypedDict, closed=True):
    entries: (
        "capo_location.types.list_jobs_response_entry_list.ListJobsResponseEntryList"
    )
    """<p>List of jobs in your Amazon Web Services account.</p>"""
    next_token: NotRequired["capo_location.types.large_token.LargeToken"]
    """<p>Token for retrieving the next page (present if more results available).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsResponse) -> dict:
    out: dict = {}
    import capo_location.types.list_jobs_response_entry_list

    out["Entries"] = capo_location.types.list_jobs_response_entry_list.serialize_json(
        value["entries"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobsResponse:
    out: ListJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Entries") is not None:
        import capo_location.types.list_jobs_response_entry_list

        out["entries"] = (
            capo_location.types.list_jobs_response_entry_list.deserialize_json(
                data["Entries"]
            )
        )
    else:
        raise DeserializationError("ListJobsResponse.entries required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListJobsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entries" in value:
        import capo_location.types.list_jobs_response_entry_list

        out["entries"] = (
            capo_location.types.list_jobs_response_entry_list.redact_sensitive(
                value["entries"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.location#ListPlaceIndexesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.list_place_indexes_response_entry_list
    import capo_location.types.token


class ListPlaceIndexesResponse(TypedDict, closed=True):
    entries: "capo_location.types.list_place_indexes_response_entry_list.ListPlaceIndexesResponseEntryList"
    """<p>Lists the place index resources that exist in your Amazon Web Services account</p>"""
    next_token: NotRequired["capo_location.types.token.Token"]
    """<p>A pagination token indicating that there are additional pages available. You can use the token in a new request to fetch the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPlaceIndexesResponse) -> dict:
    out: dict = {}
    import capo_location.types.list_place_indexes_response_entry_list

    out["Entries"] = (
        capo_location.types.list_place_indexes_response_entry_list.serialize_json(
            value["entries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPlaceIndexesResponse:
    out: ListPlaceIndexesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Entries") is not None:
        import capo_location.types.list_place_indexes_response_entry_list

        out["entries"] = (
            capo_location.types.list_place_indexes_response_entry_list.deserialize_json(
                data["Entries"]
            )
        )
    else:
        raise DeserializationError("ListPlaceIndexesResponse.entries required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListPlaceIndexesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entries" in value:
        import capo_location.types.list_place_indexes_response_entry_list

        out["entries"] = (
            capo_location.types.list_place_indexes_response_entry_list.redact_sensitive(
                value["entries"]
            )
        )
    return out

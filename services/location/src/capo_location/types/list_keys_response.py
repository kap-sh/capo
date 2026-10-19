"""Generated from Smithy shape ``com.amazonaws.location#ListKeysResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.list_keys_response_entry_list
    import capo_location.types.token


class ListKeysResponse(TypedDict, closed=True):
    entries: (
        "capo_location.types.list_keys_response_entry_list.ListKeysResponseEntryList"
    )
    """<p>Contains API key resources in your Amazon Web Services account. Details include API key name, allowed referers and timestamp for when the API key will expire.</p>"""
    next_token: NotRequired["capo_location.types.token.Token"]
    """<p>A pagination token indicating there are additional pages available. You can use the token in a following request to fetch the next set of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKeysResponse) -> dict:
    out: dict = {}
    import capo_location.types.list_keys_response_entry_list

    out["Entries"] = capo_location.types.list_keys_response_entry_list.serialize_json(
        value["entries"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKeysResponse:
    out: ListKeysResponse = {}  # type: ignore[typeddict-item]
    if data.get("Entries") is not None:
        import capo_location.types.list_keys_response_entry_list

        out["entries"] = (
            capo_location.types.list_keys_response_entry_list.deserialize_json(
                data["Entries"]
            )
        )
    else:
        out["entries"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListKeysResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entries" in value:
        import capo_location.types.list_keys_response_entry_list

        out["entries"] = (
            capo_location.types.list_keys_response_entry_list.redact_sensitive(
                value["entries"]
            )
        )
    return out

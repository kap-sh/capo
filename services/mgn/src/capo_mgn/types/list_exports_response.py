"""Generated from Smithy shape ``com.amazonaws.mgn#ListExportsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.exports_list
    import capo_mgn.types.pagination_token


class ListExportsResponse(TypedDict, closed=True):
    items: NotRequired["capo_mgn.types.exports_list.ExportsList"]
    """<p>List export response items.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>List export response next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExportsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.exports_list

        out["items"] = capo_mgn.types.exports_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExportsResponse:
    out: ListExportsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_mgn.types.exports_list

        out["items"] = capo_mgn.types.exports_list.deserialize_json(data["items"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListExportsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_mgn.types.exports_list

        out["items"] = capo_mgn.types.exports_list.redact_sensitive(value["items"])
    return out

"""Generated from Smithy shape ``com.amazonaws.mgn#ListImportsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.import_list
    import capo_mgn.types.pagination_token


class ListImportsResponse(TypedDict, closed=True):
    items: NotRequired["capo_mgn.types.import_list.ImportList"]
    """<p>List import response items.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>List import response next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.import_list

        out["items"] = capo_mgn.types.import_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImportsResponse:
    out: ListImportsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_mgn.types.import_list

        out["items"] = capo_mgn.types.import_list.deserialize_json(data["items"])
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListImportsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_mgn.types.import_list

        out["items"] = capo_mgn.types.import_list.redact_sensitive(value["items"])
    return out

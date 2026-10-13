"""Generated from Smithy shape ``com.amazonaws.securityir#ListCommentsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_security_ir.types.list_comments_items


class ListCommentsResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>An optional string that, if supplied on subsequent calls to ListComments, allows the API to fetch the next page of results. </p>"""
    items: NotRequired["capo_security_ir.types.list_comments_items.ListCommentsItems"]
    """<p>Response element for ListComments providing the body, commentID, createDate, creator, lastUpdatedBy and lastUpdatedDate for each response. </p>"""
    total: NotRequired["int"]
    """<p>Response element for ListComments identifying the number of responses.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCommentsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "items" in value:
        import capo_security_ir.types.list_comments_items

        out["items"] = capo_security_ir.types.list_comments_items.serialize_json(
            value["items"]
        )
    if "total" in value:
        out["total"] = value["total"]
    return out


def deserialize_json(data: dict) -> ListCommentsResponse:
    out: ListCommentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("items") is not None:
        import capo_security_ir.types.list_comments_items

        out["items"] = capo_security_ir.types.list_comments_items.deserialize_json(
            data["items"]
        )
    if data.get("total") is not None:
        out["total"] = data["total"]
    return out


def redact_sensitive(value: ListCommentsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_security_ir.types.list_comments_items

        out["items"] = capo_security_ir.types.list_comments_items.redact_sensitive(
            value["items"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.repostspace#SendInvitesInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_repostspace.errors import DeserializationError

if TYPE_CHECKING:
    import capo_repostspace.types.accessor_id_list
    import capo_repostspace.types.invite_body
    import capo_repostspace.types.invite_title
    import capo_repostspace.types.space_id


class SendInvitesInput(TypedDict, closed=True):
    space_id: "capo_repostspace.types.space_id.SpaceId"
    """<p>The ID of the private re:Post.</p>"""
    accessor_ids: "capo_repostspace.types.accessor_id_list.AccessorIdList"
    """<p>The array of identifiers for the users and groups.</p>"""
    title: "capo_repostspace.types.invite_title.InviteTitle"
    """<p>The title of the invite.</p>"""
    body: "capo_repostspace.types.invite_body.InviteBody"
    """<p>The body of the invite.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendInvitesInput) -> dict:
    out: dict = {}
    import capo_repostspace.types.accessor_id_list

    out["accessorIds"] = capo_repostspace.types.accessor_id_list.serialize_json(
        value["accessor_ids"]
    )
    out["title"] = value["title"]
    out["body"] = value["body"]
    return out


def deserialize_json(data: dict) -> SendInvitesInput:
    out: SendInvitesInput = {}  # type: ignore[typeddict-item]
    if data.get("accessorIds") is not None:
        import capo_repostspace.types.accessor_id_list

        out["accessor_ids"] = capo_repostspace.types.accessor_id_list.deserialize_json(
            data["accessorIds"]
        )
    else:
        raise DeserializationError("SendInvitesInput.accessor_ids required")
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        raise DeserializationError("SendInvitesInput.title required")
    if data.get("body") is not None:
        out["body"] = data["body"]
    else:
        raise DeserializationError("SendInvitesInput.body required")
    return out


def redact_sensitive(value: SendInvitesInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "body" in value:
        out["body"] = "*** Sensitive Data Redacted ***"
    return out

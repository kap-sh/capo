"""Generated from Smithy shape ``com.amazonaws.chime#Invite``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.email_address
    import capo_chime.types.email_status
    import capo_chime.types.invite_status
    import capo_chime.types.string


class Invite(TypedDict, closed=True):
    invite_id: NotRequired["capo_chime.types.string.String"]
    """<p>The invite ID.</p>"""
    status: NotRequired["capo_chime.types.invite_status.InviteStatus"]
    """<p>The status of the invite.</p>"""
    email_address: NotRequired["capo_chime.types.email_address.EmailAddress"]
    """<p>The email address to which the invite is sent.</p>"""
    email_status: NotRequired["capo_chime.types.email_status.EmailStatus"]
    """<p>The status of the invite email.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Invite) -> dict:
    out: dict = {}
    if "invite_id" in value:
        out["InviteId"] = value["invite_id"]
    if "status" in value:
        import capo_chime.types.invite_status

        out["Status"] = capo_chime.types.invite_status.serialize_json(value["status"])
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "email_status" in value:
        import capo_chime.types.email_status

        out["EmailStatus"] = capo_chime.types.email_status.serialize_json(
            value["email_status"]
        )
    return out


def deserialize_json(data: dict) -> Invite:
    out: Invite = {}  # type: ignore[typeddict-item]
    if data.get("InviteId") is not None:
        out["invite_id"] = data["InviteId"]
    if data.get("Status") is not None:
        import capo_chime.types.invite_status

        out["status"] = capo_chime.types.invite_status.deserialize_json(data["Status"])
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    if data.get("EmailStatus") is not None:
        import capo_chime.types.email_status

        out["email_status"] = capo_chime.types.email_status.deserialize_json(
            data["EmailStatus"]
        )
    return out


def redact_sensitive(value: Invite) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    return out

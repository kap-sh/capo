"""Generated from Smithy shape ``com.amazonaws.pinpointemail#CreateEmailIdentityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.identity
    import capo_pinpoint_email.types.tag_list


class CreateEmailIdentityRequest(TypedDict, closed=True):
    email_identity: "capo_pinpoint_email.types.identity.Identity"
    """<p>The email address or domain that you want to verify.</p>"""
    tags: NotRequired["capo_pinpoint_email.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) that you want to associate with the email identity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEmailIdentityRequest) -> dict:
    out: dict = {}
    out["EmailIdentity"] = value["email_identity"]
    if "tags" in value:
        import capo_pinpoint_email.types.tag_list

        out["Tags"] = capo_pinpoint_email.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateEmailIdentityRequest:
    out: CreateEmailIdentityRequest = {}  # type: ignore[typeddict-item]
    if data.get("EmailIdentity") is not None:
        out["email_identity"] = data["EmailIdentity"]
    else:
        out["email_identity"] = ""
    if data.get("Tags") is not None:
        import capo_pinpoint_email.types.tag_list

        out["tags"] = capo_pinpoint_email.types.tag_list.deserialize_json(data["Tags"])
    return out

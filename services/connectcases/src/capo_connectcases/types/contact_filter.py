"""Generated from Smithy shape ``com.amazonaws.connectcases#ContactFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.channel_list
    import capo_connectcases.types.contact_arn


class ContactFilter(TypedDict, closed=True):
    channel: NotRequired["capo_connectcases.types.channel_list.ChannelList"]
    """<p>A list of channels to filter on for related items of type <code>Contact</code>.</p>"""
    contact_arn: NotRequired["capo_connectcases.types.contact_arn.ContactArn"]
    """<p>A unique identifier of a contact in Connect Customer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFilter) -> dict:
    out: dict = {}
    if "channel" in value:
        import capo_connectcases.types.channel_list

        out["channel"] = capo_connectcases.types.channel_list.serialize_json(
            value["channel"]
        )
    if "contact_arn" in value:
        out["contactArn"] = value["contact_arn"]
    return out


def deserialize_json(data: dict) -> ContactFilter:
    out: ContactFilter = {}  # type: ignore[typeddict-item]
    if data.get("channel") is not None:
        import capo_connectcases.types.channel_list

        out["channel"] = capo_connectcases.types.channel_list.deserialize_json(
            data["channel"]
        )
    if data.get("contactArn") is not None:
        out["contact_arn"] = data["contactArn"]
    return out

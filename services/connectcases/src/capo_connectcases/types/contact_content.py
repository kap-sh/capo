"""Generated from Smithy shape ``com.amazonaws.connectcases#ContactContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.channel
    import capo_connectcases.types.connected_to_system_time
    import capo_connectcases.types.contact_arn


class ContactContent(TypedDict, closed=True):
    contact_arn: "capo_connectcases.types.contact_arn.ContactArn"
    """<p>A unique identifier of a contact in Amazon Connect.</p>"""
    channel: "capo_connectcases.types.channel.Channel"
    """<p>A list of channels to filter on for related items of type <code>Contact</code>.</p>"""
    connected_to_system_time: (
        "capo_connectcases.types.connected_to_system_time.ConnectedToSystemTime"
    )
    """<p>The difference between the <code>InitiationTimestamp</code> and the <code>DisconnectTimestamp</code> of the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactContent) -> dict:
    out: dict = {}
    out["contactArn"] = value["contact_arn"]
    out["channel"] = value["channel"]
    import capo_connectcases.types.connected_to_system_time

    out["connectedToSystemTime"] = (
        capo_connectcases.types.connected_to_system_time.serialize_json(
            value["connected_to_system_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> ContactContent:
    out: ContactContent = {}  # type: ignore[typeddict-item]
    if data.get("contactArn") is not None:
        out["contact_arn"] = data["contactArn"]
    else:
        out["contact_arn"] = ""
    if data.get("channel") is not None:
        out["channel"] = data["channel"]
    else:
        out["channel"] = ""
    if data.get("connectedToSystemTime") is not None:
        import capo_connectcases.types.connected_to_system_time

        out["connected_to_system_time"] = (
            capo_connectcases.types.connected_to_system_time.deserialize_json(
                data["connectedToSystemTime"]
            )
        )
    else:
        import datetime

        out["connected_to_system_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out

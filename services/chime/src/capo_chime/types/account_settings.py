"""Generated from Smithy shape ``com.amazonaws.chime#AccountSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.boolean


class AccountSettings(TypedDict, closed=True):
    disable_remote_control: NotRequired["capo_chime.types.boolean.Boolean"]
    """<p>Setting that stops or starts remote control of shared screens during meetings.</p>"""
    enable_dial_out: NotRequired["capo_chime.types.boolean.Boolean"]
    """<p>Setting that allows meeting participants to choose the <b>Call me at a phone number</b> option. For more information, see <a href="https://docs.aws.amazon.com/chime/latest/ug/chime-join-meeting.html">Join a Meeting without the Amazon Chime App</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountSettings) -> dict:
    out: dict = {}
    if "disable_remote_control" in value:
        out["DisableRemoteControl"] = value["disable_remote_control"]
    if "enable_dial_out" in value:
        out["EnableDialOut"] = value["enable_dial_out"]
    return out


def deserialize_json(data: dict) -> AccountSettings:
    out: AccountSettings = {}  # type: ignore[typeddict-item]
    if data.get("DisableRemoteControl") is not None:
        out["disable_remote_control"] = data["DisableRemoteControl"]
    if data.get("EnableDialOut") is not None:
        out["enable_dial_out"] = data["EnableDialOut"]
    return out

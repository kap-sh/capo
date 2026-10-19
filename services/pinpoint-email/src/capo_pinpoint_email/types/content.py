"""Generated from Smithy shape ``com.amazonaws.pinpointemail#Content``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.charset
    import capo_pinpoint_email.types.message_data


class Content(TypedDict, closed=True):
    data: "capo_pinpoint_email.types.message_data.MessageData"
    """<p>The content of the message itself.</p>"""
    charset: NotRequired["capo_pinpoint_email.types.charset.Charset"]
    """<p>The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify <code>UTF-8</code>, <code>ISO-8859-1</code>, or <code>Shift_JIS</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Content) -> dict:
    out: dict = {}
    out["Data"] = value["data"]
    if "charset" in value:
        out["Charset"] = value["charset"]
    return out


def deserialize_json(data: dict) -> Content:
    out: Content = {}  # type: ignore[typeddict-item]
    if data.get("Data") is not None:
        out["data"] = data["Data"]
    else:
        out["data"] = ""
    if data.get("Charset") is not None:
        out["charset"] = data["Charset"]
    return out

"""Generated from Smithy shape ``com.amazonaws.sesv2#PutAccountSendingAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.enabled


class PutAccountSendingAttributesRequest(TypedDict, closed=True):
    sending_enabled: NotRequired["capo_sesv2.types.enabled.Enabled"]
    """<p>Enables or disables your account's ability to send email. Set to <code>true</code> to enable email sending, or set to <code>false</code> to disable email sending.</p> <note> <p>If Amazon Web Services paused your account's ability to send email, you can't use this operation to resume your account's ability to send email.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountSendingAttributesRequest) -> dict:
    out: dict = {}
    if "sending_enabled" in value:
        out["SendingEnabled"] = value["sending_enabled"]
    return out


def deserialize_json(data: dict) -> PutAccountSendingAttributesRequest:
    out: PutAccountSendingAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("SendingEnabled") is not None:
        out["sending_enabled"] = data["SendingEnabled"]
    return out

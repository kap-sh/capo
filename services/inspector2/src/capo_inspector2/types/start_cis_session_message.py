"""Generated from Smithy shape ``com.amazonaws.inspector2#StartCisSessionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.uuid


class StartCisSessionMessage(TypedDict, closed=True):
    session_token: "capo_inspector2.types.uuid.UUID"
    """<p>The unique token that identifies the CIS session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCisSessionMessage) -> dict:
    out: dict = {}
    out["sessionToken"] = value["session_token"]
    return out


def deserialize_json(data: dict) -> StartCisSessionMessage:
    out: StartCisSessionMessage = {}  # type: ignore[typeddict-item]
    if data.get("sessionToken") is not None:
        out["session_token"] = data["sessionToken"]
    else:
        out["session_token"] = ""
    return out

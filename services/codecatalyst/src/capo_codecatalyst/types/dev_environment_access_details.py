"""Generated from Smithy shape ``com.amazonaws.codecatalyst#DevEnvironmentAccessDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.sensitive_string


class DevEnvironmentAccessDetails(TypedDict, closed=True):
    stream_url: "capo_codecatalyst.types.sensitive_string.SensitiveString"
    """<p>The URL used to send commands to and from the Dev Environment.</p>"""
    token_value: "capo_codecatalyst.types.sensitive_string.SensitiveString"
    """<p>An encrypted token value that contains session and caller information used to authenticate the connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DevEnvironmentAccessDetails) -> dict:
    out: dict = {}
    out["streamUrl"] = value["stream_url"]
    out["tokenValue"] = value["token_value"]
    return out


def deserialize_json(data: dict) -> DevEnvironmentAccessDetails:
    out: DevEnvironmentAccessDetails = {}  # type: ignore[typeddict-item]
    if data.get("streamUrl") is not None:
        out["stream_url"] = data["streamUrl"]
    else:
        out["stream_url"] = ""
    if data.get("tokenValue") is not None:
        out["token_value"] = data["tokenValue"]
    else:
        out["token_value"] = ""
    return out

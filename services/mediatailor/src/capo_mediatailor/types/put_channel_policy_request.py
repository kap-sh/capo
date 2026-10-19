"""Generated from Smithy shape ``com.amazonaws.mediatailor#PutChannelPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediatailor.types.__string


class PutChannelPolicyRequest(TypedDict, closed=True):
    channel_name: "capo_mediatailor.types.__string.__string"
    """<p>The channel name associated with this Channel Policy.</p>"""
    policy: "capo_mediatailor.types.__string.__string"
    """<p>Adds an IAM role that determines the permissions of your channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutChannelPolicyRequest) -> dict:
    out: dict = {}
    out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutChannelPolicyRequest:
    out: PutChannelPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        out["policy"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#SessionConfig``."""

from typing_extensions import TypedDict


class SessionConfig(TypedDict, closed=True):
    session_timeout_minutes: "int"
    """<p> The number of minutes of inactivity after which an agent session is considered complete and ready for evaluation. Default is 15 minutes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionConfig) -> dict:
    out: dict = {}
    out["sessionTimeoutMinutes"] = value["session_timeout_minutes"]
    return out


def deserialize_json(data: dict) -> SessionConfig:
    out: SessionConfig = {}  # type: ignore[typeddict-item]
    if data.get("sessionTimeoutMinutes") is not None:
        out["session_timeout_minutes"] = data["sessionTimeoutMinutes"]
    else:
        out["session_timeout_minutes"] = 0
    return out

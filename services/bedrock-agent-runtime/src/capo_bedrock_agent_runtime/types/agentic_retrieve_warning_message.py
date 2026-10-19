"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveWarningMessage``."""

from typing_extensions import TypedDict


class AgenticRetrieveWarningMessage(TypedDict, closed=True):
    message: "str"
    """<p>The warning message text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveWarningMessage) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AgenticRetrieveWarningMessage:
    out: AgenticRetrieveWarningMessage = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out

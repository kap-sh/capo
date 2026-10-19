"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AgenticRetrieveFailure``."""

from typing_extensions import TypedDict


class AgenticRetrieveFailure(TypedDict, closed=True):
    message: "str"
    """<p>A message describing the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgenticRetrieveFailure) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AgenticRetrieveFailure:
    out: AgenticRetrieveFailure = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out

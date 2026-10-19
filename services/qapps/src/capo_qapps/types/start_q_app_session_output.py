"""Generated from Smithy shape ``com.amazonaws.qapps#StartQAppSessionOutput``."""

from typing_extensions import TypedDict


class StartQAppSessionOutput(TypedDict, closed=True):
    session_id: "str"
    """<p>The unique identifier of the new or retrieved Q App session.</p>"""
    session_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the new Q App session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartQAppSessionOutput) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["sessionArn"] = value["session_arn"]
    return out


def deserialize_json(data: dict) -> StartQAppSessionOutput:
    out: StartQAppSessionOutput = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        out["session_arn"] = ""
    return out

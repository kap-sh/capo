"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentError``."""

from typing_extensions import NotRequired, TypedDict


class EnvironmentError(TypedDict, closed=True):
    code: NotRequired["str"]
    """<p>The error code for the failure reason for the environment deployment.</p>"""
    message: "str"
    """<p>The error message for the failure reason for the environment deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentError) -> dict:
    out: dict = {}
    if "code" in value:
        out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> EnvironmentError:
    out: EnvironmentError = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out

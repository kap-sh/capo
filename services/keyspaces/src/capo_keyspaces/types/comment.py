"""Generated from Smithy shape ``com.amazonaws.keyspaces#Comment``."""

from typing_extensions import TypedDict


class Comment(TypedDict, closed=True):
    message: "str"
    """<p>An optional description of the table.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Comment) -> dict:
    out: dict = {}
    out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Comment:
    out: Comment = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out

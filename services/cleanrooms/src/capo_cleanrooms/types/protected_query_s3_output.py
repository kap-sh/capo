"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryS3Output``."""

from typing_extensions import TypedDict


class ProtectedQueryS3Output(TypedDict, closed=True):
    location: "str"
    """<p>The S3 location of the result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryS3Output) -> dict:
    out: dict = {}
    out["location"] = value["location"]
    return out


def deserialize_json(data: dict) -> ProtectedQueryS3Output:
    out: ProtectedQueryS3Output = {}  # type: ignore[typeddict-item]
    if data.get("location") is not None:
        out["location"] = data["location"]
    else:
        out["location"] = ""
    return out

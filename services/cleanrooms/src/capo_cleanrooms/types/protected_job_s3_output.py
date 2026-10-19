"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobS3Output``."""

from typing_extensions import TypedDict


class ProtectedJobS3Output(TypedDict, closed=True):
    location: "str"
    """<p> The S3 location for the protected job output.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobS3Output) -> dict:
    out: dict = {}
    out["location"] = value["location"]
    return out


def deserialize_json(data: dict) -> ProtectedJobS3Output:
    out: ProtectedJobS3Output = {}  # type: ignore[typeddict-item]
    if data.get("location") is not None:
        out["location"] = data["location"]
    else:
        out["location"] = ""
    return out

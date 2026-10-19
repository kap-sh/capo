"""Generated from Smithy shape ``com.amazonaws.omics#UploadReadSetPartResponse``."""

from typing_extensions import TypedDict


class UploadReadSetPartResponse(TypedDict, closed=True):
    checksum: "str"
    """<p>An identifier used to confirm that parts are being added to the intended upload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UploadReadSetPartResponse) -> dict:
    out: dict = {}
    out["checksum"] = value["checksum"]
    return out


def deserialize_json(data: dict) -> UploadReadSetPartResponse:
    out: UploadReadSetPartResponse = {}  # type: ignore[typeddict-item]
    if data.get("checksum") is not None:
        out["checksum"] = data["checksum"]
    else:
        out["checksum"] = ""
    return out

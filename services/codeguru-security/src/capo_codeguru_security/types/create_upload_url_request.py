"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#CreateUploadUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguru_security.types.scan_name


class CreateUploadUrlRequest(TypedDict, closed=True):
    scan_name: "capo_codeguru_security.types.scan_name.ScanName"
    """<p>The name of the scan that will use the uploaded resource. CodeGuru Security uses the unique scan name to track revisions across multiple scans of the same resource. Use this <code>scanName</code> when you call <code>CreateScan</code> on the code resource you upload to this URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUploadUrlRequest) -> dict:
    out: dict = {}
    out["scanName"] = value["scan_name"]
    return out


def deserialize_json(data: dict) -> CreateUploadUrlRequest:
    out: CreateUploadUrlRequest = {}  # type: ignore[typeddict-item]
    if data.get("scanName") is not None:
        out["scan_name"] = data["scanName"]
    else:
        out["scan_name"] = ""
    return out

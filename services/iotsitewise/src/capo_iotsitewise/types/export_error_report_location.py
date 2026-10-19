"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExportErrorReportLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.s3_uri


class ExportErrorReportLocation(TypedDict, closed=True):
    s3_uri: "capo_iotsitewise.types.s3_uri.S3Uri"
    """<p>The S3 URI prefix for the error report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportErrorReportLocation) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> ExportErrorReportLocation:
    out: ExportErrorReportLocation = {}  # type: ignore[typeddict-item]
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    else:
        out["s3_uri"] = ""
    return out

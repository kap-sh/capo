"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#S3ReportOutput``."""

from typing_extensions import TypedDict


class S3ReportOutput(TypedDict, closed=True):
    s3_object_key: "str"
    """<p>The S3 object key for the generated report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ReportOutput) -> dict:
    out: dict = {}
    out["s3ObjectKey"] = value["s3_object_key"]
    return out


def deserialize_json(data: dict) -> S3ReportOutput:
    out: S3ReportOutput = {}  # type: ignore[typeddict-item]
    if data.get("s3ObjectKey") is not None:
        out["s3_object_key"] = data["s3ObjectKey"]
    else:
        out["s3_object_key"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#S3ReportOutput``."""

from typing_extensions import NotRequired, TypedDict


class S3ReportOutput(TypedDict, closed=True):
    s3_object_key: NotRequired["str"]
    """<p>The S3 object key where the generated report is stored.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: S3ReportOutput) -> dict:
    out: dict = {}
    if "s3_object_key" in value:
        out["s3ObjectKey"] = value["s3_object_key"]
    return out


def deserialize_aws_json_1_0(data: dict) -> S3ReportOutput:
    out: S3ReportOutput = {}  # type: ignore[typeddict-item]
    if data.get("s3ObjectKey") is not None:
        out["s3_object_key"] = data["s3ObjectKey"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: S3ReportOutput) -> dict:
    out: dict = {}
    if "s3_object_key" in value:
        out["s3ObjectKey"] = value["s3_object_key"]
    return out


def deserialize_cbor(data: dict) -> S3ReportOutput:
    out: S3ReportOutput = {}  # type: ignore[typeddict-item]
    if data.get("s3ObjectKey") is not None:
        out["s3_object_key"] = data["s3ObjectKey"]
    return out

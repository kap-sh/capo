"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportWithRawData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.string


class ReportWithRawData(TypedDict, closed=True):
    report_arn: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the report.</p>"""
    data: NotRequired["capo_codebuild.types.string.String"]
    """<p>The value of the requested data field from the report.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportWithRawData) -> dict:
    out: dict = {}
    if "report_arn" in value:
        out["reportArn"] = value["report_arn"]
    if "data" in value:
        out["data"] = value["data"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportWithRawData:
    out: ReportWithRawData = {}  # type: ignore[typeddict-item]
    if data.get("reportArn") is not None:
        out["report_arn"] = data["reportArn"]
    if data.get("data") is not None:
        out["data"] = data["data"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportWithRawData) -> dict:
    out: dict = {}
    if "report_arn" in value:
        out["reportArn"] = value["report_arn"]
    if "data" in value:
        out["data"] = value["data"]
    return out


def deserialize_cbor(data: dict) -> ReportWithRawData:
    out: ReportWithRawData = {}  # type: ignore[typeddict-item]
    if data.get("reportArn") is not None:
        out["report_arn"] = data["reportArn"]
    if data.get("data") is not None:
        out["data"] = data["data"]
    return out

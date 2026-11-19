"""Generated from Smithy shape ``com.amazonaws.codebuild#ReportFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.report_status_type


class ReportFilter(TypedDict, closed=True):
    status: NotRequired["capo_codebuild.types.report_status_type.ReportStatusType"]
    """<p> The status used to filter reports. You can filter using one status only. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReportFilter) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_codebuild.types.report_status_type

        out["status"] = capo_codebuild.types.report_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReportFilter:
    out: ReportFilter = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_codebuild.types.report_status_type

        out["status"] = (
            capo_codebuild.types.report_status_type.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReportFilter) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_codebuild.types.report_status_type

        out["status"] = capo_codebuild.types.report_status_type.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> ReportFilter:
    out: ReportFilter = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_codebuild.types.report_status_type

        out["status"] = capo_codebuild.types.report_status_type.deserialize_cbor(
            data["status"]
        )
    return out

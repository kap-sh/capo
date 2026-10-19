"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#FailedReportOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.report_generation_error_code


class FailedReportOutput(TypedDict, closed=True):
    error_code: "capo_resiliencehubv2.types.report_generation_error_code.ReportGenerationErrorCode"
    """<p>The error code describing why the report generation failed.</p>"""
    error_message: NotRequired["str"]
    """<p>The error message describing why the report generation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailedReportOutput) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.report_generation_error_code

    out["errorCode"] = (
        capo_resiliencehubv2.types.report_generation_error_code.serialize_json(
            value["error_code"]
        )
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> FailedReportOutput:
    out: FailedReportOutput = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        import capo_resiliencehubv2.types.report_generation_error_code

        out["error_code"] = (
            capo_resiliencehubv2.types.report_generation_error_code.deserialize_json(
                data["errorCode"]
            )
        )
    else:
        import typing

        out["error_code"] = typing.cast(
            "capo_resiliencehubv2.types.report_generation_error_code.ReportGenerationErrorCode",
            "",
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out

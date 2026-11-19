"""Generated from Smithy shape ``com.amazonaws.appstream#LastReportGenerationExecutionError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.string
    import capo_appstream.types.usage_report_execution_error_code


class LastReportGenerationExecutionError(TypedDict, closed=True):
    error_code: NotRequired[
        "capo_appstream.types.usage_report_execution_error_code.UsageReportExecutionErrorCode"
    ]
    """<p>The error code for the error that is returned when a usage report can't be generated.</p>"""
    error_message: NotRequired["capo_appstream.types.string.String"]
    """<p>The error message for the error that is returned when a usage report can't be generated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastReportGenerationExecutionError) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_appstream.types.usage_report_execution_error_code

        out["ErrorCode"] = (
            capo_appstream.types.usage_report_execution_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LastReportGenerationExecutionError:
    out: LastReportGenerationExecutionError = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        import capo_appstream.types.usage_report_execution_error_code

        out["error_code"] = (
            capo_appstream.types.usage_report_execution_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LastReportGenerationExecutionError) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_appstream.types.usage_report_execution_error_code

        out["ErrorCode"] = (
            capo_appstream.types.usage_report_execution_error_code.serialize_cbor(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> LastReportGenerationExecutionError:
    out: LastReportGenerationExecutionError = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        import capo_appstream.types.usage_report_execution_error_code

        out["error_code"] = (
            capo_appstream.types.usage_report_execution_error_code.deserialize_cbor(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out

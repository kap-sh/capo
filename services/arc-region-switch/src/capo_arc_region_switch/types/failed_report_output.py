"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#FailedReportOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.failed_report_error_code


class FailedReportOutput(TypedDict, closed=True):
    error_code: NotRequired[
        "capo_arc_region_switch.types.failed_report_error_code.FailedReportErrorCode"
    ]
    """<p>The error code for the failed report generation.</p>"""
    error_message: NotRequired["str"]
    """<p>The error message for the failed report generation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FailedReportOutput) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_arc_region_switch.types.failed_report_error_code

        out["errorCode"] = (
            capo_arc_region_switch.types.failed_report_error_code.serialize_aws_json_1_0(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> FailedReportOutput:
    out: FailedReportOutput = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        import capo_arc_region_switch.types.failed_report_error_code

        out["error_code"] = (
            capo_arc_region_switch.types.failed_report_error_code.deserialize_aws_json_1_0(
                data["errorCode"]
            )
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FailedReportOutput) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_arc_region_switch.types.failed_report_error_code

        out["errorCode"] = (
            capo_arc_region_switch.types.failed_report_error_code.serialize_cbor(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> FailedReportOutput:
    out: FailedReportOutput = {}  # type: ignore[typeddict-item]
    if data.get("errorCode") is not None:
        import capo_arc_region_switch.types.failed_report_error_code

        out["error_code"] = (
            capo_arc_region_switch.types.failed_report_error_code.deserialize_cbor(
                data["errorCode"]
            )
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out

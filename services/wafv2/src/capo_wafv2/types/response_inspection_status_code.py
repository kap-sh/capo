"""Generated from Smithy shape ``com.amazonaws.wafv2#ResponseInspectionStatusCode``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.response_inspection_status_code_failure_codes
    import capo_wafv2.types.response_inspection_status_code_success_codes


class ResponseInspectionStatusCode(TypedDict, closed=True):
    success_codes: "capo_wafv2.types.response_inspection_status_code_success_codes.ResponseInspectionStatusCodeSuccessCodes"
    """<p>Status codes in the response that indicate a successful login or account creation attempt. To be counted as a success, the response status code must match one of these. Each code must be unique among the success and failure status codes. </p> <p>JSON example: <code>"SuccessCodes": [ 200, 201 ]</code> </p>"""
    failure_codes: "capo_wafv2.types.response_inspection_status_code_failure_codes.ResponseInspectionStatusCodeFailureCodes"
    """<p>Status codes in the response that indicate a failed login or account creation attempt. To be counted as a failure, the response status code must match one of these. Each code must be unique among the success and failure status codes. </p> <p>JSON example: <code>"FailureCodes": [ 400, 404 ]</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseInspectionStatusCode) -> dict:
    out: dict = {}
    import capo_wafv2.types.response_inspection_status_code_success_codes

    out["SuccessCodes"] = (
        capo_wafv2.types.response_inspection_status_code_success_codes.serialize_aws_json_1_1(
            value["success_codes"]
        )
    )
    import capo_wafv2.types.response_inspection_status_code_failure_codes

    out["FailureCodes"] = (
        capo_wafv2.types.response_inspection_status_code_failure_codes.serialize_aws_json_1_1(
            value["failure_codes"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponseInspectionStatusCode:
    out: ResponseInspectionStatusCode = {}  # type: ignore[typeddict-item]
    if data.get("SuccessCodes") is not None:
        import capo_wafv2.types.response_inspection_status_code_success_codes

        out["success_codes"] = (
            capo_wafv2.types.response_inspection_status_code_success_codes.deserialize_aws_json_1_1(
                data["SuccessCodes"]
            )
        )
    else:
        raise DeserializationError(
            "ResponseInspectionStatusCode.success_codes required"
        )
    if data.get("FailureCodes") is not None:
        import capo_wafv2.types.response_inspection_status_code_failure_codes

        out["failure_codes"] = (
            capo_wafv2.types.response_inspection_status_code_failure_codes.deserialize_aws_json_1_1(
                data["FailureCodes"]
            )
        )
    else:
        raise DeserializationError(
            "ResponseInspectionStatusCode.failure_codes required"
        )
    return out

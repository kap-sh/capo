"""Generated from Smithy shape ``com.amazonaws.wafv2#ResponseInspectionHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.response_inspection_header_failure_values
    import capo_wafv2.types.response_inspection_header_name
    import capo_wafv2.types.response_inspection_header_success_values


class ResponseInspectionHeader(TypedDict, closed=True):
    name: (
        "capo_wafv2.types.response_inspection_header_name.ResponseInspectionHeaderName"
    )
    """<p>The name of the header to match against. The name must be an exact match, including case.</p> <p>JSON example: <code>"Name": [ "RequestResult" ]</code> </p>"""
    success_values: "capo_wafv2.types.response_inspection_header_success_values.ResponseInspectionHeaderSuccessValues"
    """<p>Values in the response header with the specified name that indicate a successful login or account creation attempt. To be counted as a success, the value must be an exact match, including case. Each value must be unique among the success and failure values. </p> <p>JSON examples: <code>"SuccessValues": [ "LoginPassed", "Successful login" ]</code> and <code>"SuccessValues": [ "AccountCreated", "Successful account creation" ]</code> </p>"""
    failure_values: "capo_wafv2.types.response_inspection_header_failure_values.ResponseInspectionHeaderFailureValues"
    """<p>Values in the response header with the specified name that indicate a failed login or account creation attempt. To be counted as a failure, the value must be an exact match, including case. Each value must be unique among the success and failure values. </p> <p>JSON examples: <code>"FailureValues": [ "LoginFailed", "Failed login" ]</code> and <code>"FailureValues": [ "AccountCreationFailed" ]</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseInspectionHeader) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_wafv2.types.response_inspection_header_success_values

    out["SuccessValues"] = (
        capo_wafv2.types.response_inspection_header_success_values.serialize_aws_json_1_1(
            value["success_values"]
        )
    )
    import capo_wafv2.types.response_inspection_header_failure_values

    out["FailureValues"] = (
        capo_wafv2.types.response_inspection_header_failure_values.serialize_aws_json_1_1(
            value["failure_values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponseInspectionHeader:
    out: ResponseInspectionHeader = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ResponseInspectionHeader.name required")
    if data.get("SuccessValues") is not None:
        import capo_wafv2.types.response_inspection_header_success_values

        out["success_values"] = (
            capo_wafv2.types.response_inspection_header_success_values.deserialize_aws_json_1_1(
                data["SuccessValues"]
            )
        )
    else:
        raise DeserializationError("ResponseInspectionHeader.success_values required")
    if data.get("FailureValues") is not None:
        import capo_wafv2.types.response_inspection_header_failure_values

        out["failure_values"] = (
            capo_wafv2.types.response_inspection_header_failure_values.deserialize_aws_json_1_1(
                data["FailureValues"]
            )
        )
    else:
        raise DeserializationError("ResponseInspectionHeader.failure_values required")
    return out

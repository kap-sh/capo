"""Generated from Smithy shape ``com.amazonaws.wafv2#ResponseInspectionBodyContains``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.response_inspection_body_contains_failure_strings
    import capo_wafv2.types.response_inspection_body_contains_success_strings


class ResponseInspectionBodyContains(TypedDict, closed=True):
    success_strings: "capo_wafv2.types.response_inspection_body_contains_success_strings.ResponseInspectionBodyContainsSuccessStrings"
    """<p>Strings in the body of the response that indicate a successful login or account creation attempt. To be counted as a success, the string can be anywhere in the body and must be an exact match, including case. Each string must be unique among the success and failure strings. </p> <p>JSON examples: <code>"SuccessStrings": [ "Login successful" ]</code> and <code>"SuccessStrings": [ "Account creation successful", "Welcome to our site!" ]</code> </p>"""
    failure_strings: "capo_wafv2.types.response_inspection_body_contains_failure_strings.ResponseInspectionBodyContainsFailureStrings"
    """<p>Strings in the body of the response that indicate a failed login or account creation attempt. To be counted as a failure, the string can be anywhere in the body and must be an exact match, including case. Each string must be unique among the success and failure strings. </p> <p>JSON example: <code>"FailureStrings": [ "Request failed" ]</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseInspectionBodyContains) -> dict:
    out: dict = {}
    import capo_wafv2.types.response_inspection_body_contains_success_strings

    out["SuccessStrings"] = (
        capo_wafv2.types.response_inspection_body_contains_success_strings.serialize_aws_json_1_1(
            value["success_strings"]
        )
    )
    import capo_wafv2.types.response_inspection_body_contains_failure_strings

    out["FailureStrings"] = (
        capo_wafv2.types.response_inspection_body_contains_failure_strings.serialize_aws_json_1_1(
            value["failure_strings"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponseInspectionBodyContains:
    out: ResponseInspectionBodyContains = {}  # type: ignore[typeddict-item]
    if data.get("SuccessStrings") is not None:
        import capo_wafv2.types.response_inspection_body_contains_success_strings

        out["success_strings"] = (
            capo_wafv2.types.response_inspection_body_contains_success_strings.deserialize_aws_json_1_1(
                data["SuccessStrings"]
            )
        )
    else:
        raise DeserializationError(
            "ResponseInspectionBodyContains.success_strings required"
        )
    if data.get("FailureStrings") is not None:
        import capo_wafv2.types.response_inspection_body_contains_failure_strings

        out["failure_strings"] = (
            capo_wafv2.types.response_inspection_body_contains_failure_strings.deserialize_aws_json_1_1(
                data["FailureStrings"]
            )
        )
    else:
        raise DeserializationError(
            "ResponseInspectionBodyContains.failure_strings required"
        )
    return out

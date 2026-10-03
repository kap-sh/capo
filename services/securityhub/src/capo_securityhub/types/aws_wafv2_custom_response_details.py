"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsWafv2CustomResponseDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_wafv2_insert_headers_list
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsWafv2CustomResponseDetails(TypedDict, closed=True):
    custom_response_body_key: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> References the response body that you want WAF to return to the web request client. You can define a custom response for a rule action or a default web ACL action that is set to block. </p>"""
    response_code: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p> The HTTP status code to return to the client. For a list of status codes that you can use in your custom responses, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/customizing-the-response-status-codes.html">Supported status codes for custom response</a> in the <i>WAF Developer Guide.</i> </p>"""
    response_headers: NotRequired[
        "capo_securityhub.types.aws_wafv2_insert_headers_list.AwsWafv2InsertHeadersList"
    ]
    """<p> The HTTP headers to use in the response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsWafv2CustomResponseDetails) -> dict:
    out: dict = {}
    if "custom_response_body_key" in value:
        out["CustomResponseBodyKey"] = value["custom_response_body_key"]
    if "response_code" in value:
        out["ResponseCode"] = value["response_code"]
    if "response_headers" in value:
        import capo_securityhub.types.aws_wafv2_insert_headers_list

        out["ResponseHeaders"] = (
            capo_securityhub.types.aws_wafv2_insert_headers_list.serialize_json(
                value["response_headers"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsWafv2CustomResponseDetails:
    out: AwsWafv2CustomResponseDetails = {}  # type: ignore[typeddict-item]
    if data.get("CustomResponseBodyKey") is not None:
        out["custom_response_body_key"] = data["CustomResponseBodyKey"]
    if data.get("ResponseCode") is not None:
        out["response_code"] = data["ResponseCode"]
    if data.get("ResponseHeaders") is not None:
        import capo_securityhub.types.aws_wafv2_insert_headers_list

        out["response_headers"] = (
            capo_securityhub.types.aws_wafv2_insert_headers_list.deserialize_json(
                data["ResponseHeaders"]
            )
        )
    return out

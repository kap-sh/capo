"""Generated from Smithy shape ``com.amazonaws.wafv2#CustomResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.custom_http_headers
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.response_status_code


class CustomResponse(TypedDict, closed=True):
    response_code: "capo_wafv2.types.response_status_code.ResponseStatusCode"
    """<p>The HTTP status code to return to the client. </p> <p>For a list of status codes that you can use in your custom responses, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/customizing-the-response-status-codes.html">Supported status codes for custom response</a> in the <i>WAF Developer Guide</i>. </p>"""
    custom_response_body_key: NotRequired["capo_wafv2.types.entity_name.EntityName"]
    """<p>References the response body that you want WAF to return to the web request client. You can define a custom response for a rule action or a default web ACL action that is set to block. To do this, you first define the response body key and value in the <code>CustomResponseBodies</code> setting for the <a>WebACL</a> or <a>RuleGroup</a> where you want to use it. Then, in the rule action or web ACL default action <code>BlockAction</code> setting, you reference the response body using this key. </p>"""
    response_headers: NotRequired[
        "capo_wafv2.types.custom_http_headers.CustomHTTPHeaders"
    ]
    """<p>The HTTP headers to use in the response. You can specify any header name except for <code>content-type</code>. Duplicate header names are not allowed.</p> <p>For information about the limits on count and size for custom request and response settings, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomResponse) -> dict:
    out: dict = {}
    out["ResponseCode"] = value["response_code"]
    if "custom_response_body_key" in value:
        out["CustomResponseBodyKey"] = value["custom_response_body_key"]
    if "response_headers" in value:
        import capo_wafv2.types.custom_http_headers

        out["ResponseHeaders"] = (
            capo_wafv2.types.custom_http_headers.serialize_aws_json_1_1(
                value["response_headers"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomResponse:
    out: CustomResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResponseCode") is not None:
        out["response_code"] = data["ResponseCode"]
    else:
        raise DeserializationError("CustomResponse.response_code required")
    if data.get("CustomResponseBodyKey") is not None:
        out["custom_response_body_key"] = data["CustomResponseBodyKey"]
    if data.get("ResponseHeaders") is not None:
        import capo_wafv2.types.custom_http_headers

        out["response_headers"] = (
            capo_wafv2.types.custom_http_headers.deserialize_aws_json_1_1(
                data["ResponseHeaders"]
            )
        )
    return out

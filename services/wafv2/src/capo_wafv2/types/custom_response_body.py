"""Generated from Smithy shape ``com.amazonaws.wafv2#CustomResponseBody``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.response_content
    import capo_wafv2.types.response_content_type


class CustomResponseBody(TypedDict, closed=True):
    content_type: "capo_wafv2.types.response_content_type.ResponseContentType"
    """<p>The type of content in the payload that you are defining in the <code>Content</code> string.</p>"""
    content: "capo_wafv2.types.response_content.ResponseContent"
    """<p>The payload of the custom response. </p> <p>You can use JSON escape strings in JSON content. To do this, you must specify JSON content in the <code>ContentType</code> setting. </p> <p>For information about the limits on count and size for custom request and response settings, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomResponseBody) -> dict:
    out: dict = {}
    import capo_wafv2.types.response_content_type

    out["ContentType"] = capo_wafv2.types.response_content_type.serialize_aws_json_1_1(
        value["content_type"]
    )
    out["Content"] = value["content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomResponseBody:
    out: CustomResponseBody = {}  # type: ignore[typeddict-item]
    if data.get("ContentType") is not None:
        import capo_wafv2.types.response_content_type

        out["content_type"] = (
            capo_wafv2.types.response_content_type.deserialize_aws_json_1_1(
                data["ContentType"]
            )
        )
    else:
        raise DeserializationError("CustomResponseBody.content_type required")
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("CustomResponseBody.content required")
    return out

"""Generated from Smithy shape ``com.amazonaws.wafv2#CustomRequestHandling``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.custom_http_headers


class CustomRequestHandling(TypedDict, closed=True):
    insert_headers: "capo_wafv2.types.custom_http_headers.CustomHTTPHeaders"
    """<p>The HTTP headers to insert into the request. Duplicate header names are not allowed. </p> <p>For information about the limits on count and size for custom request and response settings, see <a href="https://docs.aws.amazon.com/waf/latest/developerguide/limits.html">WAF quotas</a> in the <i>WAF Developer Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRequestHandling) -> dict:
    out: dict = {}
    import capo_wafv2.types.custom_http_headers

    out["InsertHeaders"] = capo_wafv2.types.custom_http_headers.serialize_aws_json_1_1(
        value["insert_headers"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomRequestHandling:
    out: CustomRequestHandling = {}  # type: ignore[typeddict-item]
    if data.get("InsertHeaders") is not None:
        import capo_wafv2.types.custom_http_headers

        out["insert_headers"] = (
            capo_wafv2.types.custom_http_headers.deserialize_aws_json_1_1(
                data["InsertHeaders"]
            )
        )
    else:
        raise DeserializationError("CustomRequestHandling.insert_headers required")
    return out

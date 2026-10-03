"""Generated from Smithy shape ``com.amazonaws.mediatailor#VastRequestConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__integer
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.method_type
    import capo_mediatailor.types.runtime_type


class VastRequestConfiguration(TypedDict, closed=True):
    runtime: "capo_mediatailor.types.runtime_type.RuntimeType"
    """<p>The expression language used to evaluate expressions in the function configuration. Set this to <code>JSONata</code>.</p>"""
    output: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>A map of output bindings. Each key is a namespaced output path (such as <code>temp.wrappedAds</code>), and each value is an expression that MediaTailor evaluates at runtime. Output expressions in a <code>VAST_REQUEST</code> function can reference the <code>response</code> object, which exposes <code>response.parsedAds</code> — the ads parsed from the VAST response after schema validation and wrapper resolution — and <code>response.statusCode</code>. For more information about expression syntax, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-jsonata.html">JSONata expression reference</a> in the <i>MediaTailor User Guide</i>.</p>"""
    method_type: "capo_mediatailor.types.method_type.MethodType"
    """<p>The HTTP method for the request to the VAST endpoint. Valid values: <code>GET</code> and <code>POST</code>. Use <code>POST</code> to send a bid request body, such as an OpenRTB payload.</p>"""
    request_timeout_milliseconds: "capo_mediatailor.types.__integer.__integer"
    """<p>The maximum time, in milliseconds, that MediaTailor waits for a response from the VAST endpoint. The timeout covers the entire response, including any wrapper redirects that MediaTailor follows. If the call exceeds this timeout, MediaTailor proceeds with an empty ad list and continues output expression evaluation. Valid values: <code>100</code> to <code>2000</code>.</p>"""
    url: "capo_mediatailor.types.__string.__string"
    """<p>An expression that evaluates to the VAST endpoint URL. Use <code>{%...%}</code> delimiters for dynamic expressions. A literal value must be an <code>https://</code> URL. The expression can be up to 25,000 characters, and the URL after evaluation can be up to 2,048 characters.</p>"""
    body: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>An expression that evaluates to the request body, for example to send an OpenRTB bid request. The expression can be up to 100,000 characters, and the body after evaluation can be up to 64 KB.</p>"""
    headers: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>A map of HTTP header names to expression values. MediaTailor evaluates each header value expression at runtime and includes the result in the outbound request. Headers beginning with <code>X-Amz-</code> are reserved by the service, and method override headers are not allowed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VastRequestConfiguration) -> dict:
    out: dict = {}
    import capo_mediatailor.types.runtime_type

    out["Runtime"] = capo_mediatailor.types.runtime_type.serialize_json(
        value["runtime"]
    )
    if "output" in value:
        import capo_mediatailor.types.__map_of__string

        out["Output"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["output"]
        )
    import capo_mediatailor.types.method_type

    out["MethodType"] = capo_mediatailor.types.method_type.serialize_json(
        value["method_type"]
    )
    out["RequestTimeoutMilliseconds"] = value["request_timeout_milliseconds"]
    out["Url"] = value["url"]
    if "body" in value:
        out["Body"] = value["body"]
    if "headers" in value:
        import capo_mediatailor.types.__map_of__string

        out["Headers"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["headers"]
        )
    return out


def deserialize_json(data: dict) -> VastRequestConfiguration:
    out: VastRequestConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Runtime") is not None:
        import capo_mediatailor.types.runtime_type

        out["runtime"] = capo_mediatailor.types.runtime_type.deserialize_json(
            data["Runtime"]
        )
    else:
        raise DeserializationError("VastRequestConfiguration.runtime required")
    if data.get("Output") is not None:
        import capo_mediatailor.types.__map_of__string

        out["output"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["Output"]
        )
    if data.get("MethodType") is not None:
        import capo_mediatailor.types.method_type

        out["method_type"] = capo_mediatailor.types.method_type.deserialize_json(
            data["MethodType"]
        )
    else:
        raise DeserializationError("VastRequestConfiguration.method_type required")
    if data.get("RequestTimeoutMilliseconds") is not None:
        out["request_timeout_milliseconds"] = data["RequestTimeoutMilliseconds"]
    else:
        raise DeserializationError(
            "VastRequestConfiguration.request_timeout_milliseconds required"
        )
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        raise DeserializationError("VastRequestConfiguration.url required")
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    if data.get("Headers") is not None:
        import capo_mediatailor.types.__map_of__string

        out["headers"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["Headers"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.mediatailor#AwsServiceRequestConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__integer
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.aws_target_service
    import capo_mediatailor.types.method_type
    import capo_mediatailor.types.runtime_type


class AwsServiceRequestConfiguration(TypedDict, closed=True):
    runtime: "capo_mediatailor.types.runtime_type.RuntimeType"
    """<p>The expression language used to evaluate expressions in the function configuration. The only supported value is <code>JSONata</code>.</p>"""
    output: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>A map of output bindings. Each key is a namespaced output path, such as <code>player_params.device_type</code>. Each value is an expression that MediaTailor evaluates at runtime and can reference the <code>response</code> object from the target service. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-jsonata.html">JSONata expression reference</a> in the <i>MediaTailor User Guide</i>.</p>"""
    method_type: "capo_mediatailor.types.method_type.MethodType"
    """<p>Specifies how the function sends the request to the target service. The value must match what the target service operation requires. Valid values:</p> <ul> <li> <p> <code>GET</code> – Retrieves data from the target service.</p> </li> <li> <p> <code>POST</code> – Submits a request body to the target service.</p> </li> </ul>"""
    request_timeout_milliseconds: "capo_mediatailor.types.__integer.__integer"
    """<p>The maximum time, in milliseconds, that MediaTailor waits for a response from the AWS service. If the call exceeds this timeout, MediaTailor sets the response status code to <code>null</code> and proceeds with output expression evaluation. Valid values: <code>100</code> to <code>2000</code>.</p>"""
    url: "capo_mediatailor.types.__string.__string"
    """<p>An expression that evaluates to the endpoint URL for the target AWS service API operation. Use <code>{%...%}</code> delimiters for dynamic expressions. The URL must correspond to a valid endpoint for the service specified in <code>TargetService</code>. The maximum length after evaluation is 2,048 characters.</p>"""
    body: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>An expression that evaluates to the request body for the AWS service API call. The body must conform to the input format that the target service operation expects. Applies only when the target operation accepts a request body. The maximum size after evaluation is 64 KB.</p>"""
    headers: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>A map of HTTP header names to expression values. MediaTailor evaluates each header value expression at runtime and includes the result in the outbound request to the AWS service. Use this to pass any headers required by the target service operation. You can include a maximum of 50 headers.</p>"""
    target_service: "capo_mediatailor.types.aws_target_service.AwsTargetService"
    """<p>The AWS service to call. Valid value: <code>elemental-inference</code> (AWS Elemental Inference).</p>"""
    target_region: "capo_mediatailor.types.__string.__string"
    """<p>The AWS Region for the target service. Specify a static Region code (for example, <code>us-east-1</code>) or a JSONata expression that resolves to a Region code at runtime (for example, <code>{%inference.region%}</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsServiceRequestConfiguration) -> dict:
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
    out["TargetService"] = value["target_service"]
    out["TargetRegion"] = value["target_region"]
    return out


def deserialize_json(data: dict) -> AwsServiceRequestConfiguration:
    out: AwsServiceRequestConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Runtime") is not None:
        import capo_mediatailor.types.runtime_type

        out["runtime"] = capo_mediatailor.types.runtime_type.deserialize_json(
            data["Runtime"]
        )
    else:
        raise DeserializationError("AwsServiceRequestConfiguration.runtime required")
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
        raise DeserializationError(
            "AwsServiceRequestConfiguration.method_type required"
        )
    if data.get("RequestTimeoutMilliseconds") is not None:
        out["request_timeout_milliseconds"] = data["RequestTimeoutMilliseconds"]
    else:
        raise DeserializationError(
            "AwsServiceRequestConfiguration.request_timeout_milliseconds required"
        )
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        raise DeserializationError("AwsServiceRequestConfiguration.url required")
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    if data.get("Headers") is not None:
        import capo_mediatailor.types.__map_of__string

        out["headers"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["Headers"]
        )
    if data.get("TargetService") is not None:
        out["target_service"] = data["TargetService"]
    else:
        raise DeserializationError(
            "AwsServiceRequestConfiguration.target_service required"
        )
    if data.get("TargetRegion") is not None:
        out["target_region"] = data["TargetRegion"]
    else:
        raise DeserializationError(
            "AwsServiceRequestConfiguration.target_region required"
        )
    return out

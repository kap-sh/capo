"""Generated from Smithy shape ``com.amazonaws.mediatailor#PutFunctionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.aws_service_request_configuration
    import capo_mediatailor.types.concurrent_executor_configuration
    import capo_mediatailor.types.custom_output_configuration
    import capo_mediatailor.types.function_type
    import capo_mediatailor.types.http_request_configuration
    import capo_mediatailor.types.sequential_executor_configuration
    import capo_mediatailor.types.vast_request_configuration


class PutFunctionRequest(TypedDict, closed=True):
    function_id: "capo_mediatailor.types.__string.__string"
    """<p>The identifier of the function. The identifier must be unique within your account.</p>"""
    function_type: "capo_mediatailor.types.function_type.FunctionType"
    """<p>The type of the function, which determines what the function can do at runtime. Valid values:</p> <ul> <li> <p> <code>CUSTOM_OUTPUT</code> – Evaluates expressions and produces output bindings with no external calls.</p> </li> <li> <p> <code>HTTP_REQUEST</code> – Makes an HTTP call to an external service and evaluates output expressions that can reference the response.</p> </li> <li> <p> <code>AWS_SERVICE_REQUEST</code> – Makes an authenticated request to a supported AWS service API and evaluates output expressions that can reference the response.</p> </li> <li> <p> <code>VAST_REQUEST</code> – Calls a VAST endpoint, parses the response as VAST, and makes the parsed ads available to output expressions.</p> </li> <li> <p> <code>SEQUENTIAL_EXECUTOR</code> – Runs a sequence of child functions in order, passing data between steps through temporary data.</p> </li> <li> <p> <code>CONCURRENT_EXECUTOR</code> – Runs a set of child functions in parallel, up to a maximum concurrency, and combines their output when all functions complete.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-types.html">Function types and composition</a> in the <i>MediaTailor User Guide</i>.</p>"""
    description: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>A description of the function.</p>"""
    http_request_configuration: NotRequired[
        "capo_mediatailor.types.http_request_configuration.HttpRequestConfiguration"
    ]
    """<p>The configuration for an <code>HTTP_REQUEST</code> function. Specifies the HTTP method, URL, headers, body, timeout, and output expressions. Required when <code>FunctionType</code> is <code>HTTP_REQUEST</code>.</p>"""
    aws_service_request_configuration: NotRequired[
        "capo_mediatailor.types.aws_service_request_configuration.AwsServiceRequestConfiguration"
    ]
    """<p>The configuration for an <code>AWS_SERVICE_REQUEST</code> function. You must specify this parameter when <code>FunctionType</code> is <code>AWS_SERVICE_REQUEST</code>.</p>"""
    custom_output_configuration: NotRequired[
        "capo_mediatailor.types.custom_output_configuration.CustomOutputConfiguration"
    ]
    """<p>The configuration for a <code>CUSTOM_OUTPUT</code> function. Specifies the runtime and output expressions. Required when <code>FunctionType</code> is <code>CUSTOM_OUTPUT</code>.</p>"""
    concurrent_executor_configuration: NotRequired[
        "capo_mediatailor.types.concurrent_executor_configuration.ConcurrentExecutorConfiguration"
    ]
    """<p>The configuration for a <code>CONCURRENT_EXECUTOR</code> function. Specifies the list of child functions to run in parallel, the maximum concurrency, an optional output block, and a timeout. Required when <code>FunctionType</code> is <code>CONCURRENT_EXECUTOR</code>.</p>"""
    sequential_executor_configuration: NotRequired[
        "capo_mediatailor.types.sequential_executor_configuration.SequentialExecutorConfiguration"
    ]
    """<p>The configuration for a <code>SEQUENTIAL_EXECUTOR</code> function. Specifies the ordered list of child functions to execute, an optional output block, and a timeout. Required when <code>FunctionType</code> is <code>SEQUENTIAL_EXECUTOR</code>.</p>"""
    vast_request_configuration: NotRequired[
        "capo_mediatailor.types.vast_request_configuration.VastRequestConfiguration"
    ]
    """<p>The configuration for a <code>VAST_REQUEST</code> function. Specifies the HTTP method, URL, headers, body, timeout, and output expressions. Required when <code>FunctionType</code> is <code>VAST_REQUEST</code>.</p>"""
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags to assign to the function. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFunctionRequest) -> dict:
    out: dict = {}
    import capo_mediatailor.types.function_type

    out["FunctionType"] = capo_mediatailor.types.function_type.serialize_json(
        value["function_type"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "http_request_configuration" in value:
        import capo_mediatailor.types.http_request_configuration

        out["HttpRequestConfiguration"] = (
            capo_mediatailor.types.http_request_configuration.serialize_json(
                value["http_request_configuration"]
            )
        )
    if "aws_service_request_configuration" in value:
        import capo_mediatailor.types.aws_service_request_configuration

        out["AwsServiceRequestConfiguration"] = (
            capo_mediatailor.types.aws_service_request_configuration.serialize_json(
                value["aws_service_request_configuration"]
            )
        )
    if "custom_output_configuration" in value:
        import capo_mediatailor.types.custom_output_configuration

        out["CustomOutputConfiguration"] = (
            capo_mediatailor.types.custom_output_configuration.serialize_json(
                value["custom_output_configuration"]
            )
        )
    if "concurrent_executor_configuration" in value:
        import capo_mediatailor.types.concurrent_executor_configuration

        out["ConcurrentExecutorConfiguration"] = (
            capo_mediatailor.types.concurrent_executor_configuration.serialize_json(
                value["concurrent_executor_configuration"]
            )
        )
    if "sequential_executor_configuration" in value:
        import capo_mediatailor.types.sequential_executor_configuration

        out["SequentialExecutorConfiguration"] = (
            capo_mediatailor.types.sequential_executor_configuration.serialize_json(
                value["sequential_executor_configuration"]
            )
        )
    if "vast_request_configuration" in value:
        import capo_mediatailor.types.vast_request_configuration

        out["VastRequestConfiguration"] = (
            capo_mediatailor.types.vast_request_configuration.serialize_json(
                value["vast_request_configuration"]
            )
        )
    if "tags" in value:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> PutFunctionRequest:
    out: PutFunctionRequest = {}  # type: ignore[typeddict-item]
    if data.get("FunctionType") is not None:
        import capo_mediatailor.types.function_type

        out["function_type"] = capo_mediatailor.types.function_type.deserialize_json(
            data["FunctionType"]
        )
    else:
        raise DeserializationError("PutFunctionRequest.function_type required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("HttpRequestConfiguration") is not None:
        import capo_mediatailor.types.http_request_configuration

        out["http_request_configuration"] = (
            capo_mediatailor.types.http_request_configuration.deserialize_json(
                data["HttpRequestConfiguration"]
            )
        )
    if data.get("AwsServiceRequestConfiguration") is not None:
        import capo_mediatailor.types.aws_service_request_configuration

        out["aws_service_request_configuration"] = (
            capo_mediatailor.types.aws_service_request_configuration.deserialize_json(
                data["AwsServiceRequestConfiguration"]
            )
        )
    if data.get("CustomOutputConfiguration") is not None:
        import capo_mediatailor.types.custom_output_configuration

        out["custom_output_configuration"] = (
            capo_mediatailor.types.custom_output_configuration.deserialize_json(
                data["CustomOutputConfiguration"]
            )
        )
    if data.get("ConcurrentExecutorConfiguration") is not None:
        import capo_mediatailor.types.concurrent_executor_configuration

        out["concurrent_executor_configuration"] = (
            capo_mediatailor.types.concurrent_executor_configuration.deserialize_json(
                data["ConcurrentExecutorConfiguration"]
            )
        )
    if data.get("SequentialExecutorConfiguration") is not None:
        import capo_mediatailor.types.sequential_executor_configuration

        out["sequential_executor_configuration"] = (
            capo_mediatailor.types.sequential_executor_configuration.deserialize_json(
                data["SequentialExecutorConfiguration"]
            )
        )
    if data.get("VastRequestConfiguration") is not None:
        import capo_mediatailor.types.vast_request_configuration

        out["vast_request_configuration"] = (
            capo_mediatailor.types.vast_request_configuration.deserialize_json(
                data["VastRequestConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_mediatailor.types.__map_of__string

        out["tags"] = capo_mediatailor.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    return out

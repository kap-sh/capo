"""Generated from Smithy shape ``com.amazonaws.mediatailor#GetFunctionResponse``."""

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


class GetFunctionResponse(TypedDict, closed=True):
    function_id: "capo_mediatailor.types.__string.__string"
    """<p>The identifier of the function.</p>"""
    function_type: "capo_mediatailor.types.function_type.FunctionType"
    """<p>The type of the function.</p>"""
    description: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>A description of the function.</p>"""
    http_request_configuration: NotRequired[
        "capo_mediatailor.types.http_request_configuration.HttpRequestConfiguration"
    ]
    """<p>The configuration for an <code>HTTP_REQUEST</code> function.</p>"""
    aws_service_request_configuration: NotRequired[
        "capo_mediatailor.types.aws_service_request_configuration.AwsServiceRequestConfiguration"
    ]
    """<p>The configuration for an <code>AWS_SERVICE_REQUEST</code> function. Specifies the target service, target Region, and request parameters.</p>"""
    custom_output_configuration: NotRequired[
        "capo_mediatailor.types.custom_output_configuration.CustomOutputConfiguration"
    ]
    """<p>The configuration for a <code>CUSTOM_OUTPUT</code> function.</p>"""
    concurrent_executor_configuration: NotRequired[
        "capo_mediatailor.types.concurrent_executor_configuration.ConcurrentExecutorConfiguration"
    ]
    """<p>The configuration for a <code>CONCURRENT_EXECUTOR</code> function.</p>"""
    sequential_executor_configuration: NotRequired[
        "capo_mediatailor.types.sequential_executor_configuration.SequentialExecutorConfiguration"
    ]
    """<p>The configuration for a <code>SEQUENTIAL_EXECUTOR</code> function.</p>"""
    vast_request_configuration: NotRequired[
        "capo_mediatailor.types.vast_request_configuration.VastRequestConfiguration"
    ]
    """<p>The configuration for a <code>VAST_REQUEST</code> function.</p>"""
    tags: NotRequired["capo_mediatailor.types.__map_of__string.__mapOf__string"]
    """<p>The tags assigned to the function. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>"""
    arn: NotRequired["capo_mediatailor.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFunctionResponse) -> dict:
    out: dict = {}
    out["FunctionId"] = value["function_id"]
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
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GetFunctionResponse:
    out: GetFunctionResponse = {}  # type: ignore[typeddict-item]
    if data.get("FunctionId") is not None:
        out["function_id"] = data["FunctionId"]
    else:
        raise DeserializationError("GetFunctionResponse.function_id required")
    if data.get("FunctionType") is not None:
        import capo_mediatailor.types.function_type

        out["function_type"] = capo_mediatailor.types.function_type.deserialize_json(
            data["FunctionType"]
        )
    else:
        raise DeserializationError("GetFunctionResponse.function_type required")
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
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out

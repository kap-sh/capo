"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#UpdateApiDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.api_destination_description
    import capo_cloudwatch_events.types.api_destination_http_method
    import capo_cloudwatch_events.types.api_destination_invocation_rate_limit_per_second
    import capo_cloudwatch_events.types.api_destination_name
    import capo_cloudwatch_events.types.connection_arn
    import capo_cloudwatch_events.types.https_endpoint


class UpdateApiDestinationRequest(TypedDict, closed=True):
    name: "capo_cloudwatch_events.types.api_destination_name.ApiDestinationName"
    """<p>The name of the API destination to update.</p>"""
    description: NotRequired[
        "capo_cloudwatch_events.types.api_destination_description.ApiDestinationDescription"
    ]
    """<p>The name of the API destination to update.</p>"""
    connection_arn: NotRequired[
        "capo_cloudwatch_events.types.connection_arn.ConnectionArn"
    ]
    """<p>The ARN of the connection to use for the API destination.</p>"""
    invocation_endpoint: NotRequired[
        "capo_cloudwatch_events.types.https_endpoint.HttpsEndpoint"
    ]
    """<p>The URL to the endpoint to use for the API destination.</p>"""
    http_method: NotRequired[
        "capo_cloudwatch_events.types.api_destination_http_method.ApiDestinationHttpMethod"
    ]
    """<p>The method to use for the API destination.</p>"""
    invocation_rate_limit_per_second: NotRequired[
        "capo_cloudwatch_events.types.api_destination_invocation_rate_limit_per_second.ApiDestinationInvocationRateLimitPerSecond"
    ]
    """<p>The maximum number of invocations per second to send to the API destination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateApiDestinationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "connection_arn" in value:
        out["ConnectionArn"] = value["connection_arn"]
    if "invocation_endpoint" in value:
        out["InvocationEndpoint"] = value["invocation_endpoint"]
    if "http_method" in value:
        import capo_cloudwatch_events.types.api_destination_http_method

        out["HttpMethod"] = (
            capo_cloudwatch_events.types.api_destination_http_method.serialize_aws_json_1_1(
                value["http_method"]
            )
        )
    if "invocation_rate_limit_per_second" in value:
        out["InvocationRateLimitPerSecond"] = value["invocation_rate_limit_per_second"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateApiDestinationRequest:
    out: UpdateApiDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ConnectionArn") is not None:
        out["connection_arn"] = data["ConnectionArn"]
    if data.get("InvocationEndpoint") is not None:
        out["invocation_endpoint"] = data["InvocationEndpoint"]
    if data.get("HttpMethod") is not None:
        import capo_cloudwatch_events.types.api_destination_http_method

        out["http_method"] = (
            capo_cloudwatch_events.types.api_destination_http_method.deserialize_aws_json_1_1(
                data["HttpMethod"]
            )
        )
    if data.get("InvocationRateLimitPerSecond") is not None:
        out["invocation_rate_limit_per_second"] = data["InvocationRateLimitPerSecond"]
    return out

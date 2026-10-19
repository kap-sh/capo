"""Generated from Smithy shape ``com.amazonaws.eventbridge#CreateApiDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.api_destination_description
    import capo_eventbridge.types.api_destination_http_method
    import capo_eventbridge.types.api_destination_invocation_rate_limit_per_second
    import capo_eventbridge.types.api_destination_name
    import capo_eventbridge.types.connection_arn
    import capo_eventbridge.types.https_endpoint


class CreateApiDestinationRequest(TypedDict, closed=True):
    name: "capo_eventbridge.types.api_destination_name.ApiDestinationName"
    """<p>The name for the API destination to create.</p>"""
    description: NotRequired[
        "capo_eventbridge.types.api_destination_description.ApiDestinationDescription"
    ]
    """<p>A description for the API destination to create.</p>"""
    connection_arn: "capo_eventbridge.types.connection_arn.ConnectionArn"
    """<p>The ARN of the connection to use for the API destination. The destination endpoint must support the authorization type specified for the connection.</p>"""
    invocation_endpoint: "capo_eventbridge.types.https_endpoint.HttpsEndpoint"
    """<p>The URL to the HTTP invocation endpoint for the API destination.</p>"""
    http_method: (
        "capo_eventbridge.types.api_destination_http_method.ApiDestinationHttpMethod"
    )
    """<p>The method to use for the request to the HTTP invocation endpoint.</p>"""
    invocation_rate_limit_per_second: NotRequired[
        "capo_eventbridge.types.api_destination_invocation_rate_limit_per_second.ApiDestinationInvocationRateLimitPerSecond"
    ]
    """<p>The maximum number of requests per second to send to the HTTP invocation endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateApiDestinationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["ConnectionArn"] = value["connection_arn"]
    out["InvocationEndpoint"] = value["invocation_endpoint"]
    import capo_eventbridge.types.api_destination_http_method

    out["HttpMethod"] = (
        capo_eventbridge.types.api_destination_http_method.serialize_aws_json_1_1(
            value["http_method"]
        )
    )
    if "invocation_rate_limit_per_second" in value:
        out["InvocationRateLimitPerSecond"] = value["invocation_rate_limit_per_second"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateApiDestinationRequest:
    out: CreateApiDestinationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ConnectionArn") is not None:
        out["connection_arn"] = data["ConnectionArn"]
    else:
        out["connection_arn"] = ""
    if data.get("InvocationEndpoint") is not None:
        out["invocation_endpoint"] = data["InvocationEndpoint"]
    else:
        out["invocation_endpoint"] = ""
    if data.get("HttpMethod") is not None:
        import capo_eventbridge.types.api_destination_http_method

        out["http_method"] = (
            capo_eventbridge.types.api_destination_http_method.deserialize_aws_json_1_1(
                data["HttpMethod"]
            )
        )
    else:
        import typing

        out["http_method"] = typing.cast(
            "capo_eventbridge.types.api_destination_http_method.ApiDestinationHttpMethod",
            "",
        )
    if data.get("InvocationRateLimitPerSecond") is not None:
        out["invocation_rate_limit_per_second"] = data["InvocationRateLimitPerSecond"]
    return out

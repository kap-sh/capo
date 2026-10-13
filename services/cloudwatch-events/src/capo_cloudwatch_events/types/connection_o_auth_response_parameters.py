"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ConnectionOAuthResponseParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.connection_http_parameters
    import capo_cloudwatch_events.types.connection_o_auth_client_response_parameters
    import capo_cloudwatch_events.types.connection_o_auth_http_method
    import capo_cloudwatch_events.types.https_endpoint


class ConnectionOAuthResponseParameters(TypedDict, closed=True):
    client_parameters: NotRequired[
        "capo_cloudwatch_events.types.connection_o_auth_client_response_parameters.ConnectionOAuthClientResponseParameters"
    ]
    """<p>A <code>ConnectionOAuthClientResponseParameters</code> object that contains details about the client parameters returned when OAuth is specified as the authorization type.</p>"""
    authorization_endpoint: NotRequired[
        "capo_cloudwatch_events.types.https_endpoint.HttpsEndpoint"
    ]
    """<p>The URL to the HTTP endpoint that authorized the request.</p>"""
    http_method: NotRequired[
        "capo_cloudwatch_events.types.connection_o_auth_http_method.ConnectionOAuthHttpMethod"
    ]
    """<p>The method used to connect to the HTTP endpoint.</p>"""
    o_auth_http_parameters: NotRequired[
        "capo_cloudwatch_events.types.connection_http_parameters.ConnectionHttpParameters"
    ]
    """<p>The additional HTTP parameters used for the OAuth authorization request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionOAuthResponseParameters) -> dict:
    out: dict = {}
    if "client_parameters" in value:
        import capo_cloudwatch_events.types.connection_o_auth_client_response_parameters

        out["ClientParameters"] = (
            capo_cloudwatch_events.types.connection_o_auth_client_response_parameters.serialize_aws_json_1_1(
                value["client_parameters"]
            )
        )
    if "authorization_endpoint" in value:
        out["AuthorizationEndpoint"] = value["authorization_endpoint"]
    if "http_method" in value:
        import capo_cloudwatch_events.types.connection_o_auth_http_method

        out["HttpMethod"] = (
            capo_cloudwatch_events.types.connection_o_auth_http_method.serialize_aws_json_1_1(
                value["http_method"]
            )
        )
    if "o_auth_http_parameters" in value:
        import capo_cloudwatch_events.types.connection_http_parameters

        out["OAuthHttpParameters"] = (
            capo_cloudwatch_events.types.connection_http_parameters.serialize_aws_json_1_1(
                value["o_auth_http_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionOAuthResponseParameters:
    out: ConnectionOAuthResponseParameters = {}  # type: ignore[typeddict-item]
    if data.get("ClientParameters") is not None:
        import capo_cloudwatch_events.types.connection_o_auth_client_response_parameters

        out["client_parameters"] = (
            capo_cloudwatch_events.types.connection_o_auth_client_response_parameters.deserialize_aws_json_1_1(
                data["ClientParameters"]
            )
        )
    if data.get("AuthorizationEndpoint") is not None:
        out["authorization_endpoint"] = data["AuthorizationEndpoint"]
    if data.get("HttpMethod") is not None:
        import capo_cloudwatch_events.types.connection_o_auth_http_method

        out["http_method"] = (
            capo_cloudwatch_events.types.connection_o_auth_http_method.deserialize_aws_json_1_1(
                data["HttpMethod"]
            )
        )
    if data.get("OAuthHttpParameters") is not None:
        import capo_cloudwatch_events.types.connection_http_parameters

        out["o_auth_http_parameters"] = (
            capo_cloudwatch_events.types.connection_http_parameters.deserialize_aws_json_1_1(
                data["OAuthHttpParameters"]
            )
        )
    return out


def redact_sensitive(value: ConnectionOAuthResponseParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "o_auth_http_parameters" in value:
        import capo_cloudwatch_events.types.connection_http_parameters

        out["o_auth_http_parameters"] = (
            capo_cloudwatch_events.types.connection_http_parameters.redact_sensitive(
                value["o_auth_http_parameters"]
            )
        )
    return out

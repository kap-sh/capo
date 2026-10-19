"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#CreateConnectionOAuthRequestParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.connection_http_parameters
    import capo_cloudwatch_events.types.connection_o_auth_http_method
    import capo_cloudwatch_events.types.create_connection_o_auth_client_request_parameters
    import capo_cloudwatch_events.types.https_endpoint


class CreateConnectionOAuthRequestParameters(TypedDict, closed=True):
    client_parameters: "capo_cloudwatch_events.types.create_connection_o_auth_client_request_parameters.CreateConnectionOAuthClientRequestParameters"
    """<p>A <code>CreateConnectionOAuthClientRequestParameters</code> object that contains the client parameters for OAuth authorization.</p>"""
    authorization_endpoint: "capo_cloudwatch_events.types.https_endpoint.HttpsEndpoint"
    """<p>The URL to the authorization endpoint when OAuth is specified as the authorization type.</p>"""
    http_method: "capo_cloudwatch_events.types.connection_o_auth_http_method.ConnectionOAuthHttpMethod"
    """<p>The method to use for the authorization request.</p>"""
    o_auth_http_parameters: NotRequired[
        "capo_cloudwatch_events.types.connection_http_parameters.ConnectionHttpParameters"
    ]
    """<p>A <code>ConnectionHttpParameters</code> object that contains details about the additional parameters to use for the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionOAuthRequestParameters) -> dict:
    out: dict = {}
    import capo_cloudwatch_events.types.create_connection_o_auth_client_request_parameters

    out["ClientParameters"] = (
        capo_cloudwatch_events.types.create_connection_o_auth_client_request_parameters.serialize_aws_json_1_1(
            value["client_parameters"]
        )
    )
    out["AuthorizationEndpoint"] = value["authorization_endpoint"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionOAuthRequestParameters:
    out: CreateConnectionOAuthRequestParameters = {}  # type: ignore[typeddict-item]
    if data.get("ClientParameters") is not None:
        import capo_cloudwatch_events.types.create_connection_o_auth_client_request_parameters

        out["client_parameters"] = (
            capo_cloudwatch_events.types.create_connection_o_auth_client_request_parameters.deserialize_aws_json_1_1(
                data["ClientParameters"]
            )
        )
    else:
        raise DeserializationError(
            "CreateConnectionOAuthRequestParameters.client_parameters required"
        )
    if data.get("AuthorizationEndpoint") is not None:
        out["authorization_endpoint"] = data["AuthorizationEndpoint"]
    else:
        out["authorization_endpoint"] = ""
    if data.get("HttpMethod") is not None:
        import capo_cloudwatch_events.types.connection_o_auth_http_method

        out["http_method"] = (
            capo_cloudwatch_events.types.connection_o_auth_http_method.deserialize_aws_json_1_1(
                data["HttpMethod"]
            )
        )
    else:
        import typing

        out["http_method"] = typing.cast(
            "capo_cloudwatch_events.types.connection_o_auth_http_method.ConnectionOAuthHttpMethod",
            "",
        )
    if data.get("OAuthHttpParameters") is not None:
        import capo_cloudwatch_events.types.connection_http_parameters

        out["o_auth_http_parameters"] = (
            capo_cloudwatch_events.types.connection_http_parameters.deserialize_aws_json_1_1(
                data["OAuthHttpParameters"]
            )
        )
    return out


def redact_sensitive(value: CreateConnectionOAuthRequestParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_parameters" in value:
        import capo_cloudwatch_events.types.create_connection_o_auth_client_request_parameters

        out["client_parameters"] = (
            capo_cloudwatch_events.types.create_connection_o_auth_client_request_parameters.redact_sensitive(
                value["client_parameters"]
            )
        )
    if "o_auth_http_parameters" in value:
        import capo_cloudwatch_events.types.connection_http_parameters

        out["o_auth_http_parameters"] = (
            capo_cloudwatch_events.types.connection_http_parameters.redact_sensitive(
                value["o_auth_http_parameters"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#CreateConnectionAuthRequestParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.connection_http_parameters
    import capo_cloudwatch_events.types.create_connection_api_key_auth_request_parameters
    import capo_cloudwatch_events.types.create_connection_basic_auth_request_parameters
    import capo_cloudwatch_events.types.create_connection_o_auth_request_parameters


class CreateConnectionAuthRequestParameters(TypedDict, closed=True):
    basic_auth_parameters: NotRequired[
        "capo_cloudwatch_events.types.create_connection_basic_auth_request_parameters.CreateConnectionBasicAuthRequestParameters"
    ]
    """<p>A <code>CreateConnectionBasicAuthRequestParameters</code> object that contains the Basic authorization parameters to use for the connection.</p>"""
    o_auth_parameters: NotRequired[
        "capo_cloudwatch_events.types.create_connection_o_auth_request_parameters.CreateConnectionOAuthRequestParameters"
    ]
    """<p>A <code>CreateConnectionOAuthRequestParameters</code> object that contains the OAuth authorization parameters to use for the connection.</p>"""
    api_key_auth_parameters: NotRequired[
        "capo_cloudwatch_events.types.create_connection_api_key_auth_request_parameters.CreateConnectionApiKeyAuthRequestParameters"
    ]
    """<p>A <code>CreateConnectionApiKeyAuthRequestParameters</code> object that contains the API key authorization parameters to use for the connection.</p>"""
    invocation_http_parameters: NotRequired[
        "capo_cloudwatch_events.types.connection_http_parameters.ConnectionHttpParameters"
    ]
    """<p>A <code>ConnectionHttpParameters</code> object that contains the API key authorization parameters to use for the connection. Note that if you include additional parameters for the target of a rule via <code>HttpParameters</code>, including query strings, the parameters added for the connection take precedence.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionAuthRequestParameters) -> dict:
    out: dict = {}
    if "basic_auth_parameters" in value:
        import capo_cloudwatch_events.types.create_connection_basic_auth_request_parameters

        out["BasicAuthParameters"] = (
            capo_cloudwatch_events.types.create_connection_basic_auth_request_parameters.serialize_aws_json_1_1(
                value["basic_auth_parameters"]
            )
        )
    if "o_auth_parameters" in value:
        import capo_cloudwatch_events.types.create_connection_o_auth_request_parameters

        out["OAuthParameters"] = (
            capo_cloudwatch_events.types.create_connection_o_auth_request_parameters.serialize_aws_json_1_1(
                value["o_auth_parameters"]
            )
        )
    if "api_key_auth_parameters" in value:
        import capo_cloudwatch_events.types.create_connection_api_key_auth_request_parameters

        out["ApiKeyAuthParameters"] = (
            capo_cloudwatch_events.types.create_connection_api_key_auth_request_parameters.serialize_aws_json_1_1(
                value["api_key_auth_parameters"]
            )
        )
    if "invocation_http_parameters" in value:
        import capo_cloudwatch_events.types.connection_http_parameters

        out["InvocationHttpParameters"] = (
            capo_cloudwatch_events.types.connection_http_parameters.serialize_aws_json_1_1(
                value["invocation_http_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionAuthRequestParameters:
    out: CreateConnectionAuthRequestParameters = {}  # type: ignore[typeddict-item]
    if data.get("BasicAuthParameters") is not None:
        import capo_cloudwatch_events.types.create_connection_basic_auth_request_parameters

        out["basic_auth_parameters"] = (
            capo_cloudwatch_events.types.create_connection_basic_auth_request_parameters.deserialize_aws_json_1_1(
                data["BasicAuthParameters"]
            )
        )
    if data.get("OAuthParameters") is not None:
        import capo_cloudwatch_events.types.create_connection_o_auth_request_parameters

        out["o_auth_parameters"] = (
            capo_cloudwatch_events.types.create_connection_o_auth_request_parameters.deserialize_aws_json_1_1(
                data["OAuthParameters"]
            )
        )
    if data.get("ApiKeyAuthParameters") is not None:
        import capo_cloudwatch_events.types.create_connection_api_key_auth_request_parameters

        out["api_key_auth_parameters"] = (
            capo_cloudwatch_events.types.create_connection_api_key_auth_request_parameters.deserialize_aws_json_1_1(
                data["ApiKeyAuthParameters"]
            )
        )
    if data.get("InvocationHttpParameters") is not None:
        import capo_cloudwatch_events.types.connection_http_parameters

        out["invocation_http_parameters"] = (
            capo_cloudwatch_events.types.connection_http_parameters.deserialize_aws_json_1_1(
                data["InvocationHttpParameters"]
            )
        )
    return out


def redact_sensitive(value: CreateConnectionAuthRequestParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "basic_auth_parameters" in value:
        import capo_cloudwatch_events.types.create_connection_basic_auth_request_parameters

        out["basic_auth_parameters"] = (
            capo_cloudwatch_events.types.create_connection_basic_auth_request_parameters.redact_sensitive(
                value["basic_auth_parameters"]
            )
        )
    if "o_auth_parameters" in value:
        import capo_cloudwatch_events.types.create_connection_o_auth_request_parameters

        out["o_auth_parameters"] = (
            capo_cloudwatch_events.types.create_connection_o_auth_request_parameters.redact_sensitive(
                value["o_auth_parameters"]
            )
        )
    if "api_key_auth_parameters" in value:
        import capo_cloudwatch_events.types.create_connection_api_key_auth_request_parameters

        out["api_key_auth_parameters"] = (
            capo_cloudwatch_events.types.create_connection_api_key_auth_request_parameters.redact_sensitive(
                value["api_key_auth_parameters"]
            )
        )
    if "invocation_http_parameters" in value:
        import capo_cloudwatch_events.types.connection_http_parameters

        out["invocation_http_parameters"] = (
            capo_cloudwatch_events.types.connection_http_parameters.redact_sensitive(
                value["invocation_http_parameters"]
            )
        )
    return out

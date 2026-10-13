"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#UpdateConnectionAuthRequestParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.connection_http_parameters
    import capo_cloudwatch_events.types.update_connection_api_key_auth_request_parameters
    import capo_cloudwatch_events.types.update_connection_basic_auth_request_parameters
    import capo_cloudwatch_events.types.update_connection_o_auth_request_parameters


class UpdateConnectionAuthRequestParameters(TypedDict, closed=True):
    basic_auth_parameters: NotRequired[
        "capo_cloudwatch_events.types.update_connection_basic_auth_request_parameters.UpdateConnectionBasicAuthRequestParameters"
    ]
    """<p>A <code>UpdateConnectionBasicAuthRequestParameters</code> object that contains the authorization parameters for Basic authorization.</p>"""
    o_auth_parameters: NotRequired[
        "capo_cloudwatch_events.types.update_connection_o_auth_request_parameters.UpdateConnectionOAuthRequestParameters"
    ]
    """<p>A <code>UpdateConnectionOAuthRequestParameters</code> object that contains the authorization parameters for OAuth authorization.</p>"""
    api_key_auth_parameters: NotRequired[
        "capo_cloudwatch_events.types.update_connection_api_key_auth_request_parameters.UpdateConnectionApiKeyAuthRequestParameters"
    ]
    """<p>A <code>UpdateConnectionApiKeyAuthRequestParameters</code> object that contains the authorization parameters for API key authorization.</p>"""
    invocation_http_parameters: NotRequired[
        "capo_cloudwatch_events.types.connection_http_parameters.ConnectionHttpParameters"
    ]
    """<p>A <code>ConnectionHttpParameters</code> object that contains the additional parameters to use for the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectionAuthRequestParameters) -> dict:
    out: dict = {}
    if "basic_auth_parameters" in value:
        import capo_cloudwatch_events.types.update_connection_basic_auth_request_parameters

        out["BasicAuthParameters"] = (
            capo_cloudwatch_events.types.update_connection_basic_auth_request_parameters.serialize_aws_json_1_1(
                value["basic_auth_parameters"]
            )
        )
    if "o_auth_parameters" in value:
        import capo_cloudwatch_events.types.update_connection_o_auth_request_parameters

        out["OAuthParameters"] = (
            capo_cloudwatch_events.types.update_connection_o_auth_request_parameters.serialize_aws_json_1_1(
                value["o_auth_parameters"]
            )
        )
    if "api_key_auth_parameters" in value:
        import capo_cloudwatch_events.types.update_connection_api_key_auth_request_parameters

        out["ApiKeyAuthParameters"] = (
            capo_cloudwatch_events.types.update_connection_api_key_auth_request_parameters.serialize_aws_json_1_1(
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


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectionAuthRequestParameters:
    out: UpdateConnectionAuthRequestParameters = {}  # type: ignore[typeddict-item]
    if data.get("BasicAuthParameters") is not None:
        import capo_cloudwatch_events.types.update_connection_basic_auth_request_parameters

        out["basic_auth_parameters"] = (
            capo_cloudwatch_events.types.update_connection_basic_auth_request_parameters.deserialize_aws_json_1_1(
                data["BasicAuthParameters"]
            )
        )
    if data.get("OAuthParameters") is not None:
        import capo_cloudwatch_events.types.update_connection_o_auth_request_parameters

        out["o_auth_parameters"] = (
            capo_cloudwatch_events.types.update_connection_o_auth_request_parameters.deserialize_aws_json_1_1(
                data["OAuthParameters"]
            )
        )
    if data.get("ApiKeyAuthParameters") is not None:
        import capo_cloudwatch_events.types.update_connection_api_key_auth_request_parameters

        out["api_key_auth_parameters"] = (
            capo_cloudwatch_events.types.update_connection_api_key_auth_request_parameters.deserialize_aws_json_1_1(
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


def redact_sensitive(value: UpdateConnectionAuthRequestParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "basic_auth_parameters" in value:
        import capo_cloudwatch_events.types.update_connection_basic_auth_request_parameters

        out["basic_auth_parameters"] = (
            capo_cloudwatch_events.types.update_connection_basic_auth_request_parameters.redact_sensitive(
                value["basic_auth_parameters"]
            )
        )
    if "o_auth_parameters" in value:
        import capo_cloudwatch_events.types.update_connection_o_auth_request_parameters

        out["o_auth_parameters"] = (
            capo_cloudwatch_events.types.update_connection_o_auth_request_parameters.redact_sensitive(
                value["o_auth_parameters"]
            )
        )
    if "api_key_auth_parameters" in value:
        import capo_cloudwatch_events.types.update_connection_api_key_auth_request_parameters

        out["api_key_auth_parameters"] = (
            capo_cloudwatch_events.types.update_connection_api_key_auth_request_parameters.redact_sensitive(
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

"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectionAuthResponseParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.connection_api_key_auth_response_parameters
    import capo_eventbridge.types.connection_basic_auth_response_parameters
    import capo_eventbridge.types.connection_http_parameters
    import capo_eventbridge.types.connection_o_auth_response_parameters
    import capo_eventbridge.types.describe_connection_connectivity_parameters


class ConnectionAuthResponseParameters(TypedDict, closed=True):
    basic_auth_parameters: NotRequired[
        "capo_eventbridge.types.connection_basic_auth_response_parameters.ConnectionBasicAuthResponseParameters"
    ]
    """<p>The authorization parameters for Basic authorization.</p>"""
    o_auth_parameters: NotRequired[
        "capo_eventbridge.types.connection_o_auth_response_parameters.ConnectionOAuthResponseParameters"
    ]
    """<p>The OAuth parameters to use for authorization.</p>"""
    api_key_auth_parameters: NotRequired[
        "capo_eventbridge.types.connection_api_key_auth_response_parameters.ConnectionApiKeyAuthResponseParameters"
    ]
    """<p>The API Key parameters to use for authorization.</p>"""
    invocation_http_parameters: NotRequired[
        "capo_eventbridge.types.connection_http_parameters.ConnectionHttpParameters"
    ]
    """<p>Additional parameters for the connection that are passed through with every invocation to the HTTP endpoint.</p>"""
    connectivity_parameters: NotRequired[
        "capo_eventbridge.types.describe_connection_connectivity_parameters.DescribeConnectionConnectivityParameters"
    ]
    """<p>For private OAuth authentication endpoints. The parameters EventBridge uses to authenticate against the endpoint.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-target-connection-auth.html">Authorization methods for connections</a> in the <i> <i>Amazon EventBridge User Guide</i> </i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAuthResponseParameters) -> dict:
    out: dict = {}
    if "basic_auth_parameters" in value:
        import capo_eventbridge.types.connection_basic_auth_response_parameters

        out["BasicAuthParameters"] = (
            capo_eventbridge.types.connection_basic_auth_response_parameters.serialize_aws_json_1_1(
                value["basic_auth_parameters"]
            )
        )
    if "o_auth_parameters" in value:
        import capo_eventbridge.types.connection_o_auth_response_parameters

        out["OAuthParameters"] = (
            capo_eventbridge.types.connection_o_auth_response_parameters.serialize_aws_json_1_1(
                value["o_auth_parameters"]
            )
        )
    if "api_key_auth_parameters" in value:
        import capo_eventbridge.types.connection_api_key_auth_response_parameters

        out["ApiKeyAuthParameters"] = (
            capo_eventbridge.types.connection_api_key_auth_response_parameters.serialize_aws_json_1_1(
                value["api_key_auth_parameters"]
            )
        )
    if "invocation_http_parameters" in value:
        import capo_eventbridge.types.connection_http_parameters

        out["InvocationHttpParameters"] = (
            capo_eventbridge.types.connection_http_parameters.serialize_aws_json_1_1(
                value["invocation_http_parameters"]
            )
        )
    if "connectivity_parameters" in value:
        import capo_eventbridge.types.describe_connection_connectivity_parameters

        out["ConnectivityParameters"] = (
            capo_eventbridge.types.describe_connection_connectivity_parameters.serialize_aws_json_1_1(
                value["connectivity_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionAuthResponseParameters:
    out: ConnectionAuthResponseParameters = {}  # type: ignore[typeddict-item]
    if data.get("BasicAuthParameters") is not None:
        import capo_eventbridge.types.connection_basic_auth_response_parameters

        out["basic_auth_parameters"] = (
            capo_eventbridge.types.connection_basic_auth_response_parameters.deserialize_aws_json_1_1(
                data["BasicAuthParameters"]
            )
        )
    if data.get("OAuthParameters") is not None:
        import capo_eventbridge.types.connection_o_auth_response_parameters

        out["o_auth_parameters"] = (
            capo_eventbridge.types.connection_o_auth_response_parameters.deserialize_aws_json_1_1(
                data["OAuthParameters"]
            )
        )
    if data.get("ApiKeyAuthParameters") is not None:
        import capo_eventbridge.types.connection_api_key_auth_response_parameters

        out["api_key_auth_parameters"] = (
            capo_eventbridge.types.connection_api_key_auth_response_parameters.deserialize_aws_json_1_1(
                data["ApiKeyAuthParameters"]
            )
        )
    if data.get("InvocationHttpParameters") is not None:
        import capo_eventbridge.types.connection_http_parameters

        out["invocation_http_parameters"] = (
            capo_eventbridge.types.connection_http_parameters.deserialize_aws_json_1_1(
                data["InvocationHttpParameters"]
            )
        )
    if data.get("ConnectivityParameters") is not None:
        import capo_eventbridge.types.describe_connection_connectivity_parameters

        out["connectivity_parameters"] = (
            capo_eventbridge.types.describe_connection_connectivity_parameters.deserialize_aws_json_1_1(
                data["ConnectivityParameters"]
            )
        )
    return out

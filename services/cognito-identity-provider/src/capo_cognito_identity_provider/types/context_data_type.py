"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ContextDataType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.http_header_list
    import capo_cognito_identity_provider.types.string_type


class ContextDataType(TypedDict, closed=True):
    ip_address: "capo_cognito_identity_provider.types.string_type.StringType"
    """<p>The source IP address of your user's device.</p>"""
    server_name: "capo_cognito_identity_provider.types.string_type.StringType"
    """<p>The name of your application's service endpoint.</p>"""
    server_path: "capo_cognito_identity_provider.types.string_type.StringType"
    """<p>The path of your application's service endpoint.</p>"""
    http_headers: "capo_cognito_identity_provider.types.http_header_list.HttpHeaderList"
    """<p>The HTTP headers from your user's authentication request.</p>"""
    encoded_data: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    """<p>Encoded device-fingerprint details that your app collected with the Amazon Cognito context data collection library. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html#user-pool-settings-adaptive-authentication-device-fingerprint">Adding user device and session data to API requests</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContextDataType) -> dict:
    out: dict = {}
    out["IpAddress"] = value["ip_address"]
    out["ServerName"] = value["server_name"]
    out["ServerPath"] = value["server_path"]
    import capo_cognito_identity_provider.types.http_header_list

    out["HttpHeaders"] = (
        capo_cognito_identity_provider.types.http_header_list.serialize_aws_json_1_1(
            value["http_headers"]
        )
    )
    if "encoded_data" in value:
        out["EncodedData"] = value["encoded_data"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContextDataType:
    out: ContextDataType = {}  # type: ignore[typeddict-item]
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    else:
        raise DeserializationError("ContextDataType.ip_address required")
    if data.get("ServerName") is not None:
        out["server_name"] = data["ServerName"]
    else:
        raise DeserializationError("ContextDataType.server_name required")
    if data.get("ServerPath") is not None:
        out["server_path"] = data["ServerPath"]
    else:
        raise DeserializationError("ContextDataType.server_path required")
    if data.get("HttpHeaders") is not None:
        import capo_cognito_identity_provider.types.http_header_list

        out["http_headers"] = (
            capo_cognito_identity_provider.types.http_header_list.deserialize_aws_json_1_1(
                data["HttpHeaders"]
            )
        )
    else:
        raise DeserializationError("ContextDataType.http_headers required")
    if data.get("EncodedData") is not None:
        out["encoded_data"] = data["EncodedData"]
    return out

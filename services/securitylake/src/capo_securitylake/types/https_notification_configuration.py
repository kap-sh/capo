"""Generated from Smithy shape ``com.amazonaws.securitylake#HttpsNotificationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_securitylake.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securitylake.types.http_method
    import capo_securitylake.types.role_arn


class HttpsNotificationConfiguration(TypedDict, closed=True):
    endpoint: "str"
    """<p>The subscription endpoint in Security Lake. If you prefer notification with an HTTPs endpoint, populate this field.</p>"""
    authorization_api_key_name: NotRequired["str"]
    """<p>The key name for the notification subscription.</p>"""
    authorization_api_key_value: NotRequired["str"]
    """<p>The key value for the notification subscription.</p>"""
    http_method: NotRequired["capo_securitylake.types.http_method.HttpMethod"]
    """<p>The HTTPS method used for the notification subscription.</p>"""
    target_role_arn: "capo_securitylake.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the EventBridge API destinations IAM role that you created. For more information about ARNs and how to use them in policies, see <a href="https://docs.aws.amazon.com//security-lake/latest/userguide/subscriber-data-access.html">Managing data access</a> and <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/security-iam-awsmanpol.html">Amazon Web Services Managed Policies</a> in the <i>Amazon Security Lake User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpsNotificationConfiguration) -> dict:
    out: dict = {}
    out["endpoint"] = value["endpoint"]
    if "authorization_api_key_name" in value:
        out["authorizationApiKeyName"] = value["authorization_api_key_name"]
    if "authorization_api_key_value" in value:
        out["authorizationApiKeyValue"] = value["authorization_api_key_value"]
    if "http_method" in value:
        import capo_securitylake.types.http_method

        out["httpMethod"] = capo_securitylake.types.http_method.serialize_json(
            value["http_method"]
        )
    out["targetRoleArn"] = value["target_role_arn"]
    return out


def deserialize_json(data: dict) -> HttpsNotificationConfiguration:
    out: HttpsNotificationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("HttpsNotificationConfiguration.endpoint required")
    if data.get("authorizationApiKeyName") is not None:
        out["authorization_api_key_name"] = data["authorizationApiKeyName"]
    if data.get("authorizationApiKeyValue") is not None:
        out["authorization_api_key_value"] = data["authorizationApiKeyValue"]
    if data.get("httpMethod") is not None:
        import capo_securitylake.types.http_method

        out["http_method"] = capo_securitylake.types.http_method.deserialize_json(
            data["httpMethod"]
        )
    if data.get("targetRoleArn") is not None:
        out["target_role_arn"] = data["targetRoleArn"]
    else:
        raise DeserializationError(
            "HttpsNotificationConfiguration.target_role_arn required"
        )
    return out

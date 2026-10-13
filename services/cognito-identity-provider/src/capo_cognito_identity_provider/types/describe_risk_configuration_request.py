"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DescribeRiskConfigurationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class DescribeRiskConfigurationRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool with the risk configuration that you want to inspect. You can apply default risk configuration at the user pool level and further customize it from user pool defaults at the app-client level. Specify <code>ClientId</code> to inspect client-level configuration, or <code>UserPoolId</code> to inspect pool-level configuration.</p>"""
    client_id: NotRequired[
        "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    ]
    """<p>The ID of the app client with the risk configuration that you want to inspect. You can apply default risk configuration at the user pool level and further customize it from user pool defaults at the app-client level. Specify <code>ClientId</code> to inspect client-level configuration, or <code>UserPoolId</code> to inspect pool-level configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRiskConfigurationRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRiskConfigurationRequest:
    out: DescribeRiskConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError(
            "DescribeRiskConfigurationRequest.user_pool_id required"
        )
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    return out


def redact_sensitive(value: DescribeRiskConfigurationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    return out

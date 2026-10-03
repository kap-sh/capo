"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateUserPoolDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.custom_domain_config_type
    import capo_cognito_identity_provider.types.domain_type
    import capo_cognito_identity_provider.types.routing_type
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.wrapped_integer_type


class UpdateUserPoolDomainRequest(TypedDict, closed=True):
    domain: "capo_cognito_identity_provider.types.domain_type.DomainType"
    """<p>The name of the domain that you want to update. For custom domains, this is the fully-qualified domain name, for example <code>auth.example.com</code>. For prefix domains, this is the prefix alone, such as <code>myprefix</code>.</p>"""
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that is associated with the domain you're updating.</p>"""
    managed_login_version: NotRequired[
        "capo_cognito_identity_provider.types.wrapped_integer_type.WrappedIntegerType"
    ]
    """<p>A version number that indicates the state of managed login for your domain. Version <code>1</code> is hosted UI (classic). Version <code>2</code> is the newer managed login with the branding editor. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html">Managed login</a>.</p>"""
    custom_domain_config: NotRequired[
        "capo_cognito_identity_provider.types.custom_domain_config_type.CustomDomainConfigType"
    ]
    """<p>The configuration for a custom domain that hosts managed login for your application. In an <code>UpdateUserPoolDomain</code> request, this parameter specifies an SSL certificate for the managed login hosted webserver. The certificate must be an ACM ARN in <code>us-east-1</code>.</p> <p>When you create a custom domain, the passkey RP ID defaults to the custom domain. If you had a prefix domain active, this will cause passkey integration for your prefix domain to stop working due to a mismatch in RP ID. To keep the prefix domain passkey integration working, you can explicitly set RP ID to the prefix domain.</p>"""
    routing: NotRequired[
        "capo_cognito_identity_provider.types.routing_type.RoutingType"
    ]
    """<p>The routing configuration for the user pool domain. Specifies failover settings for multi-region deployments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserPoolDomainRequest) -> dict:
    out: dict = {}
    out["Domain"] = value["domain"]
    out["UserPoolId"] = value["user_pool_id"]
    if "managed_login_version" in value:
        out["ManagedLoginVersion"] = value["managed_login_version"]
    if "custom_domain_config" in value:
        import capo_cognito_identity_provider.types.custom_domain_config_type

        out["CustomDomainConfig"] = (
            capo_cognito_identity_provider.types.custom_domain_config_type.serialize_aws_json_1_1(
                value["custom_domain_config"]
            )
        )
    if "routing" in value:
        import capo_cognito_identity_provider.types.routing_type

        out["Routing"] = (
            capo_cognito_identity_provider.types.routing_type.serialize_aws_json_1_1(
                value["routing"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserPoolDomainRequest:
    out: UpdateUserPoolDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    else:
        raise DeserializationError("UpdateUserPoolDomainRequest.domain required")
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("UpdateUserPoolDomainRequest.user_pool_id required")
    if data.get("ManagedLoginVersion") is not None:
        out["managed_login_version"] = data["ManagedLoginVersion"]
    if data.get("CustomDomainConfig") is not None:
        import capo_cognito_identity_provider.types.custom_domain_config_type

        out["custom_domain_config"] = (
            capo_cognito_identity_provider.types.custom_domain_config_type.deserialize_aws_json_1_1(
                data["CustomDomainConfig"]
            )
        )
    if data.get("Routing") is not None:
        import capo_cognito_identity_provider.types.routing_type

        out["routing"] = (
            capo_cognito_identity_provider.types.routing_type.deserialize_aws_json_1_1(
                data["Routing"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateUserPoolDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.custom_domain_config_type
    import capo_cognito_identity_provider.types.domain_type
    import capo_cognito_identity_provider.types.routing_type
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.wrapped_integer_type


class CreateUserPoolDomainRequest(TypedDict, closed=True):
    domain: "capo_cognito_identity_provider.types.domain_type.DomainType"
    """<p>The domain string. For custom domains, this is the fully-qualified domain name, such as <code>auth.example.com</code>. For prefix domains, this is the prefix alone, such as <code>myprefix</code>. A prefix value of <code>myprefix</code> for a user pool in the <code>us-east-1</code> Region results in a domain of <code>myprefix.auth.us-east-1.amazoncognito.com</code>.</p>"""
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to add a domain.</p>"""
    managed_login_version: NotRequired[
        "capo_cognito_identity_provider.types.wrapped_integer_type.WrappedIntegerType"
    ]
    """<p>The version of managed login branding that you want to apply to your domain. A value of <code>1</code> indicates hosted UI (classic) and a version of <code>2</code> indicates managed login.</p> <p>Managed login requires that your user pool be configured for any <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html">feature plan</a> other than <code>Lite</code>.</p> <p>A <code>ManagedLoginVersion</code> value of <code>2</code> does not activate managed login pages for your app client. When you create an app client programmatically, your app client has no branding style. To use managed login, create a branding style using the <a href="https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateManagedLoginBranding.html">CreateManagedLoginBranding</a> operation. When you use the console, Amazon Cognito assigns a default branding style automatically. When you use the API or an SDK, you must create a branding style yourself.</p>"""
    custom_domain_config: NotRequired[
        "capo_cognito_identity_provider.types.custom_domain_config_type.CustomDomainConfigType"
    ]
    """<p>The configuration for a custom domain. Configures your domain with an Certificate Manager certificate in the <code>us-east-1</code> Region.</p> <p>Provide this parameter only if you want to use a <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-add-custom-domain.html">custom domain</a> for your user pool. Otherwise, you can omit this parameter and use a <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-assign-domain-prefix.html">prefix domain</a> instead.</p> <p>When you create a custom domain, the passkey RP ID defaults to the custom domain. If you had a prefix domain active, this will cause passkey integration for your prefix domain to stop working due to a mismatch in RP ID. To keep the prefix domain passkey integration working, you can explicitly set RP ID to the prefix domain.</p>"""
    routing: NotRequired[
        "capo_cognito_identity_provider.types.routing_type.RoutingType"
    ]
    """<p>The configuration of routing for requests to the domain for replicas of a replicated user pool. The routing configuration is currently only supported for custom domains.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserPoolDomainRequest) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> CreateUserPoolDomainRequest:
    out: CreateUserPoolDomainRequest = {}  # type: ignore[typeddict-item]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    else:
        raise DeserializationError("CreateUserPoolDomainRequest.domain required")
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("CreateUserPoolDomainRequest.user_pool_id required")
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

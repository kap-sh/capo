"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateUserPoolDomainResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.domain_type
    import capo_cognito_identity_provider.types.routing_type
    import capo_cognito_identity_provider.types.wrapped_integer_type


class UpdateUserPoolDomainResponse(TypedDict, closed=True):
    managed_login_version: NotRequired[
        "capo_cognito_identity_provider.types.wrapped_integer_type.WrappedIntegerType"
    ]
    """<p>A version number that indicates the state of managed login for your domain. Version <code>1</code> is hosted UI (classic). Version <code>2</code> is the newer managed login with the branding editor. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html">Managed login</a>.</p>"""
    cloud_front_domain: NotRequired[
        "capo_cognito_identity_provider.types.domain_type.DomainType"
    ]
    """<p>The fully-qualified domain name (FQDN) of the Amazon CloudFront distribution that hosts your managed login or classic hosted UI pages. You domain-name authority must have an alias record that points requests for your custom domain to this FQDN. Amazon Cognito returns this value if you set a custom domain with <code>CustomDomainConfig</code>. If you set an Amazon Cognito prefix domain, this operation returns a blank response.</p>"""
    routing: NotRequired[
        "capo_cognito_identity_provider.types.routing_type.RoutingType"
    ]
    """<p>The updated routing configuration for the user pool domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserPoolDomainResponse) -> dict:
    out: dict = {}
    if "managed_login_version" in value:
        out["ManagedLoginVersion"] = value["managed_login_version"]
    if "cloud_front_domain" in value:
        out["CloudFrontDomain"] = value["cloud_front_domain"]
    if "routing" in value:
        import capo_cognito_identity_provider.types.routing_type

        out["Routing"] = (
            capo_cognito_identity_provider.types.routing_type.serialize_aws_json_1_1(
                value["routing"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserPoolDomainResponse:
    out: UpdateUserPoolDomainResponse = {}  # type: ignore[typeddict-item]
    if data.get("ManagedLoginVersion") is not None:
        out["managed_login_version"] = data["ManagedLoginVersion"]
    if data.get("CloudFrontDomain") is not None:
        out["cloud_front_domain"] = data["CloudFrontDomain"]
    if data.get("Routing") is not None:
        import capo_cognito_identity_provider.types.routing_type

        out["routing"] = (
            capo_cognito_identity_provider.types.routing_type.deserialize_aws_json_1_1(
                data["Routing"]
            )
        )
    return out

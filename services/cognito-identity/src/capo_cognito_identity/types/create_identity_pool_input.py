"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#CreateIdentityPoolInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity.types.classic_flow
    import capo_cognito_identity.types.cognito_identity_provider_list
    import capo_cognito_identity.types.developer_provider_name
    import capo_cognito_identity.types.identity_pool_name
    import capo_cognito_identity.types.identity_pool_tags_type
    import capo_cognito_identity.types.identity_pool_unauthenticated
    import capo_cognito_identity.types.identity_providers
    import capo_cognito_identity.types.oidc_provider_list
    import capo_cognito_identity.types.saml_provider_list


class CreateIdentityPoolInput(TypedDict, closed=True):
    identity_pool_name: (
        "capo_cognito_identity.types.identity_pool_name.IdentityPoolName"
    )
    """<p>A string that you provide.</p>"""
    allow_unauthenticated_identities: "capo_cognito_identity.types.identity_pool_unauthenticated.IdentityPoolUnauthenticated"
    """<p>TRUE if the identity pool supports unauthenticated logins.</p>"""
    allow_classic_flow: NotRequired[
        "capo_cognito_identity.types.classic_flow.ClassicFlow"
    ]
    """<p>Enables or disables the Basic (Classic) authentication flow. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html">Identity Pools (Federated Identities) Authentication Flow</a> in the <i>Amazon Cognito Developer Guide</i>.</p>"""
    supported_login_providers: NotRequired[
        "capo_cognito_identity.types.identity_providers.IdentityProviders"
    ]
    """<p>Optional key:value pairs mapping provider names to provider app IDs.</p>"""
    developer_provider_name: NotRequired[
        "capo_cognito_identity.types.developer_provider_name.DeveloperProviderName"
    ]
    """<p>The "domain" by which Cognito will refer to your users. This name acts as a placeholder that allows your backend and the Cognito service to communicate about the developer provider. For the <code>DeveloperProviderName</code>, you can use letters as well as period (<code>.</code>), underscore (<code>_</code>), and dash (<code>-</code>).</p> <p>Once you have set a developer provider name, you cannot change it. Please take care in setting this parameter.</p>"""
    open_id_connect_provider_ar_ns: NotRequired[
        "capo_cognito_identity.types.oidc_provider_list.OIDCProviderList"
    ]
    """<p>The Amazon Resource Names (ARN) of the OpenID Connect providers.</p>"""
    cognito_identity_providers: NotRequired[
        "capo_cognito_identity.types.cognito_identity_provider_list.CognitoIdentityProviderList"
    ]
    """<p>An array of Amazon Cognito user pools and their client IDs.</p>"""
    saml_provider_ar_ns: NotRequired[
        "capo_cognito_identity.types.saml_provider_list.SAMLProviderList"
    ]
    """<p>An array of Amazon Resource Names (ARNs) of the SAML provider for your identity pool.</p>"""
    identity_pool_tags: NotRequired[
        "capo_cognito_identity.types.identity_pool_tags_type.IdentityPoolTagsType"
    ]
    """<p>Tags to assign to the identity pool. A tag is a label that you can apply to identity pools to categorize and manage them in different ways, such as by purpose, owner, environment, or other criteria.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateIdentityPoolInput) -> dict:
    out: dict = {}
    out["IdentityPoolName"] = value["identity_pool_name"]
    out["AllowUnauthenticatedIdentities"] = value.get(
        "allow_unauthenticated_identities", False
    )
    if "allow_classic_flow" in value:
        out["AllowClassicFlow"] = value["allow_classic_flow"]
    if "supported_login_providers" in value:
        import capo_cognito_identity.types.identity_providers

        out["SupportedLoginProviders"] = (
            capo_cognito_identity.types.identity_providers.serialize_aws_json_1_1(
                value["supported_login_providers"]
            )
        )
    if "developer_provider_name" in value:
        out["DeveloperProviderName"] = value["developer_provider_name"]
    if "open_id_connect_provider_ar_ns" in value:
        import capo_cognito_identity.types.oidc_provider_list

        out["OpenIdConnectProviderARNs"] = (
            capo_cognito_identity.types.oidc_provider_list.serialize_aws_json_1_1(
                value["open_id_connect_provider_ar_ns"]
            )
        )
    if "cognito_identity_providers" in value:
        import capo_cognito_identity.types.cognito_identity_provider_list

        out["CognitoIdentityProviders"] = (
            capo_cognito_identity.types.cognito_identity_provider_list.serialize_aws_json_1_1(
                value["cognito_identity_providers"]
            )
        )
    if "saml_provider_ar_ns" in value:
        import capo_cognito_identity.types.saml_provider_list

        out["SamlProviderARNs"] = (
            capo_cognito_identity.types.saml_provider_list.serialize_aws_json_1_1(
                value["saml_provider_ar_ns"]
            )
        )
    if "identity_pool_tags" in value:
        import capo_cognito_identity.types.identity_pool_tags_type

        out["IdentityPoolTags"] = (
            capo_cognito_identity.types.identity_pool_tags_type.serialize_aws_json_1_1(
                value["identity_pool_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateIdentityPoolInput:
    out: CreateIdentityPoolInput = {}  # type: ignore[typeddict-item]
    if data.get("IdentityPoolName") is not None:
        out["identity_pool_name"] = data["IdentityPoolName"]
    else:
        raise DeserializationError(
            "CreateIdentityPoolInput.identity_pool_name required"
        )
    if data.get("AllowUnauthenticatedIdentities") is not None:
        out["allow_unauthenticated_identities"] = data["AllowUnauthenticatedIdentities"]
    else:
        out["allow_unauthenticated_identities"] = False
    if data.get("AllowClassicFlow") is not None:
        out["allow_classic_flow"] = data["AllowClassicFlow"]
    if data.get("SupportedLoginProviders") is not None:
        import capo_cognito_identity.types.identity_providers

        out["supported_login_providers"] = (
            capo_cognito_identity.types.identity_providers.deserialize_aws_json_1_1(
                data["SupportedLoginProviders"]
            )
        )
    if data.get("DeveloperProviderName") is not None:
        out["developer_provider_name"] = data["DeveloperProviderName"]
    if data.get("OpenIdConnectProviderARNs") is not None:
        import capo_cognito_identity.types.oidc_provider_list

        out["open_id_connect_provider_ar_ns"] = (
            capo_cognito_identity.types.oidc_provider_list.deserialize_aws_json_1_1(
                data["OpenIdConnectProviderARNs"]
            )
        )
    if data.get("CognitoIdentityProviders") is not None:
        import capo_cognito_identity.types.cognito_identity_provider_list

        out["cognito_identity_providers"] = (
            capo_cognito_identity.types.cognito_identity_provider_list.deserialize_aws_json_1_1(
                data["CognitoIdentityProviders"]
            )
        )
    if data.get("SamlProviderARNs") is not None:
        import capo_cognito_identity.types.saml_provider_list

        out["saml_provider_ar_ns"] = (
            capo_cognito_identity.types.saml_provider_list.deserialize_aws_json_1_1(
                data["SamlProviderARNs"]
            )
        )
    if data.get("IdentityPoolTags") is not None:
        import capo_cognito_identity.types.identity_pool_tags_type

        out["identity_pool_tags"] = (
            capo_cognito_identity.types.identity_pool_tags_type.deserialize_aws_json_1_1(
                data["IdentityPoolTags"]
            )
        )
    return out

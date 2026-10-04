"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#IdentityProviderType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.acr_mapping_type
    import capo_cognito_identity_provider.types.attribute_mapping_type
    import capo_cognito_identity_provider.types.date_type
    import capo_cognito_identity_provider.types.identity_provider_type_type
    import capo_cognito_identity_provider.types.idp_identifiers_list_type
    import capo_cognito_identity_provider.types.provider_details_type
    import capo_cognito_identity_provider.types.provider_name_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class IdentityProviderType(TypedDict, closed=True):
    user_pool_id: NotRequired[
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The ID of the user pool associated with the IdP.</p>"""
    provider_name: NotRequired[
        "capo_cognito_identity_provider.types.provider_name_type.ProviderNameType"
    ]
    """<p>A friendly name for the IdP.</p>"""
    provider_type: NotRequired[
        "capo_cognito_identity_provider.types.identity_provider_type_type.IdentityProviderTypeType"
    ]
    """<p>The type of IdP. Either SAML, OIDC, or a named social identity provider.</p>"""
    provider_details: NotRequired[
        "capo_cognito_identity_provider.types.provider_details_type.ProviderDetailsType"
    ]
    """<p>The scopes, URLs, and identifiers for your external identity provider. The following examples describe the provider detail keys for each IdP type. These values and their schema are subject to change. Social IdP <code>authorize_scopes</code> values must match the values listed here.</p> <dl> <dt>OpenID Connect (OIDC)</dt> <dd> <p>Amazon Cognito accepts the following elements when it can't discover endpoint URLs from <code>oidc_issuer</code>: <code>attributes_url</code>, <code>authorize_url</code>, <code>jwks_uri</code>, <code>token_url</code>.</p> <p>Create or update request: <code>"ProviderDetails": { "attributes_request_method": "GET", "attributes_url": "https://auth.example.com/userInfo", "authorize_scopes": "openid profile email", "authorize_url": "https://auth.example.com/authorize", "client_id": "1example23456789", "client_secret": "provider-app-client-secret", "jwks_uri": "https://auth.example.com/.well-known/jwks.json", "oidc_issuer": "https://auth.example.com", "token_url": "https://example.com/token" }</code> </p> <p>Describe response: <code>"ProviderDetails": { "attributes_request_method": "GET", "attributes_url": "https://auth.example.com/userInfo", "attributes_url_add_attributes": "false", "authorize_scopes": "openid profile email", "authorize_url": "https://auth.example.com/authorize", "client_id": "1example23456789", "client_secret": "provider-app-client-secret", "jwks_uri": "https://auth.example.com/.well-known/jwks.json", "oidc_issuer": "https://auth.example.com", "token_url": "https://example.com/token" }</code> </p> </dd> <dt>SAML</dt> <dd> <p>Create or update request with Metadata URL: <code>"ProviderDetails": { "IDPInit": "true", "IDPSignout": "true", "EncryptedResponses" : "true", "MetadataURL": "https://auth.example.com/sso/saml/metadata", "RequestSigningAlgorithm": "rsa-sha256" }</code> </p> <p>Create or update request with Metadata file: <code>"ProviderDetails": { "IDPInit": "true", "IDPSignout": "true", "EncryptedResponses" : "true", "MetadataFile": "[metadata XML]", "RequestSigningAlgorithm": "rsa-sha256" }</code> </p> <p>The value of <code>MetadataFile</code> must be the plaintext metadata document with all quote (") characters escaped by backslashes.</p> <p>Describe response: <code>"ProviderDetails": { "IDPInit": "true", "IDPSignout": "true", "EncryptedResponses" : "true", "ActiveEncryptionCertificate": "[certificate]", "MetadataURL": "https://auth.example.com/sso/saml/metadata", "RequestSigningAlgorithm": "rsa-sha256", "SLORedirectBindingURI": "https://auth.example.com/slo/saml", "SSORedirectBindingURI": "https://auth.example.com/sso/saml" }</code> </p> </dd> <dt>LoginWithAmazon</dt> <dd> <p>Create or update request: <code>"ProviderDetails": { "authorize_scopes": "profile postal_code", "client_id": "amzn1.application-oa2-client.1example23456789", "client_secret": "provider-app-client-secret"</code> </p> <p>Describe response: <code>"ProviderDetails": { "attributes_url": "https://api.amazon.com/user/profile", "attributes_url_add_attributes": "false", "authorize_scopes": "profile postal_code", "authorize_url": "https://www.amazon.com/ap/oa", "client_id": "amzn1.application-oa2-client.1example23456789", "client_secret": "provider-app-client-secret", "token_request_method": "POST", "token_url": "https://api.amazon.com/auth/o2/token" }</code> </p> </dd> <dt>Google</dt> <dd> <p>Create or update request: <code>"ProviderDetails": { "authorize_scopes": "email profile openid", "client_id": "1example23456789.apps.googleusercontent.com", "client_secret": "provider-app-client-secret" }</code> </p> <p>Describe response: <code>"ProviderDetails": { "attributes_url": "https://people.googleapis.com/v1/people/me?personFields=", "attributes_url_add_attributes": "true", "authorize_scopes": "email profile openid", "authorize_url": "https://accounts.google.com/o/oauth2/v2/auth", "client_id": "1example23456789.apps.googleusercontent.com", "client_secret": "provider-app-client-secret", "oidc_issuer": "https://accounts.google.com", "token_request_method": "POST", "token_url": "https://www.googleapis.com/oauth2/v4/token" }</code> </p> </dd> <dt>SignInWithApple</dt> <dd> <p>Create or update request: <code>"ProviderDetails": { "authorize_scopes": "email name", "client_id": "com.example.cognito", "private_key": "1EXAMPLE", "key_id": "2EXAMPLE", "team_id": "3EXAMPLE" }</code> </p> <p>Describe response: <code>"ProviderDetails": { "attributes_url_add_attributes": "false", "authorize_scopes": "email name", "authorize_url": "https://appleid.apple.com/auth/authorize", "client_id": "com.example.cognito", "key_id": "1EXAMPLE", "oidc_issuer": "https://appleid.apple.com", "team_id": "2EXAMPLE", "token_request_method": "POST", "token_url": "https://appleid.apple.com/auth/token" }</code> </p> </dd> <dt>Facebook</dt> <dd> <p>Create or update request: <code>"ProviderDetails": { "api_version": "v17.0", "authorize_scopes": "public_profile, email", "client_id": "1example23456789", "client_secret": "provider-app-client-secret" }</code> </p> <p>Describe response: <code>"ProviderDetails": { "api_version": "v17.0", "attributes_url": "https://graph.facebook.com/v17.0/me?fields=", "attributes_url_add_attributes": "true", "authorize_scopes": "public_profile, email", "authorize_url": "https://www.facebook.com/v17.0/dialog/oauth", "client_id": "1example23456789", "client_secret": "provider-app-client-secret", "token_request_method": "GET", "token_url": "https://graph.facebook.com/v17.0/oauth/access_token" }</code> </p> </dd> </dl>"""
    attribute_mapping: NotRequired[
        "capo_cognito_identity_provider.types.attribute_mapping_type.AttributeMappingType"
    ]
    """<p>A mapping of IdP attributes to standard and custom user pool attributes.</p>"""
    idp_identifiers: NotRequired[
        "capo_cognito_identity_provider.types.idp_identifiers_list_type.IdpIdentifiersListType"
    ]
    """<p>A list of IdP identifiers. IdP identifiers are strings that represent friendly names or domain names of IdPs, for example <code>MyIdP</code> or <code>auth.example.com</code>. You can choose to route user authorization requests to the right IdP with either IdP identifiers or IdP names. For more information, see <code>identity_provider</code> and <code>idp_identifier</code> at <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/authorization-endpoint.html#get-authorize-request-parameters">Authorize endpoint</a>.</p>"""
    acr_mapping: NotRequired[
        "capo_cognito_identity_provider.types.acr_mapping_type.AcrMappingType"
    ]
    """<p>A mapping between the authentication context class reference (ACR) levels of your user pool and the ACR values of the external OpenID Connect (OIDC) identity provider (IdP), so that your application gets a consistent step-up experience regardless of which IdP authenticated the user. The map is keyed by level, from <code>Level1</code> through <code>Level4</code>.</p>"""
    last_modified_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was modified. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""
    creation_date: NotRequired[
        "capo_cognito_identity_provider.types.date_type.DateType"
    ]
    """<p>The date and time when the item was created. Amazon Cognito returns this timestamp in UNIX epoch time format. Your SDK might render the output in a human-readable format like ISO 8601 or a Java <code>Date</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityProviderType) -> dict:
    out: dict = {}
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
    if "provider_name" in value:
        out["ProviderName"] = value["provider_name"]
    if "provider_type" in value:
        import capo_cognito_identity_provider.types.identity_provider_type_type

        out["ProviderType"] = (
            capo_cognito_identity_provider.types.identity_provider_type_type.serialize_aws_json_1_1(
                value["provider_type"]
            )
        )
    if "provider_details" in value:
        import capo_cognito_identity_provider.types.provider_details_type

        out["ProviderDetails"] = (
            capo_cognito_identity_provider.types.provider_details_type.serialize_aws_json_1_1(
                value["provider_details"]
            )
        )
    if "attribute_mapping" in value:
        import capo_cognito_identity_provider.types.attribute_mapping_type

        out["AttributeMapping"] = (
            capo_cognito_identity_provider.types.attribute_mapping_type.serialize_aws_json_1_1(
                value["attribute_mapping"]
            )
        )
    if "idp_identifiers" in value:
        import capo_cognito_identity_provider.types.idp_identifiers_list_type

        out["IdpIdentifiers"] = (
            capo_cognito_identity_provider.types.idp_identifiers_list_type.serialize_aws_json_1_1(
                value["idp_identifiers"]
            )
        )
    if "acr_mapping" in value:
        import capo_cognito_identity_provider.types.acr_mapping_type

        out["AcrMapping"] = (
            capo_cognito_identity_provider.types.acr_mapping_type.serialize_aws_json_1_1(
                value["acr_mapping"]
            )
        )
    if "last_modified_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["LastModifiedDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["last_modified_date"]
            )
        )
    if "creation_date" in value:
        import capo_cognito_identity_provider.types.date_type

        out["CreationDate"] = (
            capo_cognito_identity_provider.types.date_type.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IdentityProviderType:
    out: IdentityProviderType = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    if data.get("ProviderName") is not None:
        out["provider_name"] = data["ProviderName"]
    if data.get("ProviderType") is not None:
        import capo_cognito_identity_provider.types.identity_provider_type_type

        out["provider_type"] = (
            capo_cognito_identity_provider.types.identity_provider_type_type.deserialize_aws_json_1_1(
                data["ProviderType"]
            )
        )
    if data.get("ProviderDetails") is not None:
        import capo_cognito_identity_provider.types.provider_details_type

        out["provider_details"] = (
            capo_cognito_identity_provider.types.provider_details_type.deserialize_aws_json_1_1(
                data["ProviderDetails"]
            )
        )
    if data.get("AttributeMapping") is not None:
        import capo_cognito_identity_provider.types.attribute_mapping_type

        out["attribute_mapping"] = (
            capo_cognito_identity_provider.types.attribute_mapping_type.deserialize_aws_json_1_1(
                data["AttributeMapping"]
            )
        )
    if data.get("IdpIdentifiers") is not None:
        import capo_cognito_identity_provider.types.idp_identifiers_list_type

        out["idp_identifiers"] = (
            capo_cognito_identity_provider.types.idp_identifiers_list_type.deserialize_aws_json_1_1(
                data["IdpIdentifiers"]
            )
        )
    if data.get("AcrMapping") is not None:
        import capo_cognito_identity_provider.types.acr_mapping_type

        out["acr_mapping"] = (
            capo_cognito_identity_provider.types.acr_mapping_type.deserialize_aws_json_1_1(
                data["AcrMapping"]
            )
        )
    if data.get("LastModifiedDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["last_modified_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["LastModifiedDate"]
            )
        )
    if data.get("CreationDate") is not None:
        import capo_cognito_identity_provider.types.date_type

        out["creation_date"] = (
            capo_cognito_identity_provider.types.date_type.deserialize_aws_json_1_1(
                data["CreationDate"]
            )
        )
    return out

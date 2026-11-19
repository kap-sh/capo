"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetDerivedTokenRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.audience_list_type
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.client_secret_type
    import capo_cognito_identity_provider.types.get_derived_token_token_model_type
    import capo_cognito_identity_provider.types.issued_token_type_identifier_type
    import capo_cognito_identity_provider.types.provider_name_type
    import capo_cognito_identity_provider.types.resource_list_type
    import capo_cognito_identity_provider.types.scope_list_type
    import capo_cognito_identity_provider.types.token_type_identifier_type


class GetDerivedTokenRequest(TypedDict, closed=True):
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client that requests the token exchange.</p>"""
    client_secret: NotRequired[
        "capo_cognito_identity_provider.types.client_secret_type.ClientSecretType"
    ]
    """<p>The client secret of the requested app client, if the client has a secret.</p>"""
    subject_token: "capo_cognito_identity_provider.types.get_derived_token_token_model_type.GetDerivedTokenTokenModelType"
    """<p>The token that you want to exchange for a new token. This is the credential that represents the identity of the party on behalf of whom the request is being made.</p>"""
    subject_token_type: "capo_cognito_identity_provider.types.token_type_identifier_type.TokenTypeIdentifierType"
    """<p>The type of the <code>SubjectToken</code> that you want to exchange. Valid values:</p> <ul> <li> <p> <code>ACCESS_TOKEN</code> – The subject token is an access token.</p> </li> <li> <p> <code>ID_TOKEN</code> – The subject token is an ID token.</p> </li> <li> <p> <code>SAML2</code> – The subject token is a SAML 2.0 assertion.</p> </li> </ul>"""
    subject_token_provider_name: NotRequired[
        "capo_cognito_identity_provider.types.provider_name_type.ProviderNameType"
    ]
    """<p>The name of the third-party identity provider that issued the <code>SubjectToken</code>, if the subject token isn't a Amazon Cognito token. Provide this value when your <code>SubjectToken</code> came from a SAML or OIDC provider that you registered with your user pool, so that Amazon Cognito can validate it against that provider's configuration. Omit this parameter for a Amazon Cognito ID or access token.</p>"""
    actor_token: NotRequired[
        "capo_cognito_identity_provider.types.get_derived_token_token_model_type.GetDerivedTokenTokenModelType"
    ]
    """<p>A token that identifies the intermediary service that is exchanging the token on behalf of the user. When you provide an <code>ActorToken</code>, the token that Amazon Cognito issues carries an <code>act</code> claim that identifies the intermediary, so that downstream services can distinguish a user acting directly from an intermediary acting on the user's behalf.</p>"""
    actor_token_type: NotRequired[
        "capo_cognito_identity_provider.types.token_type_identifier_type.TokenTypeIdentifierType"
    ]
    """<p>The type of the <code>ActorToken</code> that you provide. Required when you provide an <code>ActorToken</code>. Valid values:</p> <ul> <li> <p> <code>ACCESS_TOKEN</code> – The actor token is an access token.</p> </li> <li> <p> <code>ID_TOKEN</code> – The actor token is an ID token.</p> </li> <li> <p> <code>SAML2</code> – The actor token is a SAML 2.0 assertion.</p> </li> </ul>"""
    actor_token_provider_name: NotRequired[
        "capo_cognito_identity_provider.types.provider_name_type.ProviderNameType"
    ]
    """<p>The name of the third-party identity provider that issued the <code>ActorToken</code>, if the actor token isn't a Amazon Cognito token.</p>"""
    scopes: NotRequired[
        "capo_cognito_identity_provider.types.scope_list_type.ScopeListType"
    ]
    """<p>The scopes that you want the new token to have. Amazon Cognito issues a token with the intersection of these requested scopes, the scopes of your <code>SubjectToken</code>, and the scopes that are allowed for the requesting app client. If you don't specify any scopes, Amazon Cognito issues a token with the same scopes as your <code>SubjectToken</code>.</p>"""
    audiences: NotRequired[
        "capo_cognito_identity_provider.types.audience_list_type.AudienceListType"
    ]
    """<p>The logical name of the target service where you intend to use the issued token. You can't request both <code>Audiences</code> and <code>Resources</code> in the same request.</p>"""
    resources: NotRequired[
        "capo_cognito_identity_provider.types.resource_list_type.ResourceListType"
    ]
    """<p>The identifier of a resource server in your user pool where you intend to use the issued token. You can't request both <code>Resources</code> and <code>Audiences</code> in the same request.</p>"""
    requested_token_type: NotRequired[
        "capo_cognito_identity_provider.types.issued_token_type_identifier_type.IssuedTokenTypeIdentifierType"
    ]
    """<p>The type of token that you want Amazon Cognito to issue. Valid values:</p> <ul> <li> <p> <code>ACCESS_TOKEN</code> – Issues an access token.</p> </li> <li> <p> <code>ID_TOKEN</code> – Issues an ID token.</p> </li> </ul> <p>Amazon Cognito can't issue a SAML assertion, so <code>SAML2</code> isn't a valid value for this parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDerivedTokenRequest) -> dict:
    out: dict = {}
    out["ClientId"] = value["client_id"]
    if "client_secret" in value:
        out["ClientSecret"] = value["client_secret"]
    out["SubjectToken"] = value["subject_token"]
    import capo_cognito_identity_provider.types.token_type_identifier_type

    out["SubjectTokenType"] = (
        capo_cognito_identity_provider.types.token_type_identifier_type.serialize_aws_json_1_1(
            value["subject_token_type"]
        )
    )
    if "subject_token_provider_name" in value:
        out["SubjectTokenProviderName"] = value["subject_token_provider_name"]
    if "actor_token" in value:
        out["ActorToken"] = value["actor_token"]
    if "actor_token_type" in value:
        import capo_cognito_identity_provider.types.token_type_identifier_type

        out["ActorTokenType"] = (
            capo_cognito_identity_provider.types.token_type_identifier_type.serialize_aws_json_1_1(
                value["actor_token_type"]
            )
        )
    if "actor_token_provider_name" in value:
        out["ActorTokenProviderName"] = value["actor_token_provider_name"]
    if "scopes" in value:
        import capo_cognito_identity_provider.types.scope_list_type

        out["Scopes"] = (
            capo_cognito_identity_provider.types.scope_list_type.serialize_aws_json_1_1(
                value["scopes"]
            )
        )
    if "audiences" in value:
        import capo_cognito_identity_provider.types.audience_list_type

        out["Audiences"] = (
            capo_cognito_identity_provider.types.audience_list_type.serialize_aws_json_1_1(
                value["audiences"]
            )
        )
    if "resources" in value:
        import capo_cognito_identity_provider.types.resource_list_type

        out["Resources"] = (
            capo_cognito_identity_provider.types.resource_list_type.serialize_aws_json_1_1(
                value["resources"]
            )
        )
    if "requested_token_type" in value:
        import capo_cognito_identity_provider.types.issued_token_type_identifier_type

        out["RequestedTokenType"] = (
            capo_cognito_identity_provider.types.issued_token_type_identifier_type.serialize_aws_json_1_1(
                value["requested_token_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDerivedTokenRequest:
    out: GetDerivedTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        out["client_id"] = ""
    if data.get("ClientSecret") is not None:
        out["client_secret"] = data["ClientSecret"]
    if data.get("SubjectToken") is not None:
        out["subject_token"] = data["SubjectToken"]
    else:
        out["subject_token"] = ""
    if data.get("SubjectTokenType") is not None:
        import capo_cognito_identity_provider.types.token_type_identifier_type

        out["subject_token_type"] = (
            capo_cognito_identity_provider.types.token_type_identifier_type.deserialize_aws_json_1_1(
                data["SubjectTokenType"]
            )
        )
    else:
        import typing

        out["subject_token_type"] = typing.cast(
            "capo_cognito_identity_provider.types.token_type_identifier_type.TokenTypeIdentifierType",
            "",
        )
    if data.get("SubjectTokenProviderName") is not None:
        out["subject_token_provider_name"] = data["SubjectTokenProviderName"]
    if data.get("ActorToken") is not None:
        out["actor_token"] = data["ActorToken"]
    if data.get("ActorTokenType") is not None:
        import capo_cognito_identity_provider.types.token_type_identifier_type

        out["actor_token_type"] = (
            capo_cognito_identity_provider.types.token_type_identifier_type.deserialize_aws_json_1_1(
                data["ActorTokenType"]
            )
        )
    if data.get("ActorTokenProviderName") is not None:
        out["actor_token_provider_name"] = data["ActorTokenProviderName"]
    if data.get("Scopes") is not None:
        import capo_cognito_identity_provider.types.scope_list_type

        out["scopes"] = (
            capo_cognito_identity_provider.types.scope_list_type.deserialize_aws_json_1_1(
                data["Scopes"]
            )
        )
    if data.get("Audiences") is not None:
        import capo_cognito_identity_provider.types.audience_list_type

        out["audiences"] = (
            capo_cognito_identity_provider.types.audience_list_type.deserialize_aws_json_1_1(
                data["Audiences"]
            )
        )
    if data.get("Resources") is not None:
        import capo_cognito_identity_provider.types.resource_list_type

        out["resources"] = (
            capo_cognito_identity_provider.types.resource_list_type.deserialize_aws_json_1_1(
                data["Resources"]
            )
        )
    if data.get("RequestedTokenType") is not None:
        import capo_cognito_identity_provider.types.issued_token_type_identifier_type

        out["requested_token_type"] = (
            capo_cognito_identity_provider.types.issued_token_type_identifier_type.deserialize_aws_json_1_1(
                data["RequestedTokenType"]
            )
        )
    return out


def redact_sensitive(value: GetDerivedTokenRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_id" in value:
        out["client_id"] = "*** Sensitive Data Redacted ***"
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    if "subject_token" in value:
        out["subject_token"] = "*** Sensitive Data Redacted ***"
    if "actor_token" in value:
        out["actor_token"] = "*** Sensitive Data Redacted ***"
    return out

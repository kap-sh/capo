"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#DcrConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.boolean_type
    import capo_cognito_identity_provider.types.o_auth_flows_type
    import capo_cognito_identity_provider.types.scope_list_type
    import capo_cognito_identity_provider.types.status_type


class DcrConfigurationType(TypedDict, closed=True):
    enable_status: NotRequired[
        "capo_cognito_identity_provider.types.status_type.StatusType"
    ]
    """<p>Specifies whether dynamic client registration is turned on for the user pool. If you provide a dynamic client registration configuration without this value, Amazon Cognito turns dynamic client registration on.</p>"""
    open_dcr_enabled: "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    """<p>Specifies whether open registration is turned on. When open registration is on, applications can register app clients without an initial access token. The default value is <code>false</code>.</p>"""
    authenticated_grant_types: NotRequired[
        "capo_cognito_identity_provider.types.o_auth_flows_type.OAuthFlowsType"
    ]
    """<p>The OAuth grant types that an app client created through authenticated registration can request. If you don't set this value, authenticated registration permits the <code>code</code> and <code>client_credentials</code> grant types. If you set an empty list, Amazon Cognito rejects authenticated registration requests. Dynamic client registration supports the following values. Amazon Cognito accepts <code>implicit</code> in this list but ignores it.</p> <dl> <dt>code</dt> <dd> <p>Use a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the <code>/oauth2/token</code> endpoint.</p> </dd> <dt>client_credentials</dt> <dd> <p>Issue the access token from the <code>/oauth2/token</code> endpoint directly to a non-person user using a combination of the client ID and client secret.</p> </dd> </dl>"""
    open_dcr_grant_types: NotRequired[
        "capo_cognito_identity_provider.types.o_auth_flows_type.OAuthFlowsType"
    ]
    """<p>The OAuth grant types that an app client created through open registration can request. If you don't set this value, open registration permits only the <code>code</code> grant type. If you set an empty list, Amazon Cognito rejects open registration requests. If you add <code>client_credentials</code>, anyone can register an app client that requests machine-to-machine (M2M) access tokens, and you pay for the M2M token requests that those app clients make. Dynamic client registration supports the following values. Amazon Cognito accepts <code>implicit</code> in this list but ignores it.</p> <dl> <dt>code</dt> <dd> <p>Use a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the <code>/oauth2/token</code> endpoint.</p> </dd> <dt>client_credentials</dt> <dd> <p>Issue the access token from the <code>/oauth2/token</code> endpoint directly to a non-person user using a combination of the client ID and client secret.</p> </dd> </dl>"""
    allowed_scopes: NotRequired[
        "capo_cognito_identity_provider.types.scope_list_type.ScopeListType"
    ]
    """<p>The scopes that an app client created through dynamic client registration can request, in addition to the standard OpenID Connect (OIDC) scopes. You can include custom scopes from your resource servers and <code>aws.cognito.signin.user.admin</code>. Registered app clients can request the OIDC scopes <code>openid</code>, <code>email</code>, <code>phone</code>, and <code>profile</code> without listing them here. If you don't set this value, registered app clients can request only the OIDC scopes. A registered app client can't request the <code>aws.cognito/dcr/register</code> scope, even if you include it in this list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DcrConfigurationType) -> dict:
    out: dict = {}
    if "enable_status" in value:
        import capo_cognito_identity_provider.types.status_type

        out["EnableStatus"] = (
            capo_cognito_identity_provider.types.status_type.serialize_aws_json_1_1(
                value["enable_status"]
            )
        )
    out["OpenDcrEnabled"] = value.get("open_dcr_enabled", False)
    if "authenticated_grant_types" in value:
        import capo_cognito_identity_provider.types.o_auth_flows_type

        out["AuthenticatedGrantTypes"] = (
            capo_cognito_identity_provider.types.o_auth_flows_type.serialize_aws_json_1_1(
                value["authenticated_grant_types"]
            )
        )
    if "open_dcr_grant_types" in value:
        import capo_cognito_identity_provider.types.o_auth_flows_type

        out["OpenDcrGrantTypes"] = (
            capo_cognito_identity_provider.types.o_auth_flows_type.serialize_aws_json_1_1(
                value["open_dcr_grant_types"]
            )
        )
    if "allowed_scopes" in value:
        import capo_cognito_identity_provider.types.scope_list_type

        out["AllowedScopes"] = (
            capo_cognito_identity_provider.types.scope_list_type.serialize_aws_json_1_1(
                value["allowed_scopes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DcrConfigurationType:
    out: DcrConfigurationType = {}  # type: ignore[typeddict-item]
    if data.get("EnableStatus") is not None:
        import capo_cognito_identity_provider.types.status_type

        out["enable_status"] = (
            capo_cognito_identity_provider.types.status_type.deserialize_aws_json_1_1(
                data["EnableStatus"]
            )
        )
    if data.get("OpenDcrEnabled") is not None:
        out["open_dcr_enabled"] = data["OpenDcrEnabled"]
    else:
        out["open_dcr_enabled"] = False
    if data.get("AuthenticatedGrantTypes") is not None:
        import capo_cognito_identity_provider.types.o_auth_flows_type

        out["authenticated_grant_types"] = (
            capo_cognito_identity_provider.types.o_auth_flows_type.deserialize_aws_json_1_1(
                data["AuthenticatedGrantTypes"]
            )
        )
    if data.get("OpenDcrGrantTypes") is not None:
        import capo_cognito_identity_provider.types.o_auth_flows_type

        out["open_dcr_grant_types"] = (
            capo_cognito_identity_provider.types.o_auth_flows_type.deserialize_aws_json_1_1(
                data["OpenDcrGrantTypes"]
            )
        )
    if data.get("AllowedScopes") is not None:
        import capo_cognito_identity_provider.types.scope_list_type

        out["allowed_scopes"] = (
            capo_cognito_identity_provider.types.scope_list_type.deserialize_aws_json_1_1(
                data["AllowedScopes"]
            )
        )
    return out

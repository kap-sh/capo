"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateUserPoolClientRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.access_token_validity_type
    import capo_cognito_identity_provider.types.analytics_configuration_type
    import capo_cognito_identity_provider.types.auth_session_validity_type
    import capo_cognito_identity_provider.types.boolean_type
    import capo_cognito_identity_provider.types.callback_ur_ls_list_type
    import capo_cognito_identity_provider.types.client_id_type
    import capo_cognito_identity_provider.types.client_name_type
    import capo_cognito_identity_provider.types.client_permission_list_type
    import capo_cognito_identity_provider.types.explicit_auth_flows_list_type
    import capo_cognito_identity_provider.types.id_token_validity_type
    import capo_cognito_identity_provider.types.logout_ur_ls_list_type
    import capo_cognito_identity_provider.types.o_auth_flows_type
    import capo_cognito_identity_provider.types.prevent_user_existence_error_types
    import capo_cognito_identity_provider.types.redirect_url_type
    import capo_cognito_identity_provider.types.refresh_token_rotation_type
    import capo_cognito_identity_provider.types.refresh_token_validity_type
    import capo_cognito_identity_provider.types.scope_list_type
    import capo_cognito_identity_provider.types.supported_identity_providers_list_type
    import capo_cognito_identity_provider.types.token_validity_units_type
    import capo_cognito_identity_provider.types.user_pool_id_type
    import capo_cognito_identity_provider.types.wrapped_boolean_type


class UpdateUserPoolClientRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to update the app client.</p>"""
    client_id: "capo_cognito_identity_provider.types.client_id_type.ClientIdType"
    """<p>The ID of the app client that you want to update.</p>"""
    client_name: NotRequired[
        "capo_cognito_identity_provider.types.client_name_type.ClientNameType"
    ]
    """<p>A friendly name for the app client.</p>"""
    refresh_token_validity: "capo_cognito_identity_provider.types.refresh_token_validity_type.RefreshTokenValidityType"
    """<p>The refresh token time limit. After this limit expires, your user can't use their refresh token. To specify the time unit for <code>RefreshTokenValidity</code> as <code>seconds</code>, <code>minutes</code>, <code>hours</code>, or <code>days</code>, set a <code>TokenValidityUnits</code> value in your API request.</p> <p>For example, when you set <code>RefreshTokenValidity</code> as <code>10</code> and <code>TokenValidityUnits</code> as <code>days</code>, your user can refresh their session and retrieve new access and ID tokens for 10 days.</p> <p>The default time unit for <code>RefreshTokenValidity</code> in an API request is days. You can't set <code>RefreshTokenValidity</code> to 0. If you do, Amazon Cognito overrides the value with the default value of 30 days. <i>Valid range</i> is displayed below in seconds.</p> <p>If you don't specify otherwise in the configuration of your app client, your refresh tokens are valid for 30 days.</p>"""
    access_token_validity: NotRequired[
        "capo_cognito_identity_provider.types.access_token_validity_type.AccessTokenValidityType"
    ]
    """<p>The access token time limit. After this limit expires, your user can't use their access token. To specify the time unit for <code>AccessTokenValidity</code> as <code>seconds</code>, <code>minutes</code>, <code>hours</code>, or <code>days</code>, set a <code>TokenValidityUnits</code> value in your API request.</p> <p>For example, when you set <code>AccessTokenValidity</code> to <code>10</code> and <code>TokenValidityUnits</code> to <code>hours</code>, your user can authorize access with their access token for 10 hours.</p> <p>The default time unit for <code>AccessTokenValidity</code> in an API request is hours. <i>Valid range</i> is displayed below in seconds.</p> <p>If you don't specify otherwise in the configuration of your app client, your access tokens are valid for one hour.</p>"""
    id_token_validity: NotRequired[
        "capo_cognito_identity_provider.types.id_token_validity_type.IdTokenValidityType"
    ]
    """<p>The ID token time limit. After this limit expires, your user can't use their ID token. To specify the time unit for <code>IdTokenValidity</code> as <code>seconds</code>, <code>minutes</code>, <code>hours</code>, or <code>days</code>, set a <code>TokenValidityUnits</code> value in your API request.</p> <p>For example, when you set <code>IdTokenValidity</code> as <code>10</code> and <code>TokenValidityUnits</code> as <code>hours</code>, your user can authenticate their session with their ID token for 10 hours.</p> <p>The default time unit for <code>IdTokenValidity</code> in an API request is hours. <i>Valid range</i> is displayed below in seconds.</p> <p>If you don't specify otherwise in the configuration of your app client, your ID tokens are valid for one hour.</p>"""
    token_validity_units: NotRequired[
        "capo_cognito_identity_provider.types.token_validity_units_type.TokenValidityUnitsType"
    ]
    """<p>The units that validity times are represented in. The default unit for refresh tokens is days, and the default for ID and access tokens are hours.</p>"""
    read_attributes: NotRequired[
        "capo_cognito_identity_provider.types.client_permission_list_type.ClientPermissionListType"
    ]
    """<p>The list of user attributes that you want your app client to have read access to. After your user authenticates in your app, their access token authorizes them to read their own attribute value for any attribute in this list.</p> <p>When you don't specify the <code>ReadAttributes</code> for your app client, your app can read the values of <code>email_verified</code>, <code>phone_number_verified</code>, and the standard attributes of your user pool. When your user pool app client has read access to these default attributes, <code>ReadAttributes</code> doesn't return any information. Amazon Cognito only populates <code>ReadAttributes</code> in the API response if you have specified your own custom set of read attributes.</p>"""
    write_attributes: NotRequired[
        "capo_cognito_identity_provider.types.client_permission_list_type.ClientPermissionListType"
    ]
    """<p>The list of user attributes that you want your app client to have write access to. After your user authenticates in your app, their access token authorizes them to set or modify their own attribute value for any attribute in this list.</p> <p>When you don't specify the <code>WriteAttributes</code> for your app client, your app can write the values of the Standard attributes of your user pool. When your user pool has write access to these default attributes, <code>WriteAttributes</code> doesn't return any information. Amazon Cognito only populates <code>WriteAttributes</code> in the API response if you have specified your own custom set of write attributes.</p> <p>If your app client allows users to sign in through an IdP, this array must include all attributes that you have mapped to IdP attributes. Amazon Cognito updates mapped attributes when users sign in to your application through an IdP. If your app client does not have write access to a mapped attribute, Amazon Cognito throws an error when it tries to update the attribute. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html">Specifying IdP Attribute Mappings for Your user pool</a>.</p>"""
    explicit_auth_flows: NotRequired[
        "capo_cognito_identity_provider.types.explicit_auth_flows_list_type.ExplicitAuthFlowsListType"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-authentication-flow-methods.html">authentication flows</a> that you want your user pool client to support. For each app client in your user pool, you can sign in your users with any combination of one or more flows, including with a user name and Secure Remote Password (SRP), a user name and password, or a custom authentication process that you define with Lambda functions.</p> <note> <p>If you don't specify a value for <code>ExplicitAuthFlows</code>, your app client supports <code>ALLOW_REFRESH_TOKEN_AUTH</code>, <code>ALLOW_USER_SRP_AUTH</code>, and <code>ALLOW_CUSTOM_AUTH</code>. </p> </note> <p>The values for authentication flow options include the following.</p> <ul> <li> <p> <code>ALLOW_USER_AUTH</code>: Enable selection-based sign-in with <code>USER_AUTH</code>. This setting covers username-password, secure remote password (SRP), passwordless, and passkey authentication. This authentiation flow can do username-password and SRP authentication without other <code>ExplicitAuthFlows</code> permitting them. For example users can complete an SRP challenge through <code>USER_AUTH</code> without the flow <code>USER_SRP_AUTH</code> being active for the app client. This flow doesn't include <code>CUSTOM_AUTH</code>. </p> <p>To activate this setting, your user pool must be in the <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-essentials.html"> Essentials tier</a> or higher.</p> </li> <li> <p> <code>ALLOW_ADMIN_USER_PASSWORD_AUTH</code>: Enable admin based user password authentication flow <code>ADMIN_USER_PASSWORD_AUTH</code>. This setting replaces the <code>ADMIN_NO_SRP_AUTH</code> setting. With this authentication flow, your app passes a user name and password to Amazon Cognito in the request, instead of using the Secure Remote Password (SRP) protocol to securely transmit the password.</p> </li> <li> <p> <code>ALLOW_CUSTOM_AUTH</code>: Enable Lambda trigger based authentication.</p> </li> <li> <p> <code>ALLOW_USER_PASSWORD_AUTH</code>: Enable user password-based authentication. In this flow, Amazon Cognito receives the password in the request instead of using the SRP protocol to verify passwords.</p> </li> <li> <p> <code>ALLOW_USER_SRP_AUTH</code>: Enable SRP-based authentication.</p> </li> <li> <p> <code>ALLOW_REFRESH_TOKEN_AUTH</code>: Enable authflow to refresh tokens.</p> </li> </ul> <p>In some environments, you will see the values <code>ADMIN_NO_SRP_AUTH</code>, <code>CUSTOM_AUTH_FLOW_ONLY</code>, or <code>USER_PASSWORD_AUTH</code>. You can't assign these legacy <code>ExplicitAuthFlows</code> values to user pool clients at the same time as values that begin with <code>ALLOW_</code>, like <code>ALLOW_USER_SRP_AUTH</code>.</p>"""
    supported_identity_providers: NotRequired[
        "capo_cognito_identity_provider.types.supported_identity_providers_list_type.SupportedIdentityProvidersListType"
    ]
    """<p>A list of provider names for the identity providers (IdPs) that are supported on this client. The following are supported: <code>COGNITO</code>, <code>Facebook</code>, <code>Google</code>, <code>SignInWithApple</code>, and <code>LoginWithAmazon</code>. You can also specify the names that you configured for the SAML and OIDC IdPs in your user pool, for example <code>MySAMLIdP</code> or <code>MyOIDCIdP</code>.</p> <p>This parameter sets the IdPs that <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-managed-login.html">managed login</a> will display on the login page for your app client. The removal of <code>COGNITO</code> from this list doesn't prevent authentication operations for local users with the user pools API in an Amazon Web Services SDK. The only way to prevent SDK-based authentication is to block access with a <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-waf.html">WAF rule</a>. </p>"""
    callback_ur_ls: NotRequired[
        "capo_cognito_identity_provider.types.callback_ur_ls_list_type.CallbackURLsListType"
    ]
    """<p>A list of allowed redirect, or callback, URLs for managed login authentication. These URLs are the paths where you want to send your users' browsers after they complete authentication with managed login or a third-party IdP. Typically, callback URLs are the home of an application that uses OAuth or OIDC libraries to process authentication outcomes.</p> <p>A redirect URI must meet the following requirements:</p> <ul> <li> <p>Be an absolute URI.</p> </li> <li> <p>Be registered with the authorization server. Amazon Cognito doesn't accept authorization requests with <code>redirect_uri</code> values that aren't in the list of <code>CallbackURLs</code> that you provide in this parameter.</p> </li> <li> <p>Not include a fragment component.</p> </li> </ul> <p>See <a href="https://tools.ietf.org/html/rfc6749#section-3.1.2">OAuth 2.0 - Redirection Endpoint</a>.</p> <p>Amazon Cognito requires HTTPS over HTTP except for http://localhost for testing purposes only.</p> <p>App callback URLs such as <code>myapp://example</code> are also supported.</p>"""
    logout_ur_ls: NotRequired[
        "capo_cognito_identity_provider.types.logout_ur_ls_list_type.LogoutURLsListType"
    ]
    """<p>A list of allowed logout URLs for managed login authentication. When you pass <code>logout_uri</code> and <code>client_id</code> parameters to <code>/logout</code>, Amazon Cognito signs out your user and redirects them to the logout URL. This parameter describes the URLs that you want to be the permitted targets of <code>logout_uri</code>. A typical use of these URLs is when a user selects "Sign out" and you redirect them to your public homepage. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/logout-endpoint.html">Logout endpoint</a>.</p>"""
    default_redirect_uri: NotRequired[
        "capo_cognito_identity_provider.types.redirect_url_type.RedirectUrlType"
    ]
    """<p>The default redirect URI. In app clients with one assigned IdP, replaces <code>redirect_uri</code> in authentication requests. Must be in the <code>CallbackURLs</code> list.</p>"""
    allowed_o_auth_flows: NotRequired[
        "capo_cognito_identity_provider.types.o_auth_flows_type.OAuthFlowsType"
    ]
    """<p>The OAuth grant types that you want your app client to generate. To create an app client that generates client credentials grants, you must add <code>client_credentials</code> as the only allowed OAuth flow.</p> <dl> <dt>code</dt> <dd> <p>Use a code grant flow, which provides an authorization code as the response. This code can be exchanged for access tokens with the <code>/oauth2/token</code> endpoint.</p> </dd> <dt>implicit</dt> <dd> <p>Issue the access token (and, optionally, ID token, based on scopes) directly to your user.</p> </dd> <dt>client_credentials</dt> <dd> <p>Issue the access token from the <code>/oauth2/token</code> endpoint directly to a non-person user using a combination of the client ID and client secret.</p> </dd> </dl>"""
    allowed_o_auth_scopes: NotRequired[
        "capo_cognito_identity_provider.types.scope_list_type.ScopeListType"
    ]
    """<p>The OAuth, OpenID Connect (OIDC), and custom scopes that you want to permit your app client to authorize access with. Scopes govern access control to user pool self-service API operations, user data from the <code>userInfo</code> endpoint, and third-party APIs. Scope values include <code>phone</code>, <code>email</code>, <code>openid</code>, and <code>profile</code>. The <code>aws.cognito.signin.user.admin</code> scope authorizes user self-service operations. Custom scopes with resource servers authorize access to external APIs.</p>"""
    allowed_o_auth_flows_user_pool_client: (
        "capo_cognito_identity_provider.types.boolean_type.BooleanType"
    )
    """<p>Set to <code>true</code> to use OAuth 2.0 authorization server features in your app client.</p> <p>This parameter must have a value of <code>true</code> before you can configure the following features in your app client.</p> <ul> <li> <p> <code>CallBackURLs</code>: Callback URLs.</p> </li> <li> <p> <code>LogoutURLs</code>: Sign-out redirect URLs.</p> </li> <li> <p> <code>AllowedOAuthScopes</code>: OAuth 2.0 scopes.</p> </li> <li> <p> <code>AllowedOAuthFlows</code>: Support for authorization code, implicit, and client credentials OAuth 2.0 grants.</p> </li> </ul> <p>To use authorization server features, configure one of these features in the Amazon Cognito console or set <code>AllowedOAuthFlowsUserPoolClient</code> to <code>true</code> in a <code>CreateUserPoolClient</code> or <code>UpdateUserPoolClient</code> API request. If you don't set a value for <code>AllowedOAuthFlowsUserPoolClient</code> in a request with the CLI or SDKs, it defaults to <code>false</code>. When <code>false</code>, only SDK-based API sign-in is permitted.</p>"""
    analytics_configuration: NotRequired[
        "capo_cognito_identity_provider.types.analytics_configuration_type.AnalyticsConfigurationType"
    ]
    """<p>The user pool analytics configuration for collecting metrics and sending them to your Amazon Pinpoint campaign.</p> <p>In Amazon Web Services Regions where Amazon Pinpoint isn't available, user pools might not have access to analytics or might be configurable with campaigns in the US East (N. Virginia) Region. For more information, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-pinpoint-integration.html">Using Amazon Pinpoint analytics</a>.</p>"""
    prevent_user_existence_errors: NotRequired[
        "capo_cognito_identity_provider.types.prevent_user_existence_error_types.PreventUserExistenceErrorTypes"
    ]
    """<p>When <code>ENABLED</code>, suppresses messages that might indicate a valid user exists when someone attempts sign-in. This parameters sets your preference for the errors and responses that you want Amazon Cognito APIs to return during authentication, account confirmation, and password recovery when the user doesn't exist in the user pool. When set to <code>ENABLED</code> and the user doesn't exist, authentication returns an error indicating either the username or password was incorrect. Account confirmation and password recovery return a response indicating a code was sent to a simulated destination. When set to <code>LEGACY</code>, those APIs return a <code>UserNotFoundException</code> exception if the user doesn't exist in the user pool.</p> <p>Defaults to <code>LEGACY</code>.</p>"""
    enable_token_revocation: NotRequired[
        "capo_cognito_identity_provider.types.wrapped_boolean_type.WrappedBooleanType"
    ]
    """<p>Activates or deactivates <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/token-revocation.html">token revocation</a> in the target app client.</p>"""
    enable_propagate_additional_user_context_data: NotRequired[
        "capo_cognito_identity_provider.types.wrapped_boolean_type.WrappedBooleanType"
    ]
    """<p>When <code>true</code>, your application can include additional <code>UserContextData</code> in authentication requests. This data includes the IP address, and contributes to analysis by threat protection features. For more information about propagation of user context data, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-adaptive-authentication.html#user-pool-settings-adaptive-authentication-device-fingerprint">Adding session data to API requests</a>. If you don’t include this parameter, you can't send the source IP address to Amazon Cognito threat protection features. You can only activate <code>EnablePropagateAdditionalUserContextData</code> in an app client that has a client secret.</p>"""
    auth_session_validity: NotRequired[
        "capo_cognito_identity_provider.types.auth_session_validity_type.AuthSessionValidityType"
    ]
    """<p>Amazon Cognito creates a session token for each API request in an authentication flow. <code>AuthSessionValidity</code> is the duration, in minutes, of that session token. Your user pool native user must respond to each authentication challenge before the session expires.</p>"""
    refresh_token_rotation: NotRequired[
        "capo_cognito_identity_provider.types.refresh_token_rotation_type.RefreshTokenRotationType"
    ]
    """<p>The configuration of your app client for refresh token rotation. When enabled, your app client issues new ID, access, and refresh tokens when users renew their sessions with refresh tokens. When disabled, token refresh issues only ID and access tokens.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserPoolClientRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["ClientId"] = value["client_id"]
    if "client_name" in value:
        out["ClientName"] = value["client_name"]
    out["RefreshTokenValidity"] = value.get("refresh_token_validity", 0)
    if "access_token_validity" in value:
        out["AccessTokenValidity"] = value["access_token_validity"]
    if "id_token_validity" in value:
        out["IdTokenValidity"] = value["id_token_validity"]
    if "token_validity_units" in value:
        import capo_cognito_identity_provider.types.token_validity_units_type

        out["TokenValidityUnits"] = (
            capo_cognito_identity_provider.types.token_validity_units_type.serialize_aws_json_1_1(
                value["token_validity_units"]
            )
        )
    if "read_attributes" in value:
        import capo_cognito_identity_provider.types.client_permission_list_type

        out["ReadAttributes"] = (
            capo_cognito_identity_provider.types.client_permission_list_type.serialize_aws_json_1_1(
                value["read_attributes"]
            )
        )
    if "write_attributes" in value:
        import capo_cognito_identity_provider.types.client_permission_list_type

        out["WriteAttributes"] = (
            capo_cognito_identity_provider.types.client_permission_list_type.serialize_aws_json_1_1(
                value["write_attributes"]
            )
        )
    if "explicit_auth_flows" in value:
        import capo_cognito_identity_provider.types.explicit_auth_flows_list_type

        out["ExplicitAuthFlows"] = (
            capo_cognito_identity_provider.types.explicit_auth_flows_list_type.serialize_aws_json_1_1(
                value["explicit_auth_flows"]
            )
        )
    if "supported_identity_providers" in value:
        import capo_cognito_identity_provider.types.supported_identity_providers_list_type

        out["SupportedIdentityProviders"] = (
            capo_cognito_identity_provider.types.supported_identity_providers_list_type.serialize_aws_json_1_1(
                value["supported_identity_providers"]
            )
        )
    if "callback_ur_ls" in value:
        import capo_cognito_identity_provider.types.callback_ur_ls_list_type

        out["CallbackURLs"] = (
            capo_cognito_identity_provider.types.callback_ur_ls_list_type.serialize_aws_json_1_1(
                value["callback_ur_ls"]
            )
        )
    if "logout_ur_ls" in value:
        import capo_cognito_identity_provider.types.logout_ur_ls_list_type

        out["LogoutURLs"] = (
            capo_cognito_identity_provider.types.logout_ur_ls_list_type.serialize_aws_json_1_1(
                value["logout_ur_ls"]
            )
        )
    if "default_redirect_uri" in value:
        out["DefaultRedirectURI"] = value["default_redirect_uri"]
    if "allowed_o_auth_flows" in value:
        import capo_cognito_identity_provider.types.o_auth_flows_type

        out["AllowedOAuthFlows"] = (
            capo_cognito_identity_provider.types.o_auth_flows_type.serialize_aws_json_1_1(
                value["allowed_o_auth_flows"]
            )
        )
    if "allowed_o_auth_scopes" in value:
        import capo_cognito_identity_provider.types.scope_list_type

        out["AllowedOAuthScopes"] = (
            capo_cognito_identity_provider.types.scope_list_type.serialize_aws_json_1_1(
                value["allowed_o_auth_scopes"]
            )
        )
    out["AllowedOAuthFlowsUserPoolClient"] = value.get(
        "allowed_o_auth_flows_user_pool_client", False
    )
    if "analytics_configuration" in value:
        import capo_cognito_identity_provider.types.analytics_configuration_type

        out["AnalyticsConfiguration"] = (
            capo_cognito_identity_provider.types.analytics_configuration_type.serialize_aws_json_1_1(
                value["analytics_configuration"]
            )
        )
    if "prevent_user_existence_errors" in value:
        import capo_cognito_identity_provider.types.prevent_user_existence_error_types

        out["PreventUserExistenceErrors"] = (
            capo_cognito_identity_provider.types.prevent_user_existence_error_types.serialize_aws_json_1_1(
                value["prevent_user_existence_errors"]
            )
        )
    if "enable_token_revocation" in value:
        out["EnableTokenRevocation"] = value["enable_token_revocation"]
    if "enable_propagate_additional_user_context_data" in value:
        out["EnablePropagateAdditionalUserContextData"] = value[
            "enable_propagate_additional_user_context_data"
        ]
    if "auth_session_validity" in value:
        out["AuthSessionValidity"] = value["auth_session_validity"]
    if "refresh_token_rotation" in value:
        import capo_cognito_identity_provider.types.refresh_token_rotation_type

        out["RefreshTokenRotation"] = (
            capo_cognito_identity_provider.types.refresh_token_rotation_type.serialize_aws_json_1_1(
                value["refresh_token_rotation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserPoolClientRequest:
    out: UpdateUserPoolClientRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserPoolId") is not None:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("UpdateUserPoolClientRequest.user_pool_id required")
    if data.get("ClientId") is not None:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError("UpdateUserPoolClientRequest.client_id required")
    if data.get("ClientName") is not None:
        out["client_name"] = data["ClientName"]
    if data.get("RefreshTokenValidity") is not None:
        out["refresh_token_validity"] = data["RefreshTokenValidity"]
    else:
        out["refresh_token_validity"] = 0
    if data.get("AccessTokenValidity") is not None:
        out["access_token_validity"] = data["AccessTokenValidity"]
    if data.get("IdTokenValidity") is not None:
        out["id_token_validity"] = data["IdTokenValidity"]
    if data.get("TokenValidityUnits") is not None:
        import capo_cognito_identity_provider.types.token_validity_units_type

        out["token_validity_units"] = (
            capo_cognito_identity_provider.types.token_validity_units_type.deserialize_aws_json_1_1(
                data["TokenValidityUnits"]
            )
        )
    if data.get("ReadAttributes") is not None:
        import capo_cognito_identity_provider.types.client_permission_list_type

        out["read_attributes"] = (
            capo_cognito_identity_provider.types.client_permission_list_type.deserialize_aws_json_1_1(
                data["ReadAttributes"]
            )
        )
    if data.get("WriteAttributes") is not None:
        import capo_cognito_identity_provider.types.client_permission_list_type

        out["write_attributes"] = (
            capo_cognito_identity_provider.types.client_permission_list_type.deserialize_aws_json_1_1(
                data["WriteAttributes"]
            )
        )
    if data.get("ExplicitAuthFlows") is not None:
        import capo_cognito_identity_provider.types.explicit_auth_flows_list_type

        out["explicit_auth_flows"] = (
            capo_cognito_identity_provider.types.explicit_auth_flows_list_type.deserialize_aws_json_1_1(
                data["ExplicitAuthFlows"]
            )
        )
    if data.get("SupportedIdentityProviders") is not None:
        import capo_cognito_identity_provider.types.supported_identity_providers_list_type

        out["supported_identity_providers"] = (
            capo_cognito_identity_provider.types.supported_identity_providers_list_type.deserialize_aws_json_1_1(
                data["SupportedIdentityProviders"]
            )
        )
    if data.get("CallbackURLs") is not None:
        import capo_cognito_identity_provider.types.callback_ur_ls_list_type

        out["callback_ur_ls"] = (
            capo_cognito_identity_provider.types.callback_ur_ls_list_type.deserialize_aws_json_1_1(
                data["CallbackURLs"]
            )
        )
    if data.get("LogoutURLs") is not None:
        import capo_cognito_identity_provider.types.logout_ur_ls_list_type

        out["logout_ur_ls"] = (
            capo_cognito_identity_provider.types.logout_ur_ls_list_type.deserialize_aws_json_1_1(
                data["LogoutURLs"]
            )
        )
    if data.get("DefaultRedirectURI") is not None:
        out["default_redirect_uri"] = data["DefaultRedirectURI"]
    if data.get("AllowedOAuthFlows") is not None:
        import capo_cognito_identity_provider.types.o_auth_flows_type

        out["allowed_o_auth_flows"] = (
            capo_cognito_identity_provider.types.o_auth_flows_type.deserialize_aws_json_1_1(
                data["AllowedOAuthFlows"]
            )
        )
    if data.get("AllowedOAuthScopes") is not None:
        import capo_cognito_identity_provider.types.scope_list_type

        out["allowed_o_auth_scopes"] = (
            capo_cognito_identity_provider.types.scope_list_type.deserialize_aws_json_1_1(
                data["AllowedOAuthScopes"]
            )
        )
    if data.get("AllowedOAuthFlowsUserPoolClient") is not None:
        out["allowed_o_auth_flows_user_pool_client"] = data[
            "AllowedOAuthFlowsUserPoolClient"
        ]
    else:
        out["allowed_o_auth_flows_user_pool_client"] = False
    if data.get("AnalyticsConfiguration") is not None:
        import capo_cognito_identity_provider.types.analytics_configuration_type

        out["analytics_configuration"] = (
            capo_cognito_identity_provider.types.analytics_configuration_type.deserialize_aws_json_1_1(
                data["AnalyticsConfiguration"]
            )
        )
    if data.get("PreventUserExistenceErrors") is not None:
        import capo_cognito_identity_provider.types.prevent_user_existence_error_types

        out["prevent_user_existence_errors"] = (
            capo_cognito_identity_provider.types.prevent_user_existence_error_types.deserialize_aws_json_1_1(
                data["PreventUserExistenceErrors"]
            )
        )
    if data.get("EnableTokenRevocation") is not None:
        out["enable_token_revocation"] = data["EnableTokenRevocation"]
    if data.get("EnablePropagateAdditionalUserContextData") is not None:
        out["enable_propagate_additional_user_context_data"] = data[
            "EnablePropagateAdditionalUserContextData"
        ]
    if data.get("AuthSessionValidity") is not None:
        out["auth_session_validity"] = data["AuthSessionValidity"]
    if data.get("RefreshTokenRotation") is not None:
        import capo_cognito_identity_provider.types.refresh_token_rotation_type

        out["refresh_token_rotation"] = (
            capo_cognito_identity_provider.types.refresh_token_rotation_type.deserialize_aws_json_1_1(
                data["RefreshTokenRotation"]
            )
        )
    return out

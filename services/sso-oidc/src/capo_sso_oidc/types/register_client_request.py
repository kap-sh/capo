"""Generated from Smithy shape ``com.amazonaws.ssooidc#RegisterClientRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_oidc.types.arn_type
    import capo_sso_oidc.types.client_name
    import capo_sso_oidc.types.client_type
    import capo_sso_oidc.types.grant_types
    import capo_sso_oidc.types.redirect_uris
    import capo_sso_oidc.types.scopes
    import capo_sso_oidc.types.uri


class RegisterClientRequest(TypedDict, closed=True):
    client_name: "capo_sso_oidc.types.client_name.ClientName"
    """<p>The friendly name of the client.</p>"""
    client_type: "capo_sso_oidc.types.client_type.ClientType"
    """<p>The type of client. The service supports only <code>public</code> as a client type. Anything other than public will be rejected by the service.</p>"""
    scopes: NotRequired["capo_sso_oidc.types.scopes.Scopes"]
    """<p>The list of scopes that are defined by the client. Upon authorization, this list is used to restrict permissions when granting an access token.</p>"""
    redirect_uris: NotRequired["capo_sso_oidc.types.redirect_uris.RedirectUris"]
    """<p>The list of redirect URI that are defined by the client. At completion of authorization, this list is used to restrict what locations the user agent can be redirected back to.</p>"""
    grant_types: NotRequired["capo_sso_oidc.types.grant_types.GrantTypes"]
    """<p>The list of OAuth 2.0 grant types that are defined by the client. This list is used to restrict the token granting flows available to the client. Supports the following OAuth 2.0 grant types: Authorization Code, Device Code, and Refresh Token. </p> <p>* Authorization Code - <code>authorization_code</code> </p> <p>* Device Code - <code>urn:ietf:params:oauth:grant-type:device_code</code> </p> <p>* Refresh Token - <code>refresh_token</code> </p>"""
    issuer_url: NotRequired["capo_sso_oidc.types.uri.URI"]
    """<p>The IAM Identity Center Issuer URL associated with an instance of IAM Identity Center. This value is needed for user access to resources through the client.</p>"""
    entitled_application_arn: NotRequired["capo_sso_oidc.types.arn_type.ArnType"]
    """<p>This IAM Identity Center application ARN is used to define administrator-managed configuration for public client access to resources. At authorization, the scopes, grants, and redirect URI available to this client will be restricted by this application resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterClientRequest) -> dict:
    out: dict = {}
    out["clientName"] = value["client_name"]
    out["clientType"] = value["client_type"]
    if "scopes" in value:
        import capo_sso_oidc.types.scopes

        out["scopes"] = capo_sso_oidc.types.scopes.serialize_json(value["scopes"])
    if "redirect_uris" in value:
        import capo_sso_oidc.types.redirect_uris

        out["redirectUris"] = capo_sso_oidc.types.redirect_uris.serialize_json(
            value["redirect_uris"]
        )
    if "grant_types" in value:
        import capo_sso_oidc.types.grant_types

        out["grantTypes"] = capo_sso_oidc.types.grant_types.serialize_json(
            value["grant_types"]
        )
    if "issuer_url" in value:
        out["issuerUrl"] = value["issuer_url"]
    if "entitled_application_arn" in value:
        out["entitledApplicationArn"] = value["entitled_application_arn"]
    return out


def deserialize_json(data: dict) -> RegisterClientRequest:
    out: RegisterClientRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientName") is not None:
        out["client_name"] = data["clientName"]
    else:
        out["client_name"] = ""
    if data.get("clientType") is not None:
        out["client_type"] = data["clientType"]
    else:
        out["client_type"] = ""
    if data.get("scopes") is not None:
        import capo_sso_oidc.types.scopes

        out["scopes"] = capo_sso_oidc.types.scopes.deserialize_json(data["scopes"])
    if data.get("redirectUris") is not None:
        import capo_sso_oidc.types.redirect_uris

        out["redirect_uris"] = capo_sso_oidc.types.redirect_uris.deserialize_json(
            data["redirectUris"]
        )
    if data.get("grantTypes") is not None:
        import capo_sso_oidc.types.grant_types

        out["grant_types"] = capo_sso_oidc.types.grant_types.deserialize_json(
            data["grantTypes"]
        )
    if data.get("issuerUrl") is not None:
        out["issuer_url"] = data["issuerUrl"]
    if data.get("entitledApplicationArn") is not None:
        out["entitled_application_arn"] = data["entitledApplicationArn"]
    return out

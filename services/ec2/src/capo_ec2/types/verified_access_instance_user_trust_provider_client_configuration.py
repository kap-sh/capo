"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstanceUserTrustProviderClientConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.client_secret_type
    import capo_ec2.types.string
    import capo_ec2.types.user_trust_provider_type


class VerifiedAccessInstanceUserTrustProviderClientConfiguration(
    TypedDict, closed=True
):
    type: NotRequired["capo_ec2.types.user_trust_provider_type.UserTrustProviderType"]
    """<p>The trust provider type.</p>"""
    scopes: NotRequired["capo_ec2.types.string.String"]
    """<p>The set of user claims to be requested from the IdP.</p>"""
    issuer: NotRequired["capo_ec2.types.string.String"]
    """<p>The OIDC issuer identifier of the IdP.</p>"""
    authorization_endpoint: NotRequired["capo_ec2.types.string.String"]
    """<p>The authorization endpoint of the IdP.</p>"""
    public_signing_key_endpoint: NotRequired["capo_ec2.types.string.String"]
    """<p>The public signing key endpoint.</p>"""
    token_endpoint: NotRequired["capo_ec2.types.string.String"]
    """<p>The token endpoint of the IdP.</p>"""
    user_info_endpoint: NotRequired["capo_ec2.types.string.String"]
    """<p>The user info endpoint of the IdP.</p>"""
    client_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The OAuth 2.0 client identifier.</p>"""
    client_secret: NotRequired["capo_ec2.types.client_secret_type.ClientSecretType"]
    """<p>The OAuth 2.0 client secret.</p>"""
    pkce_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether Proof of Key Code Exchange (PKCE) is enabled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessInstanceUserTrustProviderClientConfiguration,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type" in value:
        import capo_ec2.types.user_trust_provider_type

        capo_ec2.types.user_trust_provider_type.serialize_ec2_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "scopes" in value:
        pairs.append((f"{key_prefix}Scopes", str(value["scopes"])))
    if "issuer" in value:
        pairs.append((f"{key_prefix}Issuer", str(value["issuer"])))
    if "authorization_endpoint" in value:
        pairs.append(
            (f"{key_prefix}AuthorizationEndpoint", str(value["authorization_endpoint"]))
        )
    if "public_signing_key_endpoint" in value:
        pairs.append(
            (
                f"{key_prefix}PublicSigningKeyEndpoint",
                str(value["public_signing_key_endpoint"]),
            )
        )
    if "token_endpoint" in value:
        pairs.append((f"{key_prefix}TokenEndpoint", str(value["token_endpoint"])))
    if "user_info_endpoint" in value:
        pairs.append(
            (f"{key_prefix}UserInfoEndpoint", str(value["user_info_endpoint"]))
        )
    if "client_id" in value:
        pairs.append((f"{key_prefix}ClientId", str(value["client_id"])))
    if "client_secret" in value:
        pairs.append((f"{key_prefix}ClientSecret", str(value["client_secret"])))
    if "pkce_enabled" in value:
        pairs.append(
            (f"{key_prefix}PkceEnabled", "true" if value["pkce_enabled"] else "false")
        )


def deserialize_ec2_query(
    el: Element,
) -> VerifiedAccessInstanceUserTrustProviderClientConfiguration:
    out: VerifiedAccessInstanceUserTrustProviderClientConfiguration = {}  # type: ignore[typeddict-item]
    child_type = el.find("type")
    if child_type is not None:
        import capo_ec2.types.user_trust_provider_type

        out["type"] = capo_ec2.types.user_trust_provider_type.deserialize_ec2_query(
            child_type
        )
    child_scopes = el.find("scopes")
    if child_scopes is not None:
        out["scopes"] = str(child_scopes.text or "")
    child_issuer = el.find("issuer")
    if child_issuer is not None:
        out["issuer"] = str(child_issuer.text or "")
    child_authorization_endpoint = el.find("authorizationEndpoint")
    if child_authorization_endpoint is not None:
        out["authorization_endpoint"] = str(child_authorization_endpoint.text or "")
    child_public_signing_key_endpoint = el.find("publicSigningKeyEndpoint")
    if child_public_signing_key_endpoint is not None:
        out["public_signing_key_endpoint"] = str(
            child_public_signing_key_endpoint.text or ""
        )
    child_token_endpoint = el.find("tokenEndpoint")
    if child_token_endpoint is not None:
        out["token_endpoint"] = str(child_token_endpoint.text or "")
    child_user_info_endpoint = el.find("userInfoEndpoint")
    if child_user_info_endpoint is not None:
        out["user_info_endpoint"] = str(child_user_info_endpoint.text or "")
    child_client_id = el.find("clientId")
    if child_client_id is not None:
        out["client_id"] = str(child_client_id.text or "")
    child_client_secret = el.find("clientSecret")
    if child_client_secret is not None:
        out["client_secret"] = str(child_client_secret.text or "")
    child_pkce_enabled = el.find("pkceEnabled")
    if child_pkce_enabled is not None:
        out["pkce_enabled"] = (child_pkce_enabled.text or "").lower() == "true"
    return out


def redact_sensitive(
    value: VerifiedAccessInstanceUserTrustProviderClientConfiguration,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out

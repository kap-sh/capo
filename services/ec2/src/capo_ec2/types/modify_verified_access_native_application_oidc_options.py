"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessNativeApplicationOidcOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_secret_type
    import capo_ec2.types.string


class ModifyVerifiedAccessNativeApplicationOidcOptions(TypedDict, closed=True):
    public_signing_key_endpoint: NotRequired["capo_ec2.types.string.String"]
    """<p>The public signing key endpoint.</p>"""
    issuer: NotRequired["capo_ec2.types.string.String"]
    """<p>The OIDC issuer identifier of the IdP.</p>"""
    authorization_endpoint: NotRequired["capo_ec2.types.string.String"]
    """<p>The authorization endpoint of the IdP.</p>"""
    token_endpoint: NotRequired["capo_ec2.types.string.String"]
    """<p>The token endpoint of the IdP.</p>"""
    user_info_endpoint: NotRequired["capo_ec2.types.string.String"]
    """<p>The user info endpoint of the IdP.</p>"""
    client_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The OAuth 2.0 client identifier.</p>"""
    client_secret: NotRequired["capo_ec2.types.client_secret_type.ClientSecretType"]
    """<p>The OAuth 2.0 client secret.</p>"""
    scope: NotRequired["capo_ec2.types.string.String"]
    """<p>The set of user claims to be requested from the IdP.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVerifiedAccessNativeApplicationOidcOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "public_signing_key_endpoint" in value:
        pairs.append(
            (
                f"{key_prefix}PublicSigningKeyEndpoint",
                str(value["public_signing_key_endpoint"]),
            )
        )
    if "issuer" in value:
        pairs.append((f"{key_prefix}Issuer", str(value["issuer"])))
    if "authorization_endpoint" in value:
        pairs.append(
            (f"{key_prefix}AuthorizationEndpoint", str(value["authorization_endpoint"]))
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
    if "scope" in value:
        pairs.append((f"{key_prefix}Scope", str(value["scope"])))


def deserialize_ec2_query(
    el: Element,
) -> ModifyVerifiedAccessNativeApplicationOidcOptions:
    out: ModifyVerifiedAccessNativeApplicationOidcOptions = {}  # type: ignore[typeddict-item]
    child_public_signing_key_endpoint = el.find("PublicSigningKeyEndpoint")
    if child_public_signing_key_endpoint is not None:
        out["public_signing_key_endpoint"] = str(
            child_public_signing_key_endpoint.text or ""
        )
    child_issuer = el.find("Issuer")
    if child_issuer is not None:
        out["issuer"] = str(child_issuer.text or "")
    child_authorization_endpoint = el.find("AuthorizationEndpoint")
    if child_authorization_endpoint is not None:
        out["authorization_endpoint"] = str(child_authorization_endpoint.text or "")
    child_token_endpoint = el.find("TokenEndpoint")
    if child_token_endpoint is not None:
        out["token_endpoint"] = str(child_token_endpoint.text or "")
    child_user_info_endpoint = el.find("UserInfoEndpoint")
    if child_user_info_endpoint is not None:
        out["user_info_endpoint"] = str(child_user_info_endpoint.text or "")
    child_client_id = el.find("ClientId")
    if child_client_id is not None:
        out["client_id"] = str(child_client_id.text or "")
    child_client_secret = el.find("ClientSecret")
    if child_client_secret is not None:
        out["client_secret"] = str(child_client_secret.text or "")
    child_scope = el.find("Scope")
    if child_scope is not None:
        out["scope"] = str(child_scope.text or "")
    return out


def redact_sensitive(
    value: ModifyVerifiedAccessNativeApplicationOidcOptions,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out

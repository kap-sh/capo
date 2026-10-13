"""Generated from Smithy shape ``com.amazonaws.ec2#OidcOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_secret_type
    import capo_ec2.types.string


class OidcOptions(TypedDict, closed=True):
    issuer: NotRequired["capo_ec2.types.string.String"]
    """<p>The OIDC issuer.</p>"""
    authorization_endpoint: NotRequired["capo_ec2.types.string.String"]
    """<p>The OIDC authorization endpoint.</p>"""
    token_endpoint: NotRequired["capo_ec2.types.string.String"]
    """<p>The OIDC token endpoint.</p>"""
    user_info_endpoint: NotRequired["capo_ec2.types.string.String"]
    """<p>The OIDC user info endpoint.</p>"""
    client_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The client identifier.</p>"""
    client_secret: NotRequired["capo_ec2.types.client_secret_type.ClientSecretType"]
    """<p>The client secret.</p>"""
    scope: NotRequired["capo_ec2.types.string.String"]
    """<p>The OpenID Connect (OIDC) scope specified.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: OidcOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
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


def deserialize_ec2_query(el: Element) -> OidcOptions:
    out: OidcOptions = {}  # type: ignore[typeddict-item]
    child_issuer = el.find("issuer")
    if child_issuer is not None:
        out["issuer"] = str(child_issuer.text or "")
    child_authorization_endpoint = el.find("authorizationEndpoint")
    if child_authorization_endpoint is not None:
        out["authorization_endpoint"] = str(child_authorization_endpoint.text or "")
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
    child_scope = el.find("scope")
    if child_scope is not None:
        out["scope"] = str(child_scope.text or "")
    return out


def redact_sensitive(value: OidcOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_secret" in value:
        out["client_secret"] = "*** Sensitive Data Redacted ***"
    return out

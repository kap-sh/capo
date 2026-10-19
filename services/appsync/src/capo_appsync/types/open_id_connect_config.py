"""Generated from Smithy shape ``com.amazonaws.appsync#OpenIDConnectConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.long
    import capo_appsync.types.string


class OpenIDConnectConfig(TypedDict, closed=True):
    issuer: "capo_appsync.types.string.String"
    """<p>The issuer for the OIDC configuration. The issuer returned by discovery must exactly match the value of <code>iss</code> in the ID token.</p>"""
    client_id: NotRequired["capo_appsync.types.string.String"]
    """<p>The client identifier of the relying party at the OpenID identity provider. This identifier is typically obtained when the relying party is registered with the OpenID identity provider. You can specify a regular expression so that AppSync can validate against multiple client identifiers at a time.</p>"""
    iat_ttl: "capo_appsync.types.long.Long"
    """<p>The number of milliseconds that a token is valid after it's issued to a user.</p>"""
    auth_ttl: "capo_appsync.types.long.Long"
    """<p>The number of milliseconds that a token is valid after being authenticated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenIDConnectConfig) -> dict:
    out: dict = {}
    out["issuer"] = value["issuer"]
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    out["iatTTL"] = value.get("iat_ttl", 0)
    out["authTTL"] = value.get("auth_ttl", 0)
    return out


def deserialize_json(data: dict) -> OpenIDConnectConfig:
    out: OpenIDConnectConfig = {}  # type: ignore[typeddict-item]
    if data.get("issuer") is not None:
        out["issuer"] = data["issuer"]
    else:
        out["issuer"] = ""
    if data.get("clientId") is not None:
        out["client_id"] = data["clientId"]
    if data.get("iatTTL") is not None:
        out["iat_ttl"] = data["iatTTL"]
    else:
        out["iat_ttl"] = 0
    if data.get("authTTL") is not None:
        out["auth_ttl"] = data["authTTL"]
    else:
        out["auth_ttl"] = 0
    return out

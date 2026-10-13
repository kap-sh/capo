"""Generated from Smithy shape ``com.amazonaws.sts#GetWebIdentityTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.date_type
    import capo_sts.types.web_identity_token_type


class GetWebIdentityTokenResponse(TypedDict, closed=True):
    web_identity_token: NotRequired[
        "capo_sts.types.web_identity_token_type.webIdentityTokenType"
    ]
    """<p>A signed JSON Web Token (JWT) that represents the caller's Amazon Web Services identity. The token contains standard JWT claims such as subject, audience, expiration time, and additional identity attributes added by STS as custom claims. You can also add your own custom claims to the token by passing tags as request parameters to the <code>GetWebIdentityToken</code> API. The token is signed using the specified signing algorithm and can be verified using the verification keys available at the issuer's JWKS endpoint.</p>"""
    expiration: NotRequired["capo_sts.types.date_type.dateType"]
    """<p>The date and time when the web identity token expires, in UTC. The expiration is determined by adding the <code>DurationSeconds</code> value to the time the token was issued. After this time, the token should no longer be considered valid.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetWebIdentityTokenResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "web_identity_token" in value:
        pairs.append(
            (f"{key_prefix}WebIdentityToken", str(value["web_identity_token"]))
        )
    if "expiration" in value:
        import capo_sts.types.date_type

        capo_sts.types.date_type.serialize_query(
            value["expiration"], pairs, f"{key_prefix}Expiration"
        )


def deserialize_query(el: Element) -> GetWebIdentityTokenResponse:
    out: GetWebIdentityTokenResponse = {}  # type: ignore[typeddict-item]
    child_web_identity_token = el.find("WebIdentityToken")
    if child_web_identity_token is not None:
        out["web_identity_token"] = str(child_web_identity_token.text or "")
    child_expiration = el.find("Expiration")
    if child_expiration is not None:
        import capo_sts.types.date_type

        out["expiration"] = capo_sts.types.date_type.deserialize_query(child_expiration)
    return out


def redact_sensitive(value: GetWebIdentityTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "web_identity_token" in value:
        out["web_identity_token"] = "*** Sensitive Data Redacted ***"
    return out

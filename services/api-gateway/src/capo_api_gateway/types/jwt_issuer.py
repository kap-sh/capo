"""Generated from Smithy shape ``com.amazonaws.apigateway#JwtIssuer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_jwt_additional_claim
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.string


class JwtIssuer(TypedDict, closed=True):
    issuer: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The OpenID Connect (OIDC) issuer URL.</p>"""
    audiences: NotRequired["capo_api_gateway.types.list_of_string.ListOfString"]
    """<p>The audiences that the issuer can issue tokens for.</p>"""
    additional_claims: NotRequired[
        "capo_api_gateway.types.list_of_jwt_additional_claim.ListOfJwtAdditionalClaim"
    ]
    """<p>The additional claim rules configured for this issuer.</p>"""
    jwks_uri: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The JSON Web Key Set (JWKS) URI that API Gateway resolved from the issuer's OpenID Connect discovery document. This value is read-only and cannot be set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JwtIssuer) -> dict:
    out: dict = {}
    if "issuer" in value:
        out["issuer"] = value["issuer"]
    if "audiences" in value:
        import capo_api_gateway.types.list_of_string

        out["audiences"] = capo_api_gateway.types.list_of_string.serialize_json(
            value["audiences"]
        )
    if "additional_claims" in value:
        import capo_api_gateway.types.list_of_jwt_additional_claim

        out["additionalClaims"] = (
            capo_api_gateway.types.list_of_jwt_additional_claim.serialize_json(
                value["additional_claims"]
            )
        )
    if "jwks_uri" in value:
        out["jwksUri"] = value["jwks_uri"]
    return out


def deserialize_json(data: dict) -> JwtIssuer:
    out: JwtIssuer = {}  # type: ignore[typeddict-item]
    if data.get("issuer") is not None:
        out["issuer"] = data["issuer"]
    if data.get("audiences") is not None:
        import capo_api_gateway.types.list_of_string

        out["audiences"] = capo_api_gateway.types.list_of_string.deserialize_json(
            data["audiences"]
        )
    if data.get("additionalClaims") is not None:
        import capo_api_gateway.types.list_of_jwt_additional_claim

        out["additional_claims"] = (
            capo_api_gateway.types.list_of_jwt_additional_claim.deserialize_json(
                data["additionalClaims"]
            )
        )
    if data.get("jwksUri") is not None:
        out["jwks_uri"] = data["jwksUri"]
    return out

"""Generated from Smithy shape ``com.amazonaws.apigateway#JwtIssuerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_jwt_additional_claim
    import capo_api_gateway.types.list_of_string
    import capo_api_gateway.types.string


class JwtIssuerInput(TypedDict, closed=True):
    issuer: "capo_api_gateway.types.string.String"
    """<p>The OpenID Connect (OIDC) issuer URL. The value must be an absolute <code>https</code> URL that includes a host and has no user information, query, or fragment. It must exactly match the <code>iss</code> claim of the token, and the issuer's OIDC discovery document must name this exact issuer.</p>"""
    audiences: "capo_api_gateway.types.list_of_string.ListOfString"
    """<p>The audiences that the issuer can issue tokens for. None can be empty. The token's <code>aud</code> claim must contain at least one of these values.</p>"""
    additional_claims: NotRequired[
        "capo_api_gateway.types.list_of_jwt_additional_claim.ListOfJwtAdditionalClaim"
    ]
    """<p>The additional claim rules for this issuer. Claim names must be unique within the issuer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JwtIssuerInput) -> dict:
    out: dict = {}
    out["issuer"] = value["issuer"]
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
    return out


def deserialize_json(data: dict) -> JwtIssuerInput:
    out: JwtIssuerInput = {}  # type: ignore[typeddict-item]
    if data.get("issuer") is not None:
        out["issuer"] = data["issuer"]
    else:
        out["issuer"] = ""
    if data.get("audiences") is not None:
        import capo_api_gateway.types.list_of_string

        out["audiences"] = capo_api_gateway.types.list_of_string.deserialize_json(
            data["audiences"]
        )
    else:
        out["audiences"] = []
    if data.get("additionalClaims") is not None:
        import capo_api_gateway.types.list_of_jwt_additional_claim

        out["additional_claims"] = (
            capo_api_gateway.types.list_of_jwt_additional_claim.deserialize_json(
                data["additionalClaims"]
            )
        )
    return out

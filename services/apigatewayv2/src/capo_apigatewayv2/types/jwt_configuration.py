"""Generated from Smithy shape ``com.amazonaws.apigatewayv2#JWTConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apigatewayv2.types.__list_of__string
    import capo_apigatewayv2.types.uri_with_length_between1_and2048


class JWTConfiguration(TypedDict, closed=True):
    audience: NotRequired["capo_apigatewayv2.types.__list_of__string.__listOf__string"]
    """<p>A list of the intended recipients of the JWT. A valid JWT must provide an aud that matches at least one entry in this list. See <a href="https://tools.ietf.org/html/rfc7519#section-4.1.3">RFC 7519</a>. Supported only for HTTP APIs.</p>"""
    issuer: NotRequired[
        "capo_apigatewayv2.types.uri_with_length_between1_and2048.UriWithLengthBetween1And2048"
    ]
    """<p>The base domain of the identity provider that issues JSON Web Tokens. For example, an Amazon Cognito user pool has the following format: https://cognito-idp.<replaceable>{region}</replaceable>.amazonaws.com/<replaceable>{userPoolId}</replaceable> . Required for the JWT authorizer type. Supported only for HTTP APIs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JWTConfiguration) -> dict:
    out: dict = {}
    if "audience" in value:
        import capo_apigatewayv2.types.__list_of__string

        out["audience"] = capo_apigatewayv2.types.__list_of__string.serialize_json(
            value["audience"]
        )
    if "issuer" in value:
        out["issuer"] = value["issuer"]
    return out


def deserialize_json(data: dict) -> JWTConfiguration:
    out: JWTConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("audience") is not None:
        import capo_apigatewayv2.types.__list_of__string

        out["audience"] = capo_apigatewayv2.types.__list_of__string.deserialize_json(
            data["audience"]
        )
    if data.get("issuer") is not None:
        out["issuer"] = data["issuer"]
    return out

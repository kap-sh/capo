"""Generated from Smithy shape ``com.amazonaws.apigateway#JwtConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_jwt_issuer
    import capo_api_gateway.types.list_of_jwt_signing_algorithm


class JwtConfiguration(TypedDict, closed=True):
    issuers: NotRequired["capo_api_gateway.types.list_of_jwt_issuer.ListOfJwtIssuer"]
    """<p>The trusted issuers configured for the authorizer.</p>"""
    default_algorithms: NotRequired[
        "capo_api_gateway.types.list_of_jwt_signing_algorithm.ListOfJwtSigningAlgorithm"
    ]
    """<p>The signing algorithms configured for the authorizer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JwtConfiguration) -> dict:
    out: dict = {}
    if "issuers" in value:
        import capo_api_gateway.types.list_of_jwt_issuer

        out["issuers"] = capo_api_gateway.types.list_of_jwt_issuer.serialize_json(
            value["issuers"]
        )
    if "default_algorithms" in value:
        import capo_api_gateway.types.list_of_jwt_signing_algorithm

        out["defaultAlgorithms"] = (
            capo_api_gateway.types.list_of_jwt_signing_algorithm.serialize_json(
                value["default_algorithms"]
            )
        )
    return out


def deserialize_json(data: dict) -> JwtConfiguration:
    out: JwtConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("issuers") is not None:
        import capo_api_gateway.types.list_of_jwt_issuer

        out["issuers"] = capo_api_gateway.types.list_of_jwt_issuer.deserialize_json(
            data["issuers"]
        )
    if data.get("defaultAlgorithms") is not None:
        import capo_api_gateway.types.list_of_jwt_signing_algorithm

        out["default_algorithms"] = (
            capo_api_gateway.types.list_of_jwt_signing_algorithm.deserialize_json(
                data["defaultAlgorithms"]
            )
        )
    return out

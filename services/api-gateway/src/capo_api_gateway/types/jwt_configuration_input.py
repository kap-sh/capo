"""Generated from Smithy shape ``com.amazonaws.apigateway#JwtConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_jwt_issuer_input
    import capo_api_gateway.types.list_of_jwt_signing_algorithm


class JwtConfigurationInput(TypedDict, closed=True):
    issuers: "capo_api_gateway.types.list_of_jwt_issuer_input.ListOfJwtIssuerInput"
    """<p>The issuers that the authorizer trusts. Issuer URLs must be unique.</p>"""
    default_algorithms: (
        "capo_api_gateway.types.list_of_jwt_signing_algorithm.ListOfJwtSigningAlgorithm"
    )
    """<p>The signing algorithms that the authorizer accepts, applied to every issuer. Valid values are <code>RS256</code>, <code>RS384</code>, <code>RS512</code>, <code>ES256</code>, <code>ES384</code>, and <code>ES512</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JwtConfigurationInput) -> dict:
    out: dict = {}
    import capo_api_gateway.types.list_of_jwt_issuer_input

    out["issuers"] = capo_api_gateway.types.list_of_jwt_issuer_input.serialize_json(
        value["issuers"]
    )
    import capo_api_gateway.types.list_of_jwt_signing_algorithm

    out["defaultAlgorithms"] = (
        capo_api_gateway.types.list_of_jwt_signing_algorithm.serialize_json(
            value["default_algorithms"]
        )
    )
    return out


def deserialize_json(data: dict) -> JwtConfigurationInput:
    out: JwtConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("issuers") is not None:
        import capo_api_gateway.types.list_of_jwt_issuer_input

        out["issuers"] = (
            capo_api_gateway.types.list_of_jwt_issuer_input.deserialize_json(
                data["issuers"]
            )
        )
    else:
        out["issuers"] = []
    if data.get("defaultAlgorithms") is not None:
        import capo_api_gateway.types.list_of_jwt_signing_algorithm

        out["default_algorithms"] = (
            capo_api_gateway.types.list_of_jwt_signing_algorithm.deserialize_json(
                data["defaultAlgorithms"]
            )
        )
    else:
        out["default_algorithms"] = []
    return out

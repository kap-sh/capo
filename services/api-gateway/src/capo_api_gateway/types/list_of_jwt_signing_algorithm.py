"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfJwtSigningAlgorithm``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.jwt_signing_algorithm

ListOfJwtSigningAlgorithm: TypeAlias = list[
    "capo_api_gateway.types.jwt_signing_algorithm.JwtSigningAlgorithm"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfJwtSigningAlgorithm) -> list:
    import capo_api_gateway.types.jwt_signing_algorithm

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.jwt_signing_algorithm.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfJwtSigningAlgorithm:
    import capo_api_gateway.types.jwt_signing_algorithm

    out: ListOfJwtSigningAlgorithm = []
    for item in data:
        if item is None:
            continue
        out.append(capo_api_gateway.types.jwt_signing_algorithm.deserialize_json(item))
    return out

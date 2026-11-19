"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfJwtAdditionalClaim``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.jwt_additional_claim

ListOfJwtAdditionalClaim: TypeAlias = list[
    "capo_api_gateway.types.jwt_additional_claim.JwtAdditionalClaim"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfJwtAdditionalClaim) -> list:
    import capo_api_gateway.types.jwt_additional_claim

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.jwt_additional_claim.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfJwtAdditionalClaim:
    import capo_api_gateway.types.jwt_additional_claim

    out: ListOfJwtAdditionalClaim = []
    for item in data:
        if item is None:
            continue
        out.append(capo_api_gateway.types.jwt_additional_claim.deserialize_json(item))
    return out

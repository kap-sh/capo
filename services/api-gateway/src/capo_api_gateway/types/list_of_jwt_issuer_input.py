"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfJwtIssuerInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.jwt_issuer_input

ListOfJwtIssuerInput: TypeAlias = list[
    "capo_api_gateway.types.jwt_issuer_input.JwtIssuerInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfJwtIssuerInput) -> list:
    import capo_api_gateway.types.jwt_issuer_input

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.jwt_issuer_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfJwtIssuerInput:
    import capo_api_gateway.types.jwt_issuer_input

    out: ListOfJwtIssuerInput = []
    for item in data:
        if item is None:
            continue
        out.append(capo_api_gateway.types.jwt_issuer_input.deserialize_json(item))
    return out

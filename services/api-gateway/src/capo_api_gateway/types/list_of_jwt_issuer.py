"""Generated from Smithy shape ``com.amazonaws.apigateway#ListOfJwtIssuer``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.jwt_issuer

ListOfJwtIssuer: TypeAlias = list["capo_api_gateway.types.jwt_issuer.JwtIssuer"]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfJwtIssuer) -> list:
    import capo_api_gateway.types.jwt_issuer

    out: list = []
    for item in value:
        out.append(capo_api_gateway.types.jwt_issuer.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfJwtIssuer:
    import capo_api_gateway.types.jwt_issuer

    out: ListOfJwtIssuer = []
    for item in data:
        if item is None:
            continue
        out.append(capo_api_gateway.types.jwt_issuer.deserialize_json(item))
    return out

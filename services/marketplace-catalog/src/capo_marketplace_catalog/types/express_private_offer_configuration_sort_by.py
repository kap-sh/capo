"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ExpressPrivateOfferConfigurationSortBy``."""

from typing import Literal, TypeAlias, cast

ExpressPrivateOfferConfigurationSortBy: TypeAlias = Literal[
    "EntityId",
    "LastModifiedDate",
    "ProductId",
    "State",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExpressPrivateOfferConfigurationSortBy) -> str:
    return value


def deserialize_json(data: str) -> ExpressPrivateOfferConfigurationSortBy:
    return cast(ExpressPrivateOfferConfigurationSortBy, data)

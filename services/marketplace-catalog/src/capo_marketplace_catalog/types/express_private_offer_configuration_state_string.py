"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ExpressPrivateOfferConfigurationStateString``."""

from typing import Literal, TypeAlias, cast

ExpressPrivateOfferConfigurationStateString: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExpressPrivateOfferConfigurationStateString) -> str:
    return value


def deserialize_json(data: str) -> ExpressPrivateOfferConfigurationStateString:
    return cast(ExpressPrivateOfferConfigurationStateString, data)

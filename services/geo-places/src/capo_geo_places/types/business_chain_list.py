"""Generated from Smithy shape ``com.amazonaws.geoplaces#BusinessChainList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_geo_places.types.business_chain

BusinessChainList: TypeAlias = list[
    "capo_geo_places.types.business_chain.BusinessChain"
]


# --- restJson1 ser/de ---
def serialize_json(value: BusinessChainList) -> list:
    import capo_geo_places.types.business_chain

    out: list = []
    for item in value:
        out.append(capo_geo_places.types.business_chain.serialize_json(item))
    return out


def deserialize_json(data: list) -> BusinessChainList:
    import capo_geo_places.types.business_chain

    out: BusinessChainList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_geo_places.types.business_chain.deserialize_json(item))
    return out


def redact_sensitive(value: BusinessChainList) -> list[Any]:
    import capo_geo_places.types.business_chain

    return [
        capo_geo_places.types.business_chain.redact_sensitive(item) for item in value
    ]

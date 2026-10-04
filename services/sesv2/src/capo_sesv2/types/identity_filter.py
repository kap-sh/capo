"""Generated from Smithy shape ``com.amazonaws.sesv2#IdentityFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.identity_filter_key
    import capo_sesv2.types.identity_filter_value

IdentityFilter: TypeAlias = dict[
    "capo_sesv2.types.identity_filter_key.IdentityFilterKey",
    "capo_sesv2.types.identity_filter_value.IdentityFilterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: IdentityFilter) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sesv2.types.identity_filter_key

        out[capo_sesv2.types.identity_filter_key.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> IdentityFilter:
    out: IdentityFilter = {}
    for key, value in data.items():
        import capo_sesv2.types.identity_filter_key

        if value is None:
            continue
        out[capo_sesv2.types.identity_filter_key.deserialize_json(key)] = value
    return out

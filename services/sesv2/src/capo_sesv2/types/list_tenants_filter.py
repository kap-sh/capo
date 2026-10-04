"""Generated from Smithy shape ``com.amazonaws.sesv2#ListTenantsFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.list_tenants_filter_key
    import capo_sesv2.types.list_tenants_filter_value

ListTenantsFilter: TypeAlias = dict[
    "capo_sesv2.types.list_tenants_filter_key.ListTenantsFilterKey",
    "capo_sesv2.types.list_tenants_filter_value.ListTenantsFilterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ListTenantsFilter) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_sesv2.types.list_tenants_filter_key

        out[capo_sesv2.types.list_tenants_filter_key.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> ListTenantsFilter:
    out: ListTenantsFilter = {}
    for key, value in data.items():
        import capo_sesv2.types.list_tenants_filter_key

        if value is None:
            continue
        out[capo_sesv2.types.list_tenants_filter_key.deserialize_json(key)] = value
    return out

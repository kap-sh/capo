"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#FilterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridgev2.types.filter

FilterList: TypeAlias = list["capo_eventbridgev2.types.filter.Filter"]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FilterList) -> list:
    import capo_eventbridgev2.types.filter

    out: list = []
    for item in value:
        out.append(capo_eventbridgev2.types.filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> FilterList:
    import capo_eventbridgev2.types.filter

    out: FilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_eventbridgev2.types.filter.deserialize_cbor(item))
    return out


def redact_sensitive(value: FilterList) -> list[Any]:
    import capo_eventbridgev2.types.filter

    return [capo_eventbridgev2.types.filter.redact_sensitive(item) for item in value]

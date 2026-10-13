"""Generated from Smithy shape ``com.amazonaws.novaact#Calls``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_nova_act.types.call

Calls: TypeAlias = list["capo_nova_act.types.call.Call"]


# --- restJson1 ser/de ---
def serialize_json(value: Calls) -> list:
    import capo_nova_act.types.call

    out: list = []
    for item in value:
        out.append(capo_nova_act.types.call.serialize_json(item))
    return out


def deserialize_json(data: list) -> Calls:
    import capo_nova_act.types.call

    out: Calls = []
    for item in data:
        if item is None:
            continue
        out.append(capo_nova_act.types.call.deserialize_json(item))
    return out


def redact_sensitive(value: Calls) -> list[Any]:
    import capo_nova_act.types.call

    return [capo_nova_act.types.call.redact_sensitive(item) for item in value]

"""Generated from Smithy shape ``com.amazonaws.novaact#CallResults``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_nova_act.types.call_result

CallResults: TypeAlias = list["capo_nova_act.types.call_result.CallResult"]


# --- restJson1 ser/de ---
def serialize_json(value: CallResults) -> list:
    import capo_nova_act.types.call_result

    out: list = []
    for item in value:
        out.append(capo_nova_act.types.call_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> CallResults:
    import capo_nova_act.types.call_result

    out: CallResults = []
    for item in data:
        if item is None:
            continue
        out.append(capo_nova_act.types.call_result.deserialize_json(item))
    return out


def redact_sensitive(value: CallResults) -> list[Any]:
    import capo_nova_act.types.call_result

    return [capo_nova_act.types.call_result.redact_sensitive(item) for item in value]

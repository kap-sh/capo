"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#ActiveContextsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.active_context

ActiveContextsList: TypeAlias = list[
    "capo_lex_runtime_v2.types.active_context.ActiveContext"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActiveContextsList) -> list:
    import capo_lex_runtime_v2.types.active_context

    out: list = []
    for item in value:
        out.append(capo_lex_runtime_v2.types.active_context.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActiveContextsList:
    import capo_lex_runtime_v2.types.active_context

    out: ActiveContextsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lex_runtime_v2.types.active_context.deserialize_json(item))
    return out


def redact_sensitive(value: ActiveContextsList) -> list[Any]:
    import capo_lex_runtime_v2.types.active_context

    return [
        capo_lex_runtime_v2.types.active_context.redact_sensitive(item)
        for item in value
    ]

"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#Messages``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.message

Messages: TypeAlias = list["capo_lex_runtime_v2.types.message.Message"]


# --- restJson1 ser/de ---
def serialize_json(value: Messages) -> list:
    import capo_lex_runtime_v2.types.message

    out: list = []
    for item in value:
        out.append(capo_lex_runtime_v2.types.message.serialize_json(item))
    return out


def deserialize_json(data: list) -> Messages:
    import capo_lex_runtime_v2.types.message

    out: Messages = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lex_runtime_v2.types.message.deserialize_json(item))
    return out


def redact_sensitive(value: Messages) -> list[Any]:
    import capo_lex_runtime_v2.types.message

    return [capo_lex_runtime_v2.types.message.redact_sensitive(item) for item in value]

"""Generated from Smithy shape ``com.amazonaws.novaact#CallResultContents``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_nova_act.types.call_result_content

CallResultContents: TypeAlias = list[
    "capo_nova_act.types.call_result_content.CallResultContent"
]


# --- restJson1 ser/de ---
def serialize_json(value: CallResultContents) -> list:
    import capo_nova_act.types.call_result_content

    out: list = []
    for item in value:
        out.append(capo_nova_act.types.call_result_content.serialize_json(item))
    return out


def deserialize_json(data: list) -> CallResultContents:
    import capo_nova_act.types.call_result_content

    out: CallResultContents = []
    for item in data:
        if item is None:
            continue
        out.append(capo_nova_act.types.call_result_content.deserialize_json(item))
    return out


def redact_sensitive(value: CallResultContents) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)

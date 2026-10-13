"""Generated from Smithy shape ``com.amazonaws.lambda#Events``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.event

Events: TypeAlias = list["capo_lambda.types.event.Event"]


# --- restJson1 ser/de ---
def serialize_json(value: Events) -> list:
    import capo_lambda.types.event

    out: list = []
    for item in value:
        out.append(capo_lambda.types.event.serialize_json(item))
    return out


def deserialize_json(data: list) -> Events:
    import capo_lambda.types.event

    out: Events = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda.types.event.deserialize_json(item))
    return out


def redact_sensitive(value: Events) -> list[Any]:
    import capo_lambda.types.event

    return [capo_lambda.types.event.redact_sensitive(item) for item in value]

"""Generated from Smithy shape ``com.amazonaws.lambda#Operations``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.operation

Operations: TypeAlias = list["capo_lambda.types.operation.Operation"]


# --- restJson1 ser/de ---
def serialize_json(value: Operations) -> list:
    import capo_lambda.types.operation

    out: list = []
    for item in value:
        out.append(capo_lambda.types.operation.serialize_json(item))
    return out


def deserialize_json(data: list) -> Operations:
    import capo_lambda.types.operation

    out: Operations = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda.types.operation.deserialize_json(item))
    return out


def redact_sensitive(value: Operations) -> list[Any]:
    import capo_lambda.types.operation

    return [capo_lambda.types.operation.redact_sensitive(item) for item in value]

"""Generated from Smithy shape ``com.amazonaws.lambda#OperationUpdates``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.operation_update

OperationUpdates: TypeAlias = list["capo_lambda.types.operation_update.OperationUpdate"]


# --- restJson1 ser/de ---
def serialize_json(value: OperationUpdates) -> list:
    import capo_lambda.types.operation_update

    out: list = []
    for item in value:
        out.append(capo_lambda.types.operation_update.serialize_json(item))
    return out


def deserialize_json(data: list) -> OperationUpdates:
    import capo_lambda.types.operation_update

    out: OperationUpdates = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda.types.operation_update.deserialize_json(item))
    return out


def redact_sensitive(value: OperationUpdates) -> list[Any]:
    import capo_lambda.types.operation_update

    return [capo_lambda.types.operation_update.redact_sensitive(item) for item in value]

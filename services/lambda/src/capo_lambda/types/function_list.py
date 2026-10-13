"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_lambda.types.function_configuration

FunctionList: TypeAlias = list[
    "capo_lambda.types.function_configuration.FunctionConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: FunctionList) -> list:
    import capo_lambda.types.function_configuration

    out: list = []
    for item in value:
        out.append(capo_lambda.types.function_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> FunctionList:
    import capo_lambda.types.function_configuration

    out: FunctionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda.types.function_configuration.deserialize_json(item))
    return out


def redact_sensitive(value: FunctionList) -> list[Any]:
    import capo_lambda.types.function_configuration

    return [
        capo_lambda.types.function_configuration.redact_sensitive(item)
        for item in value
    ]

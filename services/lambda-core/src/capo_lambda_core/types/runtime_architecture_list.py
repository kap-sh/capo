"""Generated from Smithy shape ``com.amazonaws.lambdacore#RuntimeArchitectureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_architecture

RuntimeArchitectureList: TypeAlias = list[
    "capo_lambda_core.types.runtime_architecture.RuntimeArchitecture"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeArchitectureList) -> list:
    import capo_lambda_core.types.runtime_architecture

    out: list = []
    for item in value:
        out.append(capo_lambda_core.types.runtime_architecture.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuntimeArchitectureList:
    import capo_lambda_core.types.runtime_architecture

    out: RuntimeArchitectureList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_core.types.runtime_architecture.deserialize_json(item))
    return out

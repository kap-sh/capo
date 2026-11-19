"""Generated from Smithy shape ``com.amazonaws.lambdacore#RuntimeAliasList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_alias_info

RuntimeAliasList: TypeAlias = list[
    "capo_lambda_core.types.runtime_alias_info.RuntimeAliasInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeAliasList) -> list:
    import capo_lambda_core.types.runtime_alias_info

    out: list = []
    for item in value:
        out.append(capo_lambda_core.types.runtime_alias_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuntimeAliasList:
    import capo_lambda_core.types.runtime_alias_info

    out: RuntimeAliasList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_core.types.runtime_alias_info.deserialize_json(item))
    return out

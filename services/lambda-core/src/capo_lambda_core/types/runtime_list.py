"""Generated from Smithy shape ``com.amazonaws.lambdacore#RuntimeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_info

RuntimeList: TypeAlias = list["capo_lambda_core.types.runtime_info.RuntimeInfo"]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeList) -> list:
    import capo_lambda_core.types.runtime_info

    out: list = []
    for item in value:
        out.append(capo_lambda_core.types.runtime_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuntimeList:
    import capo_lambda_core.types.runtime_info

    out: RuntimeList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_core.types.runtime_info.deserialize_json(item))
    return out

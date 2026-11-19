"""Generated from Smithy shape ``com.amazonaws.lambdacore#RuntimeVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_core.types.runtime_version_info

RuntimeVersionList: TypeAlias = list[
    "capo_lambda_core.types.runtime_version_info.RuntimeVersionInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeVersionList) -> list:
    import capo_lambda_core.types.runtime_version_info

    out: list = []
    for item in value:
        out.append(capo_lambda_core.types.runtime_version_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuntimeVersionList:
    import capo_lambda_core.types.runtime_version_info

    out: RuntimeVersionList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_core.types.runtime_version_info.deserialize_json(item))
    return out

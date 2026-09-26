"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#CpuConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_microvms.types.cpu_configuration

CpuConfigurationList: TypeAlias = list[
    "capo_lambda_microvms.types.cpu_configuration.CpuConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CpuConfigurationList) -> list:
    import capo_lambda_microvms.types.cpu_configuration

    out: list = []
    for item in value:
        out.append(capo_lambda_microvms.types.cpu_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> CpuConfigurationList:
    import capo_lambda_microvms.types.cpu_configuration

    out: CpuConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_microvms.types.cpu_configuration.deserialize_json(item))
    return out

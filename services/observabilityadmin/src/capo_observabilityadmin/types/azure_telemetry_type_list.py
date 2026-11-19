"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureTelemetryTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_telemetry_type

AzureTelemetryTypeList: TypeAlias = list[
    "capo_observabilityadmin.types.azure_telemetry_type.AzureTelemetryType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureTelemetryTypeList) -> list:
    import capo_observabilityadmin.types.azure_telemetry_type

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.azure_telemetry_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AzureTelemetryTypeList:
    import capo_observabilityadmin.types.azure_telemetry_type

    out: AzureTelemetryTypeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_observabilityadmin.types.azure_telemetry_type.deserialize_json(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureScopeItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_scope
    import capo_observabilityadmin.types.azure_telemetry_type_list


class AzureScopeItem(TypedDict, closed=True):
    telemetry_types: (
        "capo_observabilityadmin.types.azure_telemetry_type_list.AzureTelemetryTypeList"
    )
    """<p>The telemetry types to collect.</p>"""
    scope: "capo_observabilityadmin.types.azure_scope.AzureScope"
    """<p>The Azure resources to collect telemetry from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureScopeItem) -> dict:
    out: dict = {}
    import capo_observabilityadmin.types.azure_telemetry_type_list

    out["TelemetryTypes"] = (
        capo_observabilityadmin.types.azure_telemetry_type_list.serialize_json(
            value["telemetry_types"]
        )
    )
    import capo_observabilityadmin.types.azure_scope

    out["Scope"] = capo_observabilityadmin.types.azure_scope.serialize_json(
        value["scope"]
    )
    return out


def deserialize_json(data: dict) -> AzureScopeItem:
    out: AzureScopeItem = {}  # type: ignore[typeddict-item]
    if data.get("TelemetryTypes") is not None:
        import capo_observabilityadmin.types.azure_telemetry_type_list

        out["telemetry_types"] = (
            capo_observabilityadmin.types.azure_telemetry_type_list.deserialize_json(
                data["TelemetryTypes"]
            )
        )
    else:
        out["telemetry_types"] = []
    if data.get("Scope") is not None:
        import capo_observabilityadmin.types.azure_scope

        out["scope"] = capo_observabilityadmin.types.azure_scope.deserialize_json(
            data["Scope"]
        )
    else:
        raise DeserializationError("AzureScopeItem.scope required")
    return out

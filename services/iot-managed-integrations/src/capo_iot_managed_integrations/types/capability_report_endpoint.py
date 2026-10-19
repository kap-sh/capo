"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CapabilityReportEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.capability_report_capabilities
    import capo_iot_managed_integrations.types.device_types
    import capo_iot_managed_integrations.types.endpoint_id


class CapabilityReportEndpoint(TypedDict, closed=True):
    id: "capo_iot_managed_integrations.types.endpoint_id.EndpointId"
    """<p>The id of the endpoint used in the capability report.</p>"""
    device_types: "capo_iot_managed_integrations.types.device_types.DeviceTypes"
    """<p>The type of device.</p>"""
    capabilities: "capo_iot_managed_integrations.types.capability_report_capabilities.CapabilityReportCapabilities"
    """<p>The capabilities used in the capability report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityReportEndpoint) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_iot_managed_integrations.types.device_types

    out["deviceTypes"] = (
        capo_iot_managed_integrations.types.device_types.serialize_json(
            value["device_types"]
        )
    )
    import capo_iot_managed_integrations.types.capability_report_capabilities

    out["capabilities"] = (
        capo_iot_managed_integrations.types.capability_report_capabilities.serialize_json(
            value["capabilities"]
        )
    )
    return out


def deserialize_json(data: dict) -> CapabilityReportEndpoint:
    out: CapabilityReportEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("deviceTypes") is not None:
        import capo_iot_managed_integrations.types.device_types

        out["device_types"] = (
            capo_iot_managed_integrations.types.device_types.deserialize_json(
                data["deviceTypes"]
            )
        )
    else:
        out["device_types"] = []
    if data.get("capabilities") is not None:
        import capo_iot_managed_integrations.types.capability_report_capabilities

        out["capabilities"] = (
            capo_iot_managed_integrations.types.capability_report_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    else:
        out["capabilities"] = []
    return out

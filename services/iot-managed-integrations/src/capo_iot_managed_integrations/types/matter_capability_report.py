"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCapabilityReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.capability_report_version
    import capo_iot_managed_integrations.types.matter_capability_report_endpoints
    import capo_iot_managed_integrations.types.node_id


class MatterCapabilityReport(TypedDict, closed=True):
    version: "capo_iot_managed_integrations.types.capability_report_version.CapabilityReportVersion"
    """<p>The version of the capability report.</p>"""
    node_id: NotRequired["capo_iot_managed_integrations.types.node_id.NodeId"]
    """<p>The numeric identifier of the node.</p>"""
    endpoints: "capo_iot_managed_integrations.types.matter_capability_report_endpoints.MatterCapabilityReportEndpoints"
    """<p>The endpoints used in the capability report.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatterCapabilityReport) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    if "node_id" in value:
        out["nodeId"] = value["node_id"]
    import capo_iot_managed_integrations.types.matter_capability_report_endpoints

    out["endpoints"] = (
        capo_iot_managed_integrations.types.matter_capability_report_endpoints.serialize_json(
            value["endpoints"]
        )
    )
    return out


def deserialize_json(data: dict) -> MatterCapabilityReport:
    out: MatterCapabilityReport = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("nodeId") is not None:
        out["node_id"] = data["nodeId"]
    if data.get("endpoints") is not None:
        import capo_iot_managed_integrations.types.matter_capability_report_endpoints

        out["endpoints"] = (
            capo_iot_managed_integrations.types.matter_capability_report_endpoints.deserialize_json(
                data["endpoints"]
            )
        )
    else:
        out["endpoints"] = []
    return out

"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterCapabilityReportEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.device_types
    import capo_iot_managed_integrations.types.endpoint_id
    import capo_iot_managed_integrations.types.matter_capability_report_clusters
    import capo_iot_managed_integrations.types.matter_capability_report_endpoint_client_clusters
    import capo_iot_managed_integrations.types.matter_capability_report_endpoint_parts
    import capo_iot_managed_integrations.types.matter_capability_report_endpoint_semantic_tags


class MatterCapabilityReportEndpoint(TypedDict, closed=True):
    id: "capo_iot_managed_integrations.types.endpoint_id.EndpointId"
    """<p>The id of the Amazon Web Services Matter capability report endpoint.</p>"""
    device_types: "capo_iot_managed_integrations.types.device_types.DeviceTypes"
    """<p>The type of device.</p>"""
    clusters: "capo_iot_managed_integrations.types.matter_capability_report_clusters.MatterCapabilityReportClusters"
    """<p>Matter clusters used in capability report.</p>"""
    parts: NotRequired[
        "capo_iot_managed_integrations.types.matter_capability_report_endpoint_parts.MatterCapabilityReportEndpointParts"
    ]
    """<p>Heirachy of child endpoints contained in the given endpoint.</p>"""
    semantic_tags: NotRequired[
        "capo_iot_managed_integrations.types.matter_capability_report_endpoint_semantic_tags.MatterCapabilityReportEndpointSemanticTags"
    ]
    """<p>Semantic information related to endpoint.</p>"""
    client_clusters: NotRequired[
        "capo_iot_managed_integrations.types.matter_capability_report_endpoint_client_clusters.MatterCapabilityReportEndpointClientClusters"
    ]
    """<p>Semantic information related to endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatterCapabilityReportEndpoint) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_iot_managed_integrations.types.device_types

    out["deviceTypes"] = (
        capo_iot_managed_integrations.types.device_types.serialize_json(
            value["device_types"]
        )
    )
    import capo_iot_managed_integrations.types.matter_capability_report_clusters

    out["clusters"] = (
        capo_iot_managed_integrations.types.matter_capability_report_clusters.serialize_json(
            value["clusters"]
        )
    )
    if "parts" in value:
        import capo_iot_managed_integrations.types.matter_capability_report_endpoint_parts

        out["parts"] = (
            capo_iot_managed_integrations.types.matter_capability_report_endpoint_parts.serialize_json(
                value["parts"]
            )
        )
    if "semantic_tags" in value:
        import capo_iot_managed_integrations.types.matter_capability_report_endpoint_semantic_tags

        out["semanticTags"] = (
            capo_iot_managed_integrations.types.matter_capability_report_endpoint_semantic_tags.serialize_json(
                value["semantic_tags"]
            )
        )
    if "client_clusters" in value:
        import capo_iot_managed_integrations.types.matter_capability_report_endpoint_client_clusters

        out["clientClusters"] = (
            capo_iot_managed_integrations.types.matter_capability_report_endpoint_client_clusters.serialize_json(
                value["client_clusters"]
            )
        )
    return out


def deserialize_json(data: dict) -> MatterCapabilityReportEndpoint:
    out: MatterCapabilityReportEndpoint = {}  # type: ignore[typeddict-item]
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
    if data.get("clusters") is not None:
        import capo_iot_managed_integrations.types.matter_capability_report_clusters

        out["clusters"] = (
            capo_iot_managed_integrations.types.matter_capability_report_clusters.deserialize_json(
                data["clusters"]
            )
        )
    else:
        out["clusters"] = []
    if data.get("parts") is not None:
        import capo_iot_managed_integrations.types.matter_capability_report_endpoint_parts

        out["parts"] = (
            capo_iot_managed_integrations.types.matter_capability_report_endpoint_parts.deserialize_json(
                data["parts"]
            )
        )
    if data.get("semanticTags") is not None:
        import capo_iot_managed_integrations.types.matter_capability_report_endpoint_semantic_tags

        out["semantic_tags"] = (
            capo_iot_managed_integrations.types.matter_capability_report_endpoint_semantic_tags.deserialize_json(
                data["semanticTags"]
            )
        )
    if data.get("clientClusters") is not None:
        import capo_iot_managed_integrations.types.matter_capability_report_endpoint_client_clusters

        out["client_clusters"] = (
            capo_iot_managed_integrations.types.matter_capability_report_endpoint_client_clusters.deserialize_json(
                data["clientClusters"]
            )
        )
    return out

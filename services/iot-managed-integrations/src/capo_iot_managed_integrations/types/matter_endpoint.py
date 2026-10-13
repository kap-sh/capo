"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#MatterEndpoint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.endpoint_id
    import capo_iot_managed_integrations.types.matter_clusters


class MatterEndpoint(TypedDict, closed=True):
    id: NotRequired["capo_iot_managed_integrations.types.endpoint_id.EndpointId"]
    """<p>The Matter endpoint id.</p>"""
    clusters: NotRequired[
        "capo_iot_managed_integrations.types.matter_clusters.MatterClusters"
    ]
    """<p>A list of Matter clusters for a managed thing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MatterEndpoint) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "clusters" in value:
        import capo_iot_managed_integrations.types.matter_clusters

        out["clusters"] = (
            capo_iot_managed_integrations.types.matter_clusters.serialize_json(
                value["clusters"]
            )
        )
    return out


def deserialize_json(data: dict) -> MatterEndpoint:
    out: MatterEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("clusters") is not None:
        import capo_iot_managed_integrations.types.matter_clusters

        out["clusters"] = (
            capo_iot_managed_integrations.types.matter_clusters.deserialize_json(
                data["clusters"]
            )
        )
    return out


def redact_sensitive(value: MatterEndpoint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "clusters" in value:
        import capo_iot_managed_integrations.types.matter_clusters

        out["clusters"] = (
            capo_iot_managed_integrations.types.matter_clusters.redact_sensitive(
                value["clusters"]
            )
        )
    return out

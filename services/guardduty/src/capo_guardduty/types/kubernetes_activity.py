"""Generated from Smithy shape ``com.amazonaws.guardduty#KubernetesActivity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.enrichment
    import capo_guardduty.types.investigation_kubernetes_workload
    import capo_guardduty.types.kubernetes_anomaly
    import capo_guardduty.types.kubernetes_api_call


class KubernetesActivity(TypedDict, closed=True):
    api_call: NotRequired["capo_guardduty.types.kubernetes_api_call.KubernetesApiCall"]
    """<p>Details about a Kubernetes API call.</p>"""
    anomaly: NotRequired["capo_guardduty.types.kubernetes_anomaly.KubernetesAnomaly"]
    """<p>Details about anomalous Kubernetes behavior.</p>"""
    workload: NotRequired[
        "capo_guardduty.types.investigation_kubernetes_workload.InvestigationKubernetesWorkload"
    ]
    """<p>The Kubernetes workload that is associated with the anomaly.</p>"""
    enrichment: NotRequired["capo_guardduty.types.enrichment.Enrichment"]
    """<p>Additional context about the API call, such as geolocation information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KubernetesActivity) -> dict:
    out: dict = {}
    if "api_call" in value:
        import capo_guardduty.types.kubernetes_api_call

        out["apiCall"] = capo_guardduty.types.kubernetes_api_call.serialize_json(
            value["api_call"]
        )
    if "anomaly" in value:
        import capo_guardduty.types.kubernetes_anomaly

        out["anomaly"] = capo_guardduty.types.kubernetes_anomaly.serialize_json(
            value["anomaly"]
        )
    if "workload" in value:
        import capo_guardduty.types.investigation_kubernetes_workload

        out["workload"] = (
            capo_guardduty.types.investigation_kubernetes_workload.serialize_json(
                value["workload"]
            )
        )
    if "enrichment" in value:
        import capo_guardduty.types.enrichment

        out["enrichment"] = capo_guardduty.types.enrichment.serialize_json(
            value["enrichment"]
        )
    return out


def deserialize_json(data: dict) -> KubernetesActivity:
    out: KubernetesActivity = {}  # type: ignore[typeddict-item]
    if data.get("apiCall") is not None:
        import capo_guardduty.types.kubernetes_api_call

        out["api_call"] = capo_guardduty.types.kubernetes_api_call.deserialize_json(
            data["apiCall"]
        )
    if data.get("anomaly") is not None:
        import capo_guardduty.types.kubernetes_anomaly

        out["anomaly"] = capo_guardduty.types.kubernetes_anomaly.deserialize_json(
            data["anomaly"]
        )
    if data.get("workload") is not None:
        import capo_guardduty.types.investigation_kubernetes_workload

        out["workload"] = (
            capo_guardduty.types.investigation_kubernetes_workload.deserialize_json(
                data["workload"]
            )
        )
    if data.get("enrichment") is not None:
        import capo_guardduty.types.enrichment

        out["enrichment"] = capo_guardduty.types.enrichment.deserialize_json(
            data["enrichment"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.datazone#HyperPodPropertiesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.hyper_pod_orchestrator


class HyperPodPropertiesOutput(TypedDict, closed=True):
    cluster_name: "str"
    """<p>The cluster name the hyper pod properties.</p>"""
    cluster_arn: NotRequired["str"]
    """<p>The cluster ARN of the hyper pod properties.</p>"""
    orchestrator: NotRequired[
        "capo_datazone.types.hyper_pod_orchestrator.HyperPodOrchestrator"
    ]
    """<p>The orchestrator of the hyper pod properties.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HyperPodPropertiesOutput) -> dict:
    out: dict = {}
    out["clusterName"] = value["cluster_name"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "orchestrator" in value:
        import capo_datazone.types.hyper_pod_orchestrator

        out["orchestrator"] = capo_datazone.types.hyper_pod_orchestrator.serialize_json(
            value["orchestrator"]
        )
    return out


def deserialize_json(data: dict) -> HyperPodPropertiesOutput:
    out: HyperPodPropertiesOutput = {}  # type: ignore[typeddict-item]
    if data.get("clusterName") is not None:
        out["cluster_name"] = data["clusterName"]
    else:
        out["cluster_name"] = ""
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    if data.get("orchestrator") is not None:
        import capo_datazone.types.hyper_pod_orchestrator

        out["orchestrator"] = (
            capo_datazone.types.hyper_pod_orchestrator.deserialize_json(
                data["orchestrator"]
            )
        )
    return out

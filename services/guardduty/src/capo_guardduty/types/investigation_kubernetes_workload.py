"""Generated from Smithy shape ``com.amazonaws.guardduty#InvestigationKubernetesWorkload``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.string


class InvestigationKubernetesWorkload(TypedDict, closed=True):
    workload_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The type of the workload.</p>"""
    workload_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The name of the workload.</p>"""
    containers: NotRequired["capo_guardduty.types.string.String"]
    """<p>The containers in the workload.</p>"""
    volumes: NotRequired["capo_guardduty.types.string.String"]
    """<p>The volumes of the workload.</p>"""
    security_context: NotRequired["capo_guardduty.types.string.String"]
    """<p>The security context of the workload.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationKubernetesWorkload) -> dict:
    out: dict = {}
    if "workload_type" in value:
        out["workloadType"] = value["workload_type"]
    if "workload_name" in value:
        out["workloadName"] = value["workload_name"]
    if "containers" in value:
        out["containers"] = value["containers"]
    if "volumes" in value:
        out["volumes"] = value["volumes"]
    if "security_context" in value:
        out["securityContext"] = value["security_context"]
    return out


def deserialize_json(data: dict) -> InvestigationKubernetesWorkload:
    out: InvestigationKubernetesWorkload = {}  # type: ignore[typeddict-item]
    if data.get("workloadType") is not None:
        out["workload_type"] = data["workloadType"]
    if data.get("workloadName") is not None:
        out["workload_name"] = data["workloadName"]
    if data.get("containers") is not None:
        out["containers"] = data["containers"]
    if data.get("volumes") is not None:
        out["volumes"] = data["volumes"]
    if data.get("securityContext") is not None:
        out["security_context"] = data["securityContext"]
    return out

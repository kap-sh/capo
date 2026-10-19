"""Generated from Smithy shape ``com.amazonaws.deadline#DependencyCounts``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.integer


class DependencyCounts(TypedDict, closed=True):
    dependencies_resolved: "capo_deadline.types.integer.Integer"
    """<p>The number of resolved dependencies.</p>"""
    dependencies_unresolved: "capo_deadline.types.integer.Integer"
    """<p>The number of unresolved dependencies.</p>"""
    consumers_resolved: "capo_deadline.types.integer.Integer"
    """<p>The number of consumers resolved.</p>"""
    consumers_unresolved: "capo_deadline.types.integer.Integer"
    """<p>The number of unresolved consumers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DependencyCounts) -> dict:
    out: dict = {}
    out["dependenciesResolved"] = value["dependencies_resolved"]
    out["dependenciesUnresolved"] = value["dependencies_unresolved"]
    out["consumersResolved"] = value["consumers_resolved"]
    out["consumersUnresolved"] = value["consumers_unresolved"]
    return out


def deserialize_json(data: dict) -> DependencyCounts:
    out: DependencyCounts = {}  # type: ignore[typeddict-item]
    if data.get("dependenciesResolved") is not None:
        out["dependencies_resolved"] = data["dependenciesResolved"]
    else:
        out["dependencies_resolved"] = 0
    if data.get("dependenciesUnresolved") is not None:
        out["dependencies_unresolved"] = data["dependenciesUnresolved"]
    else:
        out["dependencies_unresolved"] = 0
    if data.get("consumersResolved") is not None:
        out["consumers_resolved"] = data["consumersResolved"]
    else:
        out["consumers_resolved"] = 0
    if data.get("consumersUnresolved") is not None:
        out["consumers_unresolved"] = data["consumersUnresolved"]
    else:
        out["consumers_unresolved"] = 0
    return out

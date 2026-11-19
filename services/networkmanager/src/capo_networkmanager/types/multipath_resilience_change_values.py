"""Generated from Smithy shape ``com.amazonaws.networkmanager#MultipathResilienceChangeValues``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.edge_set_list
    import capo_networkmanager.types.multipath_resilience_mode


class MultipathResilienceChangeValues(TypedDict, closed=True):
    mode: NotRequired[
        "capo_networkmanager.types.multipath_resilience_mode.MultipathResilienceMode"
    ]
    """<p>The mode (best-effort/disabled) of multipath resilience.</p>"""
    edge_sets: NotRequired["capo_networkmanager.types.edge_set_list.EdgeSetList"]
    """<p>A set of two edge locations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultipathResilienceChangeValues) -> dict:
    out: dict = {}
    if "mode" in value:
        import capo_networkmanager.types.multipath_resilience_mode

        out["Mode"] = (
            capo_networkmanager.types.multipath_resilience_mode.serialize_json(
                value["mode"]
            )
        )
    if "edge_sets" in value:
        import capo_networkmanager.types.edge_set_list

        out["EdgeSets"] = capo_networkmanager.types.edge_set_list.serialize_json(
            value["edge_sets"]
        )
    return out


def deserialize_json(data: dict) -> MultipathResilienceChangeValues:
    out: MultipathResilienceChangeValues = {}  # type: ignore[typeddict-item]
    if data.get("Mode") is not None:
        import capo_networkmanager.types.multipath_resilience_mode

        out["mode"] = (
            capo_networkmanager.types.multipath_resilience_mode.deserialize_json(
                data["Mode"]
            )
        )
    if data.get("EdgeSets") is not None:
        import capo_networkmanager.types.edge_set_list

        out["edge_sets"] = capo_networkmanager.types.edge_set_list.deserialize_json(
            data["EdgeSets"]
        )
    return out

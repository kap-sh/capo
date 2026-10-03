"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#LiveSimulationState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.domain_list
    import capo_simspaceweaver.types.simulation_clock_list


class LiveSimulationState(TypedDict, closed=True):
    domains: NotRequired["capo_simspaceweaver.types.domain_list.DomainList"]
    """<p>A list of domains for the simulation. For more information about domains, see <a href="https://docs.aws.amazon.com/simspaceweaver/latest/userguide/what-is_key-concepts.html#what-is_key-concepts_domains">Key concepts: Domains</a> in the <i>SimSpace Weaver User Guide</i>.</p>"""
    clocks: NotRequired[
        "capo_simspaceweaver.types.simulation_clock_list.SimulationClockList"
    ]
    """<p>A list of simulation clocks.</p> <note> <p>At this time, a simulation has only one clock.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: LiveSimulationState) -> dict:
    out: dict = {}
    if "domains" in value:
        import capo_simspaceweaver.types.domain_list

        out["Domains"] = capo_simspaceweaver.types.domain_list.serialize_json(
            value["domains"]
        )
    if "clocks" in value:
        import capo_simspaceweaver.types.simulation_clock_list

        out["Clocks"] = capo_simspaceweaver.types.simulation_clock_list.serialize_json(
            value["clocks"]
        )
    return out


def deserialize_json(data: dict) -> LiveSimulationState:
    out: LiveSimulationState = {}  # type: ignore[typeddict-item]
    if data.get("Domains") is not None:
        import capo_simspaceweaver.types.domain_list

        out["domains"] = capo_simspaceweaver.types.domain_list.deserialize_json(
            data["Domains"]
        )
    if data.get("Clocks") is not None:
        import capo_simspaceweaver.types.simulation_clock_list

        out["clocks"] = (
            capo_simspaceweaver.types.simulation_clock_list.deserialize_json(
                data["Clocks"]
            )
        )
    return out

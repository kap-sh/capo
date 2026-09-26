"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ListRegistriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.next_token
    import capo_agent_registry_control.types.registry_summary_list


class ListRegistriesResponse(TypedDict, closed=True):
    registries: (
        "capo_agent_registry_control.types.registry_summary_list.RegistrySummaryList"
    )
    """<p>List of registry summaries</p>"""
    next_token: NotRequired["capo_agent_registry_control.types.next_token.NextToken"]
    """<p>Token for next page of results</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegistriesResponse) -> dict:
    out: dict = {}
    import capo_agent_registry_control.types.registry_summary_list

    out["registries"] = (
        capo_agent_registry_control.types.registry_summary_list.serialize_json(
            value["registries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRegistriesResponse:
    out: ListRegistriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("registries") is not None:
        import capo_agent_registry_control.types.registry_summary_list

        out["registries"] = (
            capo_agent_registry_control.types.registry_summary_list.deserialize_json(
                data["registries"]
            )
        )
    else:
        raise DeserializationError("ListRegistriesResponse.registries required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

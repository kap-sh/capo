"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#ListRegistryRecordsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.next_token
    import capo_agent_registry_control.types.registry_record_summary_list


class ListRegistryRecordsResponse(TypedDict, closed=True):
    registry_records: "capo_agent_registry_control.types.registry_record_summary_list.RegistryRecordSummaryList"
    """<p>List of registry record summaries</p>"""
    next_token: NotRequired["capo_agent_registry_control.types.next_token.NextToken"]
    """<p>Token for next page of results</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegistryRecordsResponse) -> dict:
    out: dict = {}
    import capo_agent_registry_control.types.registry_record_summary_list

    out["registryRecords"] = (
        capo_agent_registry_control.types.registry_record_summary_list.serialize_json(
            value["registry_records"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRegistryRecordsResponse:
    out: ListRegistryRecordsResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryRecords") is not None:
        import capo_agent_registry_control.types.registry_record_summary_list

        out["registry_records"] = (
            capo_agent_registry_control.types.registry_record_summary_list.deserialize_json(
                data["registryRecords"]
            )
        )
    else:
        raise DeserializationError(
            "ListRegistryRecordsResponse.registry_records required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListRegistryRecordsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.registry_record_summary_list


class ListRegistryRecordsResponse(TypedDict, closed=True):
    registry_records: "capo_bedrock_agentcore_control.types.registry_record_summary_list.RegistryRecordSummaryList"
    """<p>The list of registry record summaries. For details about the fields in each summary, see the <code>RegistryRecordSummary</code> data type.</p>"""
    next_token: NotRequired["capo_bedrock_agentcore_control.types.next_token.NextToken"]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegistryRecordsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.registry_record_summary_list

    out["registryRecords"] = (
        capo_bedrock_agentcore_control.types.registry_record_summary_list.serialize_json(
            value["registry_records"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRegistryRecordsResponse:
    out: ListRegistryRecordsResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryRecords") is not None:
        import capo_bedrock_agentcore_control.types.registry_record_summary_list

        out["registry_records"] = (
            capo_bedrock_agentcore_control.types.registry_record_summary_list.deserialize_json(
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


def redact_sensitive(value: ListRegistryRecordsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "registry_records" in value:
        import capo_bedrock_agentcore_control.types.registry_record_summary_list

        out["registry_records"] = (
            capo_bedrock_agentcore_control.types.registry_record_summary_list.redact_sensitive(
                value["registry_records"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListWorkloadIdentitiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.workload_identity_list


class ListWorkloadIdentitiesResponse(TypedDict, closed=True):
    workload_identities: "capo_bedrock_agentcore_control.types.workload_identity_list.WorkloadIdentityList"
    """<p>The list of workload identities.</p>"""
    next_token: NotRequired["str"]
    """<p>Pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkloadIdentitiesResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.workload_identity_list

    out["workloadIdentities"] = (
        capo_bedrock_agentcore_control.types.workload_identity_list.serialize_json(
            value["workload_identities"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWorkloadIdentitiesResponse:
    out: ListWorkloadIdentitiesResponse = {}  # type: ignore[typeddict-item]
    if data.get("workloadIdentities") is not None:
        import capo_bedrock_agentcore_control.types.workload_identity_list

        out["workload_identities"] = (
            capo_bedrock_agentcore_control.types.workload_identity_list.deserialize_json(
                data["workloadIdentities"]
            )
        )
    else:
        out["workload_identities"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

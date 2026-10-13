"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ListWorkspaceInstancesRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.max_results
    import capo_workspaces_instances.types.next_token
    import capo_workspaces_instances.types.provision_states


class ListWorkspaceInstancesRequest(TypedDict, closed=True):
    provision_states: NotRequired[
        "capo_workspaces_instances.types.provision_states.ProvisionStates"
    ]
    """<p>Filter WorkSpaces Instances by their current provisioning states.</p>"""
    max_results: NotRequired["capo_workspaces_instances.types.max_results.MaxResults"]
    """<p>Maximum number of WorkSpaces Instances to return in a single response.</p>"""
    next_token: NotRequired["capo_workspaces_instances.types.next_token.NextToken"]
    """<p>Pagination token for retrieving subsequent pages of WorkSpaces Instances.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListWorkspaceInstancesRequest) -> dict:
    out: dict = {}
    if "provision_states" in value:
        import capo_workspaces_instances.types.provision_states

        out["ProvisionStates"] = (
            capo_workspaces_instances.types.provision_states.serialize_aws_json_1_0(
                value["provision_states"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListWorkspaceInstancesRequest:
    out: ListWorkspaceInstancesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionStates") is not None:
        import capo_workspaces_instances.types.provision_states

        out["provision_states"] = (
            capo_workspaces_instances.types.provision_states.deserialize_aws_json_1_0(
                data["ProvisionStates"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListWorkspaceInstancesRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out

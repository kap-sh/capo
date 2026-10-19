"""Generated from Smithy shape ``com.amazonaws.launchwizard#ListDeploymentEventsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_launch_wizard.types.deployment_id
    import capo_launch_wizard.types.max_deployment_event_results
    import capo_launch_wizard.types.next_token


class ListDeploymentEventsInput(TypedDict, closed=True):
    deployment_id: "capo_launch_wizard.types.deployment_id.DeploymentId"
    """<p>The ID of the deployment.</p>"""
    max_results: NotRequired[
        "capo_launch_wizard.types.max_deployment_event_results.MaxDeploymentEventResults"
    ]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p>"""
    next_token: NotRequired["capo_launch_wizard.types.next_token.NextToken"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeploymentEventsInput) -> dict:
    out: dict = {}
    out["deploymentId"] = value["deployment_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDeploymentEventsInput:
    out: ListDeploymentEventsInput = {}  # type: ignore[typeddict-item]
    if data.get("deploymentId") is not None:
        out["deployment_id"] = data["deploymentId"]
    else:
        out["deployment_id"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

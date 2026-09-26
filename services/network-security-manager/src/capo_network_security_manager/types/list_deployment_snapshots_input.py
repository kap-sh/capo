"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ListDeploymentSnapshotsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.deployment_identifier
    import capo_network_security_manager.types.max_results
    import capo_network_security_manager.types.next_token


class ListDeploymentSnapshotsInput(TypedDict, closed=True):
    deployment_identifier: (
        "capo_network_security_manager.types.deployment_identifier.DeploymentIdentifier"
    )
    """<p>The identifier of the deployment. This is the deployment's Amazon Resource Name (ARN).</p>"""
    max_results: NotRequired[
        "capo_network_security_manager.types.max_results.MaxResults"
    ]
    """<p>The maximum number of results to return in a single call. Valid range: 1-100. To retrieve the remaining results, use the returned <code>nextToken</code> value in a subsequent call.</p>"""
    next_token: NotRequired["capo_network_security_manager.types.next_token.NextToken"]
    """<p>The token for the next page of results. To retrieve the next page, call the operation again and provide this value. When there are no more results, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDeploymentSnapshotsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDeploymentSnapshotsInput:
    out: ListDeploymentSnapshotsInput = {}  # type: ignore[typeddict-item]
    return out

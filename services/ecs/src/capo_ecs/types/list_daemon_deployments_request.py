"""Generated from Smithy shape ``com.amazonaws.ecs#ListDaemonDeploymentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.created_at
    import capo_ecs.types.daemon_deployment_status_list
    import capo_ecs.types.string


class ListDaemonDeploymentsRequest(TypedDict, closed=True):
    daemon_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the daemon to list deployments for.</p>"""
    status: NotRequired[
        "capo_ecs.types.daemon_deployment_status_list.DaemonDeploymentStatusList"
    ]
    """<p>An optional filter to narrow the <code>ListDaemonDeployments</code> results by deployment status. If you don't specify a status, all deployments are returned.</p>"""
    created_at: NotRequired["capo_ecs.types.created_at.CreatedAt"]
    """<p>An optional filter to narrow the <code>ListDaemonDeployments</code> results by creation time. If you don't specify a time range, all deployments are returned.</p>"""
    max_results: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of daemon deployment results that <code>ListDaemonDeployments</code> returned in paginated output. When this parameter is used, <code>ListDaemonDeployments</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListDaemonDeployments</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListDaemonDeployments</code> returns up to 20 results and a <code>nextToken</code> value if applicable.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListDaemonDeployments</code> request indicating that more results are available to fulfill the request and further calls will be needed. If <code>maxResults</code> was provided, it's possible for the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDaemonDeploymentsRequest) -> dict:
    out: dict = {}
    out["daemonArn"] = value["daemon_arn"]
    if "status" in value:
        import capo_ecs.types.daemon_deployment_status_list

        out["status"] = (
            capo_ecs.types.daemon_deployment_status_list.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "created_at" in value:
        import capo_ecs.types.created_at

        out["createdAt"] = capo_ecs.types.created_at.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDaemonDeploymentsRequest:
    out: ListDaemonDeploymentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("daemonArn") is not None:
        out["daemon_arn"] = data["daemonArn"]
    else:
        out["daemon_arn"] = ""
    if data.get("status") is not None:
        import capo_ecs.types.daemon_deployment_status_list

        out["status"] = (
            capo_ecs.types.daemon_deployment_status_list.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_ecs.types.created_at

        out["created_at"] = capo_ecs.types.created_at.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.ecs#ListServiceDeploymentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.created_at
    import capo_ecs.types.service_deployment_status_list
    import capo_ecs.types.string


class ListServiceDeploymentsRequest(TypedDict, closed=True):
    service: "capo_ecs.types.string.String"
    """<p>The ARN or name of the service</p>"""
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The cluster that hosts the service. This can either be the cluster name or ARN. Starting April 15, 2023, Amazon Web Services will not onboard new customers to Amazon Elastic Inference (EI), and will help current customers migrate their workloads to options that offer better price and performance. If you don't specify a cluster, <code>default</code> is used.</p>"""
    status: NotRequired[
        "capo_ecs.types.service_deployment_status_list.ServiceDeploymentStatusList"
    ]
    """<p>An optional filter you can use to narrow the results. If you do not specify a status, then all status values are included in the result.</p>"""
    created_at: NotRequired["capo_ecs.types.created_at.CreatedAt"]
    """<p>An optional filter you can use to narrow the results by the service creation date. If you do not specify a value, the result includes all services created before the current time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListServiceDeployments</code> request indicating that more results are available to fulfill the request and further calls are needed. If you provided <code>maxResults</code>, it's possible the number of results is fewer than <code>maxResults</code>.</p>"""
    max_results: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of service deployment results that <code>ListServiceDeployments</code> returned in paginated output. When this parameter is used, <code>ListServiceDeployments</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListServiceDeployments</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListServiceDeployments</code> returns up to 20 results and a <code>nextToken</code> value if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServiceDeploymentsRequest) -> dict:
    out: dict = {}
    out["service"] = value["service"]
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "status" in value:
        import capo_ecs.types.service_deployment_status_list

        out["status"] = (
            capo_ecs.types.service_deployment_status_list.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "created_at" in value:
        import capo_ecs.types.created_at

        out["createdAt"] = capo_ecs.types.created_at.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServiceDeploymentsRequest:
    out: ListServiceDeploymentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        out["service"] = data["service"]
    else:
        out["service"] = ""
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("status") is not None:
        import capo_ecs.types.service_deployment_status_list

        out["status"] = (
            capo_ecs.types.service_deployment_status_list.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_ecs.types.created_at

        out["created_at"] = capo_ecs.types.created_at.deserialize_aws_json_1_1(
            data["createdAt"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out

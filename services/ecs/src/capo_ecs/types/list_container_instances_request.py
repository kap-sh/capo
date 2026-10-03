"""Generated from Smithy shape ``com.amazonaws.ecs#ListContainerInstancesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.container_instance_status
    import capo_ecs.types.string


class ListContainerInstancesRequest(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instances to list. If you do not specify a cluster, the default cluster is assumed.</p>"""
    filter: NotRequired["capo_ecs.types.string.String"]
    """<p>You can filter the results of a <code>ListContainerInstances</code> operation with cluster query language statements. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster-query-language.html">Cluster Query Language</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListContainerInstances</code> request indicating that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of container instance results that <code>ListContainerInstances</code> returned in paginated output. When this parameter is used, <code>ListContainerInstances</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListContainerInstances</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListContainerInstances</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""
    status: NotRequired[
        "capo_ecs.types.container_instance_status.ContainerInstanceStatus"
    ]
    """<p>Filters the container instances by status. For example, if you specify the <code>DRAINING</code> status, the results include only container instances that have been set to <code>DRAINING</code> using <a href="https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateContainerInstancesState.html">UpdateContainerInstancesState</a>. If you don't specify this parameter, the The default is to include container instances set to all states other than <code>INACTIVE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListContainerInstancesRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "filter" in value:
        out["filter"] = value["filter"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "status" in value:
        import capo_ecs.types.container_instance_status

        out["status"] = capo_ecs.types.container_instance_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListContainerInstancesRequest:
    out: ListContainerInstancesRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("filter") is not None:
        out["filter"] = data["filter"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("status") is not None:
        import capo_ecs.types.container_instance_status

        out["status"] = (
            capo_ecs.types.container_instance_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.ecs#ListServicesByNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.string


class ListServicesByNamespaceRequest(TypedDict, closed=True):
    namespace: "capo_ecs.types.string.String"
    """<p>The namespace name or full Amazon Resource Name (ARN) of the Cloud Map namespace to list the services in.</p> <p>Tasks that run in a namespace can use short names to connect to services in the namespace. Tasks can connect to services across all of the clusters in the namespace. Tasks connect through a managed proxy container that collects logs and metrics for increased visibility. Only the tasks that Amazon ECS services create are supported with Service Connect. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value that's returned from a <code>ListServicesByNamespace</code> request. It indicates that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> is returned, it is possible the number of results is less than <code>maxResults</code>.</p>"""
    max_results: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of service results that <code>ListServicesByNamespace</code> returns in paginated output. When this parameter is used, <code>ListServicesByNamespace</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListServicesByNamespace</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListServicesByNamespace</code> returns up to 10 results and a <code>nextToken</code> value if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServicesByNamespaceRequest) -> dict:
    out: dict = {}
    out["namespace"] = value["namespace"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServicesByNamespaceRequest:
    out: ListServicesByNamespaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        raise DeserializationError("ListServicesByNamespaceRequest.namespace required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out

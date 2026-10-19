"""Generated from Smithy shape ``com.amazonaws.ecs#ListAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.string
    import capo_ecs.types.target_type


class ListAttributesRequest(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster to list attributes. If you do not specify a cluster, the default cluster is assumed.</p>"""
    target_type: "capo_ecs.types.target_type.TargetType"
    """<p>The type of the target to list attributes with.</p>"""
    attribute_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The name of the attribute to filter the results with. </p>"""
    attribute_value: NotRequired["capo_ecs.types.string.String"]
    """<p>The value of the attribute to filter results with. You must also specify an attribute name to use this parameter.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a <code>ListAttributes</code> request indicating that more results are available to fulfill the request and further calls are needed. If <code>maxResults</code> was provided, it's possible the number of results to be fewer than <code>maxResults</code>.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of cluster results that <code>ListAttributes</code> returned in paginated output. When this parameter is used, <code>ListAttributes</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListAttributes</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter isn't used, then <code>ListAttributes</code> returns up to 100 results and a <code>nextToken</code> value if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAttributesRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    import capo_ecs.types.target_type

    out["targetType"] = capo_ecs.types.target_type.serialize_aws_json_1_1(
        value["target_type"]
    )
    if "attribute_name" in value:
        out["attributeName"] = value["attribute_name"]
    if "attribute_value" in value:
        out["attributeValue"] = value["attribute_value"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAttributesRequest:
    out: ListAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("targetType") is not None:
        import capo_ecs.types.target_type

        out["target_type"] = capo_ecs.types.target_type.deserialize_aws_json_1_1(
            data["targetType"]
        )
    else:
        import typing

        out["target_type"] = typing.cast("capo_ecs.types.target_type.TargetType", "")
    if data.get("attributeName") is not None:
        out["attribute_name"] = data["attributeName"]
    if data.get("attributeValue") is not None:
        out["attribute_value"] = data["attributeValue"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out

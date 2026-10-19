"""Generated from Smithy shape ``com.amazonaws.ecr#GetLifecyclePolicyPreviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_identifier_list
    import capo_ecr.types.lifecycle_policy_preview_filter
    import capo_ecr.types.lifecycle_preview_max_results
    import capo_ecr.types.next_token
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name


class GetLifecyclePolicyPreviewRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the repository. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository.</p>"""
    image_ids: NotRequired["capo_ecr.types.image_identifier_list.ImageIdentifierList"]
    """<p>The list of imageIDs to be included.</p>"""
    next_token: NotRequired["capo_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>GetLifecyclePolicyPreviewRequest</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return. This option cannot be used when you specify images with <code>imageIds</code>.</p>"""
    max_results: NotRequired[
        "capo_ecr.types.lifecycle_preview_max_results.LifecyclePreviewMaxResults"
    ]
    """<p>The maximum number of repository results returned by <code>GetLifecyclePolicyPreviewRequest</code> in paginated output. When this parameter is used, <code>GetLifecyclePolicyPreviewRequest</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>GetLifecyclePolicyPreviewRequest</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 100. If this parameter is not used, then <code>GetLifecyclePolicyPreviewRequest</code> returns up to 100 results and a <code>nextToken</code> value, if applicable. This option cannot be used when you specify images with <code>imageIds</code>.</p>"""
    filter: NotRequired[
        "capo_ecr.types.lifecycle_policy_preview_filter.LifecyclePolicyPreviewFilter"
    ]
    """<p>An optional parameter that filters results based on image tag status and all tags, if tagged.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLifecyclePolicyPreviewRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    if "image_ids" in value:
        import capo_ecr.types.image_identifier_list

        out["imageIds"] = capo_ecr.types.image_identifier_list.serialize_aws_json_1_1(
            value["image_ids"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filter" in value:
        import capo_ecr.types.lifecycle_policy_preview_filter

        out["filter"] = (
            capo_ecr.types.lifecycle_policy_preview_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLifecyclePolicyPreviewRequest:
    out: GetLifecyclePolicyPreviewRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("imageIds") is not None:
        import capo_ecr.types.image_identifier_list

        out["image_ids"] = (
            capo_ecr.types.image_identifier_list.deserialize_aws_json_1_1(
                data["imageIds"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("filter") is not None:
        import capo_ecr.types.lifecycle_policy_preview_filter

        out["filter"] = (
            capo_ecr.types.lifecycle_policy_preview_filter.deserialize_aws_json_1_1(
                data["filter"]
            )
        )
    return out

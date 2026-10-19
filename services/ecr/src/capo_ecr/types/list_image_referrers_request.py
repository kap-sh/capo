"""Generated from Smithy shape ``com.amazonaws.ecr#ListImageReferrersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr.types.fifty_max_results
    import capo_ecr.types.list_image_referrers_filter
    import capo_ecr.types.next_token
    import capo_ecr.types.registry_id
    import capo_ecr.types.repository_name
    import capo_ecr.types.subject_identifier


class ListImageReferrersRequest(TypedDict, closed=True):
    registry_id: NotRequired["capo_ecr.types.registry_id.RegistryId"]
    """<p>The Amazon Web Services account ID associated with the registry that contains the repository in which to list image referrers. If you do not specify a registry, the default registry is assumed.</p>"""
    repository_name: "capo_ecr.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the subject image.</p>"""
    subject_id: "capo_ecr.types.subject_identifier.SubjectIdentifier"
    """<p>An object containing the image digest of the subject image for which to retrieve associated artifacts.</p>"""
    filter: NotRequired[
        "capo_ecr.types.list_image_referrers_filter.ListImageReferrersFilter"
    ]
    """<p>The filter key and value with which to filter your <code>ListImageReferrers</code> results. If no filter is specified, only artifacts with <code>ACTIVE</code> status are returned.</p>"""
    next_token: NotRequired["capo_ecr.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> value returned from a previous paginated <code>ListImageReferrers</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. This value is <code>null</code> when there are no more results to return.</p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>"""
    max_results: NotRequired["capo_ecr.types.fifty_max_results.FiftyMaxResults"]
    """<p>The maximum number of image referrer results returned by <code>ListImageReferrers</code> in paginated output. When this parameter is used, <code>ListImageReferrers</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListImageReferrers</code> request with the returned <code>nextToken</code> value. This value can be between 1 and 50. If this parameter is not used, then <code>ListImageReferrers</code> returns up to 20 results and a <code>nextToken</code> value, if applicable.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListImageReferrersRequest) -> dict:
    out: dict = {}
    if "registry_id" in value:
        out["registryId"] = value["registry_id"]
    out["repositoryName"] = value["repository_name"]
    import capo_ecr.types.subject_identifier

    out["subjectId"] = capo_ecr.types.subject_identifier.serialize_aws_json_1_1(
        value["subject_id"]
    )
    if "filter" in value:
        import capo_ecr.types.list_image_referrers_filter

        out["filter"] = (
            capo_ecr.types.list_image_referrers_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListImageReferrersRequest:
    out: ListImageReferrersRequest = {}  # type: ignore[typeddict-item]
    if data.get("registryId") is not None:
        out["registry_id"] = data["registryId"]
    if data.get("repositoryName") is not None:
        out["repository_name"] = data["repositoryName"]
    else:
        out["repository_name"] = ""
    if data.get("subjectId") is not None:
        import capo_ecr.types.subject_identifier

        out["subject_id"] = capo_ecr.types.subject_identifier.deserialize_aws_json_1_1(
            data["subjectId"]
        )
    else:
        raise DeserializationError("ListImageReferrersRequest.subject_id required")
    if data.get("filter") is not None:
        import capo_ecr.types.list_image_referrers_filter

        out["filter"] = (
            capo_ecr.types.list_image_referrers_filter.deserialize_aws_json_1_1(
                data["filter"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out

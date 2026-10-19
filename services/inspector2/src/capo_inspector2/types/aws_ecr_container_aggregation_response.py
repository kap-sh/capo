"""Generated from Smithy shape ``com.amazonaws.inspector2#AwsEcrContainerAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.date_time_timestamp
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.severity_counts
    import capo_inspector2.types.string_list


class AwsEcrContainerAggregationResponse(TypedDict, closed=True):
    resource_id: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The resource ID of the container.</p>"""
    image_sha: NotRequired["str"]
    """<p>The SHA value of the container image.</p>"""
    repository: NotRequired["str"]
    """<p>The container repository.</p>"""
    architecture: NotRequired["str"]
    """<p>The architecture of the container.</p>"""
    image_tags: NotRequired["capo_inspector2.types.string_list.StringList"]
    """<p>The container image stags.</p>"""
    account_id: NotRequired["capo_inspector2.types.account_id.AccountId"]
    """<p>The Amazon Web Services account ID of the account that owns the container.</p>"""
    severity_counts: NotRequired["capo_inspector2.types.severity_counts.SeverityCounts"]
    """<p>The number of finding by severity.</p>"""
    last_in_use_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The last time an Amazon ECR image was used in an Amazon ECS task or Amazon EKS pod.</p>"""
    in_use_count: NotRequired["int"]
    """<p>The number of Amazon ECS tasks or Amazon EKS pods where the Amazon ECR container image is in use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcrContainerAggregationResponse) -> dict:
    out: dict = {}
    out["resourceId"] = value["resource_id"]
    if "image_sha" in value:
        out["imageSha"] = value["image_sha"]
    if "repository" in value:
        out["repository"] = value["repository"]
    if "architecture" in value:
        out["architecture"] = value["architecture"]
    if "image_tags" in value:
        import capo_inspector2.types.string_list

        out["imageTags"] = capo_inspector2.types.string_list.serialize_json(
            value["image_tags"]
        )
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "severity_counts" in value:
        import capo_inspector2.types.severity_counts

        out["severityCounts"] = capo_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    if "last_in_use_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["lastInUseAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["last_in_use_at"]
        )
    if "in_use_count" in value:
        out["inUseCount"] = value["in_use_count"]
    return out


def deserialize_json(data: dict) -> AwsEcrContainerAggregationResponse:
    out: AwsEcrContainerAggregationResponse = {}  # type: ignore[typeddict-item]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("imageSha") is not None:
        out["image_sha"] = data["imageSha"]
    if data.get("repository") is not None:
        out["repository"] = data["repository"]
    if data.get("architecture") is not None:
        out["architecture"] = data["architecture"]
    if data.get("imageTags") is not None:
        import capo_inspector2.types.string_list

        out["image_tags"] = capo_inspector2.types.string_list.deserialize_json(
            data["imageTags"]
        )
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("severityCounts") is not None:
        import capo_inspector2.types.severity_counts

        out["severity_counts"] = capo_inspector2.types.severity_counts.deserialize_json(
            data["severityCounts"]
        )
    if data.get("lastInUseAt") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["last_in_use_at"] = (
            capo_inspector2.types.date_time_timestamp.deserialize_json(
                data["lastInUseAt"]
            )
        )
    if data.get("inUseCount") is not None:
        out["in_use_count"] = data["inUseCount"]
    return out

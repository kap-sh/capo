"""Generated from Smithy shape ``com.amazonaws.codedeploy#ListApplicationRevisionsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.application_name
    import capo_codedeploy.types.application_revision_sort_by
    import capo_codedeploy.types.list_state_filter_action
    import capo_codedeploy.types.next_token
    import capo_codedeploy.types.s3_bucket
    import capo_codedeploy.types.s3_key
    import capo_codedeploy.types.sort_order


class ListApplicationRevisionsInput(TypedDict, closed=True):
    application_name: "capo_codedeploy.types.application_name.ApplicationName"
    """<p> The name of an CodeDeploy application associated with the user or Amazon Web Services account. </p>"""
    sort_by: NotRequired[
        "capo_codedeploy.types.application_revision_sort_by.ApplicationRevisionSortBy"
    ]
    """<p>The column name to use to sort the list results:</p> <ul> <li> <p> <code>registerTime</code>: Sort by the time the revisions were registered with CodeDeploy.</p> </li> <li> <p> <code>firstUsedTime</code>: Sort by the time the revisions were first used in a deployment.</p> </li> <li> <p> <code>lastUsedTime</code>: Sort by the time the revisions were last used in a deployment.</p> </li> </ul> <p> If not specified or set to null, the results are returned in an arbitrary order. </p>"""
    sort_order: NotRequired["capo_codedeploy.types.sort_order.SortOrder"]
    """<p> The order in which to sort the list results: </p> <ul> <li> <p> <code>ascending</code>: ascending order.</p> </li> <li> <p> <code>descending</code>: descending order.</p> </li> </ul> <p>If not specified, the results are sorted in ascending order.</p> <p>If set to null, the results are sorted in an arbitrary order.</p>"""
    s3_bucket: NotRequired["capo_codedeploy.types.s3_bucket.S3Bucket"]
    """<p> An Amazon S3 bucket name to limit the search for revisions. </p> <p> If set to null, all of the user's buckets are searched. </p>"""
    s3_key_prefix: NotRequired["capo_codedeploy.types.s3_key.S3Key"]
    """<p> A key prefix for the set of Amazon S3 objects to limit the search for revisions. </p>"""
    deployed: NotRequired[
        "capo_codedeploy.types.list_state_filter_action.ListStateFilterAction"
    ]
    """<p> Whether to list revisions based on whether the revision is the target revision of a deployment group: </p> <ul> <li> <p> <code>include</code>: List revisions that are target revisions of a deployment group.</p> </li> <li> <p> <code>exclude</code>: Do not list revisions that are target revisions of a deployment group.</p> </li> <li> <p> <code>ignore</code>: List all revisions.</p> </li> </ul>"""
    next_token: NotRequired["capo_codedeploy.types.next_token.NextToken"]
    """<p>An identifier returned from the previous <code>ListApplicationRevisions</code> call. It can be used to return the next set of applications in the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListApplicationRevisionsInput) -> dict:
    out: dict = {}
    out["applicationName"] = value["application_name"]
    if "sort_by" in value:
        import capo_codedeploy.types.application_revision_sort_by

        out["sortBy"] = (
            capo_codedeploy.types.application_revision_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_codedeploy.types.sort_order

        out["sortOrder"] = capo_codedeploy.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "s3_bucket" in value:
        out["s3Bucket"] = value["s3_bucket"]
    if "s3_key_prefix" in value:
        out["s3KeyPrefix"] = value["s3_key_prefix"]
    if "deployed" in value:
        import capo_codedeploy.types.list_state_filter_action

        out["deployed"] = (
            capo_codedeploy.types.list_state_filter_action.serialize_aws_json_1_1(
                value["deployed"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListApplicationRevisionsInput:
    out: ListApplicationRevisionsInput = {}  # type: ignore[typeddict-item]
    if data.get("applicationName") is not None:
        out["application_name"] = data["applicationName"]
    else:
        out["application_name"] = ""
    if data.get("sortBy") is not None:
        import capo_codedeploy.types.application_revision_sort_by

        out["sort_by"] = (
            capo_codedeploy.types.application_revision_sort_by.deserialize_aws_json_1_1(
                data["sortBy"]
            )
        )
    if data.get("sortOrder") is not None:
        import capo_codedeploy.types.sort_order

        out["sort_order"] = capo_codedeploy.types.sort_order.deserialize_aws_json_1_1(
            data["sortOrder"]
        )
    if data.get("s3Bucket") is not None:
        out["s3_bucket"] = data["s3Bucket"]
    if data.get("s3KeyPrefix") is not None:
        out["s3_key_prefix"] = data["s3KeyPrefix"]
    if data.get("deployed") is not None:
        import capo_codedeploy.types.list_state_filter_action

        out["deployed"] = (
            capo_codedeploy.types.list_state_filter_action.deserialize_aws_json_1_1(
                data["deployed"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

"""Generated from Smithy shape ``com.amazonaws.codebuild#WebhookFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.string
    import capo_codebuild.types.webhook_filter_type
    import capo_codebuild.types.wrapper_boolean


class WebhookFilter(TypedDict, closed=True):
    type: "capo_codebuild.types.webhook_filter_type.WebhookFilterType"
    """<p> The type of webhook filter. There are 11 webhook filter types: <code>EVENT</code>, <code>ACTOR_ACCOUNT_ID</code>, <code>HEAD_REF</code>, <code>BASE_REF</code>, <code>FILE_PATH</code>, <code>COMMIT_MESSAGE</code>, <code>TAG_NAME</code>, <code>RELEASE_NAME</code>, <code>REPOSITORY_NAME</code>, <code>ORGANIZATION_NAME</code>, and <code>WORKFLOW_NAME</code>. </p> <ul> <li> <p> EVENT </p> <ul> <li> <p> A webhook event triggers a build when the provided <code>pattern</code> matches one of nine event types: <code>PUSH</code>, <code>PULL_REQUEST_CREATED</code>, <code>PULL_REQUEST_UPDATED</code>, <code>PULL_REQUEST_CLOSED</code>, <code>PULL_REQUEST_REOPENED</code>, <code>PULL_REQUEST_MERGED</code>, <code>RELEASED</code>, <code>PRERELEASED</code>, and <code>WORKFLOW_JOB_QUEUED</code>. The <code>EVENT</code> patterns are specified as a comma-separated string. For example, <code>PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED</code> filters all push, pull request created, and pull request updated events. </p> <note> <p> Types <code>PULL_REQUEST_REOPENED</code> and <code>WORKFLOW_JOB_QUEUED</code> work with GitHub and GitHub Enterprise only. Types <code>RELEASED</code> and <code>PRERELEASED</code> work with GitHub only.</p> </note> </li> </ul> </li> <li> <p>ACTOR_ACCOUNT_ID</p> <ul> <li> <p> A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket account ID matches the regular expression <code>pattern</code>. </p> </li> </ul> </li> <li> <p>HEAD_REF</p> <ul> <li> <p> A webhook event triggers a build when the head reference matches the regular expression <code>pattern</code>. For example, <code>refs/heads/branch-name</code> and <code>refs/tags/tag-name</code>. </p> <note> <p> Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull request, Bitbucket push, and Bitbucket pull request events.</p> </note> </li> </ul> </li> <li> <p>BASE_REF</p> <ul> <li> <p> A webhook event triggers a build when the base reference matches the regular expression <code>pattern</code>. For example, <code>refs/heads/branch-name</code>. </p> <note> <p> Works with pull request events only. </p> </note> </li> </ul> </li> <li> <p>FILE_PATH</p> <ul> <li> <p> A webhook triggers a build when the path of a changed file matches the regular expression <code>pattern</code>. </p> <note> <p> Works with push and pull request events only. </p> </note> </li> </ul> </li> <li> <p>COMMIT_MESSAGE</p> <ul> <li> <p>A webhook triggers a build when the head commit message matches the regular expression <code>pattern</code>.</p> <note> <p> Works with push and pull request events only. </p> </note> </li> </ul> </li> <li> <p>TAG_NAME</p> <ul> <li> <p>A webhook triggers a build when the tag name of the release matches the regular expression <code>pattern</code>.</p> <note> <p> Works with <code>RELEASED</code> and <code>PRERELEASED</code> events only. </p> </note> </li> </ul> </li> <li> <p>RELEASE_NAME</p> <ul> <li> <p>A webhook triggers a build when the release name matches the regular expression <code>pattern</code>.</p> <note> <p> Works with <code>RELEASED</code> and <code>PRERELEASED</code> events only. </p> </note> </li> </ul> </li> <li> <p>REPOSITORY_NAME</p> <ul> <li> <p>A webhook triggers a build when the repository name matches the regular expression <code>pattern</code>.</p> <note> <p> Works with GitHub global or organization webhooks only. </p> </note> </li> </ul> </li> <li> <p>ORGANIZATION_NAME</p> <ul> <li> <p>A webhook triggers a build when the organization name matches the regular expression <code>pattern</code>.</p> <note> <p> Works with GitHub global webhooks only. </p> </note> </li> </ul> </li> <li> <p>WORKFLOW_NAME</p> <ul> <li> <p>A webhook triggers a build when the workflow name matches the regular expression <code>pattern</code>.</p> <note> <p> Works with <code>WORKFLOW_JOB_QUEUED</code> events only. </p> </note> <note> <p>For CodeBuild-hosted Buildkite runner builds, WORKFLOW_NAME filters will filter by pipeline name.</p> </note> </li> </ul> </li> </ul>"""
    pattern: "capo_codebuild.types.string.String"
    """<p> For a <code>WebHookFilter</code> that uses <code>EVENT</code> type, a comma-separated string that specifies one or more events. For example, the webhook filter <code>PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED</code> allows all push, pull request created, and pull request updated events to trigger a build. </p> <p> For a <code>WebHookFilter</code> that uses any of the other filter types, a regular expression pattern. For example, a <code>WebHookFilter</code> that uses <code>HEAD_REF</code> for its <code>type</code> and the pattern <code>^refs/heads/</code> triggers a build when the head reference is a branch with a reference name <code>refs/heads/branch-name</code>. </p>"""
    exclude_matched_pattern: NotRequired[
        "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p> Used to indicate that the <code>pattern</code> determines which webhook events do not trigger a build. If true, then a webhook event that does not match the <code>pattern</code> triggers a build. If false, then a webhook event that matches the <code>pattern</code> triggers a build. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebhookFilter) -> dict:
    out: dict = {}
    import capo_codebuild.types.webhook_filter_type

    out["type"] = capo_codebuild.types.webhook_filter_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["pattern"] = value["pattern"]
    if "exclude_matched_pattern" in value:
        out["excludeMatchedPattern"] = value["exclude_matched_pattern"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WebhookFilter:
    out: WebhookFilter = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codebuild.types.webhook_filter_type

        out["type"] = capo_codebuild.types.webhook_filter_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_codebuild.types.webhook_filter_type.WebhookFilterType", ""
        )
    if data.get("pattern") is not None:
        out["pattern"] = data["pattern"]
    else:
        out["pattern"] = ""
    if data.get("excludeMatchedPattern") is not None:
        out["exclude_matched_pattern"] = data["excludeMatchedPattern"]
    return out

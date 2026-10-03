"""Generated from Smithy shape ``com.amazonaws.codebuild#Webhook``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.filter_groups
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.pull_request_build_policy
    import capo_codebuild.types.scope_configuration
    import capo_codebuild.types.string
    import capo_codebuild.types.timestamp
    import capo_codebuild.types.webhook_build_type
    import capo_codebuild.types.webhook_status
    import capo_codebuild.types.wrapper_boolean


class Webhook(TypedDict, closed=True):
    url: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The URL to the webhook.</p>"""
    payload_url: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The CodeBuild endpoint where webhook events are sent.</p>"""
    secret: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The secret token of the associated repository. </p> <note> <p>A Bitbucket webhook does not support <code>secret</code>. </p> </note>"""
    branch_filter: NotRequired["capo_codebuild.types.string.String"]
    """<p>A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If <code>branchFilter</code> is empty, then all branches are built.</p> <note> <p>It is recommended that you use <code>filterGroups</code> instead of <code>branchFilter</code>. </p> </note>"""
    filter_groups: NotRequired["capo_codebuild.types.filter_groups.FilterGroups"]
    """<p>An array of arrays of <code>WebhookFilter</code> objects used to determine which webhooks are triggered. At least one <code>WebhookFilter</code> in the array must specify <code>EVENT</code> as its <code>type</code>. </p> <p>For a build to be triggered, at least one filter group in the <code>filterGroups</code> array must pass. For a filter group to pass, each of its filters must pass. </p>"""
    build_type: NotRequired["capo_codebuild.types.webhook_build_type.WebhookBuildType"]
    """<p>Specifies the type of build this webhook will trigger.</p> <note> <p> <code>RUNNER_BUILDKITE_BUILD</code> is only available for <code>NO_SOURCE</code> source type projects configured for Buildkite runner builds. For more information about CodeBuild-hosted Buildkite runner builds, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runner-buildkite.html">Tutorial: Configure a CodeBuild-hosted Buildkite runner</a> in the <i>CodeBuild user guide</i>.</p> </note>"""
    manual_creation: NotRequired["capo_codebuild.types.wrapper_boolean.WrapperBoolean"]
    """<p>If manualCreation is true, CodeBuild doesn't create a webhook in GitHub and instead returns <code>payloadUrl</code> and <code>secret</code> values for the webhook. The <code>payloadUrl</code> and <code>secret</code> values in the output can be used to manually create a webhook within GitHub.</p> <note> <p>manualCreation is only available for GitHub webhooks.</p> </note>"""
    last_modified_secret: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates the last time a repository's secret token was modified. </p>"""
    scope_configuration: NotRequired[
        "capo_codebuild.types.scope_configuration.ScopeConfiguration"
    ]
    """<p>The scope configuration for global or organization webhooks.</p> <note> <p>Global or organization webhooks are only available for GitHub and Github Enterprise webhooks.</p> </note>"""
    status: NotRequired["capo_codebuild.types.webhook_status.WebhookStatus"]
    """<p>The status of the webhook. Valid values include:</p> <ul> <li> <p> <code>CREATING</code>: The webhook is being created.</p> </li> <li> <p> <code>CREATE_FAILED</code>: The webhook has failed to create.</p> </li> <li> <p> <code>ACTIVE</code>: The webhook has succeeded and is active.</p> </li> <li> <p> <code>DELETING</code>: The webhook is being deleted.</p> </li> </ul>"""
    status_message: NotRequired["capo_codebuild.types.string.String"]
    """<p>A message associated with the status of a webhook.</p>"""
    pull_request_build_policy: NotRequired[
        "capo_codebuild.types.pull_request_build_policy.PullRequestBuildPolicy"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Webhook) -> dict:
    out: dict = {}
    if "url" in value:
        out["url"] = value["url"]
    if "payload_url" in value:
        out["payloadUrl"] = value["payload_url"]
    if "secret" in value:
        out["secret"] = value["secret"]
    if "branch_filter" in value:
        out["branchFilter"] = value["branch_filter"]
    if "filter_groups" in value:
        import capo_codebuild.types.filter_groups

        out["filterGroups"] = capo_codebuild.types.filter_groups.serialize_aws_json_1_1(
            value["filter_groups"]
        )
    if "build_type" in value:
        import capo_codebuild.types.webhook_build_type

        out["buildType"] = (
            capo_codebuild.types.webhook_build_type.serialize_aws_json_1_1(
                value["build_type"]
            )
        )
    if "manual_creation" in value:
        out["manualCreation"] = value["manual_creation"]
    if "last_modified_secret" in value:
        import capo_codebuild.types.timestamp

        out["lastModifiedSecret"] = (
            capo_codebuild.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_secret"]
            )
        )
    if "scope_configuration" in value:
        import capo_codebuild.types.scope_configuration

        out["scopeConfiguration"] = (
            capo_codebuild.types.scope_configuration.serialize_aws_json_1_1(
                value["scope_configuration"]
            )
        )
    if "status" in value:
        import capo_codebuild.types.webhook_status

        out["status"] = capo_codebuild.types.webhook_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "pull_request_build_policy" in value:
        import capo_codebuild.types.pull_request_build_policy

        out["pullRequestBuildPolicy"] = (
            capo_codebuild.types.pull_request_build_policy.serialize_aws_json_1_1(
                value["pull_request_build_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Webhook:
    out: Webhook = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    if data.get("payloadUrl") is not None:
        out["payload_url"] = data["payloadUrl"]
    if data.get("secret") is not None:
        out["secret"] = data["secret"]
    if data.get("branchFilter") is not None:
        out["branch_filter"] = data["branchFilter"]
    if data.get("filterGroups") is not None:
        import capo_codebuild.types.filter_groups

        out["filter_groups"] = (
            capo_codebuild.types.filter_groups.deserialize_aws_json_1_1(
                data["filterGroups"]
            )
        )
    if data.get("buildType") is not None:
        import capo_codebuild.types.webhook_build_type

        out["build_type"] = (
            capo_codebuild.types.webhook_build_type.deserialize_aws_json_1_1(
                data["buildType"]
            )
        )
    if data.get("manualCreation") is not None:
        out["manual_creation"] = data["manualCreation"]
    if data.get("lastModifiedSecret") is not None:
        import capo_codebuild.types.timestamp

        out["last_modified_secret"] = (
            capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
                data["lastModifiedSecret"]
            )
        )
    if data.get("scopeConfiguration") is not None:
        import capo_codebuild.types.scope_configuration

        out["scope_configuration"] = (
            capo_codebuild.types.scope_configuration.deserialize_aws_json_1_1(
                data["scopeConfiguration"]
            )
        )
    if data.get("status") is not None:
        import capo_codebuild.types.webhook_status

        out["status"] = capo_codebuild.types.webhook_status.deserialize_aws_json_1_1(
            data["status"]
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("pullRequestBuildPolicy") is not None:
        import capo_codebuild.types.pull_request_build_policy

        out["pull_request_build_policy"] = (
            capo_codebuild.types.pull_request_build_policy.deserialize_aws_json_1_1(
                data["pullRequestBuildPolicy"]
            )
        )
    return out

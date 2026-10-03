"""Generated from Smithy shape ``com.amazonaws.codebuild#CreateWebhookInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.filter_groups
    import capo_codebuild.types.project_name
    import capo_codebuild.types.pull_request_build_policy
    import capo_codebuild.types.scope_configuration
    import capo_codebuild.types.string
    import capo_codebuild.types.webhook_build_type
    import capo_codebuild.types.wrapper_boolean


class CreateWebhookInput(TypedDict, closed=True):
    project_name: "capo_codebuild.types.project_name.ProjectName"
    """<p>The name of the CodeBuild project.</p>"""
    branch_filter: NotRequired["capo_codebuild.types.string.String"]
    """<p>A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If <code>branchFilter</code> is empty, then all branches are built.</p> <note> <p>It is recommended that you use <code>filterGroups</code> instead of <code>branchFilter</code>. </p> </note>"""
    filter_groups: NotRequired["capo_codebuild.types.filter_groups.FilterGroups"]
    """<p>An array of arrays of <code>WebhookFilter</code> objects used to determine which webhooks are triggered. At least one <code>WebhookFilter</code> in the array must specify <code>EVENT</code> as its <code>type</code>. </p> <p>For a build to be triggered, at least one filter group in the <code>filterGroups</code> array must pass. For a filter group to pass, each of its filters must pass. </p>"""
    build_type: NotRequired["capo_codebuild.types.webhook_build_type.WebhookBuildType"]
    """<p>Specifies the type of build this webhook will trigger.</p> <note> <p> <code>RUNNER_BUILDKITE_BUILD</code> is only available for <code>NO_SOURCE</code> source type projects configured for Buildkite runner builds. For more information about CodeBuild-hosted Buildkite runner builds, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runner-buildkite.html">Tutorial: Configure a CodeBuild-hosted Buildkite runner</a> in the <i>CodeBuild user guide</i>.</p> </note>"""
    manual_creation: NotRequired["capo_codebuild.types.wrapper_boolean.WrapperBoolean"]
    """<p>If manualCreation is true, CodeBuild doesn't create a webhook in GitHub and instead returns <code>payloadUrl</code> and <code>secret</code> values for the webhook. The <code>payloadUrl</code> and <code>secret</code> values in the output can be used to manually create a webhook within GitHub.</p> <note> <p> <code>manualCreation</code> is only available for GitHub webhooks.</p> </note>"""
    scope_configuration: NotRequired[
        "capo_codebuild.types.scope_configuration.ScopeConfiguration"
    ]
    """<p>The scope configuration for global or organization webhooks.</p> <note> <p>Global or organization webhooks are only available for GitHub and Github Enterprise webhooks.</p> </note>"""
    pull_request_build_policy: NotRequired[
        "capo_codebuild.types.pull_request_build_policy.PullRequestBuildPolicy"
    ]
    """<p>A PullRequestBuildPolicy object that defines comment-based approval requirements for triggering builds on pull requests. This policy helps control when automated builds are executed based on contributor permissions and approval workflows.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWebhookInput) -> dict:
    out: dict = {}
    out["projectName"] = value["project_name"]
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
    if "scope_configuration" in value:
        import capo_codebuild.types.scope_configuration

        out["scopeConfiguration"] = (
            capo_codebuild.types.scope_configuration.serialize_aws_json_1_1(
                value["scope_configuration"]
            )
        )
    if "pull_request_build_policy" in value:
        import capo_codebuild.types.pull_request_build_policy

        out["pullRequestBuildPolicy"] = (
            capo_codebuild.types.pull_request_build_policy.serialize_aws_json_1_1(
                value["pull_request_build_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWebhookInput:
    out: CreateWebhookInput = {}  # type: ignore[typeddict-item]
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("CreateWebhookInput.project_name required")
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
    if data.get("scopeConfiguration") is not None:
        import capo_codebuild.types.scope_configuration

        out["scope_configuration"] = (
            capo_codebuild.types.scope_configuration.deserialize_aws_json_1_1(
                data["scopeConfiguration"]
            )
        )
    if data.get("pullRequestBuildPolicy") is not None:
        import capo_codebuild.types.pull_request_build_policy

        out["pull_request_build_policy"] = (
            capo_codebuild.types.pull_request_build_policy.deserialize_aws_json_1_1(
                data["pullRequestBuildPolicy"]
            )
        )
    return out

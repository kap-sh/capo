"""Generated from Smithy shape ``com.amazonaws.amplify#CreateBranchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.app_id
    import capo_amplify.types.backend
    import capo_amplify.types.backend_environment_arn
    import capo_amplify.types.basic_auth_credentials
    import capo_amplify.types.branch_name
    import capo_amplify.types.build_spec
    import capo_amplify.types.compute_role_arn
    import capo_amplify.types.description
    import capo_amplify.types.display_name
    import capo_amplify.types.enable_auto_build
    import capo_amplify.types.enable_basic_auth
    import capo_amplify.types.enable_notification
    import capo_amplify.types.enable_performance_mode
    import capo_amplify.types.enable_pull_request_preview
    import capo_amplify.types.enable_skew_protection
    import capo_amplify.types.environment_variables
    import capo_amplify.types.framework
    import capo_amplify.types.pull_request_environment_name
    import capo_amplify.types.stage
    import capo_amplify.types.tag_map
    import capo_amplify.types.ttl


class CreateBranchRequest(TypedDict, closed=True):
    app_id: "capo_amplify.types.app_id.AppId"
    """<p> The unique ID for an Amplify app. </p>"""
    branch_name: "capo_amplify.types.branch_name.BranchName"
    """<p>The name for the branch. </p>"""
    description: NotRequired["capo_amplify.types.description.Description"]
    """<p>The description for the branch. </p>"""
    stage: NotRequired["capo_amplify.types.stage.Stage"]
    """<p>Describes the current stage for the branch. </p>"""
    framework: NotRequired["capo_amplify.types.framework.Framework"]
    """<p> The framework for the branch. </p>"""
    enable_notification: NotRequired[
        "capo_amplify.types.enable_notification.EnableNotification"
    ]
    """<p> Enables notifications for the branch. </p>"""
    enable_auto_build: NotRequired[
        "capo_amplify.types.enable_auto_build.EnableAutoBuild"
    ]
    """<p> Enables auto building for the branch. </p>"""
    enable_skew_protection: NotRequired[
        "capo_amplify.types.enable_skew_protection.EnableSkewProtection"
    ]
    """<p>Specifies whether the skew protection feature is enabled for the branch.</p> <p>Deployment skew protection is available to Amplify applications to eliminate version skew issues between client and servers in web applications. When you apply skew protection to a branch, you can ensure that your clients always interact with the correct version of server-side assets, regardless of when a deployment occurs. For more information about skew protection, see <a href="https://docs.aws.amazon.com/amplify/latest/userguide/skew-protection.html">Skew protection for Amplify deployments</a> in the <i>Amplify User Guide</i>.</p>"""
    environment_variables: NotRequired[
        "capo_amplify.types.environment_variables.EnvironmentVariables"
    ]
    """<p> The environment variables for the branch. </p>"""
    basic_auth_credentials: NotRequired[
        "capo_amplify.types.basic_auth_credentials.BasicAuthCredentials"
    ]
    """<p> The basic authorization credentials for the branch. You must base64-encode the authorization credentials and provide them in the format <code>user:password</code>.</p>"""
    enable_basic_auth: NotRequired[
        "capo_amplify.types.enable_basic_auth.EnableBasicAuth"
    ]
    """<p> Enables basic authorization for the branch. </p>"""
    enable_performance_mode: NotRequired[
        "capo_amplify.types.enable_performance_mode.EnablePerformanceMode"
    ]
    """<p>Enables performance mode for the branch.</p> <p>Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out. </p>"""
    tags: NotRequired["capo_amplify.types.tag_map.TagMap"]
    """<p> The tag for the branch. </p>"""
    build_spec: NotRequired["capo_amplify.types.build_spec.BuildSpec"]
    """<p> The build specification (build spec) for the branch. </p>"""
    ttl: NotRequired["capo_amplify.types.ttl.TTL"]
    """<p> The content Time To Live (TTL) for the website in seconds. </p>"""
    display_name: NotRequired["capo_amplify.types.display_name.DisplayName"]
    """<p> The display name for a branch. This is used as the default domain prefix. </p>"""
    enable_pull_request_preview: NotRequired[
        "capo_amplify.types.enable_pull_request_preview.EnablePullRequestPreview"
    ]
    """<p> Enables pull request previews for this branch. </p>"""
    pull_request_environment_name: NotRequired[
        "capo_amplify.types.pull_request_environment_name.PullRequestEnvironmentName"
    ]
    """<p> The Amplify environment name for the pull request. </p>"""
    backend_environment_arn: NotRequired[
        "capo_amplify.types.backend_environment_arn.BackendEnvironmentArn"
    ]
    """<p>The Amazon Resource Name (ARN) for a backend environment that is part of a Gen 1 Amplify app. </p> <p>This field is available to Amplify Gen 1 apps only where the backend is created using Amplify Studio or the Amplify command line interface (CLI).</p>"""
    backend: NotRequired["capo_amplify.types.backend.Backend"]
    """<p>The backend for a <code>Branch</code> of an Amplify app. Use for a backend created from an CloudFormation stack.</p> <p>This field is available to Amplify Gen 2 apps only. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.</p>"""
    compute_role_arn: NotRequired["capo_amplify.types.compute_role_arn.ComputeRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to assign to a branch of an SSR app. The SSR Compute role allows the Amplify Hosting compute service to securely access specific Amazon Web Services resources based on the role's permissions. For more information about the SSR Compute role, see <a href="https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html">Adding an SSR Compute role</a> in the <i>Amplify User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBranchRequest) -> dict:
    out: dict = {}
    out["branchName"] = value["branch_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "stage" in value:
        import capo_amplify.types.stage

        out["stage"] = capo_amplify.types.stage.serialize_json(value["stage"])
    if "framework" in value:
        out["framework"] = value["framework"]
    if "enable_notification" in value:
        out["enableNotification"] = value["enable_notification"]
    if "enable_auto_build" in value:
        out["enableAutoBuild"] = value["enable_auto_build"]
    if "enable_skew_protection" in value:
        out["enableSkewProtection"] = value["enable_skew_protection"]
    if "environment_variables" in value:
        import capo_amplify.types.environment_variables

        out["environmentVariables"] = (
            capo_amplify.types.environment_variables.serialize_json(
                value["environment_variables"]
            )
        )
    if "basic_auth_credentials" in value:
        out["basicAuthCredentials"] = value["basic_auth_credentials"]
    if "enable_basic_auth" in value:
        out["enableBasicAuth"] = value["enable_basic_auth"]
    if "enable_performance_mode" in value:
        out["enablePerformanceMode"] = value["enable_performance_mode"]
    if "tags" in value:
        import capo_amplify.types.tag_map

        out["tags"] = capo_amplify.types.tag_map.serialize_json(value["tags"])
    if "build_spec" in value:
        out["buildSpec"] = value["build_spec"]
    if "ttl" in value:
        out["ttl"] = value["ttl"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "enable_pull_request_preview" in value:
        out["enablePullRequestPreview"] = value["enable_pull_request_preview"]
    if "pull_request_environment_name" in value:
        out["pullRequestEnvironmentName"] = value["pull_request_environment_name"]
    if "backend_environment_arn" in value:
        out["backendEnvironmentArn"] = value["backend_environment_arn"]
    if "backend" in value:
        import capo_amplify.types.backend

        out["backend"] = capo_amplify.types.backend.serialize_json(value["backend"])
    if "compute_role_arn" in value:
        out["computeRoleArn"] = value["compute_role_arn"]
    return out


def deserialize_json(data: dict) -> CreateBranchRequest:
    out: CreateBranchRequest = {}  # type: ignore[typeddict-item]
    if data.get("branchName") is not None:
        out["branch_name"] = data["branchName"]
    else:
        raise DeserializationError("CreateBranchRequest.branch_name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("stage") is not None:
        import capo_amplify.types.stage

        out["stage"] = capo_amplify.types.stage.deserialize_json(data["stage"])
    if data.get("framework") is not None:
        out["framework"] = data["framework"]
    if data.get("enableNotification") is not None:
        out["enable_notification"] = data["enableNotification"]
    if data.get("enableAutoBuild") is not None:
        out["enable_auto_build"] = data["enableAutoBuild"]
    if data.get("enableSkewProtection") is not None:
        out["enable_skew_protection"] = data["enableSkewProtection"]
    if data.get("environmentVariables") is not None:
        import capo_amplify.types.environment_variables

        out["environment_variables"] = (
            capo_amplify.types.environment_variables.deserialize_json(
                data["environmentVariables"]
            )
        )
    if data.get("basicAuthCredentials") is not None:
        out["basic_auth_credentials"] = data["basicAuthCredentials"]
    if data.get("enableBasicAuth") is not None:
        out["enable_basic_auth"] = data["enableBasicAuth"]
    if data.get("enablePerformanceMode") is not None:
        out["enable_performance_mode"] = data["enablePerformanceMode"]
    if data.get("tags") is not None:
        import capo_amplify.types.tag_map

        out["tags"] = capo_amplify.types.tag_map.deserialize_json(data["tags"])
    if data.get("buildSpec") is not None:
        out["build_spec"] = data["buildSpec"]
    if data.get("ttl") is not None:
        out["ttl"] = data["ttl"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("enablePullRequestPreview") is not None:
        out["enable_pull_request_preview"] = data["enablePullRequestPreview"]
    if data.get("pullRequestEnvironmentName") is not None:
        out["pull_request_environment_name"] = data["pullRequestEnvironmentName"]
    if data.get("backendEnvironmentArn") is not None:
        out["backend_environment_arn"] = data["backendEnvironmentArn"]
    if data.get("backend") is not None:
        import capo_amplify.types.backend

        out["backend"] = capo_amplify.types.backend.deserialize_json(data["backend"])
    if data.get("computeRoleArn") is not None:
        out["compute_role_arn"] = data["computeRoleArn"]
    return out

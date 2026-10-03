"""Generated from Smithy shape ``com.amazonaws.amplify#Branch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.active_job_id
    import capo_amplify.types.associated_resources
    import capo_amplify.types.backend
    import capo_amplify.types.backend_environment_arn
    import capo_amplify.types.basic_auth_credentials
    import capo_amplify.types.branch_arn
    import capo_amplify.types.branch_name
    import capo_amplify.types.build_spec
    import capo_amplify.types.compute_role_arn
    import capo_amplify.types.create_time
    import capo_amplify.types.custom_domains
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
    import capo_amplify.types.thumbnail_url
    import capo_amplify.types.total_number_of_jobs
    import capo_amplify.types.ttl
    import capo_amplify.types.update_time


class Branch(TypedDict, closed=True):
    branch_arn: "capo_amplify.types.branch_arn.BranchArn"
    """<p> The Amazon Resource Name (ARN) for a branch that is part of an Amplify app. </p>"""
    branch_name: "capo_amplify.types.branch_name.BranchName"
    """<p> The name for the branch that is part of an Amplify app. </p>"""
    description: "capo_amplify.types.description.Description"
    """<p> The description for the branch that is part of an Amplify app. </p>"""
    tags: NotRequired["capo_amplify.types.tag_map.TagMap"]
    """<p> The tag for the branch of an Amplify app. </p>"""
    stage: "capo_amplify.types.stage.Stage"
    """<p> The current stage for the branch that is part of an Amplify app. </p>"""
    display_name: "capo_amplify.types.display_name.DisplayName"
    """<p> The display name for the branch. This is used as the default domain prefix. </p>"""
    enable_notification: "capo_amplify.types.enable_notification.EnableNotification"
    """<p> Enables notifications for a branch that is part of an Amplify app. </p>"""
    create_time: "capo_amplify.types.create_time.CreateTime"
    """<p>A timestamp of when Amplify created the branch.</p>"""
    update_time: "capo_amplify.types.update_time.UpdateTime"
    """<p>A timestamp for the last updated time for a branch.</p>"""
    environment_variables: (
        "capo_amplify.types.environment_variables.EnvironmentVariables"
    )
    """<p> The environment variables specific to a branch of an Amplify app. </p>"""
    enable_auto_build: "capo_amplify.types.enable_auto_build.EnableAutoBuild"
    """<p> Enables auto-building on push for a branch of an Amplify app. </p>"""
    enable_skew_protection: NotRequired[
        "capo_amplify.types.enable_skew_protection.EnableSkewProtection"
    ]
    """<p>Specifies whether the skew protection feature is enabled for the branch.</p> <p>Deployment skew protection is available to Amplify applications to eliminate version skew issues between client and servers in web applications. When you apply skew protection to a branch, you can ensure that your clients always interact with the correct version of server-side assets, regardless of when a deployment occurs. For more information about skew protection, see <a href="https://docs.aws.amazon.com/amplify/latest/userguide/skew-protection.html">Skew protection for Amplify deployments</a> in the <i>Amplify User Guide</i>.</p>"""
    custom_domains: "capo_amplify.types.custom_domains.CustomDomains"
    """<p> The custom domains for a branch of an Amplify app. </p>"""
    framework: "capo_amplify.types.framework.Framework"
    """<p> The framework for a branch of an Amplify app. </p>"""
    active_job_id: "capo_amplify.types.active_job_id.ActiveJobId"
    """<p> The ID of the active job for a branch of an Amplify app. </p>"""
    total_number_of_jobs: "capo_amplify.types.total_number_of_jobs.TotalNumberOfJobs"
    """<p> The total number of jobs that are part of an Amplify app. </p>"""
    enable_basic_auth: "capo_amplify.types.enable_basic_auth.EnableBasicAuth"
    """<p> Enables basic authorization for a branch of an Amplify app. </p>"""
    enable_performance_mode: NotRequired[
        "capo_amplify.types.enable_performance_mode.EnablePerformanceMode"
    ]
    """<p>Enables performance mode for the branch.</p> <p>Performance mode optimizes for faster hosting performance by keeping content cached at the edge for a longer interval. When performance mode is enabled, hosting configuration or code changes can take up to 10 minutes to roll out. </p>"""
    thumbnail_url: NotRequired["capo_amplify.types.thumbnail_url.ThumbnailUrl"]
    """<p> The thumbnail URL for the branch of an Amplify app. </p>"""
    basic_auth_credentials: NotRequired[
        "capo_amplify.types.basic_auth_credentials.BasicAuthCredentials"
    ]
    """<p> The basic authorization credentials for a branch of an Amplify app. You must base64-encode the authorization credentials and provide them in the format <code>user:password</code>.</p>"""
    build_spec: NotRequired["capo_amplify.types.build_spec.BuildSpec"]
    """<p> The build specification (build spec) content for the branch of an Amplify app. </p>"""
    ttl: "capo_amplify.types.ttl.TTL"
    """<p> The content Time to Live (TTL) for the website in seconds. </p>"""
    associated_resources: NotRequired[
        "capo_amplify.types.associated_resources.AssociatedResources"
    ]
    """<p> A list of custom resources that are linked to this branch. </p>"""
    enable_pull_request_preview: (
        "capo_amplify.types.enable_pull_request_preview.EnablePullRequestPreview"
    )
    """<p> Enables pull request previews for the branch. </p>"""
    pull_request_environment_name: NotRequired[
        "capo_amplify.types.pull_request_environment_name.PullRequestEnvironmentName"
    ]
    """<p> The Amplify environment name for the pull request. </p>"""
    destination_branch: NotRequired["capo_amplify.types.branch_name.BranchName"]
    """<p> The destination branch if the branch is a pull request branch. </p>"""
    source_branch: NotRequired["capo_amplify.types.branch_name.BranchName"]
    """<p> The source branch if the branch is a pull request branch. </p>"""
    backend_environment_arn: NotRequired[
        "capo_amplify.types.backend_environment_arn.BackendEnvironmentArn"
    ]
    """<p> The Amazon Resource Name (ARN) for a backend environment that is part of an Amplify app. </p> <p>This property is available to Amplify Gen 1 apps only. When you deploy an application with Amplify Gen 2, you provision the app's backend infrastructure using Typescript code.</p>"""
    backend: NotRequired["capo_amplify.types.backend.Backend"]
    compute_role_arn: NotRequired["capo_amplify.types.compute_role_arn.ComputeRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role for a branch of an SSR app. The Compute role allows the Amplify Hosting compute service to securely access specific Amazon Web Services resources based on the role's permissions. For more information about the SSR Compute role, see <a href="https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html">Adding an SSR Compute role</a> in the <i>Amplify User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Branch) -> dict:
    out: dict = {}
    out["branchArn"] = value["branch_arn"]
    out["branchName"] = value["branch_name"]
    out["description"] = value["description"]
    if "tags" in value:
        import capo_amplify.types.tag_map

        out["tags"] = capo_amplify.types.tag_map.serialize_json(value["tags"])
    import capo_amplify.types.stage

    out["stage"] = capo_amplify.types.stage.serialize_json(value["stage"])
    out["displayName"] = value["display_name"]
    out["enableNotification"] = value["enable_notification"]
    import capo_amplify.types.create_time

    out["createTime"] = capo_amplify.types.create_time.serialize_json(
        value["create_time"]
    )
    import capo_amplify.types.update_time

    out["updateTime"] = capo_amplify.types.update_time.serialize_json(
        value["update_time"]
    )
    import capo_amplify.types.environment_variables

    out["environmentVariables"] = (
        capo_amplify.types.environment_variables.serialize_json(
            value["environment_variables"]
        )
    )
    out["enableAutoBuild"] = value["enable_auto_build"]
    if "enable_skew_protection" in value:
        out["enableSkewProtection"] = value["enable_skew_protection"]
    import capo_amplify.types.custom_domains

    out["customDomains"] = capo_amplify.types.custom_domains.serialize_json(
        value["custom_domains"]
    )
    out["framework"] = value["framework"]
    out["activeJobId"] = value["active_job_id"]
    out["totalNumberOfJobs"] = value["total_number_of_jobs"]
    out["enableBasicAuth"] = value["enable_basic_auth"]
    if "enable_performance_mode" in value:
        out["enablePerformanceMode"] = value["enable_performance_mode"]
    if "thumbnail_url" in value:
        out["thumbnailUrl"] = value["thumbnail_url"]
    if "basic_auth_credentials" in value:
        out["basicAuthCredentials"] = value["basic_auth_credentials"]
    if "build_spec" in value:
        out["buildSpec"] = value["build_spec"]
    out["ttl"] = value["ttl"]
    if "associated_resources" in value:
        import capo_amplify.types.associated_resources

        out["associatedResources"] = (
            capo_amplify.types.associated_resources.serialize_json(
                value["associated_resources"]
            )
        )
    out["enablePullRequestPreview"] = value["enable_pull_request_preview"]
    if "pull_request_environment_name" in value:
        out["pullRequestEnvironmentName"] = value["pull_request_environment_name"]
    if "destination_branch" in value:
        out["destinationBranch"] = value["destination_branch"]
    if "source_branch" in value:
        out["sourceBranch"] = value["source_branch"]
    if "backend_environment_arn" in value:
        out["backendEnvironmentArn"] = value["backend_environment_arn"]
    if "backend" in value:
        import capo_amplify.types.backend

        out["backend"] = capo_amplify.types.backend.serialize_json(value["backend"])
    if "compute_role_arn" in value:
        out["computeRoleArn"] = value["compute_role_arn"]
    return out


def deserialize_json(data: dict) -> Branch:
    out: Branch = {}  # type: ignore[typeddict-item]
    if data.get("branchArn") is not None:
        out["branch_arn"] = data["branchArn"]
    else:
        raise DeserializationError("Branch.branch_arn required")
    if data.get("branchName") is not None:
        out["branch_name"] = data["branchName"]
    else:
        raise DeserializationError("Branch.branch_name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        raise DeserializationError("Branch.description required")
    if data.get("tags") is not None:
        import capo_amplify.types.tag_map

        out["tags"] = capo_amplify.types.tag_map.deserialize_json(data["tags"])
    if data.get("stage") is not None:
        import capo_amplify.types.stage

        out["stage"] = capo_amplify.types.stage.deserialize_json(data["stage"])
    else:
        raise DeserializationError("Branch.stage required")
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("Branch.display_name required")
    if data.get("enableNotification") is not None:
        out["enable_notification"] = data["enableNotification"]
    else:
        raise DeserializationError("Branch.enable_notification required")
    if data.get("createTime") is not None:
        import capo_amplify.types.create_time

        out["create_time"] = capo_amplify.types.create_time.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError("Branch.create_time required")
    if data.get("updateTime") is not None:
        import capo_amplify.types.update_time

        out["update_time"] = capo_amplify.types.update_time.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("Branch.update_time required")
    if data.get("environmentVariables") is not None:
        import capo_amplify.types.environment_variables

        out["environment_variables"] = (
            capo_amplify.types.environment_variables.deserialize_json(
                data["environmentVariables"]
            )
        )
    else:
        raise DeserializationError("Branch.environment_variables required")
    if data.get("enableAutoBuild") is not None:
        out["enable_auto_build"] = data["enableAutoBuild"]
    else:
        raise DeserializationError("Branch.enable_auto_build required")
    if data.get("enableSkewProtection") is not None:
        out["enable_skew_protection"] = data["enableSkewProtection"]
    if data.get("customDomains") is not None:
        import capo_amplify.types.custom_domains

        out["custom_domains"] = capo_amplify.types.custom_domains.deserialize_json(
            data["customDomains"]
        )
    else:
        raise DeserializationError("Branch.custom_domains required")
    if data.get("framework") is not None:
        out["framework"] = data["framework"]
    else:
        raise DeserializationError("Branch.framework required")
    if data.get("activeJobId") is not None:
        out["active_job_id"] = data["activeJobId"]
    else:
        raise DeserializationError("Branch.active_job_id required")
    if data.get("totalNumberOfJobs") is not None:
        out["total_number_of_jobs"] = data["totalNumberOfJobs"]
    else:
        raise DeserializationError("Branch.total_number_of_jobs required")
    if data.get("enableBasicAuth") is not None:
        out["enable_basic_auth"] = data["enableBasicAuth"]
    else:
        raise DeserializationError("Branch.enable_basic_auth required")
    if data.get("enablePerformanceMode") is not None:
        out["enable_performance_mode"] = data["enablePerformanceMode"]
    if data.get("thumbnailUrl") is not None:
        out["thumbnail_url"] = data["thumbnailUrl"]
    if data.get("basicAuthCredentials") is not None:
        out["basic_auth_credentials"] = data["basicAuthCredentials"]
    if data.get("buildSpec") is not None:
        out["build_spec"] = data["buildSpec"]
    if data.get("ttl") is not None:
        out["ttl"] = data["ttl"]
    else:
        raise DeserializationError("Branch.ttl required")
    if data.get("associatedResources") is not None:
        import capo_amplify.types.associated_resources

        out["associated_resources"] = (
            capo_amplify.types.associated_resources.deserialize_json(
                data["associatedResources"]
            )
        )
    if data.get("enablePullRequestPreview") is not None:
        out["enable_pull_request_preview"] = data["enablePullRequestPreview"]
    else:
        raise DeserializationError("Branch.enable_pull_request_preview required")
    if data.get("pullRequestEnvironmentName") is not None:
        out["pull_request_environment_name"] = data["pullRequestEnvironmentName"]
    if data.get("destinationBranch") is not None:
        out["destination_branch"] = data["destinationBranch"]
    if data.get("sourceBranch") is not None:
        out["source_branch"] = data["sourceBranch"]
    if data.get("backendEnvironmentArn") is not None:
        out["backend_environment_arn"] = data["backendEnvironmentArn"]
    if data.get("backend") is not None:
        import capo_amplify.types.backend

        out["backend"] = capo_amplify.types.backend.deserialize_json(data["backend"])
    if data.get("computeRoleArn") is not None:
        out["compute_role_arn"] = data["computeRoleArn"]
    return out

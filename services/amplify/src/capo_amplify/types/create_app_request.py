"""Generated from Smithy shape ``com.amazonaws.amplify#CreateAppRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.access_token
    import capo_amplify.types.auto_branch_creation_config
    import capo_amplify.types.auto_branch_creation_patterns
    import capo_amplify.types.basic_auth_credentials
    import capo_amplify.types.build_spec
    import capo_amplify.types.cache_config
    import capo_amplify.types.compute_role_arn
    import capo_amplify.types.custom_headers
    import capo_amplify.types.custom_rules
    import capo_amplify.types.description
    import capo_amplify.types.enable_auto_branch_creation
    import capo_amplify.types.enable_basic_auth
    import capo_amplify.types.enable_branch_auto_build
    import capo_amplify.types.enable_branch_auto_deletion
    import capo_amplify.types.environment_variables
    import capo_amplify.types.job_config
    import capo_amplify.types.name
    import capo_amplify.types.oauth_token
    import capo_amplify.types.platform
    import capo_amplify.types.repository
    import capo_amplify.types.service_role_arn
    import capo_amplify.types.tag_map


class CreateAppRequest(TypedDict, closed=True):
    name: "capo_amplify.types.name.Name"
    """<p>The name of the Amplify app. </p>"""
    description: NotRequired["capo_amplify.types.description.Description"]
    """<p>The description of the Amplify app. </p>"""
    repository: NotRequired["capo_amplify.types.repository.Repository"]
    """<p>The Git repository for the Amplify app. </p>"""
    platform: NotRequired["capo_amplify.types.platform.Platform"]
    """<p>The platform for the Amplify app. For a static app, set the platform type to <code>WEB</code>. For a dynamic server-side rendered (SSR) app, set the platform type to <code>WEB_COMPUTE</code>. For an app requiring Amplify Hosting's original SSR support only, set the platform type to <code>WEB_DYNAMIC</code>.</p> <p>If you are deploying an SSG only app with Next.js version 14 or later, you must set the platform type to <code>WEB_COMPUTE</code> and set the artifacts <code>baseDirectory</code> to <code>.next</code> in the application's build settings. For an example of the build specification settings, see <a href="https://docs.aws.amazon.com/amplify/latest/userguide/deploy-nextjs-app.html#build-setting-detection-ssg-14">Amplify build settings for a Next.js 14 SSG application</a> in the <i>Amplify Hosting User Guide</i>.</p>"""
    compute_role_arn: NotRequired["capo_amplify.types.compute_role_arn.ComputeRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role to assign to an SSR app. The SSR Compute role allows the Amplify Hosting compute service to securely access specific Amazon Web Services resources based on the role's permissions. For more information about the SSR Compute role, see <a href="https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html">Adding an SSR Compute role</a> in the <i>Amplify User Guide</i>.</p>"""
    iam_service_role_arn: NotRequired[
        "capo_amplify.types.service_role_arn.ServiceRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM service role for the Amplify app.</p>"""
    oauth_token: NotRequired["capo_amplify.types.oauth_token.OauthToken"]
    """<p>The OAuth token for a third-party source control system for an Amplify app. The OAuth token is used to create a webhook and a read-only deploy key using SSH cloning. The OAuth token is not stored.</p> <p>Use <code>oauthToken</code> for repository providers other than GitHub, such as Bitbucket or CodeCommit. To authorize access to GitHub as your repository provider, use <code>accessToken</code>.</p> <p>You must specify either <code>oauthToken</code> or <code>accessToken</code> when you create a new app.</p> <p>Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see <a href="https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth">Migrating an existing OAuth app to the Amplify GitHub App</a> in the <i>Amplify User Guide</i> .</p>"""
    access_token: NotRequired["capo_amplify.types.access_token.AccessToken"]
    """<p>The personal access token for a GitHub repository for an Amplify app. The personal access token is used to authorize access to a GitHub repository using the Amplify GitHub App. The token is not stored.</p> <p>Use <code>accessToken</code> for GitHub repositories only. To authorize access to a repository provider such as Bitbucket or CodeCommit, use <code>oauthToken</code>.</p> <p>You must specify either <code>accessToken</code> or <code>oauthToken</code> when you create a new app.</p> <p>Existing Amplify apps deployed from a GitHub repository using OAuth continue to work with CI/CD. However, we strongly recommend that you migrate these apps to use the GitHub App. For more information, see <a href="https://docs.aws.amazon.com/amplify/latest/userguide/setting-up-GitHub-access.html#migrating-to-github-app-auth">Migrating an existing OAuth app to the Amplify GitHub App</a> in the <i>Amplify User Guide</i> .</p>"""
    environment_variables: NotRequired[
        "capo_amplify.types.environment_variables.EnvironmentVariables"
    ]
    """<p>The environment variables map for an Amplify app. </p> <p>For a list of the environment variables that are accessible to Amplify by default, see <a href="https://docs.aws.amazon.com/amplify/latest/userguide/amplify-console-environment-variables.html">Amplify Environment variables</a> in the <i>Amplify Hosting User Guide</i>.</p>"""
    enable_branch_auto_build: NotRequired[
        "capo_amplify.types.enable_branch_auto_build.EnableBranchAutoBuild"
    ]
    """<p>Enables the auto building of branches for an Amplify app. </p>"""
    enable_branch_auto_deletion: NotRequired[
        "capo_amplify.types.enable_branch_auto_deletion.EnableBranchAutoDeletion"
    ]
    """<p>Automatically disconnects a branch in the Amplify console when you delete a branch from your Git repository. </p>"""
    enable_basic_auth: NotRequired[
        "capo_amplify.types.enable_basic_auth.EnableBasicAuth"
    ]
    """<p>Enables basic authorization for an Amplify app. This will apply to all branches that are part of this app. </p>"""
    basic_auth_credentials: NotRequired[
        "capo_amplify.types.basic_auth_credentials.BasicAuthCredentials"
    ]
    """<p>The credentials for basic authorization for an Amplify app. You must base64-encode the authorization credentials and provide them in the format <code>user:password</code>.</p>"""
    custom_rules: NotRequired["capo_amplify.types.custom_rules.CustomRules"]
    """<p>The custom rewrite and redirect rules for an Amplify app. </p>"""
    tags: NotRequired["capo_amplify.types.tag_map.TagMap"]
    """<p>The tag for an Amplify app. </p>"""
    build_spec: NotRequired["capo_amplify.types.build_spec.BuildSpec"]
    """<p>The build specification (build spec) for an Amplify app. </p>"""
    custom_headers: NotRequired["capo_amplify.types.custom_headers.CustomHeaders"]
    """<p>The custom HTTP headers for an Amplify app.</p>"""
    enable_auto_branch_creation: NotRequired[
        "capo_amplify.types.enable_auto_branch_creation.EnableAutoBranchCreation"
    ]
    """<p>Enables automated branch creation for an Amplify app. </p>"""
    auto_branch_creation_patterns: NotRequired[
        "capo_amplify.types.auto_branch_creation_patterns.AutoBranchCreationPatterns"
    ]
    """<p>The automated branch creation glob patterns for an Amplify app. </p>"""
    auto_branch_creation_config: NotRequired[
        "capo_amplify.types.auto_branch_creation_config.AutoBranchCreationConfig"
    ]
    """<p>The automated branch creation configuration for an Amplify app. </p>"""
    job_config: NotRequired["capo_amplify.types.job_config.JobConfig"]
    """<p>Describes the configuration details that apply to the jobs for an Amplify app.</p>"""
    cache_config: NotRequired["capo_amplify.types.cache_config.CacheConfig"]
    """<p>The cache configuration for the Amplify app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "repository" in value:
        out["repository"] = value["repository"]
    if "platform" in value:
        import capo_amplify.types.platform

        out["platform"] = capo_amplify.types.platform.serialize_json(value["platform"])
    if "compute_role_arn" in value:
        out["computeRoleArn"] = value["compute_role_arn"]
    if "iam_service_role_arn" in value:
        out["iamServiceRoleArn"] = value["iam_service_role_arn"]
    if "oauth_token" in value:
        out["oauthToken"] = value["oauth_token"]
    if "access_token" in value:
        out["accessToken"] = value["access_token"]
    if "environment_variables" in value:
        import capo_amplify.types.environment_variables

        out["environmentVariables"] = (
            capo_amplify.types.environment_variables.serialize_json(
                value["environment_variables"]
            )
        )
    if "enable_branch_auto_build" in value:
        out["enableBranchAutoBuild"] = value["enable_branch_auto_build"]
    if "enable_branch_auto_deletion" in value:
        out["enableBranchAutoDeletion"] = value["enable_branch_auto_deletion"]
    if "enable_basic_auth" in value:
        out["enableBasicAuth"] = value["enable_basic_auth"]
    if "basic_auth_credentials" in value:
        out["basicAuthCredentials"] = value["basic_auth_credentials"]
    if "custom_rules" in value:
        import capo_amplify.types.custom_rules

        out["customRules"] = capo_amplify.types.custom_rules.serialize_json(
            value["custom_rules"]
        )
    if "tags" in value:
        import capo_amplify.types.tag_map

        out["tags"] = capo_amplify.types.tag_map.serialize_json(value["tags"])
    if "build_spec" in value:
        out["buildSpec"] = value["build_spec"]
    if "custom_headers" in value:
        out["customHeaders"] = value["custom_headers"]
    if "enable_auto_branch_creation" in value:
        out["enableAutoBranchCreation"] = value["enable_auto_branch_creation"]
    if "auto_branch_creation_patterns" in value:
        import capo_amplify.types.auto_branch_creation_patterns

        out["autoBranchCreationPatterns"] = (
            capo_amplify.types.auto_branch_creation_patterns.serialize_json(
                value["auto_branch_creation_patterns"]
            )
        )
    if "auto_branch_creation_config" in value:
        import capo_amplify.types.auto_branch_creation_config

        out["autoBranchCreationConfig"] = (
            capo_amplify.types.auto_branch_creation_config.serialize_json(
                value["auto_branch_creation_config"]
            )
        )
    if "job_config" in value:
        import capo_amplify.types.job_config

        out["jobConfig"] = capo_amplify.types.job_config.serialize_json(
            value["job_config"]
        )
    if "cache_config" in value:
        import capo_amplify.types.cache_config

        out["cacheConfig"] = capo_amplify.types.cache_config.serialize_json(
            value["cache_config"]
        )
    return out


def deserialize_json(data: dict) -> CreateAppRequest:
    out: CreateAppRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAppRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("repository") is not None:
        out["repository"] = data["repository"]
    if data.get("platform") is not None:
        import capo_amplify.types.platform

        out["platform"] = capo_amplify.types.platform.deserialize_json(data["platform"])
    if data.get("computeRoleArn") is not None:
        out["compute_role_arn"] = data["computeRoleArn"]
    if data.get("iamServiceRoleArn") is not None:
        out["iam_service_role_arn"] = data["iamServiceRoleArn"]
    if data.get("oauthToken") is not None:
        out["oauth_token"] = data["oauthToken"]
    if data.get("accessToken") is not None:
        out["access_token"] = data["accessToken"]
    if data.get("environmentVariables") is not None:
        import capo_amplify.types.environment_variables

        out["environment_variables"] = (
            capo_amplify.types.environment_variables.deserialize_json(
                data["environmentVariables"]
            )
        )
    if data.get("enableBranchAutoBuild") is not None:
        out["enable_branch_auto_build"] = data["enableBranchAutoBuild"]
    if data.get("enableBranchAutoDeletion") is not None:
        out["enable_branch_auto_deletion"] = data["enableBranchAutoDeletion"]
    if data.get("enableBasicAuth") is not None:
        out["enable_basic_auth"] = data["enableBasicAuth"]
    if data.get("basicAuthCredentials") is not None:
        out["basic_auth_credentials"] = data["basicAuthCredentials"]
    if data.get("customRules") is not None:
        import capo_amplify.types.custom_rules

        out["custom_rules"] = capo_amplify.types.custom_rules.deserialize_json(
            data["customRules"]
        )
    if data.get("tags") is not None:
        import capo_amplify.types.tag_map

        out["tags"] = capo_amplify.types.tag_map.deserialize_json(data["tags"])
    if data.get("buildSpec") is not None:
        out["build_spec"] = data["buildSpec"]
    if data.get("customHeaders") is not None:
        out["custom_headers"] = data["customHeaders"]
    if data.get("enableAutoBranchCreation") is not None:
        out["enable_auto_branch_creation"] = data["enableAutoBranchCreation"]
    if data.get("autoBranchCreationPatterns") is not None:
        import capo_amplify.types.auto_branch_creation_patterns

        out["auto_branch_creation_patterns"] = (
            capo_amplify.types.auto_branch_creation_patterns.deserialize_json(
                data["autoBranchCreationPatterns"]
            )
        )
    if data.get("autoBranchCreationConfig") is not None:
        import capo_amplify.types.auto_branch_creation_config

        out["auto_branch_creation_config"] = (
            capo_amplify.types.auto_branch_creation_config.deserialize_json(
                data["autoBranchCreationConfig"]
            )
        )
    if data.get("jobConfig") is not None:
        import capo_amplify.types.job_config

        out["job_config"] = capo_amplify.types.job_config.deserialize_json(
            data["jobConfig"]
        )
    if data.get("cacheConfig") is not None:
        import capo_amplify.types.cache_config

        out["cache_config"] = capo_amplify.types.cache_config.deserialize_json(
            data["cacheConfig"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.amplify#App``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_amplify.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amplify.types.app_arn
    import capo_amplify.types.app_id
    import capo_amplify.types.auto_branch_creation_config
    import capo_amplify.types.auto_branch_creation_patterns
    import capo_amplify.types.basic_auth_credentials
    import capo_amplify.types.build_spec
    import capo_amplify.types.cache_config
    import capo_amplify.types.compute_role_arn
    import capo_amplify.types.create_time
    import capo_amplify.types.custom_headers
    import capo_amplify.types.custom_rules
    import capo_amplify.types.default_domain
    import capo_amplify.types.description
    import capo_amplify.types.enable_auto_branch_creation
    import capo_amplify.types.enable_basic_auth
    import capo_amplify.types.enable_branch_auto_build
    import capo_amplify.types.enable_branch_auto_deletion
    import capo_amplify.types.environment_variables
    import capo_amplify.types.job_config
    import capo_amplify.types.name
    import capo_amplify.types.platform
    import capo_amplify.types.production_branch
    import capo_amplify.types.repository
    import capo_amplify.types.repository_clone_method
    import capo_amplify.types.service_role_arn
    import capo_amplify.types.tag_map
    import capo_amplify.types.update_time
    import capo_amplify.types.waf_configuration
    import capo_amplify.types.webhook_create_time


class App(TypedDict, closed=True):
    app_id: "capo_amplify.types.app_id.AppId"
    """<p>The unique ID of the Amplify app. </p>"""
    app_arn: "capo_amplify.types.app_arn.AppArn"
    """<p>The Amazon Resource Name (ARN) of the Amplify app. </p>"""
    name: "capo_amplify.types.name.Name"
    """<p>The name for the Amplify app. </p>"""
    tags: NotRequired["capo_amplify.types.tag_map.TagMap"]
    """<p>The tag for the Amplify app. </p>"""
    description: "capo_amplify.types.description.Description"
    """<p>The description for the Amplify app. </p>"""
    repository: "capo_amplify.types.repository.Repository"
    """<p>The Git repository for the Amplify app. </p>"""
    platform: "capo_amplify.types.platform.Platform"
    """<p>The platform for the Amplify app. For a static app, set the platform type to <code>WEB</code>. For a dynamic server-side rendered (SSR) app, set the platform type to <code>WEB_COMPUTE</code>. For an app requiring Amplify Hosting's original SSR support only, set the platform type to <code>WEB_DYNAMIC</code>.</p> <p>If you are deploying an SSG only app with Next.js 14 or later, you must use the platform type <code>WEB_COMPUTE</code>.</p>"""
    create_time: "capo_amplify.types.create_time.CreateTime"
    """<p>A timestamp of when Amplify created the application.</p>"""
    update_time: "capo_amplify.types.update_time.UpdateTime"
    """<p>A timestamp of when Amplify updated the application.</p>"""
    compute_role_arn: NotRequired["capo_amplify.types.compute_role_arn.ComputeRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role for an SSR app. The Compute role allows the Amplify Hosting compute service to securely access specific Amazon Web Services resources based on the role's permissions. For more information about the SSR Compute role, see <a href="https://docs.aws.amazon.com/amplify/latest/userguide/amplify-SSR-compute-role.html">Adding an SSR Compute role</a> in the <i>Amplify User Guide</i>.</p>"""
    iam_service_role_arn: NotRequired[
        "capo_amplify.types.service_role_arn.ServiceRoleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM service role for the Amplify app.</p>"""
    environment_variables: (
        "capo_amplify.types.environment_variables.EnvironmentVariables"
    )
    """<p>The environment variables for the Amplify app. </p> <p>For a list of the environment variables that are accessible to Amplify by default, see <a href="https://docs.aws.amazon.com/amplify/latest/userguide/amplify-console-environment-variables.html">Amplify Environment variables</a> in the <i>Amplify Hosting User Guide</i>.</p>"""
    default_domain: "capo_amplify.types.default_domain.DefaultDomain"
    """<p>The default domain for the Amplify app. </p>"""
    enable_branch_auto_build: (
        "capo_amplify.types.enable_branch_auto_build.EnableBranchAutoBuild"
    )
    """<p>Enables the auto-building of branches for the Amplify app. </p>"""
    enable_branch_auto_deletion: NotRequired[
        "capo_amplify.types.enable_branch_auto_deletion.EnableBranchAutoDeletion"
    ]
    """<p>Automatically disconnect a branch in the Amplify console when you delete a branch from your Git repository.</p>"""
    enable_basic_auth: "capo_amplify.types.enable_basic_auth.EnableBasicAuth"
    """<p>Enables basic authorization for the Amplify app's branches. </p>"""
    basic_auth_credentials: NotRequired[
        "capo_amplify.types.basic_auth_credentials.BasicAuthCredentials"
    ]
    """<p>The basic authorization credentials for branches for the Amplify app. You must base64-encode the authorization credentials and provide them in the format <code>user:password</code>.</p>"""
    custom_rules: NotRequired["capo_amplify.types.custom_rules.CustomRules"]
    """<p>Describes the custom redirect and rewrite rules for the Amplify app. </p>"""
    production_branch: NotRequired[
        "capo_amplify.types.production_branch.ProductionBranch"
    ]
    """<p>Describes the information about a production branch of the Amplify app. </p>"""
    build_spec: NotRequired["capo_amplify.types.build_spec.BuildSpec"]
    """<p>Describes the content of the build specification (build spec) for the Amplify app. </p>"""
    custom_headers: NotRequired["capo_amplify.types.custom_headers.CustomHeaders"]
    """<p>Describes the custom HTTP headers for the Amplify app.</p>"""
    enable_auto_branch_creation: NotRequired[
        "capo_amplify.types.enable_auto_branch_creation.EnableAutoBranchCreation"
    ]
    """<p>Enables automated branch creation for the Amplify app. </p>"""
    auto_branch_creation_patterns: NotRequired[
        "capo_amplify.types.auto_branch_creation_patterns.AutoBranchCreationPatterns"
    ]
    """<p>Describes the automated branch creation glob patterns for the Amplify app. </p>"""
    auto_branch_creation_config: NotRequired[
        "capo_amplify.types.auto_branch_creation_config.AutoBranchCreationConfig"
    ]
    """<p>Describes the automated branch creation configuration for the Amplify app. </p>"""
    repository_clone_method: NotRequired[
        "capo_amplify.types.repository_clone_method.RepositoryCloneMethod"
    ]
    """<note> <p>This is for internal use.</p> </note> <p>The Amplify service uses this parameter to specify the authentication protocol to use to access the Git repository for an Amplify app. Amplify specifies <code>TOKEN</code> for a GitHub repository, <code>SIGV4</code> for an Amazon Web Services CodeCommit repository, and <code>SSH</code> for GitLab and Bitbucket repositories.</p>"""
    cache_config: NotRequired["capo_amplify.types.cache_config.CacheConfig"]
    """<p>The cache configuration for the Amplify app. If you don't specify the cache configuration <code>type</code>, Amplify uses the default <code>AMPLIFY_MANAGED</code> setting.</p>"""
    webhook_create_time: NotRequired[
        "capo_amplify.types.webhook_create_time.webhookCreateTime"
    ]
    """<p>A timestamp of when Amplify created the webhook in your Git repository.</p>"""
    waf_configuration: NotRequired[
        "capo_amplify.types.waf_configuration.WafConfiguration"
    ]
    """<p>Describes the Firewall configuration for the Amplify app. Firewall support enables you to protect your hosted applications with a direct integration with WAF.</p>"""
    job_config: NotRequired["capo_amplify.types.job_config.JobConfig"]
    """<p>The configuration details that apply to the jobs for an Amplify app.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: App) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["appArn"] = value["app_arn"]
    out["name"] = value["name"]
    if "tags" in value:
        import capo_amplify.types.tag_map

        out["tags"] = capo_amplify.types.tag_map.serialize_json(value["tags"])
    out["description"] = value["description"]
    out["repository"] = value["repository"]
    import capo_amplify.types.platform

    out["platform"] = capo_amplify.types.platform.serialize_json(value["platform"])
    import capo_amplify.types.create_time

    out["createTime"] = capo_amplify.types.create_time.serialize_json(
        value["create_time"]
    )
    import capo_amplify.types.update_time

    out["updateTime"] = capo_amplify.types.update_time.serialize_json(
        value["update_time"]
    )
    if "compute_role_arn" in value:
        out["computeRoleArn"] = value["compute_role_arn"]
    if "iam_service_role_arn" in value:
        out["iamServiceRoleArn"] = value["iam_service_role_arn"]
    import capo_amplify.types.environment_variables

    out["environmentVariables"] = (
        capo_amplify.types.environment_variables.serialize_json(
            value["environment_variables"]
        )
    )
    out["defaultDomain"] = value["default_domain"]
    out["enableBranchAutoBuild"] = value["enable_branch_auto_build"]
    if "enable_branch_auto_deletion" in value:
        out["enableBranchAutoDeletion"] = value["enable_branch_auto_deletion"]
    out["enableBasicAuth"] = value["enable_basic_auth"]
    if "basic_auth_credentials" in value:
        out["basicAuthCredentials"] = value["basic_auth_credentials"]
    if "custom_rules" in value:
        import capo_amplify.types.custom_rules

        out["customRules"] = capo_amplify.types.custom_rules.serialize_json(
            value["custom_rules"]
        )
    if "production_branch" in value:
        import capo_amplify.types.production_branch

        out["productionBranch"] = capo_amplify.types.production_branch.serialize_json(
            value["production_branch"]
        )
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
    if "repository_clone_method" in value:
        import capo_amplify.types.repository_clone_method

        out["repositoryCloneMethod"] = (
            capo_amplify.types.repository_clone_method.serialize_json(
                value["repository_clone_method"]
            )
        )
    if "cache_config" in value:
        import capo_amplify.types.cache_config

        out["cacheConfig"] = capo_amplify.types.cache_config.serialize_json(
            value["cache_config"]
        )
    if "webhook_create_time" in value:
        import capo_amplify.types.webhook_create_time

        out["webhookCreateTime"] = (
            capo_amplify.types.webhook_create_time.serialize_json(
                value["webhook_create_time"]
            )
        )
    if "waf_configuration" in value:
        import capo_amplify.types.waf_configuration

        out["wafConfiguration"] = capo_amplify.types.waf_configuration.serialize_json(
            value["waf_configuration"]
        )
    if "job_config" in value:
        import capo_amplify.types.job_config

        out["jobConfig"] = capo_amplify.types.job_config.serialize_json(
            value["job_config"]
        )
    return out


def deserialize_json(data: dict) -> App:
    out: App = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        raise DeserializationError("App.app_id required")
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("App.app_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("App.name required")
    if data.get("tags") is not None:
        import capo_amplify.types.tag_map

        out["tags"] = capo_amplify.types.tag_map.deserialize_json(data["tags"])
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        raise DeserializationError("App.description required")
    if data.get("repository") is not None:
        out["repository"] = data["repository"]
    else:
        raise DeserializationError("App.repository required")
    if data.get("platform") is not None:
        import capo_amplify.types.platform

        out["platform"] = capo_amplify.types.platform.deserialize_json(data["platform"])
    else:
        raise DeserializationError("App.platform required")
    if data.get("createTime") is not None:
        import capo_amplify.types.create_time

        out["create_time"] = capo_amplify.types.create_time.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError("App.create_time required")
    if data.get("updateTime") is not None:
        import capo_amplify.types.update_time

        out["update_time"] = capo_amplify.types.update_time.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("App.update_time required")
    if data.get("computeRoleArn") is not None:
        out["compute_role_arn"] = data["computeRoleArn"]
    if data.get("iamServiceRoleArn") is not None:
        out["iam_service_role_arn"] = data["iamServiceRoleArn"]
    if data.get("environmentVariables") is not None:
        import capo_amplify.types.environment_variables

        out["environment_variables"] = (
            capo_amplify.types.environment_variables.deserialize_json(
                data["environmentVariables"]
            )
        )
    else:
        raise DeserializationError("App.environment_variables required")
    if data.get("defaultDomain") is not None:
        out["default_domain"] = data["defaultDomain"]
    else:
        raise DeserializationError("App.default_domain required")
    if data.get("enableBranchAutoBuild") is not None:
        out["enable_branch_auto_build"] = data["enableBranchAutoBuild"]
    else:
        raise DeserializationError("App.enable_branch_auto_build required")
    if data.get("enableBranchAutoDeletion") is not None:
        out["enable_branch_auto_deletion"] = data["enableBranchAutoDeletion"]
    if data.get("enableBasicAuth") is not None:
        out["enable_basic_auth"] = data["enableBasicAuth"]
    else:
        raise DeserializationError("App.enable_basic_auth required")
    if data.get("basicAuthCredentials") is not None:
        out["basic_auth_credentials"] = data["basicAuthCredentials"]
    if data.get("customRules") is not None:
        import capo_amplify.types.custom_rules

        out["custom_rules"] = capo_amplify.types.custom_rules.deserialize_json(
            data["customRules"]
        )
    if data.get("productionBranch") is not None:
        import capo_amplify.types.production_branch

        out["production_branch"] = (
            capo_amplify.types.production_branch.deserialize_json(
                data["productionBranch"]
            )
        )
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
    if data.get("repositoryCloneMethod") is not None:
        import capo_amplify.types.repository_clone_method

        out["repository_clone_method"] = (
            capo_amplify.types.repository_clone_method.deserialize_json(
                data["repositoryCloneMethod"]
            )
        )
    if data.get("cacheConfig") is not None:
        import capo_amplify.types.cache_config

        out["cache_config"] = capo_amplify.types.cache_config.deserialize_json(
            data["cacheConfig"]
        )
    if data.get("webhookCreateTime") is not None:
        import capo_amplify.types.webhook_create_time

        out["webhook_create_time"] = (
            capo_amplify.types.webhook_create_time.deserialize_json(
                data["webhookCreateTime"]
            )
        )
    if data.get("wafConfiguration") is not None:
        import capo_amplify.types.waf_configuration

        out["waf_configuration"] = (
            capo_amplify.types.waf_configuration.deserialize_json(
                data["wafConfiguration"]
            )
        )
    if data.get("jobConfig") is not None:
        import capo_amplify.types.job_config

        out["job_config"] = capo_amplify.types.job_config.deserialize_json(
            data["jobConfig"]
        )
    return out

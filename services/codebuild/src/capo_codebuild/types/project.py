"""Generated from Smithy shape ``com.amazonaws.codebuild#Project``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.build_time_out
    import capo_codebuild.types.logs_config
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.project_artifacts
    import capo_codebuild.types.project_artifacts_list
    import capo_codebuild.types.project_badge
    import capo_codebuild.types.project_build_batch_config
    import capo_codebuild.types.project_cache
    import capo_codebuild.types.project_description
    import capo_codebuild.types.project_environment
    import capo_codebuild.types.project_file_system_locations
    import capo_codebuild.types.project_name
    import capo_codebuild.types.project_secondary_source_versions
    import capo_codebuild.types.project_source
    import capo_codebuild.types.project_sources
    import capo_codebuild.types.project_visibility_type
    import capo_codebuild.types.string
    import capo_codebuild.types.tag_list
    import capo_codebuild.types.time_out
    import capo_codebuild.types.timestamp
    import capo_codebuild.types.vpc_config
    import capo_codebuild.types.webhook
    import capo_codebuild.types.wrapper_int


class Project(TypedDict, closed=True):
    name: NotRequired["capo_codebuild.types.project_name.ProjectName"]
    """<p>The name of the build project.</p>"""
    arn: NotRequired["capo_codebuild.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the build project.</p>"""
    description: NotRequired[
        "capo_codebuild.types.project_description.ProjectDescription"
    ]
    """<p>A description that makes the build project easy to identify.</p>"""
    source: NotRequired["capo_codebuild.types.project_source.ProjectSource"]
    """<p>Information about the build input source code for this build project.</p>"""
    secondary_sources: NotRequired[
        "capo_codebuild.types.project_sources.ProjectSources"
    ]
    """<p>An array of <code>ProjectSource</code> objects. </p>"""
    source_version: NotRequired["capo_codebuild.types.string.String"]
    """<p>A version of the build input to be built for this project. If not specified, the latest version is used. If specified, it must be one of:</p> <ul> <li> <p>For CodeCommit: the commit ID, branch, or Git tag to use.</p> </li> <li> <p>For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format <code>pr/pull-request-ID</code> (for example <code>pr/25</code>). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For GitLab: the commit ID, branch, or Git tag to use.</p> </li> <li> <p>For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For Amazon S3: the version ID of the object that represents the build input ZIP file to use.</p> </li> </ul> <p>If <code>sourceVersion</code> is specified at the build level, then that version takes precedence over this <code>sourceVersion</code> (at the project level). </p> <p>For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html">Source Version Sample with CodeBuild</a> in the <i>CodeBuild User Guide</i>. </p>"""
    secondary_source_versions: NotRequired[
        "capo_codebuild.types.project_secondary_source_versions.ProjectSecondarySourceVersions"
    ]
    """<p>An array of <code>ProjectSourceVersion</code> objects. If <code>secondarySourceVersions</code> is specified at the build level, then they take over these <code>secondarySourceVersions</code> (at the project level). </p>"""
    artifacts: NotRequired["capo_codebuild.types.project_artifacts.ProjectArtifacts"]
    """<p>Information about the build output artifacts for the build project.</p>"""
    secondary_artifacts: NotRequired[
        "capo_codebuild.types.project_artifacts_list.ProjectArtifactsList"
    ]
    """<p>An array of <code>ProjectArtifacts</code> objects. </p>"""
    cache: NotRequired["capo_codebuild.types.project_cache.ProjectCache"]
    """<p>Information about the cache for the build project.</p>"""
    environment: NotRequired[
        "capo_codebuild.types.project_environment.ProjectEnvironment"
    ]
    """<p>Information about the build environment for this build project.</p>"""
    service_role: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the IAM role that enables CodeBuild to interact with dependent Amazon Web Services services on behalf of the Amazon Web Services account.</p>"""
    timeout_in_minutes: NotRequired["capo_codebuild.types.build_time_out.BuildTimeOut"]
    """<p>How long, in minutes, from 5 to 2160 (36 hours), for CodeBuild to wait before timing out any related build that did not get marked as completed. The default is 60 minutes.</p>"""
    queued_timeout_in_minutes: NotRequired["capo_codebuild.types.time_out.TimeOut"]
    """<p>The number of minutes a build is allowed to be queued before it times out. </p>"""
    encryption_key: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The Key Management Service customer master key (CMK) to be used for encrypting the build output artifacts.</p> <note> <p>You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key. </p> </note> <p>You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format <code>alias/<alias-name></code>). If you don't specify a value, CodeBuild uses the managed CMK for Amazon Simple Storage Service (Amazon S3). </p>"""
    tags: NotRequired["capo_codebuild.types.tag_list.TagList"]
    """<p>A list of tag key and value pairs associated with this build project.</p> <p>These tags are available for use by Amazon Web Services services that support CodeBuild build project tags.</p>"""
    created: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>When the build project was created, expressed in Unix time format.</p>"""
    last_modified: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>When the build project's settings were last modified, expressed in Unix time format.</p>"""
    webhook: NotRequired["capo_codebuild.types.webhook.Webhook"]
    """<p>Information about a webhook that connects repository events to a build project in CodeBuild.</p>"""
    vpc_config: NotRequired["capo_codebuild.types.vpc_config.VpcConfig"]
    """<p>Information about the VPC configuration that CodeBuild accesses.</p>"""
    badge: NotRequired["capo_codebuild.types.project_badge.ProjectBadge"]
    """<p>Information about the build badge for the build project.</p>"""
    logs_config: NotRequired["capo_codebuild.types.logs_config.LogsConfig"]
    """<p>Information about logs for the build project. A project can create logs in CloudWatch Logs, an S3 bucket, or both. </p>"""
    file_system_locations: NotRequired[
        "capo_codebuild.types.project_file_system_locations.ProjectFileSystemLocations"
    ]
    """<p> An array of <code>ProjectFileSystemLocation</code> objects for a CodeBuild build project. A <code>ProjectFileSystemLocation</code> object specifies the <code>identifier</code>, <code>location</code>, <code>mountOptions</code>, <code>mountPoint</code>, and <code>type</code> of a file system created using Amazon Elastic File System. </p>"""
    build_batch_config: NotRequired[
        "capo_codebuild.types.project_build_batch_config.ProjectBuildBatchConfig"
    ]
    """<p>A <a>ProjectBuildBatchConfig</a> object that defines the batch build options for the project.</p>"""
    concurrent_build_limit: NotRequired["capo_codebuild.types.wrapper_int.WrapperInt"]
    """<p>The maximum number of concurrent builds that are allowed for this project.</p> <p>New builds are only started if the current number of builds is less than or equal to this limit. If the current build count meets this limit, new builds are throttled and are not run.</p>"""
    project_visibility: NotRequired[
        "capo_codebuild.types.project_visibility_type.ProjectVisibilityType"
    ]
    public_project_alias: NotRequired[
        "capo_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>Contains the project identifier used with the public build APIs. </p>"""
    resource_access_role: NotRequired[
        "capo_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the IAM role that enables CodeBuild to access the CloudWatch Logs and Amazon S3 artifacts for the project's builds.</p>"""
    auto_retry_limit: NotRequired["capo_codebuild.types.wrapper_int.WrapperInt"]
    """<p>The maximum number of additional automatic retries after a failed build. For example, if the auto-retry limit is set to 2, CodeBuild will call the <code>RetryBuild</code> API to automatically retry your build for up to 2 additional times.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Project) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "source" in value:
        import capo_codebuild.types.project_source

        out["source"] = capo_codebuild.types.project_source.serialize_aws_json_1_1(
            value["source"]
        )
    if "secondary_sources" in value:
        import capo_codebuild.types.project_sources

        out["secondarySources"] = (
            capo_codebuild.types.project_sources.serialize_aws_json_1_1(
                value["secondary_sources"]
            )
        )
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
    if "secondary_source_versions" in value:
        import capo_codebuild.types.project_secondary_source_versions

        out["secondarySourceVersions"] = (
            capo_codebuild.types.project_secondary_source_versions.serialize_aws_json_1_1(
                value["secondary_source_versions"]
            )
        )
    if "artifacts" in value:
        import capo_codebuild.types.project_artifacts

        out["artifacts"] = (
            capo_codebuild.types.project_artifacts.serialize_aws_json_1_1(
                value["artifacts"]
            )
        )
    if "secondary_artifacts" in value:
        import capo_codebuild.types.project_artifacts_list

        out["secondaryArtifacts"] = (
            capo_codebuild.types.project_artifacts_list.serialize_aws_json_1_1(
                value["secondary_artifacts"]
            )
        )
    if "cache" in value:
        import capo_codebuild.types.project_cache

        out["cache"] = capo_codebuild.types.project_cache.serialize_aws_json_1_1(
            value["cache"]
        )
    if "environment" in value:
        import capo_codebuild.types.project_environment

        out["environment"] = (
            capo_codebuild.types.project_environment.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "timeout_in_minutes" in value:
        out["timeoutInMinutes"] = value["timeout_in_minutes"]
    if "queued_timeout_in_minutes" in value:
        out["queuedTimeoutInMinutes"] = value["queued_timeout_in_minutes"]
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    if "tags" in value:
        import capo_codebuild.types.tag_list

        out["tags"] = capo_codebuild.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "created" in value:
        import capo_codebuild.types.timestamp

        out["created"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["created"]
        )
    if "last_modified" in value:
        import capo_codebuild.types.timestamp

        out["lastModified"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["last_modified"]
        )
    if "webhook" in value:
        import capo_codebuild.types.webhook

        out["webhook"] = capo_codebuild.types.webhook.serialize_aws_json_1_1(
            value["webhook"]
        )
    if "vpc_config" in value:
        import capo_codebuild.types.vpc_config

        out["vpcConfig"] = capo_codebuild.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "badge" in value:
        import capo_codebuild.types.project_badge

        out["badge"] = capo_codebuild.types.project_badge.serialize_aws_json_1_1(
            value["badge"]
        )
    if "logs_config" in value:
        import capo_codebuild.types.logs_config

        out["logsConfig"] = capo_codebuild.types.logs_config.serialize_aws_json_1_1(
            value["logs_config"]
        )
    if "file_system_locations" in value:
        import capo_codebuild.types.project_file_system_locations

        out["fileSystemLocations"] = (
            capo_codebuild.types.project_file_system_locations.serialize_aws_json_1_1(
                value["file_system_locations"]
            )
        )
    if "build_batch_config" in value:
        import capo_codebuild.types.project_build_batch_config

        out["buildBatchConfig"] = (
            capo_codebuild.types.project_build_batch_config.serialize_aws_json_1_1(
                value["build_batch_config"]
            )
        )
    if "concurrent_build_limit" in value:
        out["concurrentBuildLimit"] = value["concurrent_build_limit"]
    if "project_visibility" in value:
        import capo_codebuild.types.project_visibility_type

        out["projectVisibility"] = (
            capo_codebuild.types.project_visibility_type.serialize_aws_json_1_1(
                value["project_visibility"]
            )
        )
    if "public_project_alias" in value:
        out["publicProjectAlias"] = value["public_project_alias"]
    if "resource_access_role" in value:
        out["resourceAccessRole"] = value["resource_access_role"]
    if "auto_retry_limit" in value:
        out["autoRetryLimit"] = value["auto_retry_limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Project:
    out: Project = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("source") is not None:
        import capo_codebuild.types.project_source

        out["source"] = capo_codebuild.types.project_source.deserialize_aws_json_1_1(
            data["source"]
        )
    if data.get("secondarySources") is not None:
        import capo_codebuild.types.project_sources

        out["secondary_sources"] = (
            capo_codebuild.types.project_sources.deserialize_aws_json_1_1(
                data["secondarySources"]
            )
        )
    if data.get("sourceVersion") is not None:
        out["source_version"] = data["sourceVersion"]
    if data.get("secondarySourceVersions") is not None:
        import capo_codebuild.types.project_secondary_source_versions

        out["secondary_source_versions"] = (
            capo_codebuild.types.project_secondary_source_versions.deserialize_aws_json_1_1(
                data["secondarySourceVersions"]
            )
        )
    if data.get("artifacts") is not None:
        import capo_codebuild.types.project_artifacts

        out["artifacts"] = (
            capo_codebuild.types.project_artifacts.deserialize_aws_json_1_1(
                data["artifacts"]
            )
        )
    if data.get("secondaryArtifacts") is not None:
        import capo_codebuild.types.project_artifacts_list

        out["secondary_artifacts"] = (
            capo_codebuild.types.project_artifacts_list.deserialize_aws_json_1_1(
                data["secondaryArtifacts"]
            )
        )
    if data.get("cache") is not None:
        import capo_codebuild.types.project_cache

        out["cache"] = capo_codebuild.types.project_cache.deserialize_aws_json_1_1(
            data["cache"]
        )
    if data.get("environment") is not None:
        import capo_codebuild.types.project_environment

        out["environment"] = (
            capo_codebuild.types.project_environment.deserialize_aws_json_1_1(
                data["environment"]
            )
        )
    if data.get("serviceRole") is not None:
        out["service_role"] = data["serviceRole"]
    if data.get("timeoutInMinutes") is not None:
        out["timeout_in_minutes"] = data["timeoutInMinutes"]
    if data.get("queuedTimeoutInMinutes") is not None:
        out["queued_timeout_in_minutes"] = data["queuedTimeoutInMinutes"]
    if data.get("encryptionKey") is not None:
        out["encryption_key"] = data["encryptionKey"]
    if data.get("tags") is not None:
        import capo_codebuild.types.tag_list

        out["tags"] = capo_codebuild.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    if data.get("created") is not None:
        import capo_codebuild.types.timestamp

        out["created"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["created"]
        )
    if data.get("lastModified") is not None:
        import capo_codebuild.types.timestamp

        out["last_modified"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["lastModified"]
        )
    if data.get("webhook") is not None:
        import capo_codebuild.types.webhook

        out["webhook"] = capo_codebuild.types.webhook.deserialize_aws_json_1_1(
            data["webhook"]
        )
    if data.get("vpcConfig") is not None:
        import capo_codebuild.types.vpc_config

        out["vpc_config"] = capo_codebuild.types.vpc_config.deserialize_aws_json_1_1(
            data["vpcConfig"]
        )
    if data.get("badge") is not None:
        import capo_codebuild.types.project_badge

        out["badge"] = capo_codebuild.types.project_badge.deserialize_aws_json_1_1(
            data["badge"]
        )
    if data.get("logsConfig") is not None:
        import capo_codebuild.types.logs_config

        out["logs_config"] = capo_codebuild.types.logs_config.deserialize_aws_json_1_1(
            data["logsConfig"]
        )
    if data.get("fileSystemLocations") is not None:
        import capo_codebuild.types.project_file_system_locations

        out["file_system_locations"] = (
            capo_codebuild.types.project_file_system_locations.deserialize_aws_json_1_1(
                data["fileSystemLocations"]
            )
        )
    if data.get("buildBatchConfig") is not None:
        import capo_codebuild.types.project_build_batch_config

        out["build_batch_config"] = (
            capo_codebuild.types.project_build_batch_config.deserialize_aws_json_1_1(
                data["buildBatchConfig"]
            )
        )
    if data.get("concurrentBuildLimit") is not None:
        out["concurrent_build_limit"] = data["concurrentBuildLimit"]
    if data.get("projectVisibility") is not None:
        import capo_codebuild.types.project_visibility_type

        out["project_visibility"] = (
            capo_codebuild.types.project_visibility_type.deserialize_aws_json_1_1(
                data["projectVisibility"]
            )
        )
    if data.get("publicProjectAlias") is not None:
        out["public_project_alias"] = data["publicProjectAlias"]
    if data.get("resourceAccessRole") is not None:
        out["resource_access_role"] = data["resourceAccessRole"]
    if data.get("autoRetryLimit") is not None:
        out["auto_retry_limit"] = data["autoRetryLimit"]
    return out

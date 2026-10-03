"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildBatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.boolean
    import capo_codebuild.types.build_artifacts
    import capo_codebuild.types.build_artifacts_list
    import capo_codebuild.types.build_batch_phases
    import capo_codebuild.types.build_groups
    import capo_codebuild.types.build_report_arns
    import capo_codebuild.types.logs_config
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.project_build_batch_config
    import capo_codebuild.types.project_cache
    import capo_codebuild.types.project_environment
    import capo_codebuild.types.project_file_system_locations
    import capo_codebuild.types.project_secondary_source_versions
    import capo_codebuild.types.project_source
    import capo_codebuild.types.project_sources
    import capo_codebuild.types.status_type
    import capo_codebuild.types.string
    import capo_codebuild.types.timestamp
    import capo_codebuild.types.vpc_config
    import capo_codebuild.types.wrapper_boolean
    import capo_codebuild.types.wrapper_int
    import capo_codebuild.types.wrapper_long


class BuildBatch(TypedDict, closed=True):
    id: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the batch build.</p>"""
    arn: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the batch build.</p>"""
    start_time: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>The date and time that the batch build started.</p>"""
    end_time: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>The date and time that the batch build ended.</p>"""
    current_phase: NotRequired["capo_codebuild.types.string.String"]
    """<p>The current phase of the batch build.</p>"""
    build_batch_status: NotRequired["capo_codebuild.types.status_type.StatusType"]
    """<p>The status of the batch build.</p>"""
    source_version: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the version of the source code to be built.</p>"""
    resolved_source_version: NotRequired[
        "capo_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>The identifier of the resolved version of this batch build's source code.</p> <ul> <li> <p>For CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID.</p> </li> <li> <p>For CodePipeline, the source revision provided by CodePipeline.</p> </li> <li> <p>For Amazon S3, this does not apply.</p> </li> </ul>"""
    project_name: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The name of the batch build project.</p>"""
    phases: NotRequired["capo_codebuild.types.build_batch_phases.BuildBatchPhases"]
    """<p>An array of <code>BuildBatchPhase</code> objects the specify the phases of the batch build.</p>"""
    source: NotRequired["capo_codebuild.types.project_source.ProjectSource"]
    secondary_sources: NotRequired[
        "capo_codebuild.types.project_sources.ProjectSources"
    ]
    """<p>An array of <code>ProjectSource</code> objects that define the sources for the batch build.</p>"""
    secondary_source_versions: NotRequired[
        "capo_codebuild.types.project_secondary_source_versions.ProjectSecondarySourceVersions"
    ]
    """<p>An array of <code>ProjectSourceVersion</code> objects. Each <code>ProjectSourceVersion</code> must be one of: </p> <ul> <li> <p>For CodeCommit: the commit ID, branch, or Git tag to use.</p> </li> <li> <p>For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format <code>pr/pull-request-ID</code> (for example, <code>pr/25</code>). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For Amazon S3: the version ID of the object that represents the build input ZIP file to use.</p> </li> </ul>"""
    artifacts: NotRequired["capo_codebuild.types.build_artifacts.BuildArtifacts"]
    """<p>A <code>BuildArtifacts</code> object the defines the build artifacts for this batch build.</p>"""
    secondary_artifacts: NotRequired[
        "capo_codebuild.types.build_artifacts_list.BuildArtifactsList"
    ]
    """<p>An array of <code>BuildArtifacts</code> objects the define the build artifacts for this batch build.</p>"""
    cache: NotRequired["capo_codebuild.types.project_cache.ProjectCache"]
    environment: NotRequired[
        "capo_codebuild.types.project_environment.ProjectEnvironment"
    ]
    service_role: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The name of a service role used for builds in the batch.</p>"""
    log_config: NotRequired["capo_codebuild.types.logs_config.LogsConfig"]
    build_timeout_in_minutes: NotRequired["capo_codebuild.types.wrapper_int.WrapperInt"]
    """<p>Specifies the maximum amount of time, in minutes, that the build in a batch must be completed in.</p>"""
    queued_timeout_in_minutes: NotRequired[
        "capo_codebuild.types.wrapper_int.WrapperInt"
    ]
    """<p>Specifies the amount of time, in minutes, that the batch build is allowed to be queued before it times out.</p>"""
    complete: "capo_codebuild.types.boolean.Boolean"
    """<p>Indicates if the batch build is complete.</p>"""
    initiator: NotRequired["capo_codebuild.types.string.String"]
    """<p>The entity that started the batch build. Valid values include:</p> <ul> <li> <p>If CodePipeline started the build, the pipeline's name (for example, <code>codepipeline/my-demo-pipeline</code>).</p> </li> <li> <p>If a user started the build, the user's name.</p> </li> <li> <p>If the Jenkins plugin for CodeBuild started the build, the string <code>CodeBuild-Jenkins-Plugin</code>.</p> </li> </ul>"""
    vpc_config: NotRequired["capo_codebuild.types.vpc_config.VpcConfig"]
    encryption_key: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The Key Management Service customer master key (CMK) to be used for encrypting the batch build output artifacts.</p> <note> <p>You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key. </p> </note> <p>You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format <code>alias/<alias-name></code>).</p>"""
    build_batch_number: NotRequired["capo_codebuild.types.wrapper_long.WrapperLong"]
    """<p>The number of the batch build. For each project, the <code>buildBatchNumber</code> of its first batch build is <code>1</code>. The <code>buildBatchNumber</code> of each subsequent batch build is incremented by <code>1</code>. If a batch build is deleted, the <code>buildBatchNumber</code> of other batch builds does not change.</p>"""
    file_system_locations: NotRequired[
        "capo_codebuild.types.project_file_system_locations.ProjectFileSystemLocations"
    ]
    """<p>An array of <code>ProjectFileSystemLocation</code> objects for the batch build project. A <code>ProjectFileSystemLocation</code> object specifies the <code>identifier</code>, <code>location</code>, <code>mountOptions</code>, <code>mountPoint</code>, and <code>type</code> of a file system created using Amazon Elastic File System. </p>"""
    build_batch_config: NotRequired[
        "capo_codebuild.types.project_build_batch_config.ProjectBuildBatchConfig"
    ]
    build_groups: NotRequired["capo_codebuild.types.build_groups.BuildGroups"]
    """<p>An array of <code>BuildGroup</code> objects that define the build groups for the batch build.</p>"""
    debug_session_enabled: NotRequired[
        "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p>Specifies if session debugging is enabled for this batch build. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/session-manager.html">Viewing a running build in Session Manager</a>. Batch session debugging is not supported for matrix batch builds.</p>"""
    report_arns: NotRequired["capo_codebuild.types.build_report_arns.BuildReportArns"]
    """<p>An array that contains the ARNs of reports created by merging reports from builds associated with this batch build.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildBatch) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "start_time" in value:
        import capo_codebuild.types.timestamp

        out["startTime"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_codebuild.types.timestamp

        out["endTime"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["end_time"]
        )
    if "current_phase" in value:
        out["currentPhase"] = value["current_phase"]
    if "build_batch_status" in value:
        import capo_codebuild.types.status_type

        out["buildBatchStatus"] = (
            capo_codebuild.types.status_type.serialize_aws_json_1_1(
                value["build_batch_status"]
            )
        )
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
    if "resolved_source_version" in value:
        out["resolvedSourceVersion"] = value["resolved_source_version"]
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    if "phases" in value:
        import capo_codebuild.types.build_batch_phases

        out["phases"] = capo_codebuild.types.build_batch_phases.serialize_aws_json_1_1(
            value["phases"]
        )
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
    if "secondary_source_versions" in value:
        import capo_codebuild.types.project_secondary_source_versions

        out["secondarySourceVersions"] = (
            capo_codebuild.types.project_secondary_source_versions.serialize_aws_json_1_1(
                value["secondary_source_versions"]
            )
        )
    if "artifacts" in value:
        import capo_codebuild.types.build_artifacts

        out["artifacts"] = capo_codebuild.types.build_artifacts.serialize_aws_json_1_1(
            value["artifacts"]
        )
    if "secondary_artifacts" in value:
        import capo_codebuild.types.build_artifacts_list

        out["secondaryArtifacts"] = (
            capo_codebuild.types.build_artifacts_list.serialize_aws_json_1_1(
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
    if "log_config" in value:
        import capo_codebuild.types.logs_config

        out["logConfig"] = capo_codebuild.types.logs_config.serialize_aws_json_1_1(
            value["log_config"]
        )
    if "build_timeout_in_minutes" in value:
        out["buildTimeoutInMinutes"] = value["build_timeout_in_minutes"]
    if "queued_timeout_in_minutes" in value:
        out["queuedTimeoutInMinutes"] = value["queued_timeout_in_minutes"]
    out["complete"] = value.get("complete", False)
    if "initiator" in value:
        out["initiator"] = value["initiator"]
    if "vpc_config" in value:
        import capo_codebuild.types.vpc_config

        out["vpcConfig"] = capo_codebuild.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    if "build_batch_number" in value:
        out["buildBatchNumber"] = value["build_batch_number"]
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
    if "build_groups" in value:
        import capo_codebuild.types.build_groups

        out["buildGroups"] = capo_codebuild.types.build_groups.serialize_aws_json_1_1(
            value["build_groups"]
        )
    if "debug_session_enabled" in value:
        out["debugSessionEnabled"] = value["debug_session_enabled"]
    if "report_arns" in value:
        import capo_codebuild.types.build_report_arns

        out["reportArns"] = (
            capo_codebuild.types.build_report_arns.serialize_aws_json_1_1(
                value["report_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BuildBatch:
    out: BuildBatch = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("startTime") is not None:
        import capo_codebuild.types.timestamp

        out["start_time"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_codebuild.types.timestamp

        out["end_time"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["endTime"]
        )
    if data.get("currentPhase") is not None:
        out["current_phase"] = data["currentPhase"]
    if data.get("buildBatchStatus") is not None:
        import capo_codebuild.types.status_type

        out["build_batch_status"] = (
            capo_codebuild.types.status_type.deserialize_aws_json_1_1(
                data["buildBatchStatus"]
            )
        )
    if data.get("sourceVersion") is not None:
        out["source_version"] = data["sourceVersion"]
    if data.get("resolvedSourceVersion") is not None:
        out["resolved_source_version"] = data["resolvedSourceVersion"]
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    if data.get("phases") is not None:
        import capo_codebuild.types.build_batch_phases

        out["phases"] = (
            capo_codebuild.types.build_batch_phases.deserialize_aws_json_1_1(
                data["phases"]
            )
        )
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
    if data.get("secondarySourceVersions") is not None:
        import capo_codebuild.types.project_secondary_source_versions

        out["secondary_source_versions"] = (
            capo_codebuild.types.project_secondary_source_versions.deserialize_aws_json_1_1(
                data["secondarySourceVersions"]
            )
        )
    if data.get("artifacts") is not None:
        import capo_codebuild.types.build_artifacts

        out["artifacts"] = (
            capo_codebuild.types.build_artifacts.deserialize_aws_json_1_1(
                data["artifacts"]
            )
        )
    if data.get("secondaryArtifacts") is not None:
        import capo_codebuild.types.build_artifacts_list

        out["secondary_artifacts"] = (
            capo_codebuild.types.build_artifacts_list.deserialize_aws_json_1_1(
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
    if data.get("logConfig") is not None:
        import capo_codebuild.types.logs_config

        out["log_config"] = capo_codebuild.types.logs_config.deserialize_aws_json_1_1(
            data["logConfig"]
        )
    if data.get("buildTimeoutInMinutes") is not None:
        out["build_timeout_in_minutes"] = data["buildTimeoutInMinutes"]
    if data.get("queuedTimeoutInMinutes") is not None:
        out["queued_timeout_in_minutes"] = data["queuedTimeoutInMinutes"]
    if data.get("complete") is not None:
        out["complete"] = data["complete"]
    else:
        out["complete"] = False
    if data.get("initiator") is not None:
        out["initiator"] = data["initiator"]
    if data.get("vpcConfig") is not None:
        import capo_codebuild.types.vpc_config

        out["vpc_config"] = capo_codebuild.types.vpc_config.deserialize_aws_json_1_1(
            data["vpcConfig"]
        )
    if data.get("encryptionKey") is not None:
        out["encryption_key"] = data["encryptionKey"]
    if data.get("buildBatchNumber") is not None:
        out["build_batch_number"] = data["buildBatchNumber"]
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
    if data.get("buildGroups") is not None:
        import capo_codebuild.types.build_groups

        out["build_groups"] = (
            capo_codebuild.types.build_groups.deserialize_aws_json_1_1(
                data["buildGroups"]
            )
        )
    if data.get("debugSessionEnabled") is not None:
        out["debug_session_enabled"] = data["debugSessionEnabled"]
    if data.get("reportArns") is not None:
        import capo_codebuild.types.build_report_arns

        out["report_arns"] = (
            capo_codebuild.types.build_report_arns.deserialize_aws_json_1_1(
                data["reportArns"]
            )
        )
    return out

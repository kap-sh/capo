"""Generated from Smithy shape ``com.amazonaws.codebuild#Build``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.auto_retry_config
    import capo_codebuild.types.boolean
    import capo_codebuild.types.build_artifacts
    import capo_codebuild.types.build_artifacts_list
    import capo_codebuild.types.build_phases
    import capo_codebuild.types.build_report_arns
    import capo_codebuild.types.debug_session
    import capo_codebuild.types.exported_environment_variables
    import capo_codebuild.types.logs_location
    import capo_codebuild.types.network_interface
    import capo_codebuild.types.non_empty_string
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
    import capo_codebuild.types.wrapper_int
    import capo_codebuild.types.wrapper_long


class Build(TypedDict, closed=True):
    id: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The unique ID for the build.</p>"""
    arn: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the build.</p>"""
    build_number: NotRequired["capo_codebuild.types.wrapper_long.WrapperLong"]
    """<p>The number of the build. For each project, the <code>buildNumber</code> of its first build is <code>1</code>. The <code>buildNumber</code> of each subsequent build is incremented by <code>1</code>. If a build is deleted, the <code>buildNumber</code> of other builds does not change.</p>"""
    start_time: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>When the build process started, expressed in Unix time format.</p>"""
    end_time: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>When the build process ended, expressed in Unix time format.</p>"""
    current_phase: NotRequired["capo_codebuild.types.string.String"]
    """<p>The current build phase.</p>"""
    build_status: NotRequired["capo_codebuild.types.status_type.StatusType"]
    """<p>The current status of the build. Valid values include:</p> <ul> <li> <p> <code>FAILED</code>: The build failed.</p> </li> <li> <p> <code>FAULT</code>: The build faulted.</p> </li> <li> <p> <code>IN_PROGRESS</code>: The build is still in progress.</p> </li> <li> <p> <code>STOPPED</code>: The build stopped.</p> </li> <li> <p> <code>SUCCEEDED</code>: The build succeeded.</p> </li> <li> <p> <code>TIMED_OUT</code>: The build timed out.</p> </li> </ul>"""
    source_version: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>Any version identifier for the version of the source code to be built. If <code>sourceVersion</code> is specified at the project level, then this <code>sourceVersion</code> (at the build level) takes precedence. </p> <p> For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html">Source Version Sample with CodeBuild</a> in the <i>CodeBuild User Guide</i>. </p>"""
    resolved_source_version: NotRequired[
        "capo_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p> An identifier for the version of this build's source code. </p> <ul> <li> <p> For CodeCommit, GitHub, GitHub Enterprise, and BitBucket, the commit ID. </p> </li> <li> <p> For CodePipeline, the source revision provided by CodePipeline. </p> </li> <li> <p> For Amazon S3, this does not apply. </p> </li> </ul>"""
    project_name: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The name of the CodeBuild project.</p>"""
    phases: NotRequired["capo_codebuild.types.build_phases.BuildPhases"]
    """<p>Information about all previous build phases that are complete and information about any current build phase that is not yet complete.</p>"""
    source: NotRequired["capo_codebuild.types.project_source.ProjectSource"]
    """<p>Information about the source code to be built.</p>"""
    secondary_sources: NotRequired[
        "capo_codebuild.types.project_sources.ProjectSources"
    ]
    """<p> An array of <code>ProjectSource</code> objects. </p>"""
    secondary_source_versions: NotRequired[
        "capo_codebuild.types.project_secondary_source_versions.ProjectSecondarySourceVersions"
    ]
    """<p> An array of <code>ProjectSourceVersion</code> objects. Each <code>ProjectSourceVersion</code> must be one of: </p> <ul> <li> <p>For CodeCommit: the commit ID, branch, or Git tag to use.</p> </li> <li> <p>For GitHub: the commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format <code>pr/pull-request-ID</code> (for example, <code>pr/25</code>). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For Bitbucket: the commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </li> <li> <p>For Amazon S3: the version ID of the object that represents the build input ZIP file to use.</p> </li> </ul>"""
    artifacts: NotRequired["capo_codebuild.types.build_artifacts.BuildArtifacts"]
    """<p>Information about the output artifacts for the build.</p>"""
    secondary_artifacts: NotRequired[
        "capo_codebuild.types.build_artifacts_list.BuildArtifactsList"
    ]
    """<p> An array of <code>ProjectArtifacts</code> objects. </p>"""
    cache: NotRequired["capo_codebuild.types.project_cache.ProjectCache"]
    """<p>Information about the cache for the build.</p>"""
    environment: NotRequired[
        "capo_codebuild.types.project_environment.ProjectEnvironment"
    ]
    """<p>Information about the build environment for this build.</p>"""
    service_role: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The name of a service role used for this build.</p>"""
    logs: NotRequired["capo_codebuild.types.logs_location.LogsLocation"]
    """<p>Information about the build's logs in CloudWatch Logs.</p>"""
    timeout_in_minutes: NotRequired["capo_codebuild.types.wrapper_int.WrapperInt"]
    """<p>How long, in minutes, from 5 to 2160 (36 hours), for CodeBuild to wait before timing out this build if it does not get marked as completed.</p>"""
    queued_timeout_in_minutes: NotRequired[
        "capo_codebuild.types.wrapper_int.WrapperInt"
    ]
    """<p> The number of minutes a build is allowed to be queued before it times out. </p>"""
    build_complete: "capo_codebuild.types.boolean.Boolean"
    """<p>Whether the build is complete. True if complete; otherwise, false.</p>"""
    initiator: NotRequired["capo_codebuild.types.string.String"]
    """<p>The entity that started the build. Valid values include:</p> <ul> <li> <p>If CodePipeline started the build, the pipeline's name (for example, <code>codepipeline/my-demo-pipeline</code>).</p> </li> <li> <p>If a user started the build, the user's name (for example, <code>MyUserName</code>).</p> </li> <li> <p>If the Jenkins plugin for CodeBuild started the build, the string <code>CodeBuild-Jenkins-Plugin</code>.</p> </li> </ul>"""
    vpc_config: NotRequired["capo_codebuild.types.vpc_config.VpcConfig"]
    """<p>If your CodeBuild project accesses resources in an Amazon VPC, you provide this parameter that identifies the VPC ID and the list of security group IDs and subnet IDs. The security groups and subnets must belong to the same VPC. You must provide at least one security group and one subnet ID.</p>"""
    network_interface: NotRequired[
        "capo_codebuild.types.network_interface.NetworkInterface"
    ]
    """<p>Describes a network interface.</p>"""
    encryption_key: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The Key Management Service customer master key (CMK) to be used for encrypting the build output artifacts.</p> <note> <p> You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key. </p> </note> <p>You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format <code>alias/<alias-name></code>).</p>"""
    exported_environment_variables: NotRequired[
        "capo_codebuild.types.exported_environment_variables.ExportedEnvironmentVariables"
    ]
    """<p>A list of exported environment variables for this build.</p> <p>Exported environment variables are used in conjunction with CodePipeline to export environment variables from the current build stage to subsequent stages in the pipeline. For more information, see <a href="https://docs.aws.amazon.com/codepipeline/latest/userguide/actions-variables.html">Working with variables</a> in the <i>CodePipeline User Guide</i>.</p>"""
    report_arns: NotRequired["capo_codebuild.types.build_report_arns.BuildReportArns"]
    """<p> An array of the ARNs associated with this build's reports. </p>"""
    file_system_locations: NotRequired[
        "capo_codebuild.types.project_file_system_locations.ProjectFileSystemLocations"
    ]
    """<p> An array of <code>ProjectFileSystemLocation</code> objects for a CodeBuild build project. A <code>ProjectFileSystemLocation</code> object specifies the <code>identifier</code>, <code>location</code>, <code>mountOptions</code>, <code>mountPoint</code>, and <code>type</code> of a file system created using Amazon Elastic File System. </p>"""
    debug_session: NotRequired["capo_codebuild.types.debug_session.DebugSession"]
    """<p>Contains information about the debug session for this build.</p>"""
    build_batch_arn: NotRequired["capo_codebuild.types.string.String"]
    """<p>The ARN of the batch build that this build is a member of, if applicable.</p>"""
    auto_retry_config: NotRequired[
        "capo_codebuild.types.auto_retry_config.AutoRetryConfig"
    ]
    """<p>Information about the auto-retry configuration for the build.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Build) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "build_number" in value:
        out["buildNumber"] = value["build_number"]
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
    if "build_status" in value:
        import capo_codebuild.types.status_type

        out["buildStatus"] = capo_codebuild.types.status_type.serialize_aws_json_1_1(
            value["build_status"]
        )
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
    if "resolved_source_version" in value:
        out["resolvedSourceVersion"] = value["resolved_source_version"]
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    if "phases" in value:
        import capo_codebuild.types.build_phases

        out["phases"] = capo_codebuild.types.build_phases.serialize_aws_json_1_1(
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
    if "logs" in value:
        import capo_codebuild.types.logs_location

        out["logs"] = capo_codebuild.types.logs_location.serialize_aws_json_1_1(
            value["logs"]
        )
    if "timeout_in_minutes" in value:
        out["timeoutInMinutes"] = value["timeout_in_minutes"]
    if "queued_timeout_in_minutes" in value:
        out["queuedTimeoutInMinutes"] = value["queued_timeout_in_minutes"]
    out["buildComplete"] = value.get("build_complete", False)
    if "initiator" in value:
        out["initiator"] = value["initiator"]
    if "vpc_config" in value:
        import capo_codebuild.types.vpc_config

        out["vpcConfig"] = capo_codebuild.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "network_interface" in value:
        import capo_codebuild.types.network_interface

        out["networkInterface"] = (
            capo_codebuild.types.network_interface.serialize_aws_json_1_1(
                value["network_interface"]
            )
        )
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    if "exported_environment_variables" in value:
        import capo_codebuild.types.exported_environment_variables

        out["exportedEnvironmentVariables"] = (
            capo_codebuild.types.exported_environment_variables.serialize_aws_json_1_1(
                value["exported_environment_variables"]
            )
        )
    if "report_arns" in value:
        import capo_codebuild.types.build_report_arns

        out["reportArns"] = (
            capo_codebuild.types.build_report_arns.serialize_aws_json_1_1(
                value["report_arns"]
            )
        )
    if "file_system_locations" in value:
        import capo_codebuild.types.project_file_system_locations

        out["fileSystemLocations"] = (
            capo_codebuild.types.project_file_system_locations.serialize_aws_json_1_1(
                value["file_system_locations"]
            )
        )
    if "debug_session" in value:
        import capo_codebuild.types.debug_session

        out["debugSession"] = capo_codebuild.types.debug_session.serialize_aws_json_1_1(
            value["debug_session"]
        )
    if "build_batch_arn" in value:
        out["buildBatchArn"] = value["build_batch_arn"]
    if "auto_retry_config" in value:
        import capo_codebuild.types.auto_retry_config

        out["autoRetryConfig"] = (
            capo_codebuild.types.auto_retry_config.serialize_aws_json_1_1(
                value["auto_retry_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Build:
    out: Build = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("buildNumber") is not None:
        out["build_number"] = data["buildNumber"]
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
    if data.get("buildStatus") is not None:
        import capo_codebuild.types.status_type

        out["build_status"] = capo_codebuild.types.status_type.deserialize_aws_json_1_1(
            data["buildStatus"]
        )
    if data.get("sourceVersion") is not None:
        out["source_version"] = data["sourceVersion"]
    if data.get("resolvedSourceVersion") is not None:
        out["resolved_source_version"] = data["resolvedSourceVersion"]
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    if data.get("phases") is not None:
        import capo_codebuild.types.build_phases

        out["phases"] = capo_codebuild.types.build_phases.deserialize_aws_json_1_1(
            data["phases"]
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
    if data.get("logs") is not None:
        import capo_codebuild.types.logs_location

        out["logs"] = capo_codebuild.types.logs_location.deserialize_aws_json_1_1(
            data["logs"]
        )
    if data.get("timeoutInMinutes") is not None:
        out["timeout_in_minutes"] = data["timeoutInMinutes"]
    if data.get("queuedTimeoutInMinutes") is not None:
        out["queued_timeout_in_minutes"] = data["queuedTimeoutInMinutes"]
    if data.get("buildComplete") is not None:
        out["build_complete"] = data["buildComplete"]
    else:
        out["build_complete"] = False
    if data.get("initiator") is not None:
        out["initiator"] = data["initiator"]
    if data.get("vpcConfig") is not None:
        import capo_codebuild.types.vpc_config

        out["vpc_config"] = capo_codebuild.types.vpc_config.deserialize_aws_json_1_1(
            data["vpcConfig"]
        )
    if data.get("networkInterface") is not None:
        import capo_codebuild.types.network_interface

        out["network_interface"] = (
            capo_codebuild.types.network_interface.deserialize_aws_json_1_1(
                data["networkInterface"]
            )
        )
    if data.get("encryptionKey") is not None:
        out["encryption_key"] = data["encryptionKey"]
    if data.get("exportedEnvironmentVariables") is not None:
        import capo_codebuild.types.exported_environment_variables

        out["exported_environment_variables"] = (
            capo_codebuild.types.exported_environment_variables.deserialize_aws_json_1_1(
                data["exportedEnvironmentVariables"]
            )
        )
    if data.get("reportArns") is not None:
        import capo_codebuild.types.build_report_arns

        out["report_arns"] = (
            capo_codebuild.types.build_report_arns.deserialize_aws_json_1_1(
                data["reportArns"]
            )
        )
    if data.get("fileSystemLocations") is not None:
        import capo_codebuild.types.project_file_system_locations

        out["file_system_locations"] = (
            capo_codebuild.types.project_file_system_locations.deserialize_aws_json_1_1(
                data["fileSystemLocations"]
            )
        )
    if data.get("debugSession") is not None:
        import capo_codebuild.types.debug_session

        out["debug_session"] = (
            capo_codebuild.types.debug_session.deserialize_aws_json_1_1(
                data["debugSession"]
            )
        )
    if data.get("buildBatchArn") is not None:
        out["build_batch_arn"] = data["buildBatchArn"]
    if data.get("autoRetryConfig") is not None:
        import capo_codebuild.types.auto_retry_config

        out["auto_retry_config"] = (
            capo_codebuild.types.auto_retry_config.deserialize_aws_json_1_1(
                data["autoRetryConfig"]
            )
        )
    return out

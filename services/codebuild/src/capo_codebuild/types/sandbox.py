"""Generated from Smithy shape ``com.amazonaws.codebuild#Sandbox``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.logs_config
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.project_environment
    import capo_codebuild.types.project_file_system_locations
    import capo_codebuild.types.project_secondary_source_versions
    import capo_codebuild.types.project_source
    import capo_codebuild.types.project_sources
    import capo_codebuild.types.sandbox_session
    import capo_codebuild.types.string
    import capo_codebuild.types.timestamp
    import capo_codebuild.types.vpc_config
    import capo_codebuild.types.wrapper_int


class Sandbox(TypedDict, closed=True):
    id: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the sandbox.</p>"""
    arn: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the sandbox.</p>"""
    project_name: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The CodeBuild project name.</p>"""
    request_time: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>When the sandbox process was initially requested, expressed in Unix time format.</p>"""
    start_time: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>When the sandbox process started, expressed in Unix time format.</p>"""
    end_time: NotRequired["capo_codebuild.types.timestamp.Timestamp"]
    """<p>When the sandbox process ended, expressed in Unix time format.</p>"""
    status: NotRequired["capo_codebuild.types.string.String"]
    """<p>The status of the sandbox.</p>"""
    source: NotRequired["capo_codebuild.types.project_source.ProjectSource"]
    source_version: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>Any version identifier for the version of the sandbox to be built.</p>"""
    secondary_sources: NotRequired[
        "capo_codebuild.types.project_sources.ProjectSources"
    ]
    """<p> An array of <code>ProjectSource</code> objects. </p>"""
    secondary_source_versions: NotRequired[
        "capo_codebuild.types.project_secondary_source_versions.ProjectSecondarySourceVersions"
    ]
    """<p> An array of <code>ProjectSourceVersion</code> objects.</p>"""
    environment: NotRequired[
        "capo_codebuild.types.project_environment.ProjectEnvironment"
    ]
    file_system_locations: NotRequired[
        "capo_codebuild.types.project_file_system_locations.ProjectFileSystemLocations"
    ]
    """<p> An array of <code>ProjectFileSystemLocation</code> objects for a CodeBuild build project. A <code>ProjectFileSystemLocation</code> object specifies the <code>identifier</code>, <code>location</code>, <code>mountOptions</code>, <code>mountPoint</code>, and <code>type</code> of a file system created using Amazon Elastic File System. </p>"""
    timeout_in_minutes: NotRequired["capo_codebuild.types.wrapper_int.WrapperInt"]
    """<p>How long, in minutes, from 5 to 2160 (36 hours), for CodeBuild to wait before timing out this sandbox if it does not get marked as completed.</p>"""
    queued_timeout_in_minutes: NotRequired[
        "capo_codebuild.types.wrapper_int.WrapperInt"
    ]
    """<p>The number of minutes a sandbox is allowed to be queued before it times out. </p>"""
    vpc_config: NotRequired["capo_codebuild.types.vpc_config.VpcConfig"]
    log_config: NotRequired["capo_codebuild.types.logs_config.LogsConfig"]
    encryption_key: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The Key Management Service customer master key (CMK) to be used for encrypting the sandbox output artifacts.</p>"""
    service_role: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The name of a service role used for this sandbox.</p>"""
    current_session: NotRequired["capo_codebuild.types.sandbox_session.SandboxSession"]
    """<p>The current session for the sandbox.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Sandbox) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    if "request_time" in value:
        import capo_codebuild.types.timestamp

        out["requestTime"] = capo_codebuild.types.timestamp.serialize_aws_json_1_1(
            value["request_time"]
        )
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
    if "status" in value:
        out["status"] = value["status"]
    if "source" in value:
        import capo_codebuild.types.project_source

        out["source"] = capo_codebuild.types.project_source.serialize_aws_json_1_1(
            value["source"]
        )
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
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
    if "environment" in value:
        import capo_codebuild.types.project_environment

        out["environment"] = (
            capo_codebuild.types.project_environment.serialize_aws_json_1_1(
                value["environment"]
            )
        )
    if "file_system_locations" in value:
        import capo_codebuild.types.project_file_system_locations

        out["fileSystemLocations"] = (
            capo_codebuild.types.project_file_system_locations.serialize_aws_json_1_1(
                value["file_system_locations"]
            )
        )
    if "timeout_in_minutes" in value:
        out["timeoutInMinutes"] = value["timeout_in_minutes"]
    if "queued_timeout_in_minutes" in value:
        out["queuedTimeoutInMinutes"] = value["queued_timeout_in_minutes"]
    if "vpc_config" in value:
        import capo_codebuild.types.vpc_config

        out["vpcConfig"] = capo_codebuild.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "log_config" in value:
        import capo_codebuild.types.logs_config

        out["logConfig"] = capo_codebuild.types.logs_config.serialize_aws_json_1_1(
            value["log_config"]
        )
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "current_session" in value:
        import capo_codebuild.types.sandbox_session

        out["currentSession"] = (
            capo_codebuild.types.sandbox_session.serialize_aws_json_1_1(
                value["current_session"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Sandbox:
    out: Sandbox = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    if data.get("requestTime") is not None:
        import capo_codebuild.types.timestamp

        out["request_time"] = capo_codebuild.types.timestamp.deserialize_aws_json_1_1(
            data["requestTime"]
        )
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
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("source") is not None:
        import capo_codebuild.types.project_source

        out["source"] = capo_codebuild.types.project_source.deserialize_aws_json_1_1(
            data["source"]
        )
    if data.get("sourceVersion") is not None:
        out["source_version"] = data["sourceVersion"]
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
    if data.get("environment") is not None:
        import capo_codebuild.types.project_environment

        out["environment"] = (
            capo_codebuild.types.project_environment.deserialize_aws_json_1_1(
                data["environment"]
            )
        )
    if data.get("fileSystemLocations") is not None:
        import capo_codebuild.types.project_file_system_locations

        out["file_system_locations"] = (
            capo_codebuild.types.project_file_system_locations.deserialize_aws_json_1_1(
                data["fileSystemLocations"]
            )
        )
    if data.get("timeoutInMinutes") is not None:
        out["timeout_in_minutes"] = data["timeoutInMinutes"]
    if data.get("queuedTimeoutInMinutes") is not None:
        out["queued_timeout_in_minutes"] = data["queuedTimeoutInMinutes"]
    if data.get("vpcConfig") is not None:
        import capo_codebuild.types.vpc_config

        out["vpc_config"] = capo_codebuild.types.vpc_config.deserialize_aws_json_1_1(
            data["vpcConfig"]
        )
    if data.get("logConfig") is not None:
        import capo_codebuild.types.logs_config

        out["log_config"] = capo_codebuild.types.logs_config.deserialize_aws_json_1_1(
            data["logConfig"]
        )
    if data.get("encryptionKey") is not None:
        out["encryption_key"] = data["encryptionKey"]
    if data.get("serviceRole") is not None:
        out["service_role"] = data["serviceRole"]
    if data.get("currentSession") is not None:
        import capo_codebuild.types.sandbox_session

        out["current_session"] = (
            capo_codebuild.types.sandbox_session.deserialize_aws_json_1_1(
                data["currentSession"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Sandbox) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    if "request_time" in value:
        import capo_codebuild.types.timestamp

        out["requestTime"] = capo_codebuild.types.timestamp.serialize_cbor(
            value["request_time"]
        )
    if "start_time" in value:
        import capo_codebuild.types.timestamp

        out["startTime"] = capo_codebuild.types.timestamp.serialize_cbor(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_codebuild.types.timestamp

        out["endTime"] = capo_codebuild.types.timestamp.serialize_cbor(
            value["end_time"]
        )
    if "status" in value:
        out["status"] = value["status"]
    if "source" in value:
        import capo_codebuild.types.project_source

        out["source"] = capo_codebuild.types.project_source.serialize_cbor(
            value["source"]
        )
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
    if "secondary_sources" in value:
        import capo_codebuild.types.project_sources

        out["secondarySources"] = capo_codebuild.types.project_sources.serialize_cbor(
            value["secondary_sources"]
        )
    if "secondary_source_versions" in value:
        import capo_codebuild.types.project_secondary_source_versions

        out["secondarySourceVersions"] = (
            capo_codebuild.types.project_secondary_source_versions.serialize_cbor(
                value["secondary_source_versions"]
            )
        )
    if "environment" in value:
        import capo_codebuild.types.project_environment

        out["environment"] = capo_codebuild.types.project_environment.serialize_cbor(
            value["environment"]
        )
    if "file_system_locations" in value:
        import capo_codebuild.types.project_file_system_locations

        out["fileSystemLocations"] = (
            capo_codebuild.types.project_file_system_locations.serialize_cbor(
                value["file_system_locations"]
            )
        )
    if "timeout_in_minutes" in value:
        out["timeoutInMinutes"] = value["timeout_in_minutes"]
    if "queued_timeout_in_minutes" in value:
        out["queuedTimeoutInMinutes"] = value["queued_timeout_in_minutes"]
    if "vpc_config" in value:
        import capo_codebuild.types.vpc_config

        out["vpcConfig"] = capo_codebuild.types.vpc_config.serialize_cbor(
            value["vpc_config"]
        )
    if "log_config" in value:
        import capo_codebuild.types.logs_config

        out["logConfig"] = capo_codebuild.types.logs_config.serialize_cbor(
            value["log_config"]
        )
    if "encryption_key" in value:
        out["encryptionKey"] = value["encryption_key"]
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "current_session" in value:
        import capo_codebuild.types.sandbox_session

        out["currentSession"] = capo_codebuild.types.sandbox_session.serialize_cbor(
            value["current_session"]
        )
    return out


def deserialize_cbor(data: dict) -> Sandbox:
    out: Sandbox = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    if data.get("requestTime") is not None:
        import capo_codebuild.types.timestamp

        out["request_time"] = capo_codebuild.types.timestamp.deserialize_cbor(
            data["requestTime"]
        )
    if data.get("startTime") is not None:
        import capo_codebuild.types.timestamp

        out["start_time"] = capo_codebuild.types.timestamp.deserialize_cbor(
            data["startTime"]
        )
    if data.get("endTime") is not None:
        import capo_codebuild.types.timestamp

        out["end_time"] = capo_codebuild.types.timestamp.deserialize_cbor(
            data["endTime"]
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("source") is not None:
        import capo_codebuild.types.project_source

        out["source"] = capo_codebuild.types.project_source.deserialize_cbor(
            data["source"]
        )
    if data.get("sourceVersion") is not None:
        out["source_version"] = data["sourceVersion"]
    if data.get("secondarySources") is not None:
        import capo_codebuild.types.project_sources

        out["secondary_sources"] = (
            capo_codebuild.types.project_sources.deserialize_cbor(
                data["secondarySources"]
            )
        )
    if data.get("secondarySourceVersions") is not None:
        import capo_codebuild.types.project_secondary_source_versions

        out["secondary_source_versions"] = (
            capo_codebuild.types.project_secondary_source_versions.deserialize_cbor(
                data["secondarySourceVersions"]
            )
        )
    if data.get("environment") is not None:
        import capo_codebuild.types.project_environment

        out["environment"] = capo_codebuild.types.project_environment.deserialize_cbor(
            data["environment"]
        )
    if data.get("fileSystemLocations") is not None:
        import capo_codebuild.types.project_file_system_locations

        out["file_system_locations"] = (
            capo_codebuild.types.project_file_system_locations.deserialize_cbor(
                data["fileSystemLocations"]
            )
        )
    if data.get("timeoutInMinutes") is not None:
        out["timeout_in_minutes"] = data["timeoutInMinutes"]
    if data.get("queuedTimeoutInMinutes") is not None:
        out["queued_timeout_in_minutes"] = data["queuedTimeoutInMinutes"]
    if data.get("vpcConfig") is not None:
        import capo_codebuild.types.vpc_config

        out["vpc_config"] = capo_codebuild.types.vpc_config.deserialize_cbor(
            data["vpcConfig"]
        )
    if data.get("logConfig") is not None:
        import capo_codebuild.types.logs_config

        out["log_config"] = capo_codebuild.types.logs_config.deserialize_cbor(
            data["logConfig"]
        )
    if data.get("encryptionKey") is not None:
        out["encryption_key"] = data["encryptionKey"]
    if data.get("serviceRole") is not None:
        out["service_role"] = data["serviceRole"]
    if data.get("currentSession") is not None:
        import capo_codebuild.types.sandbox_session

        out["current_session"] = capo_codebuild.types.sandbox_session.deserialize_cbor(
            data["currentSession"]
        )
    return out

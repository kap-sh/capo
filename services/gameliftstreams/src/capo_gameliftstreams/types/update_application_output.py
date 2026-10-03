"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#UpdateApplicationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_gameliftstreams.types.application_log_output_uri
    import capo_gameliftstreams.types.application_source_uri
    import capo_gameliftstreams.types.application_status
    import capo_gameliftstreams.types.application_status_reason
    import capo_gameliftstreams.types.arn_list
    import capo_gameliftstreams.types.description
    import capo_gameliftstreams.types.executable_path
    import capo_gameliftstreams.types.file_paths
    import capo_gameliftstreams.types.id
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.replication_statuses
    import capo_gameliftstreams.types.runtime_environment


class UpdateApplicationOutput(TypedDict, closed=True):
    arn: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> that's assigned to an application resource and uniquely identifies it across all Amazon Web Services Regions. Format is <code>arn:aws:gameliftstreams:[AWS Region]:[AWS account]:application/[resource ID]</code>.</p>"""
    description: NotRequired["capo_gameliftstreams.types.description.Description"]
    """<p>A human-readable label for the application. You can edit this value. </p>"""
    runtime_environment: NotRequired[
        "capo_gameliftstreams.types.runtime_environment.RuntimeEnvironment"
    ]
    """<p> Configuration settings that identify the operating system for an application resource. This can also include a compatibility layer and other drivers. </p> <p>A runtime environment can be one of the following:</p> <ul> <li> <p> For Linux applications </p> <ul> <li> <p> Ubuntu 22.04 LTS (<code>Type=UBUNTU, Version=22_04_LTS</code>) </p> </li> </ul> </li> <li> <p> For Windows applications </p> <ul> <li> <p>Microsoft Windows Server 2022 Base (<code>Type=WINDOWS, Version=2022</code>)</p> </li> <li> <p>Proton 10.0-4 (<code>Type=PROTON, Version=20260204</code>)</p> </li> <li> <p>Proton 9.0-2 (<code>Type=PROTON, Version=20250516</code>)</p> </li> <li> <p>Proton 8.0-5 (<code>Type=PROTON, Version=20241007</code>)</p> </li> <li> <p>Proton 8.0-2c (<code>Type=PROTON, Version=20230704</code>)</p> </li> </ul> </li> </ul>"""
    executable_path: NotRequired[
        "capo_gameliftstreams.types.executable_path.ExecutablePath"
    ]
    """<p>The relative path and file name of the executable file that launches the content for streaming.</p>"""
    application_log_paths: NotRequired[
        "capo_gameliftstreams.types.file_paths.FilePaths"
    ]
    """<p>Locations of log files that your content generates during a stream session. Amazon GameLift Streams uploads log files to the Amazon S3 bucket that you specify in <code>ApplicationLogOutputUri</code> at the end of a stream session. To retrieve stored log files, call <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html">GetStreamSession</a> and get the <code>LogFileLocationUri</code>.</p>"""
    application_log_output_uri: NotRequired[
        "capo_gameliftstreams.types.application_log_output_uri.ApplicationLogOutputUri"
    ]
    """<p>An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more <code>ApplicationLogPaths</code>.</p>"""
    application_source_uri: NotRequired[
        "capo_gameliftstreams.types.application_source_uri.ApplicationSourceUri"
    ]
    """<p>The original Amazon S3 location of uploaded stream content for the application.</p>"""
    id: NotRequired["capo_gameliftstreams.types.id.Id"]
    """<p>A unique ID value that is assigned to the resource when it's created. Format example: <code>a-9ZY8X7Wv6</code>.</p>"""
    status: NotRequired[
        "capo_gameliftstreams.types.application_status.ApplicationStatus"
    ]
    """<p>The current status of the application resource. Possible statuses include the following:</p> <ul> <li> <p> <code>INITIALIZED</code>: Amazon GameLift Streams has received the request and is initiating the work flow to create an application. </p> </li> <li> <p> <code>PROCESSING</code>: The create application work flow is in process. Amazon GameLift Streams is copying the content and caching for future deployment in a stream group.</p> </li> <li> <p> <code>READY</code>: The application is ready to deploy in a stream group.</p> </li> <li> <p> <code>ERROR</code>: An error occurred when setting up the application. See <code>StatusReason</code> for more information.</p> </li> <li> <p> <code>DELETING</code>: Amazon GameLift Streams is in the process of deleting the application.</p> </li> </ul>"""
    status_reason: NotRequired[
        "capo_gameliftstreams.types.application_status_reason.ApplicationStatusReason"
    ]
    """<p>A short description of the status reason when the application is in <code>ERROR</code> status.</p>"""
    replication_statuses: NotRequired[
        "capo_gameliftstreams.types.replication_statuses.ReplicationStatuses"
    ]
    """<p>A set of replication statuses for each location.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>A timestamp that indicates when this resource was created. Timestamps are expressed using in ISO8601 format, such as: <code>2022-12-27T22:29:40+00:00</code> (UTC).</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>A timestamp that indicates when this resource was last updated. Timestamps are expressed using in ISO8601 format, such as: <code>2022-12-27T22:29:40+00:00</code> (UTC).</p>"""
    associated_stream_groups: NotRequired["capo_gameliftstreams.types.arn_list.ArnList"]
    """<p> A set of stream groups that this application is associated with. You can use any of these stream groups to stream your application. </p> <p>This value is a set of <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Names (ARNs)</a> that uniquely identify stream group resources. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationOutput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "runtime_environment" in value:
        import capo_gameliftstreams.types.runtime_environment

        out["RuntimeEnvironment"] = (
            capo_gameliftstreams.types.runtime_environment.serialize_json(
                value["runtime_environment"]
            )
        )
    if "executable_path" in value:
        out["ExecutablePath"] = value["executable_path"]
    if "application_log_paths" in value:
        import capo_gameliftstreams.types.file_paths

        out["ApplicationLogPaths"] = (
            capo_gameliftstreams.types.file_paths.serialize_json(
                value["application_log_paths"]
            )
        )
    if "application_log_output_uri" in value:
        out["ApplicationLogOutputUri"] = value["application_log_output_uri"]
    if "application_source_uri" in value:
        out["ApplicationSourceUri"] = value["application_source_uri"]
    if "id" in value:
        out["Id"] = value["id"]
    if "status" in value:
        import capo_gameliftstreams.types.application_status

        out["Status"] = capo_gameliftstreams.types.application_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        import capo_gameliftstreams.types.application_status_reason

        out["StatusReason"] = (
            capo_gameliftstreams.types.application_status_reason.serialize_json(
                value["status_reason"]
            )
        )
    if "replication_statuses" in value:
        import capo_gameliftstreams.types.replication_statuses

        out["ReplicationStatuses"] = (
            capo_gameliftstreams.types.replication_statuses.serialize_json(
                value["replication_statuses"]
            )
        )
    if "created_at" in value:
        import capo_gameliftstreams.types._prelude.timestamp

        out["CreatedAt"] = capo_gameliftstreams.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_gameliftstreams.types._prelude.timestamp

        out["LastUpdatedAt"] = (
            capo_gameliftstreams.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    if "associated_stream_groups" in value:
        import capo_gameliftstreams.types.arn_list

        out["AssociatedStreamGroups"] = (
            capo_gameliftstreams.types.arn_list.serialize_json(
                value["associated_stream_groups"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApplicationOutput:
    out: UpdateApplicationOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdateApplicationOutput.arn required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RuntimeEnvironment") is not None:
        import capo_gameliftstreams.types.runtime_environment

        out["runtime_environment"] = (
            capo_gameliftstreams.types.runtime_environment.deserialize_json(
                data["RuntimeEnvironment"]
            )
        )
    if data.get("ExecutablePath") is not None:
        out["executable_path"] = data["ExecutablePath"]
    if data.get("ApplicationLogPaths") is not None:
        import capo_gameliftstreams.types.file_paths

        out["application_log_paths"] = (
            capo_gameliftstreams.types.file_paths.deserialize_json(
                data["ApplicationLogPaths"]
            )
        )
    if data.get("ApplicationLogOutputUri") is not None:
        out["application_log_output_uri"] = data["ApplicationLogOutputUri"]
    if data.get("ApplicationSourceUri") is not None:
        out["application_source_uri"] = data["ApplicationSourceUri"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Status") is not None:
        import capo_gameliftstreams.types.application_status

        out["status"] = capo_gameliftstreams.types.application_status.deserialize_json(
            data["Status"]
        )
    if data.get("StatusReason") is not None:
        import capo_gameliftstreams.types.application_status_reason

        out["status_reason"] = (
            capo_gameliftstreams.types.application_status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    if data.get("ReplicationStatuses") is not None:
        import capo_gameliftstreams.types.replication_statuses

        out["replication_statuses"] = (
            capo_gameliftstreams.types.replication_statuses.deserialize_json(
                data["ReplicationStatuses"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_gameliftstreams.types._prelude.timestamp

        out["created_at"] = (
            capo_gameliftstreams.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    if data.get("LastUpdatedAt") is not None:
        import capo_gameliftstreams.types._prelude.timestamp

        out["last_updated_at"] = (
            capo_gameliftstreams.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedAt"]
            )
        )
    if data.get("AssociatedStreamGroups") is not None:
        import capo_gameliftstreams.types.arn_list

        out["associated_stream_groups"] = (
            capo_gameliftstreams.types.arn_list.deserialize_json(
                data["AssociatedStreamGroups"]
            )
        )
    return out

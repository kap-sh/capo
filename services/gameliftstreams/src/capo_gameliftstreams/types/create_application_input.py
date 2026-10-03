"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#CreateApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import capo_gameliftstreams.types.application_log_output_uri
    import capo_gameliftstreams.types.application_source_uri
    import capo_gameliftstreams.types.client_token
    import capo_gameliftstreams.types.description
    import capo_gameliftstreams.types.executable_path
    import capo_gameliftstreams.types.file_paths
    import capo_gameliftstreams.types.runtime_environment
    import capo_gameliftstreams.types.tags


class CreateApplicationInput(TypedDict, closed=True):
    description: "capo_gameliftstreams.types.description.Description"
    """<p>A human-readable label for the application. You can update this value later.</p>"""
    runtime_environment: (
        "capo_gameliftstreams.types.runtime_environment.RuntimeEnvironment"
    )
    """<p>Configuration settings that identify the operating system for an application resource. This can also include a compatibility layer and other drivers.</p> <p>A runtime environment can be one of the following:</p> <ul> <li> <p> For Linux applications </p> <ul> <li> <p> Ubuntu 22.04 LTS (<code>Type=UBUNTU, Version=22_04_LTS</code>) </p> </li> </ul> </li> <li> <p> For Windows applications </p> <ul> <li> <p>Microsoft Windows Server 2022 Base (<code>Type=WINDOWS, Version=2022</code>)</p> </li> <li> <p>Proton 10.0-4 (<code>Type=PROTON, Version=20260204</code>)</p> </li> <li> <p>Proton 9.0-2 (<code>Type=PROTON, Version=20250516</code>)</p> </li> <li> <p>Proton 8.0-5 (<code>Type=PROTON, Version=20241007</code>)</p> </li> <li> <p>Proton 8.0-2c (<code>Type=PROTON, Version=20230704</code>)</p> </li> </ul> </li> </ul>"""
    executable_path: "capo_gameliftstreams.types.executable_path.ExecutablePath"
    """<p>The relative path and file name of the executable file that Amazon GameLift Streams will stream. Specify a path relative to the location set in <code>ApplicationSourceUri</code>. The file must be contained within the application's root folder. For Windows applications, the file must be a valid Windows executable or batch file with a filename ending in .exe, .cmd, or .bat. For Linux applications, the file must be a valid Linux binary executable or a script that contains an initial interpreter line starting with a shebang ('<code>#!</code>').</p>"""
    application_source_uri: (
        "capo_gameliftstreams.types.application_source_uri.ApplicationSourceUri"
    )
    """<p>The location of the content that you want to stream. Enter an Amazon S3 URI to a bucket that contains your game or other application. The location can have a multi-level prefix structure, but it must include all the files needed to run the content. Amazon GameLift Streams copies everything under the specified location.</p> <p>This value is immutable. To designate a different content location, create a new application.</p> <note> <p>The Amazon S3 bucket and the Amazon GameLift Streams application must be in the same Amazon Web Services Region.</p> </note>"""
    application_log_paths: NotRequired[
        "capo_gameliftstreams.types.file_paths.FilePaths"
    ]
    """<p>Locations of log files that your content generates during a stream session. Enter path values that are relative to the <code>ApplicationSourceUri</code> location, or relative to the user's home directory when using a supported path variable. You can specify up to 10 log paths. Each individual log file cannot exceed 50 MB in size.</p> <p>Each path can be a directory or an exact file path. When you specify a directory, Amazon GameLift Streams collects only files with the following extensions: <code>.txt</code>, <code>.log</code>, and <code>.utrace</code>. To collect files with other extensions, specify the exact file path. The copy operation is not performed recursively in subfolders.</p> <p>The following path variables are recognized when they appear as the first component of a path: <code>%USERPROFILE%</code> (Windows and Proton), <code>$HOME</code> or <code>~</code> (Linux). Use a path variable when your application writes logs outside of the application directory.</p> <p>Amazon GameLift Streams uploads designated log files to the Amazon S3 bucket that you specify in <code>ApplicationLogOutputUri</code> at the end of a stream session. To retrieve stored log files, call <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html">GetStreamSession</a> and get the <code>LogFileLocationUri</code>.</p>"""
    application_log_output_uri: NotRequired[
        "capo_gameliftstreams.types.application_log_output_uri.ApplicationLogOutputUri"
    ]
    """<p>An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more <code>ApplicationLogPaths</code>.</p> <note> <p>The log bucket must have permissions that give Amazon GameLift Streams access to write the log files. For more information, see <a href="https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/applications.html#application-bucket-permission-template">Application log bucket permission policy</a> in the <i>Amazon GameLift Streams Developer Guide</i>.</p> </note>"""
    tags: NotRequired["capo_gameliftstreams.types.tags.Tags"]
    """<p>A list of labels to assign to the new application resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. See <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>. You can use <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TagResource.html">TagResource</a> to add tags, <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UntagResource.html">UntagResource</a> to remove tags, and <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListTagsForResource.html">ListTagsForResource</a> to view tags on existing resources.</p>"""
    client_token: NotRequired["capo_gameliftstreams.types.client_token.ClientToken"]
    """<p> A unique identifier that represents a client request. The request is idempotent, which ensures that an API request completes only once. When users send a request, Amazon GameLift Streams automatically populates this field. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationInput) -> dict:
    out: dict = {}
    out["Description"] = value["description"]
    import capo_gameliftstreams.types.runtime_environment

    out["RuntimeEnvironment"] = (
        capo_gameliftstreams.types.runtime_environment.serialize_json(
            value["runtime_environment"]
        )
    )
    out["ExecutablePath"] = value["executable_path"]
    out["ApplicationSourceUri"] = value["application_source_uri"]
    if "application_log_paths" in value:
        import capo_gameliftstreams.types.file_paths

        out["ApplicationLogPaths"] = (
            capo_gameliftstreams.types.file_paths.serialize_json(
                value["application_log_paths"]
            )
        )
    if "application_log_output_uri" in value:
        out["ApplicationLogOutputUri"] = value["application_log_output_uri"]
    if "tags" in value:
        import capo_gameliftstreams.types.tags

        out["Tags"] = capo_gameliftstreams.types.tags.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateApplicationInput:
    out: CreateApplicationInput = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        raise DeserializationError("CreateApplicationInput.description required")
    if data.get("RuntimeEnvironment") is not None:
        import capo_gameliftstreams.types.runtime_environment

        out["runtime_environment"] = (
            capo_gameliftstreams.types.runtime_environment.deserialize_json(
                data["RuntimeEnvironment"]
            )
        )
    else:
        raise DeserializationError(
            "CreateApplicationInput.runtime_environment required"
        )
    if data.get("ExecutablePath") is not None:
        out["executable_path"] = data["ExecutablePath"]
    else:
        raise DeserializationError("CreateApplicationInput.executable_path required")
    if data.get("ApplicationSourceUri") is not None:
        out["application_source_uri"] = data["ApplicationSourceUri"]
    else:
        raise DeserializationError(
            "CreateApplicationInput.application_source_uri required"
        )
    if data.get("ApplicationLogPaths") is not None:
        import capo_gameliftstreams.types.file_paths

        out["application_log_paths"] = (
            capo_gameliftstreams.types.file_paths.deserialize_json(
                data["ApplicationLogPaths"]
            )
        )
    if data.get("ApplicationLogOutputUri") is not None:
        out["application_log_output_uri"] = data["ApplicationLogOutputUri"]
    if data.get("Tags") is not None:
        import capo_gameliftstreams.types.tags

        out["tags"] = capo_gameliftstreams.types.tags.deserialize_json(data["Tags"])
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out

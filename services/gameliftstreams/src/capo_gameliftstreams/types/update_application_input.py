"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#UpdateApplicationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.application_log_output_uri
    import capo_gameliftstreams.types.description
    import capo_gameliftstreams.types.file_paths
    import capo_gameliftstreams.types.identifier


class UpdateApplicationInput(TypedDict, closed=True):
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the application resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6</code>. Example ID: <code>a-9ZY8X7Wv6</code>. </p>"""
    description: NotRequired["capo_gameliftstreams.types.description.Description"]
    """<p>A human-readable label for the application.</p>"""
    application_log_paths: NotRequired[
        "capo_gameliftstreams.types.file_paths.FilePaths"
    ]
    """<p>Locations of log files that your content generates during a stream session. Enter path values that are relative to the <code>ApplicationSourceUri</code> location, or relative to the user's home directory when using a supported path variable. You can specify up to 10 log paths. Each individual log file cannot exceed 50 MB in size.</p> <p>Each path can be a directory or an exact file path. When you specify a directory, Amazon GameLift Streams collects only files with the following extensions: <code>.txt</code>, <code>.log</code>, and <code>.utrace</code>. To collect files with other extensions, specify the exact file path. The copy operation is not performed recursively in subfolders.</p> <p>The following path variables are recognized when they appear as the first component of a path: <code>%USERPROFILE%</code> (Windows and Proton), <code>$HOME</code> or <code>~</code> (Linux). Use a path variable when your application writes logs outside of the application directory.</p> <p>Amazon GameLift Streams uploads designated log files to the Amazon S3 bucket that you specify in <code>ApplicationLogOutputUri</code> at the end of a stream session. To retrieve stored log files, call <a href="https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_GetStreamSession.html">GetStreamSession</a> and get the <code>LogFileLocationUri</code>.</p>"""
    application_log_output_uri: NotRequired[
        "capo_gameliftstreams.types.application_log_output_uri.ApplicationLogOutputUri"
    ]
    """<p>An Amazon S3 URI to a bucket where you would like Amazon GameLift Streams to save application logs. Required if you specify one or more <code>ApplicationLogPaths</code>.</p> <note> <p>The log bucket must have permissions that give Amazon GameLift Streams access to write the log files. For more information, see <a href="https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/applications.html#application-bucket-permission-template">Application log bucket permission policy</a> in the <i>Amazon GameLift Streams Developer Guide</i>. </p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "application_log_paths" in value:
        import capo_gameliftstreams.types.file_paths

        out["ApplicationLogPaths"] = (
            capo_gameliftstreams.types.file_paths.serialize_json(
                value["application_log_paths"]
            )
        )
    if "application_log_output_uri" in value:
        out["ApplicationLogOutputUri"] = value["application_log_output_uri"]
    return out


def deserialize_json(data: dict) -> UpdateApplicationInput:
    out: UpdateApplicationInput = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ApplicationLogPaths") is not None:
        import capo_gameliftstreams.types.file_paths

        out["application_log_paths"] = (
            capo_gameliftstreams.types.file_paths.deserialize_json(
                data["ApplicationLogPaths"]
            )
        )
    if data.get("ApplicationLogOutputUri") is not None:
        out["application_log_output_uri"] = data["ApplicationLogOutputUri"]
    return out

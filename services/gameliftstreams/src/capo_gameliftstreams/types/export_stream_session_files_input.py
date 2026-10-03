"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ExportStreamSessionFilesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_gameliftstreams.errors import DeserializationError

if TYPE_CHECKING:
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.output_uri


class ExportStreamSessionFilesInput(TypedDict, closed=True):
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>"""
    stream_session_identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream session resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567</code>. Example ID: <code>ABC123def4567</code>. </p>"""
    output_uri: "capo_gameliftstreams.types.output_uri.OutputUri"
    """<p> The S3 bucket URI where Amazon GameLift Streams uploads the set of compressed exported files for this stream session. Amazon GameLift Streams generates a ZIP file name based on the stream session metadata. Alternatively, you can provide a custom file name with a <code>.zip</code> file extension.</p> <p> Example 1: If you provide an S3 URI called <code>s3://amzn-s3-demo-destination-bucket/MyGame_Session1.zip</code>, then Amazon GameLift Streams will save the files at that location. </p> <p> Example 2: If you provide an S3 URI called <code>s3://amzn-s3-demo-destination-bucket/MyGameSessions_ExportedFiles/</code>, then Amazon GameLift Streams will save the files at <code>s3://amzn-s3-demo-destination-bucket/MyGameSessions_ExportedFiles/YYYYMMDD-HHMMSS-appId-sg-Id-sessionId.zip</code> or another similar name. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportStreamSessionFilesInput) -> dict:
    out: dict = {}
    out["OutputUri"] = value["output_uri"]
    return out


def deserialize_json(data: dict) -> ExportStreamSessionFilesInput:
    out: ExportStreamSessionFilesInput = {}  # type: ignore[typeddict-item]
    if data.get("OutputUri") is not None:
        out["output_uri"] = data["OutputUri"]
    else:
        raise DeserializationError("ExportStreamSessionFilesInput.output_uri required")
    return out

"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#CreateStreamSessionAdminShellInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.identifier


class CreateStreamSessionAdminShellInput(TypedDict, closed=True):
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>The stream group that runs this stream session.</p> <p>This value is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p>"""
    stream_session_identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream session resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamsession/sg-1AB2C3De4/ABC123def4567</code>. Example ID: <code>ABC123def4567</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStreamSessionAdminShellInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CreateStreamSessionAdminShellInput:
    out: CreateStreamSessionAdminShellInput = {}  # type: ignore[typeddict-item]
    return out

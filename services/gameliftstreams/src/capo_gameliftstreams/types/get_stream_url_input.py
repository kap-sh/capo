"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#GetStreamUrlInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.identifier


class GetStreamUrlInput(TypedDict, closed=True):
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p> <p>This is the stream group that owns the stream URL.</p>"""
    stream_url_identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>The unique identifier of the stream URL. Specify a stream URL ID or Amazon Resource Name (ARN). Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamurl/sg-1AB2C3De4/su-1AB2C3De4</code>. Example ID: <code>su-1AB2C3De4</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStreamUrlInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetStreamUrlInput:
    out: GetStreamUrlInput = {}  # type: ignore[typeddict-item]
    return out

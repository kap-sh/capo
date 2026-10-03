"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#RevokeStreamUrlInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.identifier
    import capo_gameliftstreams.types.revocation_mode


class RevokeStreamUrlInput(TypedDict, closed=True):
    identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>An <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Name (ARN)</a> or ID that uniquely identifies the stream group resource. Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4</code>. Example ID: <code>sg-1AB2C3De4</code>. </p> <p>This is the stream group that owns the stream URL.</p>"""
    stream_url_identifier: "capo_gameliftstreams.types.identifier.Identifier"
    """<p>The unique identifier of the stream URL to revoke. Specify a stream URL ID or Amazon Resource Name (ARN). Example ARN: <code>arn:aws:gameliftstreams:us-west-2:111122223333:streamurl/sg-1AB2C3De4/su-1AB2C3De4</code>. Example ID: <code>su-1AB2C3De4</code>.</p>"""
    revocation_mode: NotRequired[
        "capo_gameliftstreams.types.revocation_mode.RevocationMode"
    ]
    """<p>Controls what happens to running stream sessions when you revoke the stream URL. If you do not specify a value, the default is <code>REVOKE_URL</code>. Possible values include the following:</p> <ul> <li> <p> <code>REVOKE_URL</code>: Stops the stream URL from starting new stream sessions. Running sessions continue until they end.</p> </li> <li> <p> <code>REVOKE_AND_TERMINATE_SESSIONS</code>: Stops new stream sessions and ends any running stream sessions.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokeStreamUrlInput) -> dict:
    out: dict = {}
    if "revocation_mode" in value:
        import capo_gameliftstreams.types.revocation_mode

        out["RevocationMode"] = (
            capo_gameliftstreams.types.revocation_mode.serialize_json(
                value["revocation_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> RevokeStreamUrlInput:
    out: RevokeStreamUrlInput = {}  # type: ignore[typeddict-item]
    if data.get("RevocationMode") is not None:
        import capo_gameliftstreams.types.revocation_mode

        out["revocation_mode"] = (
            capo_gameliftstreams.types.revocation_mode.deserialize_json(
                data["RevocationMode"]
            )
        )
    return out

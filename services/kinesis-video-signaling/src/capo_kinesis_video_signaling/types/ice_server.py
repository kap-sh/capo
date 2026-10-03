"""Generated from Smithy shape ``com.amazonaws.kinesisvideosignaling#IceServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video_signaling.types.password
    import capo_kinesis_video_signaling.types.ttl
    import capo_kinesis_video_signaling.types.uris
    import capo_kinesis_video_signaling.types.username


class IceServer(TypedDict, closed=True):
    uris: NotRequired["capo_kinesis_video_signaling.types.uris.Uris"]
    """<p>An array of URIs, in the form specified in the <a href="https://tools.ietf.org/html/draft-petithuguenin-behave-turn-uris-03">I-D.petithuguenin-behave-turn-uris</a> spec. These URIs provide the different addresses and/or protocols that can be used to reach the TURN server.</p>"""
    username: NotRequired["capo_kinesis_video_signaling.types.username.Username"]
    """<p>A username to login to the ICE server.</p>"""
    password: NotRequired["capo_kinesis_video_signaling.types.password.Password"]
    """<p>A password to login to the ICE server.</p>"""
    ttl: NotRequired["capo_kinesis_video_signaling.types.ttl.Ttl"]
    """<p>The period of time, in seconds, during which the username and password are valid.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IceServer) -> dict:
    out: dict = {}
    if "uris" in value:
        import capo_kinesis_video_signaling.types.uris

        out["Uris"] = capo_kinesis_video_signaling.types.uris.serialize_json(
            value["uris"]
        )
    if "username" in value:
        out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
    if "ttl" in value:
        out["Ttl"] = value["ttl"]
    return out


def deserialize_json(data: dict) -> IceServer:
    out: IceServer = {}  # type: ignore[typeddict-item]
    if data.get("Uris") is not None:
        import capo_kinesis_video_signaling.types.uris

        out["uris"] = capo_kinesis_video_signaling.types.uris.deserialize_json(
            data["Uris"]
        )
    if data.get("Username") is not None:
        out["username"] = data["Username"]
    if data.get("Password") is not None:
        out["password"] = data["Password"]
    if data.get("Ttl") is not None:
        out["ttl"] = data["Ttl"]
    return out

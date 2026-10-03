"""Generated from Smithy shape ``com.amazonaws.codecatalyst#CreateAccessTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.access_token_name
    import capo_codecatalyst.types.timestamp


class CreateAccessTokenRequest(TypedDict, closed=True):
    name: "capo_codecatalyst.types.access_token_name.AccessTokenName"
    """<p>The friendly name of the personal access token.</p>"""
    expires_time: NotRequired["capo_codecatalyst.types.timestamp.Timestamp"]
    """<p>The date and time the personal access token expires, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessTokenRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "expires_time" in value:
        import capo_codecatalyst._protocol.serialize

        out["expiresTime"] = capo_codecatalyst._protocol.serialize.fmt_date_time(
            value["expires_time"]
        )
    return out


def deserialize_json(data: dict) -> CreateAccessTokenRequest:
    out: CreateAccessTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateAccessTokenRequest.name required")
    if data.get("expiresTime") is not None:
        import datetime

        out["expires_time"] = datetime.datetime.fromisoformat(
            data["expiresTime"].replace("Z", "+00:00")
        )
    return out

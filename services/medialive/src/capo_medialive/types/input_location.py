"""Generated from Smithy shape ``com.amazonaws.medialive#InputLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.__string_max2048


class InputLocation(TypedDict, closed=True):
    password_param: NotRequired["capo_medialive.types.__string.__string"]
    """key used to extract the password from EC2 Parameter store"""
    uri: NotRequired["capo_medialive.types.__string_max2048.__stringMax2048"]
    """Uniform Resource Identifier - This should be a path to a file accessible to the Live system (eg. a http:// URI) depending on the output type. For example, a RTMP destination should have a uri simliar to: "rtmp://fmsserver/live"."""
    username: NotRequired["capo_medialive.types.__string.__string"]
    """Documentation update needed"""


# --- restJson1 ser/de ---
def serialize_json(value: InputLocation) -> dict:
    out: dict = {}
    if "password_param" in value:
        out["passwordParam"] = value["password_param"]
    if "uri" in value:
        out["uri"] = value["uri"]
    if "username" in value:
        out["username"] = value["username"]
    return out


def deserialize_json(data: dict) -> InputLocation:
    out: InputLocation = {}  # type: ignore[typeddict-item]
    if data.get("passwordParam") is not None:
        out["password_param"] = data["passwordParam"]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    if data.get("username") is not None:
        out["username"] = data["username"]
    return out

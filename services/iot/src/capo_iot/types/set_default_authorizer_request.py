"""Generated from Smithy shape ``com.amazonaws.iot#SetDefaultAuthorizerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.authorizer_name


class SetDefaultAuthorizerRequest(TypedDict, closed=True):
    authorizer_name: "capo_iot.types.authorizer_name.AuthorizerName"
    """<p>The authorizer name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetDefaultAuthorizerRequest) -> dict:
    out: dict = {}
    out["authorizerName"] = value["authorizer_name"]
    return out


def deserialize_json(data: dict) -> SetDefaultAuthorizerRequest:
    out: SetDefaultAuthorizerRequest = {}  # type: ignore[typeddict-item]
    if data.get("authorizerName") is not None:
        out["authorizer_name"] = data["authorizerName"]
    else:
        out["authorizer_name"] = ""
    return out

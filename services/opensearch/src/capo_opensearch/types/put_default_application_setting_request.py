"""Generated from Smithy shape ``com.amazonaws.opensearch#PutDefaultApplicationSettingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.arn
    import capo_opensearch.types.boolean


class PutDefaultApplicationSettingRequest(TypedDict, closed=True):
    application_arn: "capo_opensearch.types.arn.ARN"
    set_as_default: "capo_opensearch.types.boolean.Boolean"
    """<p>Set to true to set the specified ARN as the default application. Set to false to clear the default application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDefaultApplicationSettingRequest) -> dict:
    out: dict = {}
    out["applicationArn"] = value["application_arn"]
    out["setAsDefault"] = value["set_as_default"]
    return out


def deserialize_json(data: dict) -> PutDefaultApplicationSettingRequest:
    out: PutDefaultApplicationSettingRequest = {}  # type: ignore[typeddict-item]
    if data.get("applicationArn") is not None:
        out["application_arn"] = data["applicationArn"]
    else:
        out["application_arn"] = ""
    if data.get("setAsDefault") is not None:
        out["set_as_default"] = data["setAsDefault"]
    else:
        out["set_as_default"] = False
    return out

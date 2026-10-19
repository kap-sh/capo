"""Generated from Smithy shape ``com.amazonaws.evs#GetDepotUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.environment_id


class GetDepotUrlRequest(TypedDict, closed=True):
    environment_id: "capo_evs.types.environment_id.EnvironmentId"
    """<p>The unique ID of the Amazon EVS environment to get the depot URL for.</p>"""
    rotate: NotRequired["bool"]
    """<p>Revokes the current authentication token and returns a new depot URL with a new token. Previously issued depot URLs will stop working within 5 minutes of rotation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetDepotUrlRequest) -> dict:
    out: dict = {}
    out["environmentId"] = value["environment_id"]
    if "rotate" in value:
        out["rotate"] = value["rotate"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetDepotUrlRequest:
    out: GetDepotUrlRequest = {}  # type: ignore[typeddict-item]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("rotate") is not None:
        out["rotate"] = data["rotate"]
    return out

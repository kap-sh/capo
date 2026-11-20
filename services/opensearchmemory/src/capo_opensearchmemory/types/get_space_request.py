"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#GetSpaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.space_id


class GetSpaceRequest(TypedDict, closed=True):
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The ID of the space.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSpaceRequest) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSpaceRequest:
    out: GetSpaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    return out

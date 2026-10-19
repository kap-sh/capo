"""Generated from Smithy shape ``com.amazonaws.repostspace#CreateSpaceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_repostspace.types.space_id


class CreateSpaceOutput(TypedDict, closed=True):
    space_id: "capo_repostspace.types.space_id.SpaceId"
    """<p>The unique ID of the private re:Post.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSpaceOutput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    return out


def deserialize_json(data: dict) -> CreateSpaceOutput:
    out: CreateSpaceOutput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    return out

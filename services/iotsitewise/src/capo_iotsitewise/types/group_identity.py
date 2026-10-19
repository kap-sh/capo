"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GroupIdentity``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.identity_id


class GroupIdentity(TypedDict, closed=True):
    id: "capo_iotsitewise.types.identity_id.IdentityId"
    """<p>The IAM Identity Center ID of the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupIdentity) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> GroupIdentity:
    out: GroupIdentity = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out

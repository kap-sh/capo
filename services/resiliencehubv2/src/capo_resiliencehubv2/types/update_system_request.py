"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateSystemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.entity_description


class UpdateSystemRequest(TypedDict, closed=True):
    system_arn: "capo_resiliencehubv2.types.arn.Arn"
    description: NotRequired[
        "capo_resiliencehubv2.types.entity_description.EntityDescription"
    ]
    sharing_enabled: NotRequired["bool"]
    """<p>Whether cross-account sharing is enabled for the system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSystemRequest) -> dict:
    out: dict = {}
    out["systemArn"] = value["system_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "sharing_enabled" in value:
        out["sharingEnabled"] = value["sharing_enabled"]
    return out


def deserialize_json(data: dict) -> UpdateSystemRequest:
    out: UpdateSystemRequest = {}  # type: ignore[typeddict-item]
    if data.get("systemArn") is not None:
        out["system_arn"] = data["systemArn"]
    else:
        out["system_arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("sharingEnabled") is not None:
        out["sharing_enabled"] = data["sharingEnabled"]
    return out

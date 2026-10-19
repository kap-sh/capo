"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.arn
    import capo_connectcampaignsv2.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    arn: "capo_connectcampaignsv2.types.arn.Arn"
    tags: "capo_connectcampaignsv2.types.tag_map.TagMap"


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_connectcampaignsv2.types.tag_map

    out["tags"] = capo_connectcampaignsv2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_connectcampaignsv2.types.tag_map

        out["tags"] = capo_connectcampaignsv2.types.tag_map.deserialize_json(
            data["tags"]
        )
    else:
        out["tags"] = {}
    return out

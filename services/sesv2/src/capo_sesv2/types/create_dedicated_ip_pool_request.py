"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateDedicatedIpPoolRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.pool_name
    import capo_sesv2.types.scaling_mode
    import capo_sesv2.types.tag_list


class CreateDedicatedIpPoolRequest(TypedDict, closed=True):
    pool_name: "capo_sesv2.types.pool_name.PoolName"
    """<p>The name of the dedicated IP pool.</p>"""
    tags: NotRequired["capo_sesv2.types.tag_list.TagList"]
    """<p>An object that defines the tags (keys and values) that you want to associate with the pool.</p>"""
    scaling_mode: NotRequired["capo_sesv2.types.scaling_mode.ScalingMode"]
    """<p>The type of scaling mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDedicatedIpPoolRequest) -> dict:
    out: dict = {}
    out["PoolName"] = value["pool_name"]
    if "tags" in value:
        import capo_sesv2.types.tag_list

        out["Tags"] = capo_sesv2.types.tag_list.serialize_json(value["tags"])
    if "scaling_mode" in value:
        import capo_sesv2.types.scaling_mode

        out["ScalingMode"] = capo_sesv2.types.scaling_mode.serialize_json(
            value["scaling_mode"]
        )
    return out


def deserialize_json(data: dict) -> CreateDedicatedIpPoolRequest:
    out: CreateDedicatedIpPoolRequest = {}  # type: ignore[typeddict-item]
    if data.get("PoolName") is not None:
        out["pool_name"] = data["PoolName"]
    else:
        out["pool_name"] = ""
    if data.get("Tags") is not None:
        import capo_sesv2.types.tag_list

        out["tags"] = capo_sesv2.types.tag_list.deserialize_json(data["Tags"])
    if data.get("ScalingMode") is not None:
        import capo_sesv2.types.scaling_mode

        out["scaling_mode"] = capo_sesv2.types.scaling_mode.deserialize_json(
            data["ScalingMode"]
        )
    return out

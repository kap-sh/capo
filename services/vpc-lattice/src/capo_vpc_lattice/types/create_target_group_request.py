"""Generated from Smithy shape ``com.amazonaws.vpclattice#CreateTargetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.client_token
    import capo_vpc_lattice.types.tag_map
    import capo_vpc_lattice.types.target_group_config
    import capo_vpc_lattice.types.target_group_name
    import capo_vpc_lattice.types.target_group_type


class CreateTargetGroupRequest(TypedDict, closed=True):
    name: "capo_vpc_lattice.types.target_group_name.TargetGroupName"
    """<p>The name of the target group. The name must be unique within the account. The valid characters are a-z, 0-9, and hyphens (-). You can't use a hyphen as the first or last character, or immediately after another hyphen.</p>"""
    type: "capo_vpc_lattice.types.target_group_type.TargetGroupType"
    """<p>The type of target group.</p>"""
    config: NotRequired["capo_vpc_lattice.types.target_group_config.TargetGroupConfig"]
    """<p>The target group configuration.</p>"""
    client_token: NotRequired["capo_vpc_lattice.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry succeeds without performing any actions. If the parameters aren't identical, the retry fails.</p>"""
    tags: NotRequired["capo_vpc_lattice.types.tag_map.TagMap"]
    """<p>The tags for the target group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTargetGroupRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["type"] = value["type"]
    if "config" in value:
        import capo_vpc_lattice.types.target_group_config

        out["config"] = capo_vpc_lattice.types.target_group_config.serialize_json(
            value["config"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateTargetGroupRequest:
    out: CreateTargetGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("config") is not None:
        import capo_vpc_lattice.types.target_group_config

        out["config"] = capo_vpc_lattice.types.target_group_config.deserialize_json(
            data["config"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_vpc_lattice.types.tag_map

        out["tags"] = capo_vpc_lattice.types.tag_map.deserialize_json(data["tags"])
    return out

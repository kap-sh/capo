"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#CreateScopeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.tag_map
    import capo_networkflowmonitor.types.target_resource_list
    import capo_networkflowmonitor.types.uuid_string


class CreateScopeInput(TypedDict, closed=True):
    targets: "capo_networkflowmonitor.types.target_resource_list.TargetResourceList"
    """<p>The targets to define the scope to be monitored. A target is an array of targetResources, which are currently Region-account pairs, defined by targetResource constructs.</p>"""
    client_token: NotRequired["capo_networkflowmonitor.types.uuid_string.UuidString"]
    """<p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Don't reuse the same client token for other API requests.</p>"""
    tags: NotRequired["capo_networkflowmonitor.types.tag_map.TagMap"]
    """<p>The tags for a scope. You can add a maximum of 200 tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateScopeInput) -> dict:
    out: dict = {}
    import capo_networkflowmonitor.types.target_resource_list

    out["targets"] = capo_networkflowmonitor.types.target_resource_list.serialize_json(
        value["targets"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_networkflowmonitor.types.tag_map

        out["tags"] = capo_networkflowmonitor.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateScopeInput:
    out: CreateScopeInput = {}  # type: ignore[typeddict-item]
    if data.get("targets") is not None:
        import capo_networkflowmonitor.types.target_resource_list

        out["targets"] = (
            capo_networkflowmonitor.types.target_resource_list.deserialize_json(
                data["targets"]
            )
        )
    else:
        out["targets"] = []
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_networkflowmonitor.types.tag_map

        out["tags"] = capo_networkflowmonitor.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out

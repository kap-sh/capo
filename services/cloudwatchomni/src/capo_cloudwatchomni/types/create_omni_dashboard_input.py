"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#CreateOmniDashboardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.client_token
    import capo_cloudwatchomni.types.space_id
    import capo_cloudwatchomni.types.tag_map


class CreateOmniDashboardInput(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space to create the dashboard in."""
    name: "str"
    """A name that identifies the dashboard."""
    body: "str"
    """The dashboard definition, as a JSON document. Maximum 1 MiB."""
    description: NotRequired["str"]
    """An optional description of the dashboard."""
    tags: NotRequired["capo_cloudwatchomni.types.tag_map.TagMap"]
    """The tags to associate with the dashboard."""
    client_token: NotRequired["capo_cloudwatchomni.types.client_token.ClientToken"]
    """Idempotency token for safe retries. Repeated requests with the same token return the original result instead of creating a duplicate."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateOmniDashboardInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["name"] = value["name"]
    out["body"] = value["body"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.serialize_cbor(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> CreateOmniDashboardInput:
    out: CreateOmniDashboardInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("body") is not None:
        out["body"] = data["body"]
    else:
        out["body"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_cloudwatchomni.types.tag_map

        out["tags"] = capo_cloudwatchomni.types.tag_map.deserialize_cbor(data["tags"])
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out

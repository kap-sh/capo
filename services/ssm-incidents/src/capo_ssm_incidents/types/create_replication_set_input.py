"""Generated from Smithy shape ``com.amazonaws.ssmincidents#CreateReplicationSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.client_token
    import capo_ssm_incidents.types.region_map_input
    import capo_ssm_incidents.types.tag_map


class CreateReplicationSetInput(TypedDict, closed=True):
    regions: "capo_ssm_incidents.types.region_map_input.RegionMapInput"
    """<p>The Regions that Incident Manager replicates your data to. You can have up to three Regions in your replication set.</p>"""
    client_token: NotRequired["capo_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token that ensures that the operation is called only once with the specified details.</p>"""
    tags: NotRequired["capo_ssm_incidents.types.tag_map.TagMap"]
    """<p>A list of tags to add to the replication set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateReplicationSetInput) -> dict:
    out: dict = {}
    import capo_ssm_incidents.types.region_map_input

    out["regions"] = capo_ssm_incidents.types.region_map_input.serialize_json(
        value["regions"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_ssm_incidents.types.tag_map

        out["tags"] = capo_ssm_incidents.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateReplicationSetInput:
    out: CreateReplicationSetInput = {}  # type: ignore[typeddict-item]
    if data.get("regions") is not None:
        import capo_ssm_incidents.types.region_map_input

        out["regions"] = capo_ssm_incidents.types.region_map_input.deserialize_json(
            data["regions"]
        )
    else:
        out["regions"] = {}
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_ssm_incidents.types.tag_map

        out["tags"] = capo_ssm_incidents.types.tag_map.deserialize_json(data["tags"])
    return out

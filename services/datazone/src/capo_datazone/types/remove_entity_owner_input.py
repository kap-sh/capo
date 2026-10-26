"""Generated from Smithy shape ``com.amazonaws.datazone#RemoveEntityOwnerInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.client_token
    import capo_datazone.types.data_zone_entity_type
    import capo_datazone.types.domain_id
    import capo_datazone.types.owner_properties


class RemoveEntityOwnerInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to remove an owner from an entity.</p>"""
    entity_type: "capo_datazone.types.data_zone_entity_type.DataZoneEntityType"
    """<p>The type of the entity from which you want to remove an owner.</p>"""
    entity_identifier: "str"
    """<p>The ID of the entity from which you want to remove an owner.</p>"""
    owner: "capo_datazone.types.owner_properties.OwnerProperties"
    """<p>The owner that you want to remove from an entity.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveEntityOwnerInput) -> dict:
    out: dict = {}
    import capo_datazone.types.owner_properties

    out["owner"] = capo_datazone.types.owner_properties.serialize_json(value["owner"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> RemoveEntityOwnerInput:
    out: RemoveEntityOwnerInput = {}  # type: ignore[typeddict-item]
    if data.get("owner") is not None:
        import capo_datazone.types.owner_properties

        out["owner"] = capo_datazone.types.owner_properties.deserialize_json(
            data["owner"]
        )
    else:
        out["owner"] = {"$unknown": {"name": ""}}
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out

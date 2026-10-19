"""Generated from Smithy shape ``com.amazonaws.datazone#CreateListingChangeSetInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.change_action
    import capo_datazone.types.client_token
    import capo_datazone.types.domain_id
    import capo_datazone.types.entity_identifier
    import capo_datazone.types.entity_type
    import capo_datazone.types.revision


class CreateListingChangeSetInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain.</p>"""
    entity_identifier: "capo_datazone.types.entity_identifier.EntityIdentifier"
    """<p>The ID of the asset.</p>"""
    entity_type: "capo_datazone.types.entity_type.EntityType"
    """<p>The type of an entity.</p>"""
    entity_revision: NotRequired["capo_datazone.types.revision.Revision"]
    """<p>The revision of an asset.</p>"""
    action: "capo_datazone.types.change_action.ChangeAction"
    """<p>Specifies whether to publish or unpublish a listing.</p>"""
    client_token: NotRequired["capo_datazone.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateListingChangeSetInput) -> dict:
    out: dict = {}
    out["entityIdentifier"] = value["entity_identifier"]
    import capo_datazone.types.entity_type

    out["entityType"] = capo_datazone.types.entity_type.serialize_json(
        value["entity_type"]
    )
    if "entity_revision" in value:
        out["entityRevision"] = value["entity_revision"]
    import capo_datazone.types.change_action

    out["action"] = capo_datazone.types.change_action.serialize_json(value["action"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateListingChangeSetInput:
    out: CreateListingChangeSetInput = {}  # type: ignore[typeddict-item]
    if data.get("entityIdentifier") is not None:
        out["entity_identifier"] = data["entityIdentifier"]
    else:
        out["entity_identifier"] = ""
    if data.get("entityType") is not None:
        import capo_datazone.types.entity_type

        out["entity_type"] = capo_datazone.types.entity_type.deserialize_json(
            data["entityType"]
        )
    else:
        import typing

        out["entity_type"] = typing.cast(
            "capo_datazone.types.entity_type.EntityType", ""
        )
    if data.get("entityRevision") is not None:
        out["entity_revision"] = data["entityRevision"]
    if data.get("action") is not None:
        import capo_datazone.types.change_action

        out["action"] = capo_datazone.types.change_action.deserialize_json(
            data["action"]
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_datazone.types.change_action.ChangeAction", ""
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out

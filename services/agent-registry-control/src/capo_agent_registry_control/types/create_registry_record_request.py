"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#CreateRegistryRecordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.client_token
    import capo_agent_registry_control.types.description
    import capo_agent_registry_control.types.descriptors
    import capo_agent_registry_control.types.provenance_list
    import capo_agent_registry_control.types.record_type
    import capo_agent_registry_control.types.registry_identifier
    import capo_agent_registry_control.types.registry_record_display_name
    import capo_agent_registry_control.types.registry_record_name
    import capo_agent_registry_control.types.registry_record_version
    import capo_agent_registry_control.types.tags_map


class CreateRegistryRecordRequest(TypedDict, closed=True):
    registry_id: (
        "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier"
    )
    """<p>The identifier of the registry in which to create the record (ARN or ID)</p>"""
    name: "capo_agent_registry_control.types.registry_record_name.RegistryRecordName"
    """<p>The name of the registry record</p>"""
    display_name: NotRequired[
        "capo_agent_registry_control.types.registry_record_display_name.RegistryRecordDisplayName"
    ]
    """<p>The human-readable display name of the registry record</p>"""
    description: NotRequired[
        "capo_agent_registry_control.types.description.Description"
    ]
    """<p>The description of the registry record</p>"""
    record_type: "capo_agent_registry_control.types.record_type.RecordType"
    """<p>The type of the registry record, which determines the descriptor format</p>"""
    descriptors: "capo_agent_registry_control.types.descriptors.Descriptors"
    """<p>The typed descriptor content for the registry record</p>"""
    record_version: NotRequired[
        "capo_agent_registry_control.types.registry_record_version.RegistryRecordVersion"
    ]
    """<p>The version of the registry record</p>"""
    client_token: NotRequired[
        "capo_agent_registry_control.types.client_token.ClientToken"
    ]
    """<p>Client token for idempotency</p>"""
    provenance: NotRequired[
        "capo_agent_registry_control.types.provenance_list.ProvenanceList"
    ]
    tags: NotRequired["capo_agent_registry_control.types.tags_map.TagsMap"]
    """<p>Tags to associate with the registry record</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRegistryRecordRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_agent_registry_control.types.record_type

    out["recordType"] = capo_agent_registry_control.types.record_type.serialize_json(
        value["record_type"]
    )
    import capo_agent_registry_control.types.descriptors

    out["descriptors"] = capo_agent_registry_control.types.descriptors.serialize_json(
        value["descriptors"]
    )
    if "record_version" in value:
        out["recordVersion"] = value["record_version"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "provenance" in value:
        import capo_agent_registry_control.types.provenance_list

        out["provenance"] = (
            capo_agent_registry_control.types.provenance_list.serialize_json(
                value["provenance"]
            )
        )
    if "tags" in value:
        import capo_agent_registry_control.types.tags_map

        out["tags"] = capo_agent_registry_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateRegistryRecordRequest:
    out: CreateRegistryRecordRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateRegistryRecordRequest.name required")
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("recordType") is not None:
        import capo_agent_registry_control.types.record_type

        out["record_type"] = (
            capo_agent_registry_control.types.record_type.deserialize_json(
                data["recordType"]
            )
        )
    else:
        raise DeserializationError("CreateRegistryRecordRequest.record_type required")
    if data.get("descriptors") is not None:
        import capo_agent_registry_control.types.descriptors

        out["descriptors"] = (
            capo_agent_registry_control.types.descriptors.deserialize_json(
                data["descriptors"]
            )
        )
    else:
        raise DeserializationError("CreateRegistryRecordRequest.descriptors required")
    if data.get("recordVersion") is not None:
        out["record_version"] = data["recordVersion"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("provenance") is not None:
        import capo_agent_registry_control.types.provenance_list

        out["provenance"] = (
            capo_agent_registry_control.types.provenance_list.deserialize_json(
                data["provenance"]
            )
        )
    if data.get("tags") is not None:
        import capo_agent_registry_control.types.tags_map

        out["tags"] = capo_agent_registry_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out

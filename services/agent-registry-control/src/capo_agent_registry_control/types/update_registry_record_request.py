"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdateRegistryRecordRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.provenance_list
    import capo_agent_registry_control.types.record_identifier
    import capo_agent_registry_control.types.record_type
    import capo_agent_registry_control.types.registry_identifier
    import capo_agent_registry_control.types.registry_record_name
    import capo_agent_registry_control.types.registry_record_version
    import capo_agent_registry_control.types.updated_description
    import capo_agent_registry_control.types.updated_descriptors
    import capo_agent_registry_control.types.updated_display_name


class UpdateRegistryRecordRequest(TypedDict, closed=True):
    registry_id: (
        "capo_agent_registry_control.types.registry_identifier.RegistryIdentifier"
    )
    """<p>The identifier of the registry containing the record (ARN or ID)</p>"""
    record_id: "capo_agent_registry_control.types.record_identifier.RecordIdentifier"
    """<p>The identifier of the registry record to update (ARN or ID)</p>"""
    name: NotRequired[
        "capo_agent_registry_control.types.registry_record_name.RegistryRecordName"
    ]
    """<p>The updated name of the registry record. Omit to leave the name unchanged.</p>"""
    display_name: NotRequired[
        "capo_agent_registry_control.types.updated_display_name.UpdatedDisplayName"
    ]
    """<p>The updated display name of the registry record. Omit to leave the display name unchanged; provide an empty wrapper to unset it.</p>"""
    description: NotRequired[
        "capo_agent_registry_control.types.updated_description.UpdatedDescription"
    ]
    """<p>The updated description of the registry record. Omit to leave the description unchanged; provide an empty wrapper to unset it.</p>"""
    record_type: NotRequired["capo_agent_registry_control.types.record_type.RecordType"]
    """<p>The updated type of the registry record. Omit to leave the record type unchanged.</p>"""
    descriptors: NotRequired[
        "capo_agent_registry_control.types.updated_descriptors.UpdatedDescriptors"
    ]
    """<p>The updated typed descriptor content for the registry record. Omit to leave the descriptors unchanged.</p>"""
    record_version: NotRequired[
        "capo_agent_registry_control.types.registry_record_version.RegistryRecordVersion"
    ]
    """<p>The updated version of the registry record. Omit to leave the version unchanged.</p>"""
    trigger_synchronization: NotRequired["bool"]
    """<p>Whether to trigger synchronization of the record's descriptor content from its source</p>"""
    provenance: NotRequired[
        "capo_agent_registry_control.types.provenance_list.ProvenanceList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRegistryRecordRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "display_name" in value:
        import capo_agent_registry_control.types.updated_display_name

        out["displayName"] = (
            capo_agent_registry_control.types.updated_display_name.serialize_json(
                value["display_name"]
            )
        )
    if "description" in value:
        import capo_agent_registry_control.types.updated_description

        out["description"] = (
            capo_agent_registry_control.types.updated_description.serialize_json(
                value["description"]
            )
        )
    if "record_type" in value:
        import capo_agent_registry_control.types.record_type

        out["recordType"] = (
            capo_agent_registry_control.types.record_type.serialize_json(
                value["record_type"]
            )
        )
    if "descriptors" in value:
        import capo_agent_registry_control.types.updated_descriptors

        out["descriptors"] = (
            capo_agent_registry_control.types.updated_descriptors.serialize_json(
                value["descriptors"]
            )
        )
    if "record_version" in value:
        out["recordVersion"] = value["record_version"]
    if "trigger_synchronization" in value:
        out["triggerSynchronization"] = value["trigger_synchronization"]
    if "provenance" in value:
        import capo_agent_registry_control.types.provenance_list

        out["provenance"] = (
            capo_agent_registry_control.types.provenance_list.serialize_json(
                value["provenance"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRegistryRecordRequest:
    out: UpdateRegistryRecordRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("displayName") is not None:
        import capo_agent_registry_control.types.updated_display_name

        out["display_name"] = (
            capo_agent_registry_control.types.updated_display_name.deserialize_json(
                data["displayName"]
            )
        )
    if data.get("description") is not None:
        import capo_agent_registry_control.types.updated_description

        out["description"] = (
            capo_agent_registry_control.types.updated_description.deserialize_json(
                data["description"]
            )
        )
    if data.get("recordType") is not None:
        import capo_agent_registry_control.types.record_type

        out["record_type"] = (
            capo_agent_registry_control.types.record_type.deserialize_json(
                data["recordType"]
            )
        )
    if data.get("descriptors") is not None:
        import capo_agent_registry_control.types.updated_descriptors

        out["descriptors"] = (
            capo_agent_registry_control.types.updated_descriptors.deserialize_json(
                data["descriptors"]
            )
        )
    if data.get("recordVersion") is not None:
        out["record_version"] = data["recordVersion"]
    if data.get("triggerSynchronization") is not None:
        out["trigger_synchronization"] = data["triggerSynchronization"]
    if data.get("provenance") is not None:
        import capo_agent_registry_control.types.provenance_list

        out["provenance"] = (
            capo_agent_registry_control.types.provenance_list.deserialize_json(
                data["provenance"]
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#SystemEventMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError, SerializationError
from capo_resiliencehubv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.system_created_metadata
    import capo_resiliencehubv2.types.system_deleted_metadata
    import capo_resiliencehubv2.types.system_policy_associated_metadata
    import capo_resiliencehubv2.types.system_policy_disassociated_metadata
    import capo_resiliencehubv2.types.system_service_associated_metadata
    import capo_resiliencehubv2.types.system_service_disassociated_metadata
    import capo_resiliencehubv2.types.system_user_journey_created_metadata
    import capo_resiliencehubv2.types.system_user_journey_deleted_metadata
    import capo_resiliencehubv2.types.system_user_journey_updated_metadata


class SystemEventMetadataSystemCreatedMember(TypedDict, closed=True):
    systemCreated: (
        "capo_resiliencehubv2.types.system_created_metadata.SystemCreatedMetadata"
    )


class SystemEventMetadataSystemDeletedMember(TypedDict, closed=True):
    systemDeleted: (
        "capo_resiliencehubv2.types.system_deleted_metadata.SystemDeletedMetadata"
    )


class SystemEventMetadataSystemUserJourneyCreatedMember(TypedDict, closed=True):
    systemUserJourneyCreated: "capo_resiliencehubv2.types.system_user_journey_created_metadata.SystemUserJourneyCreatedMetadata"


class SystemEventMetadataSystemUserJourneyUpdatedMember(TypedDict, closed=True):
    systemUserJourneyUpdated: "capo_resiliencehubv2.types.system_user_journey_updated_metadata.SystemUserJourneyUpdatedMetadata"


class SystemEventMetadataSystemUserJourneyDeletedMember(TypedDict, closed=True):
    systemUserJourneyDeleted: "capo_resiliencehubv2.types.system_user_journey_deleted_metadata.SystemUserJourneyDeletedMetadata"


class SystemEventMetadataSystemServiceAssociatedMember(TypedDict, closed=True):
    systemServiceAssociated: "capo_resiliencehubv2.types.system_service_associated_metadata.SystemServiceAssociatedMetadata"


class SystemEventMetadataSystemServiceDisassociatedMember(TypedDict, closed=True):
    systemServiceDisassociated: "capo_resiliencehubv2.types.system_service_disassociated_metadata.SystemServiceDisassociatedMetadata"


class SystemEventMetadataSystemPolicyAssociatedMember(TypedDict, closed=True):
    systemPolicyAssociated: "capo_resiliencehubv2.types.system_policy_associated_metadata.SystemPolicyAssociatedMetadata"


class SystemEventMetadataSystemPolicyDisassociatedMember(TypedDict, closed=True):
    systemPolicyDisassociated: "capo_resiliencehubv2.types.system_policy_disassociated_metadata.SystemPolicyDisassociatedMetadata"


SystemEventMetadata: TypeAlias = (
    SystemEventMetadataSystemCreatedMember
    | SystemEventMetadataSystemDeletedMember
    | SystemEventMetadataSystemUserJourneyCreatedMember
    | SystemEventMetadataSystemUserJourneyUpdatedMember
    | SystemEventMetadataSystemUserJourneyDeletedMember
    | SystemEventMetadataSystemServiceAssociatedMember
    | SystemEventMetadataSystemServiceDisassociatedMember
    | SystemEventMetadataSystemPolicyAssociatedMember
    | SystemEventMetadataSystemPolicyDisassociatedMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SystemEventMetadata) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SystemEventMetadata: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "systemCreated" in value:
        import capo_resiliencehubv2.types.system_created_metadata

        return {
            "systemCreated": capo_resiliencehubv2.types.system_created_metadata.serialize_json(
                value["systemCreated"]
            )
        }
    elif "systemDeleted" in value:
        import capo_resiliencehubv2.types.system_deleted_metadata

        return {
            "systemDeleted": capo_resiliencehubv2.types.system_deleted_metadata.serialize_json(
                value["systemDeleted"]
            )
        }
    elif "systemUserJourneyCreated" in value:
        import capo_resiliencehubv2.types.system_user_journey_created_metadata

        return {
            "systemUserJourneyCreated": capo_resiliencehubv2.types.system_user_journey_created_metadata.serialize_json(
                value["systemUserJourneyCreated"]
            )
        }
    elif "systemUserJourneyUpdated" in value:
        import capo_resiliencehubv2.types.system_user_journey_updated_metadata

        return {
            "systemUserJourneyUpdated": capo_resiliencehubv2.types.system_user_journey_updated_metadata.serialize_json(
                value["systemUserJourneyUpdated"]
            )
        }
    elif "systemUserJourneyDeleted" in value:
        import capo_resiliencehubv2.types.system_user_journey_deleted_metadata

        return {
            "systemUserJourneyDeleted": capo_resiliencehubv2.types.system_user_journey_deleted_metadata.serialize_json(
                value["systemUserJourneyDeleted"]
            )
        }
    elif "systemServiceAssociated" in value:
        import capo_resiliencehubv2.types.system_service_associated_metadata

        return {
            "systemServiceAssociated": capo_resiliencehubv2.types.system_service_associated_metadata.serialize_json(
                value["systemServiceAssociated"]
            )
        }
    elif "systemServiceDisassociated" in value:
        import capo_resiliencehubv2.types.system_service_disassociated_metadata

        return {
            "systemServiceDisassociated": capo_resiliencehubv2.types.system_service_disassociated_metadata.serialize_json(
                value["systemServiceDisassociated"]
            )
        }
    elif "systemPolicyAssociated" in value:
        import capo_resiliencehubv2.types.system_policy_associated_metadata

        return {
            "systemPolicyAssociated": capo_resiliencehubv2.types.system_policy_associated_metadata.serialize_json(
                value["systemPolicyAssociated"]
            )
        }
    elif "systemPolicyDisassociated" in value:
        import capo_resiliencehubv2.types.system_policy_disassociated_metadata

        return {
            "systemPolicyDisassociated": capo_resiliencehubv2.types.system_policy_disassociated_metadata.serialize_json(
                value["systemPolicyDisassociated"]
            )
        }
    else:
        raise SerializationError("SystemEventMetadata: no variant present")


def deserialize_json(data: dict) -> SystemEventMetadata:
    if data.get("systemCreated") is not None:
        import capo_resiliencehubv2.types.system_created_metadata

        return {
            "systemCreated": capo_resiliencehubv2.types.system_created_metadata.deserialize_json(
                data["systemCreated"]
            )
        }
    elif data.get("systemDeleted") is not None:
        import capo_resiliencehubv2.types.system_deleted_metadata

        return {
            "systemDeleted": capo_resiliencehubv2.types.system_deleted_metadata.deserialize_json(
                data["systemDeleted"]
            )
        }
    elif data.get("systemUserJourneyCreated") is not None:
        import capo_resiliencehubv2.types.system_user_journey_created_metadata

        return {
            "systemUserJourneyCreated": capo_resiliencehubv2.types.system_user_journey_created_metadata.deserialize_json(
                data["systemUserJourneyCreated"]
            )
        }
    elif data.get("systemUserJourneyUpdated") is not None:
        import capo_resiliencehubv2.types.system_user_journey_updated_metadata

        return {
            "systemUserJourneyUpdated": capo_resiliencehubv2.types.system_user_journey_updated_metadata.deserialize_json(
                data["systemUserJourneyUpdated"]
            )
        }
    elif data.get("systemUserJourneyDeleted") is not None:
        import capo_resiliencehubv2.types.system_user_journey_deleted_metadata

        return {
            "systemUserJourneyDeleted": capo_resiliencehubv2.types.system_user_journey_deleted_metadata.deserialize_json(
                data["systemUserJourneyDeleted"]
            )
        }
    elif data.get("systemServiceAssociated") is not None:
        import capo_resiliencehubv2.types.system_service_associated_metadata

        return {
            "systemServiceAssociated": capo_resiliencehubv2.types.system_service_associated_metadata.deserialize_json(
                data["systemServiceAssociated"]
            )
        }
    elif data.get("systemServiceDisassociated") is not None:
        import capo_resiliencehubv2.types.system_service_disassociated_metadata

        return {
            "systemServiceDisassociated": capo_resiliencehubv2.types.system_service_disassociated_metadata.deserialize_json(
                data["systemServiceDisassociated"]
            )
        }
    elif data.get("systemPolicyAssociated") is not None:
        import capo_resiliencehubv2.types.system_policy_associated_metadata

        return {
            "systemPolicyAssociated": capo_resiliencehubv2.types.system_policy_associated_metadata.deserialize_json(
                data["systemPolicyAssociated"]
            )
        }
    elif data.get("systemPolicyDisassociated") is not None:
        import capo_resiliencehubv2.types.system_policy_disassociated_metadata

        return {
            "systemPolicyDisassociated": capo_resiliencehubv2.types.system_policy_disassociated_metadata.deserialize_json(
                data["systemPolicyDisassociated"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SystemEventMetadata: no recognized variant key")

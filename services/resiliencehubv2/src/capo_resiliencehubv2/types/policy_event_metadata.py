"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PolicyEventMetadata``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError, SerializationError
from capo_resiliencehubv2.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.policy_attached_to_service_metadata
    import capo_resiliencehubv2.types.policy_deleted_metadata
    import capo_resiliencehubv2.types.policy_detached_from_service_metadata
    import capo_resiliencehubv2.types.policy_sharing_revoked_metadata


class _PolicyEventMetadata_policyAttachedToService(TypedDict, closed=True):
    policyAttachedToService: "capo_resiliencehubv2.types.policy_attached_to_service_metadata.PolicyAttachedToServiceMetadata"


class _PolicyEventMetadata_policyDetachedFromService(TypedDict, closed=True):
    policyDetachedFromService: "capo_resiliencehubv2.types.policy_detached_from_service_metadata.PolicyDetachedFromServiceMetadata"


class _PolicyEventMetadata_policySharingRevoked(TypedDict, closed=True):
    policySharingRevoked: "capo_resiliencehubv2.types.policy_sharing_revoked_metadata.PolicySharingRevokedMetadata"


class _PolicyEventMetadata_policyDeleted(TypedDict, closed=True):
    policyDeleted: (
        "capo_resiliencehubv2.types.policy_deleted_metadata.PolicyDeletedMetadata"
    )


PolicyEventMetadata: TypeAlias = (
    _PolicyEventMetadata_policyAttachedToService
    | _PolicyEventMetadata_policyDetachedFromService
    | _PolicyEventMetadata_policySharingRevoked
    | _PolicyEventMetadata_policyDeleted
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PolicyEventMetadata) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PolicyEventMetadata: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "policyAttachedToService" in value:
        import capo_resiliencehubv2.types.policy_attached_to_service_metadata

        return {
            "policyAttachedToService": capo_resiliencehubv2.types.policy_attached_to_service_metadata.serialize_json(
                value["policyAttachedToService"]
            )
        }
    elif "policyDetachedFromService" in value:
        import capo_resiliencehubv2.types.policy_detached_from_service_metadata

        return {
            "policyDetachedFromService": capo_resiliencehubv2.types.policy_detached_from_service_metadata.serialize_json(
                value["policyDetachedFromService"]
            )
        }
    elif "policySharingRevoked" in value:
        import capo_resiliencehubv2.types.policy_sharing_revoked_metadata

        return {
            "policySharingRevoked": capo_resiliencehubv2.types.policy_sharing_revoked_metadata.serialize_json(
                value["policySharingRevoked"]
            )
        }
    elif "policyDeleted" in value:
        import capo_resiliencehubv2.types.policy_deleted_metadata

        return {
            "policyDeleted": capo_resiliencehubv2.types.policy_deleted_metadata.serialize_json(
                value["policyDeleted"]
            )
        }
    else:
        raise SerializationError("PolicyEventMetadata: no variant present")


def deserialize_json(data: dict) -> PolicyEventMetadata:
    if data.get("policyAttachedToService") is not None:
        import capo_resiliencehubv2.types.policy_attached_to_service_metadata

        return {
            "policyAttachedToService": capo_resiliencehubv2.types.policy_attached_to_service_metadata.deserialize_json(
                data["policyAttachedToService"]
            )
        }
    elif data.get("policyDetachedFromService") is not None:
        import capo_resiliencehubv2.types.policy_detached_from_service_metadata

        return {
            "policyDetachedFromService": capo_resiliencehubv2.types.policy_detached_from_service_metadata.deserialize_json(
                data["policyDetachedFromService"]
            )
        }
    elif data.get("policySharingRevoked") is not None:
        import capo_resiliencehubv2.types.policy_sharing_revoked_metadata

        return {
            "policySharingRevoked": capo_resiliencehubv2.types.policy_sharing_revoked_metadata.deserialize_json(
                data["policySharingRevoked"]
            )
        }
    elif data.get("policyDeleted") is not None:
        import capo_resiliencehubv2.types.policy_deleted_metadata

        return {
            "policyDeleted": capo_resiliencehubv2.types.policy_deleted_metadata.deserialize_json(
                data["policyDeleted"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PolicyEventMetadata: no recognized variant key")

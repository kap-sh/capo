"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ApplicationPolicy``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_pca_connector_ad.errors import DeserializationError, SerializationError
from capo_pca_connector_ad.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.application_policy_type
    import capo_pca_connector_ad.types.custom_object_identifier


class _ApplicationPolicy_PolicyType(TypedDict, closed=True):
    PolicyType: (
        "capo_pca_connector_ad.types.application_policy_type.ApplicationPolicyType"
    )


class _ApplicationPolicy_PolicyObjectIdentifier(TypedDict, closed=True):
    PolicyObjectIdentifier: (
        "capo_pca_connector_ad.types.custom_object_identifier.CustomObjectIdentifier"
    )


ApplicationPolicy: TypeAlias = (
    _ApplicationPolicy_PolicyType
    | _ApplicationPolicy_PolicyObjectIdentifier
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationPolicy) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ApplicationPolicy: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "PolicyType" in value:
        import capo_pca_connector_ad.types.application_policy_type

        return {
            "PolicyType": capo_pca_connector_ad.types.application_policy_type.serialize_json(
                value["PolicyType"]
            )
        }
    elif "PolicyObjectIdentifier" in value:
        return {"PolicyObjectIdentifier": value["PolicyObjectIdentifier"]}
    else:
        raise SerializationError("ApplicationPolicy: no variant present")


def deserialize_json(data: dict) -> ApplicationPolicy:
    if data.get("PolicyType") is not None:
        import capo_pca_connector_ad.types.application_policy_type

        return {
            "PolicyType": capo_pca_connector_ad.types.application_policy_type.deserialize_json(
                data["PolicyType"]
            )
        }
    elif data.get("PolicyObjectIdentifier") is not None:
        return {"PolicyObjectIdentifier": data["PolicyObjectIdentifier"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ApplicationPolicy: no recognized variant key")

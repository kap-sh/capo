"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#MobileDeviceManagement``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_pca_connector_scep.errors import DeserializationError, SerializationError
from capo_pca_connector_scep.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.intune_configuration


class MobileDeviceManagementIntuneMember(TypedDict, closed=True):
    Intune: "capo_pca_connector_scep.types.intune_configuration.IntuneConfiguration"


MobileDeviceManagement: TypeAlias = (
    MobileDeviceManagementIntuneMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MobileDeviceManagement) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MobileDeviceManagement: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Intune" in value:
        import capo_pca_connector_scep.types.intune_configuration

        return {
            "Intune": capo_pca_connector_scep.types.intune_configuration.serialize_json(
                value["Intune"]
            )
        }
    else:
        raise SerializationError("MobileDeviceManagement: no variant present")


def deserialize_json(data: dict) -> MobileDeviceManagement:
    if data.get("Intune") is not None:
        import capo_pca_connector_scep.types.intune_configuration

        return {
            "Intune": capo_pca_connector_scep.types.intune_configuration.deserialize_json(
                data["Intune"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("MobileDeviceManagement: no recognized variant key")

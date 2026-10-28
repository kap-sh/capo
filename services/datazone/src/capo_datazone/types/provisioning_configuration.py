"""Generated from Smithy shape ``com.amazonaws.datazone#ProvisioningConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.lake_formation_configuration


class ProvisioningConfigurationLakeFormationConfigurationMember(TypedDict, closed=True):
    lakeFormationConfiguration: (
        "capo_datazone.types.lake_formation_configuration.LakeFormationConfiguration"
    )


ProvisioningConfiguration: TypeAlias = (
    ProvisioningConfigurationLakeFormationConfigurationMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProvisioningConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProvisioningConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "lakeFormationConfiguration" in value:
        import capo_datazone.types.lake_formation_configuration

        return {
            "lakeFormationConfiguration": capo_datazone.types.lake_formation_configuration.serialize_json(
                value["lakeFormationConfiguration"]
            )
        }
    else:
        raise SerializationError("ProvisioningConfiguration: no variant present")


def deserialize_json(data: dict) -> ProvisioningConfiguration:
    if data.get("lakeFormationConfiguration") is not None:
        import capo_datazone.types.lake_formation_configuration

        return {
            "lakeFormationConfiguration": capo_datazone.types.lake_formation_configuration.deserialize_json(
                data["lakeFormationConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ProvisioningConfiguration: no recognized variant key"
        )

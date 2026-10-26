"""Generated from Smithy shape ``com.amazonaws.datazone#ProvisioningProperties``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.cloud_formation_properties


class _ProvisioningProperties_cloudFormation(TypedDict, closed=True):
    cloudFormation: (
        "capo_datazone.types.cloud_formation_properties.CloudFormationProperties"
    )


ProvisioningProperties: TypeAlias = (
    _ProvisioningProperties_cloudFormation | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ProvisioningProperties) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProvisioningProperties: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "cloudFormation" in value:
        import capo_datazone.types.cloud_formation_properties

        return {
            "cloudFormation": capo_datazone.types.cloud_formation_properties.serialize_json(
                value["cloudFormation"]
            )
        }
    else:
        raise SerializationError("ProvisioningProperties: no variant present")


def deserialize_json(data: dict) -> ProvisioningProperties:
    if data.get("cloudFormation") is not None:
        import capo_datazone.types.cloud_formation_properties

        return {
            "cloudFormation": capo_datazone.types.cloud_formation_properties.deserialize_json(
                data["cloudFormation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ProvisioningProperties: no recognized variant key")

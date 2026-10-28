"""Generated from Smithy shape ``com.amazonaws.b2bi#CapabilityConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_b2bi.errors import DeserializationError, SerializationError
from capo_b2bi.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_b2bi.types.edi_configuration


class CapabilityConfigurationEdiMember(TypedDict, closed=True):
    edi: "capo_b2bi.types.edi_configuration.EdiConfiguration"


CapabilityConfiguration: TypeAlias = (
    CapabilityConfigurationEdiMember | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapabilityConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CapabilityConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "edi" in value:
        import capo_b2bi.types.edi_configuration

        return {
            "edi": capo_b2bi.types.edi_configuration.serialize_aws_json_1_0(
                value["edi"]
            )
        }
    else:
        raise SerializationError("CapabilityConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> CapabilityConfiguration:
    if data.get("edi") is not None:
        import capo_b2bi.types.edi_configuration

        return {
            "edi": capo_b2bi.types.edi_configuration.deserialize_aws_json_1_0(
                data["edi"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("CapabilityConfiguration: no recognized variant key")

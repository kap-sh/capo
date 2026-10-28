"""Generated from Smithy shape ``com.amazonaws.qbusiness#WebExperienceAuthConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError
from capo_qbusiness.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qbusiness.types.saml_configuration


class WebExperienceAuthConfigurationSamlConfigurationMember(TypedDict, closed=True):
    samlConfiguration: "capo_qbusiness.types.saml_configuration.SamlConfiguration"


WebExperienceAuthConfiguration: TypeAlias = (
    WebExperienceAuthConfigurationSamlConfigurationMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: WebExperienceAuthConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"WebExperienceAuthConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "samlConfiguration" in value:
        import capo_qbusiness.types.saml_configuration

        return {
            "samlConfiguration": capo_qbusiness.types.saml_configuration.serialize_json(
                value["samlConfiguration"]
            )
        }
    else:
        raise SerializationError("WebExperienceAuthConfiguration: no variant present")


def deserialize_json(data: dict) -> WebExperienceAuthConfiguration:
    if data.get("samlConfiguration") is not None:
        import capo_qbusiness.types.saml_configuration

        return {
            "samlConfiguration": capo_qbusiness.types.saml_configuration.deserialize_json(
                data["samlConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "WebExperienceAuthConfiguration: no recognized variant key"
        )

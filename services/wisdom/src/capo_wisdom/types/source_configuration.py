"""Generated from Smithy shape ``com.amazonaws.wisdom#SourceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_wisdom.errors import DeserializationError, SerializationError
from capo_wisdom.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_wisdom.types.app_integrations_configuration


class _SourceConfiguration_appIntegrations(TypedDict, closed=True):
    appIntegrations: (
        "capo_wisdom.types.app_integrations_configuration.AppIntegrationsConfiguration"
    )


SourceConfiguration: TypeAlias = (
    _SourceConfiguration_appIntegrations | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SourceConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SourceConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "appIntegrations" in value:
        import capo_wisdom.types.app_integrations_configuration

        return {
            "appIntegrations": capo_wisdom.types.app_integrations_configuration.serialize_json(
                value["appIntegrations"]
            )
        }
    else:
        raise SerializationError("SourceConfiguration: no variant present")


def deserialize_json(data: dict) -> SourceConfiguration:
    if data.get("appIntegrations") is not None:
        import capo_wisdom.types.app_integrations_configuration

        return {
            "appIntegrations": capo_wisdom.types.app_integrations_configuration.deserialize_json(
                data["appIntegrations"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SourceConfiguration: no recognized variant key")

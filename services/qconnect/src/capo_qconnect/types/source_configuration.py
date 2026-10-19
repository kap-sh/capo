"""Generated from Smithy shape ``com.amazonaws.qconnect#SourceConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.app_integrations_configuration
    import capo_qconnect.types.managed_source_configuration


class _SourceConfiguration_appIntegrations(TypedDict, closed=True):
    appIntegrations: "capo_qconnect.types.app_integrations_configuration.AppIntegrationsConfiguration"


class _SourceConfiguration_managedSourceConfiguration(TypedDict, closed=True):
    managedSourceConfiguration: (
        "capo_qconnect.types.managed_source_configuration.ManagedSourceConfiguration"
    )


SourceConfiguration: TypeAlias = (
    _SourceConfiguration_appIntegrations
    | _SourceConfiguration_managedSourceConfiguration
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SourceConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"SourceConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "appIntegrations" in value:
        import capo_qconnect.types.app_integrations_configuration

        return {
            "appIntegrations": capo_qconnect.types.app_integrations_configuration.serialize_json(
                value["appIntegrations"]
            )
        }
    elif "managedSourceConfiguration" in value:
        import capo_qconnect.types.managed_source_configuration

        return {
            "managedSourceConfiguration": capo_qconnect.types.managed_source_configuration.serialize_json(
                value["managedSourceConfiguration"]
            )
        }
    else:
        raise SerializationError("SourceConfiguration: no variant present")


def deserialize_json(data: dict) -> SourceConfiguration:
    if data.get("appIntegrations") is not None:
        import capo_qconnect.types.app_integrations_configuration

        return {
            "appIntegrations": capo_qconnect.types.app_integrations_configuration.deserialize_json(
                data["appIntegrations"]
            )
        }
    elif data.get("managedSourceConfiguration") is not None:
        import capo_qconnect.types.managed_source_configuration

        return {
            "managedSourceConfiguration": capo_qconnect.types.managed_source_configuration.deserialize_json(
                data["managedSourceConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("SourceConfiguration: no recognized variant key")


def redact_sensitive(value: SourceConfiguration) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "managedSourceConfiguration" in value:
        import capo_qconnect.types.managed_source_configuration

        out["managedSourceConfiguration"] = (
            capo_qconnect.types.managed_source_configuration.redact_sensitive(
                value["managedSourceConfiguration"]
            )
        )
    return out

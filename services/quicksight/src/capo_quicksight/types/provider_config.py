"""Generated from Smithy shape ``com.amazonaws.quicksight#ProviderConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError
from capo_quicksight.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_quicksight.types.microsoft_purview_provider_config


class ProviderConfigMicrosoftPurviewMember(TypedDict, closed=True):
    MicrosoftPurview: "capo_quicksight.types.microsoft_purview_provider_config.MicrosoftPurviewProviderConfig"


ProviderConfig: TypeAlias = ProviderConfigMicrosoftPurviewMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ProviderConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProviderConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "MicrosoftPurview" in value:
        import capo_quicksight.types.microsoft_purview_provider_config

        return {
            "MicrosoftPurview": capo_quicksight.types.microsoft_purview_provider_config.serialize_json(
                value["MicrosoftPurview"]
            )
        }
    else:
        raise SerializationError("ProviderConfig: no variant present")


def deserialize_json(data: dict) -> ProviderConfig:
    if data.get("MicrosoftPurview") is not None:
        import capo_quicksight.types.microsoft_purview_provider_config

        return {
            "MicrosoftPurview": capo_quicksight.types.microsoft_purview_provider_config.deserialize_json(
                data["MicrosoftPurview"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ProviderConfig: no recognized variant key")

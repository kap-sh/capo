"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ConfigurationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.direct_analysis_configuration_details


class _ConfigurationDetails_directAnalysisConfigurationDetails(TypedDict, closed=True):
    directAnalysisConfigurationDetails: "capo_cleanrooms.types.direct_analysis_configuration_details.DirectAnalysisConfigurationDetails"


ConfigurationDetails: TypeAlias = (
    _ConfigurationDetails_directAnalysisConfigurationDetails | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ConfigurationDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "directAnalysisConfigurationDetails" in value:
        import capo_cleanrooms.types.direct_analysis_configuration_details

        return {
            "directAnalysisConfigurationDetails": capo_cleanrooms.types.direct_analysis_configuration_details.serialize_json(
                value["directAnalysisConfigurationDetails"]
            )
        }
    else:
        raise SerializationError("ConfigurationDetails: no variant present")


def deserialize_json(data: dict) -> ConfigurationDetails:
    if data.get("directAnalysisConfigurationDetails") is not None:
        import capo_cleanrooms.types.direct_analysis_configuration_details

        return {
            "directAnalysisConfigurationDetails": capo_cleanrooms.types.direct_analysis_configuration_details.deserialize_json(
                data["directAnalysisConfigurationDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ConfigurationDetails: no recognized variant key")

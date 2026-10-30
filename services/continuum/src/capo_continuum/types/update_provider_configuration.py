"""Generated from Smithy shape ``com.amazonaws.continuum#UpdateProviderConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_continuum.errors import DeserializationError, SerializationError
from capo_continuum.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_continuum.types.update_s3_configuration


class UpdateProviderConfigurationS3Member(TypedDict, closed=True):
    s3: "capo_continuum.types.update_s3_configuration.UpdateS3Configuration"


UpdateProviderConfiguration: TypeAlias = (
    UpdateProviderConfigurationS3Member | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProviderConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UpdateProviderConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3" in value:
        import capo_continuum.types.update_s3_configuration

        return {
            "s3": capo_continuum.types.update_s3_configuration.serialize_json(
                value["s3"]
            )
        }
    else:
        raise SerializationError("UpdateProviderConfiguration: no variant present")


def deserialize_json(data: dict) -> UpdateProviderConfiguration:
    if data.get("s3") is not None:
        import capo_continuum.types.update_s3_configuration

        return {
            "s3": capo_continuum.types.update_s3_configuration.deserialize_json(
                data["s3"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "UpdateProviderConfiguration: no recognized variant key"
        )


def redact_sensitive(value: UpdateProviderConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "s3" in value:
        import capo_continuum.types.update_s3_configuration

        out["s3"] = capo_continuum.types.update_s3_configuration.redact_sensitive(
            value["s3"]
        )
    return out

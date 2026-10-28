"""Generated from Smithy shape ``com.amazonaws.omics#BatchRunSettings``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError, SerializationError
from capo_omics.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_omics.types.inline_settings
    import capo_omics.types.s3_uri_settings


class BatchRunSettingsInlineSettingsMember(TypedDict, closed=True):
    inlineSettings: "capo_omics.types.inline_settings.InlineSettings"


class BatchRunSettingsS3UriSettingsMember(TypedDict, closed=True):
    s3UriSettings: "capo_omics.types.s3_uri_settings.S3UriSettings"


BatchRunSettings: TypeAlias = (
    BatchRunSettingsInlineSettingsMember
    | BatchRunSettingsS3UriSettingsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: BatchRunSettings) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"BatchRunSettings: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "inlineSettings" in value:
        import capo_omics.types.inline_settings

        return {
            "inlineSettings": capo_omics.types.inline_settings.serialize_json(
                value["inlineSettings"]
            )
        }
    elif "s3UriSettings" in value:
        return {"s3UriSettings": value["s3UriSettings"]}
    else:
        raise SerializationError("BatchRunSettings: no variant present")


def deserialize_json(data: dict) -> BatchRunSettings:
    if data.get("inlineSettings") is not None:
        import capo_omics.types.inline_settings

        return {
            "inlineSettings": capo_omics.types.inline_settings.deserialize_json(
                data["inlineSettings"]
            )
        }
    elif data.get("s3UriSettings") is not None:
        return {"s3UriSettings": data["s3UriSettings"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("BatchRunSettings: no recognized variant key")

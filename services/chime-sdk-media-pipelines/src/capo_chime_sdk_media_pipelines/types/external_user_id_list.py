"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ExternalUserIdList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.external_user_id_type

ExternalUserIdList: TypeAlias = list[
    "capo_chime_sdk_media_pipelines.types.external_user_id_type.ExternalUserIdType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExternalUserIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> ExternalUserIdList:
    return [item for item in data if item is not None]


def redact_sensitive(value: ExternalUserIdList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)

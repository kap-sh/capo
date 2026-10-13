"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#UpsertEntitiesInfo``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.upsert_entity_info

UpsertEntitiesInfo: TypeAlias = list[
    "capo_bedrock_data_automation.types.upsert_entity_info.UpsertEntityInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpsertEntitiesInfo) -> list:
    import capo_bedrock_data_automation.types.upsert_entity_info

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation.types.upsert_entity_info.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UpsertEntitiesInfo:
    import capo_bedrock_data_automation.types.upsert_entity_info

    out: UpsertEntitiesInfo = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_data_automation.types.upsert_entity_info.deserialize_json(item)
        )
    return out


def redact_sensitive(value: UpsertEntitiesInfo) -> list[Any]:
    import capo_bedrock_data_automation.types.upsert_entity_info

    return [
        capo_bedrock_data_automation.types.upsert_entity_info.redact_sensitive(item)
        for item in value
    ]

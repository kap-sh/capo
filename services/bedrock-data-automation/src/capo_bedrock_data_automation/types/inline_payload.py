"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#InlinePayload``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_data_automation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.delete_entities_info
    import capo_bedrock_data_automation.types.upsert_entities_info


class _InlinePayload_upsertEntitiesInfo(TypedDict, closed=True):
    upsertEntitiesInfo: (
        "capo_bedrock_data_automation.types.upsert_entities_info.UpsertEntitiesInfo"
    )


class _InlinePayload_deleteEntitiesInfo(TypedDict, closed=True):
    deleteEntitiesInfo: (
        "capo_bedrock_data_automation.types.delete_entities_info.DeleteEntitiesInfo"
    )


InlinePayload: TypeAlias = (
    _InlinePayload_upsertEntitiesInfo | _InlinePayload_deleteEntitiesInfo
)


# --- restJson1 ser/de ---
def serialize_json(value: InlinePayload) -> dict:
    if "upsertEntitiesInfo" in value:
        import capo_bedrock_data_automation.types.upsert_entities_info

        return {
            "upsertEntitiesInfo": capo_bedrock_data_automation.types.upsert_entities_info.serialize_json(
                value["upsertEntitiesInfo"]
            )
        }
    elif "deleteEntitiesInfo" in value:
        import capo_bedrock_data_automation.types.delete_entities_info

        return {
            "deleteEntitiesInfo": capo_bedrock_data_automation.types.delete_entities_info.serialize_json(
                value["deleteEntitiesInfo"]
            )
        }
    else:
        raise SerializationError("InlinePayload: no variant present")


def deserialize_json(data: dict) -> InlinePayload:
    if data.get("upsertEntitiesInfo") is not None:
        import capo_bedrock_data_automation.types.upsert_entities_info

        return {
            "upsertEntitiesInfo": capo_bedrock_data_automation.types.upsert_entities_info.deserialize_json(
                data["upsertEntitiesInfo"]
            )
        }
    elif data.get("deleteEntitiesInfo") is not None:
        import capo_bedrock_data_automation.types.delete_entities_info

        return {
            "deleteEntitiesInfo": capo_bedrock_data_automation.types.delete_entities_info.deserialize_json(
                data["deleteEntitiesInfo"]
            )
        }
    else:
        raise DeserializationError("InlinePayload: no recognized variant key")


def redact_sensitive(value: InlinePayload) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "upsertEntitiesInfo" in value:
        import capo_bedrock_data_automation.types.upsert_entities_info

        out["upsertEntitiesInfo"] = (
            capo_bedrock_data_automation.types.upsert_entities_info.redact_sensitive(
                value["upsertEntitiesInfo"]
            )
        )
    return out

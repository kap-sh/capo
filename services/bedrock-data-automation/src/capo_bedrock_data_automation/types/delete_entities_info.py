"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DeleteEntitiesInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.entity_id_list


class DeleteEntitiesInfo(TypedDict, closed=True):
    entity_ids: "capo_bedrock_data_automation.types.entity_id_list.EntityIdList"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEntitiesInfo) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation.types.entity_id_list

    out["entityIds"] = capo_bedrock_data_automation.types.entity_id_list.serialize_json(
        value["entity_ids"]
    )
    return out


def deserialize_json(data: dict) -> DeleteEntitiesInfo:
    out: DeleteEntitiesInfo = {}  # type: ignore[typeddict-item]
    if data.get("entityIds") is not None:
        import capo_bedrock_data_automation.types.entity_id_list

        out["entity_ids"] = (
            capo_bedrock_data_automation.types.entity_id_list.deserialize_json(
                data["entityIds"]
            )
        )
    else:
        out["entity_ids"] = []
    return out

"""Generated from Smithy shape ``com.amazonaws.ssmincidents#RelatedItemsUpdate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError
from capo_ssm_incidents.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm_incidents.types.item_identifier
    import capo_ssm_incidents.types.related_item


class RelatedItemsUpdateItemToAddMember(TypedDict, closed=True):
    itemToAdd: "capo_ssm_incidents.types.related_item.RelatedItem"


class RelatedItemsUpdateItemToRemoveMember(TypedDict, closed=True):
    itemToRemove: "capo_ssm_incidents.types.item_identifier.ItemIdentifier"


RelatedItemsUpdate: TypeAlias = (
    RelatedItemsUpdateItemToAddMember
    | RelatedItemsUpdateItemToRemoveMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemsUpdate) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RelatedItemsUpdate: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "itemToAdd" in value:
        import capo_ssm_incidents.types.related_item

        return {
            "itemToAdd": capo_ssm_incidents.types.related_item.serialize_json(
                value["itemToAdd"]
            )
        }
    elif "itemToRemove" in value:
        import capo_ssm_incidents.types.item_identifier

        return {
            "itemToRemove": capo_ssm_incidents.types.item_identifier.serialize_json(
                value["itemToRemove"]
            )
        }
    else:
        raise SerializationError("RelatedItemsUpdate: no variant present")


def deserialize_json(data: dict) -> RelatedItemsUpdate:
    if data.get("itemToAdd") is not None:
        import capo_ssm_incidents.types.related_item

        return {
            "itemToAdd": capo_ssm_incidents.types.related_item.deserialize_json(
                data["itemToAdd"]
            )
        }
    elif data.get("itemToRemove") is not None:
        import capo_ssm_incidents.types.item_identifier

        return {
            "itemToRemove": capo_ssm_incidents.types.item_identifier.deserialize_json(
                data["itemToRemove"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RelatedItemsUpdate: no recognized variant key")

"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#PrivacyBudgets``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError, SerializationError
from capo_cleanroomsml.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanroomsml.types.access_budgets


class _PrivacyBudgets_accessBudgets(TypedDict, closed=True):
    accessBudgets: "capo_cleanroomsml.types.access_budgets.AccessBudgets"


PrivacyBudgets: TypeAlias = _PrivacyBudgets_accessBudgets | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudgets) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PrivacyBudgets: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "accessBudgets" in value:
        import capo_cleanroomsml.types.access_budgets

        return {
            "accessBudgets": capo_cleanroomsml.types.access_budgets.serialize_json(
                value["accessBudgets"]
            )
        }
    else:
        raise SerializationError("PrivacyBudgets: no variant present")


def deserialize_json(data: dict) -> PrivacyBudgets:
    if data.get("accessBudgets") is not None:
        import capo_cleanroomsml.types.access_budgets

        return {
            "accessBudgets": capo_cleanroomsml.types.access_budgets.deserialize_json(
                data["accessBudgets"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PrivacyBudgets: no recognized variant key")

"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudget``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.access_budget
    import capo_cleanrooms.types.differential_privacy_privacy_budget


class PrivacyBudgetDifferentialPrivacyMember(TypedDict, closed=True):
    differentialPrivacy: "capo_cleanrooms.types.differential_privacy_privacy_budget.DifferentialPrivacyPrivacyBudget"


class PrivacyBudgetAccessBudgetMember(TypedDict, closed=True):
    accessBudget: "capo_cleanrooms.types.access_budget.AccessBudget"


PrivacyBudget: TypeAlias = (
    PrivacyBudgetDifferentialPrivacyMember
    | PrivacyBudgetAccessBudgetMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudget) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PrivacyBudget: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "differentialPrivacy" in value:
        import capo_cleanrooms.types.differential_privacy_privacy_budget

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_privacy_budget.serialize_json(
                value["differentialPrivacy"]
            )
        }
    elif "accessBudget" in value:
        import capo_cleanrooms.types.access_budget

        return {
            "accessBudget": capo_cleanrooms.types.access_budget.serialize_json(
                value["accessBudget"]
            )
        }
    else:
        raise SerializationError("PrivacyBudget: no variant present")


def deserialize_json(data: dict) -> PrivacyBudget:
    if data.get("differentialPrivacy") is not None:
        import capo_cleanrooms.types.differential_privacy_privacy_budget

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_privacy_budget.deserialize_json(
                data["differentialPrivacy"]
            )
        }
    elif data.get("accessBudget") is not None:
        import capo_cleanrooms.types.access_budget

        return {
            "accessBudget": capo_cleanrooms.types.access_budget.deserialize_json(
                data["accessBudget"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PrivacyBudget: no recognized variant key")

"""Generated from Smithy shape ``com.amazonaws.deadline#BudgetSchedule``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.fixed_budget_schedule


class BudgetScheduleFixedMember(TypedDict, closed=True):
    fixed: "capo_deadline.types.fixed_budget_schedule.FixedBudgetSchedule"


BudgetSchedule: TypeAlias = BudgetScheduleFixedMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: BudgetSchedule) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"BudgetSchedule: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "fixed" in value:
        import capo_deadline.types.fixed_budget_schedule

        return {
            "fixed": capo_deadline.types.fixed_budget_schedule.serialize_json(
                value["fixed"]
            )
        }
    else:
        raise SerializationError("BudgetSchedule: no variant present")


def deserialize_json(data: dict) -> BudgetSchedule:
    if data.get("fixed") is not None:
        import capo_deadline.types.fixed_budget_schedule

        return {
            "fixed": capo_deadline.types.fixed_budget_schedule.deserialize_json(
                data["fixed"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("BudgetSchedule: no recognized variant key")

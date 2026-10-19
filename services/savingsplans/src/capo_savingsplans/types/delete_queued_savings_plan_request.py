"""Generated from Smithy shape ``com.amazonaws.savingsplans#DeleteQueuedSavingsPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_savingsplans.types.savings_plan_id


class DeleteQueuedSavingsPlanRequest(TypedDict, closed=True):
    savings_plan_id: "capo_savingsplans.types.savings_plan_id.SavingsPlanId"
    """<p>The ID of the Savings Plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQueuedSavingsPlanRequest) -> dict:
    out: dict = {}
    out["savingsPlanId"] = value["savings_plan_id"]
    return out


def deserialize_json(data: dict) -> DeleteQueuedSavingsPlanRequest:
    out: DeleteQueuedSavingsPlanRequest = {}  # type: ignore[typeddict-item]
    if data.get("savingsPlanId") is not None:
        out["savings_plan_id"] = data["savingsPlanId"]
    else:
        out["savings_plan_id"] = ""
    return out

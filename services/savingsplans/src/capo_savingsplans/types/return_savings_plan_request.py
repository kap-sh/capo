"""Generated from Smithy shape ``com.amazonaws.savingsplans#ReturnSavingsPlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_savingsplans.types.client_token
    import capo_savingsplans.types.savings_plan_id


class ReturnSavingsPlanRequest(TypedDict, closed=True):
    savings_plan_id: "capo_savingsplans.types.savings_plan_id.SavingsPlanId"
    """<p>The ID of the Savings Plan.</p>"""
    client_token: NotRequired["capo_savingsplans.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReturnSavingsPlanRequest) -> dict:
    out: dict = {}
    out["savingsPlanId"] = value["savings_plan_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ReturnSavingsPlanRequest:
    out: ReturnSavingsPlanRequest = {}  # type: ignore[typeddict-item]
    if data.get("savingsPlanId") is not None:
        out["savings_plan_id"] = data["savingsPlanId"]
    else:
        out["savings_plan_id"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out

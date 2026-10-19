"""Generated from Smithy shape ``com.amazonaws.costexplorer#StartCostAllocationTagBackfillRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.zoned_date_time


class StartCostAllocationTagBackfillRequest(TypedDict, closed=True):
    backfill_from: "capo_cost_explorer.types.zoned_date_time.ZonedDateTime"
    """<p> The date you want the backfill to start from. The date can only be a first day of the month (a billing start date). Dates can't precede the previous twelve months, or in the future.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCostAllocationTagBackfillRequest) -> dict:
    out: dict = {}
    out["BackfillFrom"] = value["backfill_from"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCostAllocationTagBackfillRequest:
    out: StartCostAllocationTagBackfillRequest = {}  # type: ignore[typeddict-item]
    if data.get("BackfillFrom") is not None:
        out["backfill_from"] = data["BackfillFrom"]
    else:
        out["backfill_from"] = ""
    return out

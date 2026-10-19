"""Generated from Smithy shape ``com.amazonaws.drs#ListRecoveryPlansResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.pagination_token
    import capo_drs.types.recovery_plan_summary_list


class ListRecoveryPlansResponse(TypedDict, closed=True):
    recovery_plans: "capo_drs.types.recovery_plan_summary_list.RecoveryPlanSummaryList"
    """<p>The list of Recovery Plans.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecoveryPlansResponse) -> dict:
    out: dict = {}
    import capo_drs.types.recovery_plan_summary_list

    out["recoveryPlans"] = capo_drs.types.recovery_plan_summary_list.serialize_json(
        value["recovery_plans"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecoveryPlansResponse:
    out: ListRecoveryPlansResponse = {}  # type: ignore[typeddict-item]
    if data.get("recoveryPlans") is not None:
        import capo_drs.types.recovery_plan_summary_list

        out["recovery_plans"] = (
            capo_drs.types.recovery_plan_summary_list.deserialize_json(
                data["recoveryPlans"]
            )
        )
    else:
        out["recovery_plans"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

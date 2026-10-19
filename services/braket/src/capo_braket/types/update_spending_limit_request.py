"""Generated from Smithy shape ``com.amazonaws.braket#UpdateSpendingLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_braket.types.spending_limit_arn
    import capo_braket.types.string64
    import capo_braket.types.time_period


class UpdateSpendingLimitRequest(TypedDict, closed=True):
    spending_limit_arn: "capo_braket.types.spending_limit_arn.SpendingLimitArn"
    """<p>The Amazon Resource Name (ARN) of the spending limit to update.</p>"""
    client_token: "capo_braket.types.string64.String64"
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Braket ignores the request, but does not return an error.</p>"""
    spending_limit: NotRequired["str"]
    """<p>The new maximum amount that can be spent on the specified device, in USD.</p>"""
    time_period: NotRequired["capo_braket.types.time_period.TimePeriod"]
    """<p>The new time period during which the spending limit is active, including start and end dates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSpendingLimitRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    if "spending_limit" in value:
        out["spendingLimit"] = value["spending_limit"]
    if "time_period" in value:
        import capo_braket.types.time_period

        out["timePeriod"] = capo_braket.types.time_period.serialize_json(
            value["time_period"]
        )
    return out


def deserialize_json(data: dict) -> UpdateSpendingLimitRequest:
    out: UpdateSpendingLimitRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("spendingLimit") is not None:
        out["spending_limit"] = data["spendingLimit"]
    if data.get("timePeriod") is not None:
        import capo_braket.types.time_period

        out["time_period"] = capo_braket.types.time_period.deserialize_json(
            data["timePeriod"]
        )
    return out

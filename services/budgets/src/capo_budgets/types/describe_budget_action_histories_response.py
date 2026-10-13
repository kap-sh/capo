"""Generated from Smithy shape ``com.amazonaws.budgets#DescribeBudgetActionHistoriesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_budgets.errors import DeserializationError

if TYPE_CHECKING:
    import capo_budgets.types.action_histories
    import capo_budgets.types.generic_string


class DescribeBudgetActionHistoriesResponse(TypedDict, closed=True):
    action_histories: "capo_budgets.types.action_histories.ActionHistories"
    """<p> The historical record of the budget action resource. </p>"""
    next_token: NotRequired["capo_budgets.types.generic_string.GenericString"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBudgetActionHistoriesResponse) -> dict:
    out: dict = {}
    import capo_budgets.types.action_histories

    out["ActionHistories"] = capo_budgets.types.action_histories.serialize_aws_json_1_1(
        value["action_histories"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBudgetActionHistoriesResponse:
    out: DescribeBudgetActionHistoriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ActionHistories") is not None:
        import capo_budgets.types.action_histories

        out["action_histories"] = (
            capo_budgets.types.action_histories.deserialize_aws_json_1_1(
                data["ActionHistories"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeBudgetActionHistoriesResponse.action_histories required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: DescribeBudgetActionHistoriesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "action_histories" in value:
        import capo_budgets.types.action_histories

        out["action_histories"] = capo_budgets.types.action_histories.redact_sensitive(
            value["action_histories"]
        )
    return out

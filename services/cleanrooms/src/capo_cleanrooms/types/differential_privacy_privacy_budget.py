"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacyPrivacyBudget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.differential_privacy_privacy_budget_aggregation_list
    import capo_cleanrooms.types.epsilon


class DifferentialPrivacyPrivacyBudget(TypedDict, closed=True):
    aggregations: "capo_cleanrooms.types.differential_privacy_privacy_budget_aggregation_list.DifferentialPrivacyPrivacyBudgetAggregationList"
    """<p>This information includes the configured epsilon value and the utility in terms of total aggregations, as well as the remaining aggregations.</p>"""
    epsilon: "capo_cleanrooms.types.epsilon.Epsilon"
    """<p>The epsilon value that you configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DifferentialPrivacyPrivacyBudget) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.differential_privacy_privacy_budget_aggregation_list

    out["aggregations"] = (
        capo_cleanrooms.types.differential_privacy_privacy_budget_aggregation_list.serialize_json(
            value["aggregations"]
        )
    )
    out["epsilon"] = value["epsilon"]
    return out


def deserialize_json(data: dict) -> DifferentialPrivacyPrivacyBudget:
    out: DifferentialPrivacyPrivacyBudget = {}  # type: ignore[typeddict-item]
    if data.get("aggregations") is not None:
        import capo_cleanrooms.types.differential_privacy_privacy_budget_aggregation_list

        out["aggregations"] = (
            capo_cleanrooms.types.differential_privacy_privacy_budget_aggregation_list.deserialize_json(
                data["aggregations"]
            )
        )
    else:
        out["aggregations"] = []
    if data.get("epsilon") is not None:
        out["epsilon"] = data["epsilon"]
    else:
        out["epsilon"] = 0
    return out

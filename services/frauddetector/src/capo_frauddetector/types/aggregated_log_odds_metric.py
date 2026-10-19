"""Generated from Smithy shape ``com.amazonaws.frauddetector#AggregatedLogOddsMetric``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.float
    import capo_frauddetector.types.list_of_strings


class AggregatedLogOddsMetric(TypedDict, closed=True):
    variable_names: "capo_frauddetector.types.list_of_strings.ListOfStrings"
    """<p> The names of all the variables. </p>"""
    aggregated_variables_importance: "capo_frauddetector.types.float.float"
    """<p> The relative importance of the variables in the list to the other event variable. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AggregatedLogOddsMetric) -> dict:
    out: dict = {}
    import capo_frauddetector.types.list_of_strings

    out["variableNames"] = (
        capo_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
            value["variable_names"]
        )
    )
    out["aggregatedVariablesImportance"] = (
        "NaN"
        if value["aggregated_variables_importance"]
        != value["aggregated_variables_importance"]
        else "Infinity"
        if value["aggregated_variables_importance"] == float("inf")
        else "-Infinity"
        if value["aggregated_variables_importance"] == float("-inf")
        else value["aggregated_variables_importance"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AggregatedLogOddsMetric:
    out: AggregatedLogOddsMetric = {}  # type: ignore[typeddict-item]
    if data.get("variableNames") is not None:
        import capo_frauddetector.types.list_of_strings

        out["variable_names"] = (
            capo_frauddetector.types.list_of_strings.deserialize_aws_json_1_1(
                data["variableNames"]
            )
        )
    else:
        out["variable_names"] = []
    if data.get("aggregatedVariablesImportance") is not None:
        out["aggregated_variables_importance"] = float(
            data["aggregatedVariablesImportance"]
        )
    else:
        out["aggregated_variables_importance"] = 0.0
    return out

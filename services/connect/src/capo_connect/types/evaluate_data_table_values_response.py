"""Generated from Smithy shape ``com.amazonaws.connect#EvaluateDataTableValuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.data_table_evaluated_value_list
    import capo_connect.types.next_token


class EvaluateDataTableValuesResponse(TypedDict, closed=True):
    values: (
        "capo_connect.types.data_table_evaluated_value_list.DataTableEvaluatedValueList"
    )
    """<p>A list of evaluated values with their computed results, error information, and metadata.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluateDataTableValuesResponse) -> dict:
    out: dict = {}
    import capo_connect.types.data_table_evaluated_value_list

    out["Values"] = capo_connect.types.data_table_evaluated_value_list.serialize_json(
        value["values"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> EvaluateDataTableValuesResponse:
    out: EvaluateDataTableValuesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Values") is not None:
        import capo_connect.types.data_table_evaluated_value_list

        out["values"] = (
            capo_connect.types.data_table_evaluated_value_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out

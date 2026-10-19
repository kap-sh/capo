"""Generated from Smithy shape ``com.amazonaws.connect#ListDataTablePrimaryValuesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.next_token
    import capo_connect.types.primary_values_list


class ListDataTablePrimaryValuesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    primary_values_list: "capo_connect.types.primary_values_list.PrimaryValuesList"
    """<p>A list of primary value combinations with their record IDs and modification metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataTablePrimaryValuesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_connect.types.primary_values_list

    out["PrimaryValuesList"] = capo_connect.types.primary_values_list.serialize_json(
        value["primary_values_list"]
    )
    return out


def deserialize_json(data: dict) -> ListDataTablePrimaryValuesResponse:
    out: ListDataTablePrimaryValuesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("PrimaryValuesList") is not None:
        import capo_connect.types.primary_values_list

        out["primary_values_list"] = (
            capo_connect.types.primary_values_list.deserialize_json(
                data["PrimaryValuesList"]
            )
        )
    else:
        out["primary_values_list"] = []
    return out

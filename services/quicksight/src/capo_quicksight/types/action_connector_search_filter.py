"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionConnectorSearchFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.action_connector_search_filter_name_enum
    import capo_quicksight.types.filter_operator


class ActionConnectorSearchFilter(TypedDict, closed=True):
    name: "capo_quicksight.types.action_connector_search_filter_name_enum.ActionConnectorSearchFilterNameEnum"
    """<p>The name of the filter attribute (e.g., ACTION_CONNECTOR_NAME, ACTION_CONNECTOR_TYPE, QUICKSIGHT_VIEWER_OR_OWNER).</p>"""
    operator: "capo_quicksight.types.filter_operator.FilterOperator"
    """<p>The comparison operator to use for the filter (e.g., StringEquals, StringLike).</p>"""
    value: "str"
    """<p>The value to compare against using the specified operator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionConnectorSearchFilter) -> dict:
    out: dict = {}
    import capo_quicksight.types.action_connector_search_filter_name_enum

    out["Name"] = (
        capo_quicksight.types.action_connector_search_filter_name_enum.serialize_json(
            value["name"]
        )
    )
    import capo_quicksight.types.filter_operator

    out["Operator"] = capo_quicksight.types.filter_operator.serialize_json(
        value["operator"]
    )
    out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> ActionConnectorSearchFilter:
    out: ActionConnectorSearchFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_quicksight.types.action_connector_search_filter_name_enum

        out["name"] = (
            capo_quicksight.types.action_connector_search_filter_name_enum.deserialize_json(
                data["Name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_quicksight.types.action_connector_search_filter_name_enum.ActionConnectorSearchFilterNameEnum",
            "",
        )
    if data.get("Operator") is not None:
        import capo_quicksight.types.filter_operator

        out["operator"] = capo_quicksight.types.filter_operator.deserialize_json(
            data["Operator"]
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_quicksight.types.filter_operator.FilterOperator", ""
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.quicksight#VisualCustomActionOperation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.custom_action_filter_operation
    import capo_quicksight.types.custom_action_navigation_operation
    import capo_quicksight.types.custom_action_set_parameters_operation
    import capo_quicksight.types.custom_action_url_operation


class VisualCustomActionOperation(TypedDict, closed=True):
    filter_operation: NotRequired[
        "capo_quicksight.types.custom_action_filter_operation.CustomActionFilterOperation"
    ]
    """<p>The filter operation that filters data included in a visual or in an entire sheet.</p>"""
    navigation_operation: NotRequired[
        "capo_quicksight.types.custom_action_navigation_operation.CustomActionNavigationOperation"
    ]
    """<p>The navigation operation that navigates between different sheets in the same analysis.</p>"""
    url_operation: NotRequired[
        "capo_quicksight.types.custom_action_url_operation.CustomActionURLOperation"
    ]
    """<p>The URL operation that opens a link to another webpage.</p>"""
    set_parameters_operation: NotRequired[
        "capo_quicksight.types.custom_action_set_parameters_operation.CustomActionSetParametersOperation"
    ]
    """<p>The set parameter operation that sets parameters in custom action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VisualCustomActionOperation) -> dict:
    out: dict = {}
    if "filter_operation" in value:
        import capo_quicksight.types.custom_action_filter_operation

        out["FilterOperation"] = (
            capo_quicksight.types.custom_action_filter_operation.serialize_json(
                value["filter_operation"]
            )
        )
    if "navigation_operation" in value:
        import capo_quicksight.types.custom_action_navigation_operation

        out["NavigationOperation"] = (
            capo_quicksight.types.custom_action_navigation_operation.serialize_json(
                value["navigation_operation"]
            )
        )
    if "url_operation" in value:
        import capo_quicksight.types.custom_action_url_operation

        out["URLOperation"] = (
            capo_quicksight.types.custom_action_url_operation.serialize_json(
                value["url_operation"]
            )
        )
    if "set_parameters_operation" in value:
        import capo_quicksight.types.custom_action_set_parameters_operation

        out["SetParametersOperation"] = (
            capo_quicksight.types.custom_action_set_parameters_operation.serialize_json(
                value["set_parameters_operation"]
            )
        )
    return out


def deserialize_json(data: dict) -> VisualCustomActionOperation:
    out: VisualCustomActionOperation = {}  # type: ignore[typeddict-item]
    if data.get("FilterOperation") is not None:
        import capo_quicksight.types.custom_action_filter_operation

        out["filter_operation"] = (
            capo_quicksight.types.custom_action_filter_operation.deserialize_json(
                data["FilterOperation"]
            )
        )
    if data.get("NavigationOperation") is not None:
        import capo_quicksight.types.custom_action_navigation_operation

        out["navigation_operation"] = (
            capo_quicksight.types.custom_action_navigation_operation.deserialize_json(
                data["NavigationOperation"]
            )
        )
    if data.get("URLOperation") is not None:
        import capo_quicksight.types.custom_action_url_operation

        out["url_operation"] = (
            capo_quicksight.types.custom_action_url_operation.deserialize_json(
                data["URLOperation"]
            )
        )
    if data.get("SetParametersOperation") is not None:
        import capo_quicksight.types.custom_action_set_parameters_operation

        out["set_parameters_operation"] = (
            capo_quicksight.types.custom_action_set_parameters_operation.deserialize_json(
                data["SetParametersOperation"]
            )
        )
    return out


def redact_sensitive(value: VisualCustomActionOperation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "set_parameters_operation" in value:
        import capo_quicksight.types.custom_action_set_parameters_operation

        out["set_parameters_operation"] = (
            capo_quicksight.types.custom_action_set_parameters_operation.redact_sensitive(
                value["set_parameters_operation"]
            )
        )
    return out

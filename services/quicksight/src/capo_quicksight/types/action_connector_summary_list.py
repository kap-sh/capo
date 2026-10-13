"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionConnectorSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.action_connector_summary

ActionConnectorSummaryList: TypeAlias = list[
    "capo_quicksight.types.action_connector_summary.ActionConnectorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionConnectorSummaryList) -> list:
    import capo_quicksight.types.action_connector_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.action_connector_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionConnectorSummaryList:
    import capo_quicksight.types.action_connector_summary

    out: ActionConnectorSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.action_connector_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: ActionConnectorSummaryList) -> list[Any]:
    import capo_quicksight.types.action_connector_summary

    return [
        capo_quicksight.types.action_connector_summary.redact_sensitive(item)
        for item in value
    ]

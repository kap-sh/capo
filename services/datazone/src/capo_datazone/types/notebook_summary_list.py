"""Generated from Smithy shape ``com.amazonaws.datazone#NotebookSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.notebook_summary

NotebookSummaryList: TypeAlias = list[
    "capo_datazone.types.notebook_summary.NotebookSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotebookSummaryList) -> list:
    import capo_datazone.types.notebook_summary

    out: list = []
    for item in value:
        out.append(capo_datazone.types.notebook_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> NotebookSummaryList:
    import capo_datazone.types.notebook_summary

    out: NotebookSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.notebook_summary.deserialize_json(item))
    return out


def redact_sensitive(value: NotebookSummaryList) -> list[Any]:
    import capo_datazone.types.notebook_summary

    return [
        capo_datazone.types.notebook_summary.redact_sensitive(item) for item in value
    ]

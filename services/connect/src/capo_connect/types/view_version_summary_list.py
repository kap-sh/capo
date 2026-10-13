"""Generated from Smithy shape ``com.amazonaws.connect#ViewVersionSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.view_version_summary

ViewVersionSummaryList: TypeAlias = list[
    "capo_connect.types.view_version_summary.ViewVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ViewVersionSummaryList) -> list:
    import capo_connect.types.view_version_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.view_version_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ViewVersionSummaryList:
    import capo_connect.types.view_version_summary

    out: ViewVersionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.view_version_summary.deserialize_json(item))
    return out


def redact_sensitive(value: ViewVersionSummaryList) -> list[Any]:
    import capo_connect.types.view_version_summary

    return [
        capo_connect.types.view_version_summary.redact_sensitive(item) for item in value
    ]

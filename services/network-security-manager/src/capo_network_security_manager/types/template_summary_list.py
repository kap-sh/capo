"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#TemplateSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.template_summary

TemplateSummaryList: TypeAlias = list[
    "capo_network_security_manager.types.template_summary.TemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TemplateSummaryList) -> list:
    import capo_network_security_manager.types.template_summary

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.template_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TemplateSummaryList:
    import capo_network_security_manager.types.template_summary

    out: TemplateSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.template_summary.deserialize_json(item)
        )
    return out

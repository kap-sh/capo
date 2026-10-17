"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowAliasSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_alias_summary

ContactFlowAliasSummaryList: TypeAlias = list[
    "capo_connect.types.contact_flow_alias_summary.ContactFlowAliasSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowAliasSummaryList) -> list:
    import capo_connect.types.contact_flow_alias_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.contact_flow_alias_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactFlowAliasSummaryList:
    import capo_connect.types.contact_flow_alias_summary

    out: ContactFlowAliasSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.contact_flow_alias_summary.deserialize_json(item))
    return out

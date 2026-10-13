"""Generated from Smithy shape ``com.amazonaws.proton#ComponentSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_proton.types.component_summary

ComponentSummaryList: TypeAlias = list[
    "capo_proton.types.component_summary.ComponentSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ComponentSummaryList) -> list:
    import capo_proton.types.component_summary

    out: list = []
    for item in value:
        out.append(capo_proton.types.component_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ComponentSummaryList:
    import capo_proton.types.component_summary

    out: ComponentSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_proton.types.component_summary.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: ComponentSummaryList) -> list[Any]:
    import capo_proton.types.component_summary

    return [
        capo_proton.types.component_summary.redact_sensitive(item) for item in value
    ]

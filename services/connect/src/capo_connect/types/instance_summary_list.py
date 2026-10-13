"""Generated from Smithy shape ``com.amazonaws.connect#InstanceSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.instance_summary

InstanceSummaryList: TypeAlias = list[
    "capo_connect.types.instance_summary.InstanceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceSummaryList) -> list:
    import capo_connect.types.instance_summary

    out: list = []
    for item in value:
        out.append(capo_connect.types.instance_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> InstanceSummaryList:
    import capo_connect.types.instance_summary

    out: InstanceSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connect.types.instance_summary.deserialize_json(item))
    return out


def redact_sensitive(value: InstanceSummaryList) -> list[Any]:
    import capo_connect.types.instance_summary

    return [
        capo_connect.types.instance_summary.redact_sensitive(item) for item in value
    ]

"""Generated from Smithy shape ``com.amazonaws.dsql#MetricGroupRequestList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dsql.types.metric_group_request

MetricGroupRequestList: TypeAlias = list[
    "capo_dsql.types.metric_group_request.MetricGroupRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricGroupRequestList) -> list:
    import capo_dsql.types.metric_group_request

    out: list = []
    for item in value:
        out.append(capo_dsql.types.metric_group_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricGroupRequestList:
    import capo_dsql.types.metric_group_request

    out: MetricGroupRequestList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_dsql.types.metric_group_request.deserialize_json(item))
    return out

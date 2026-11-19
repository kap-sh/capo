"""Generated from Smithy shape ``com.amazonaws.dsql#MetricGroupResponseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dsql.types.metric_group_response

MetricGroupResponseList: TypeAlias = list[
    "capo_dsql.types.metric_group_response.MetricGroupResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: MetricGroupResponseList) -> list:
    import capo_dsql.types.metric_group_response

    out: list = []
    for item in value:
        out.append(capo_dsql.types.metric_group_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> MetricGroupResponseList:
    import capo_dsql.types.metric_group_response

    out: MetricGroupResponseList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_dsql.types.metric_group_response.deserialize_json(item))
    return out

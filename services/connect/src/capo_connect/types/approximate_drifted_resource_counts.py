"""Generated from Smithy shape ``com.amazonaws.connect#ApproximateDriftedResourceCounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.approximate_drifted_resource_count

ApproximateDriftedResourceCounts: TypeAlias = list[
    "capo_connect.types.approximate_drifted_resource_count.ApproximateDriftedResourceCount"
]


# --- restJson1 ser/de ---
def serialize_json(value: ApproximateDriftedResourceCounts) -> list:
    import capo_connect.types.approximate_drifted_resource_count

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.approximate_drifted_resource_count.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ApproximateDriftedResourceCounts:
    import capo_connect.types.approximate_drifted_resource_count

    out: ApproximateDriftedResourceCounts = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connect.types.approximate_drifted_resource_count.deserialize_json(item)
        )
    return out

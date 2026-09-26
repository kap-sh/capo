"""Generated from Smithy shape ``com.amazonaws.lambdacore#AssociatedComputeResourceTypesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lambda_core.types.compute_resource_type

AssociatedComputeResourceTypesList: TypeAlias = list[
    "capo_lambda_core.types.compute_resource_type.ComputeResourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedComputeResourceTypesList) -> list:
    import capo_lambda_core.types.compute_resource_type

    out: list = []
    for item in value:
        out.append(capo_lambda_core.types.compute_resource_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedComputeResourceTypesList:
    import capo_lambda_core.types.compute_resource_type

    out: AssociatedComputeResourceTypesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lambda_core.types.compute_resource_type.deserialize_json(item))
    return out

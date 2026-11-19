"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EffectivePreferredResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer.types.effective_preferred_resource

EffectivePreferredResources: TypeAlias = list[
    "capo_compute_optimizer.types.effective_preferred_resource.EffectivePreferredResource"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EffectivePreferredResources) -> list:
    import capo_compute_optimizer.types.effective_preferred_resource

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.effective_preferred_resource.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EffectivePreferredResources:
    import capo_compute_optimizer.types.effective_preferred_resource

    out: EffectivePreferredResources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.effective_preferred_resource.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EffectivePreferredResources) -> list:
    import capo_compute_optimizer.types.effective_preferred_resource

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer.types.effective_preferred_resource.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> EffectivePreferredResources:
    import capo_compute_optimizer.types.effective_preferred_resource

    out: EffectivePreferredResources = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_compute_optimizer.types.effective_preferred_resource.deserialize_cbor(
                item
            )
        )
    return out

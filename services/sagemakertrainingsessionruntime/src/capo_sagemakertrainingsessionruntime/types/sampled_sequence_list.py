"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#SampledSequenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemakertrainingsessionruntime.types.sampled_sequence

SampledSequenceList: TypeAlias = list[
    "capo_sagemakertrainingsessionruntime.types.sampled_sequence.SampledSequence"
]


# --- restJson1 ser/de ---
def serialize_json(value: SampledSequenceList) -> list:
    import capo_sagemakertrainingsessionruntime.types.sampled_sequence

    out: list = []
    for item in value:
        out.append(
            capo_sagemakertrainingsessionruntime.types.sampled_sequence.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SampledSequenceList:
    import capo_sagemakertrainingsessionruntime.types.sampled_sequence

    out: SampledSequenceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_sagemakertrainingsessionruntime.types.sampled_sequence.deserialize_json(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.kms#EncapsulationAlgorithmSpecList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kms.types.encapsulation_algorithm_spec

EncapsulationAlgorithmSpecList: TypeAlias = list[
    "capo_kms.types.encapsulation_algorithm_spec.EncapsulationAlgorithmSpec"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EncapsulationAlgorithmSpecList) -> list:
    import capo_kms.types.encapsulation_algorithm_spec

    out: list = []
    for item in value:
        out.append(
            capo_kms.types.encapsulation_algorithm_spec.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EncapsulationAlgorithmSpecList:
    import capo_kms.types.encapsulation_algorithm_spec

    out: EncapsulationAlgorithmSpecList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kms.types.encapsulation_algorithm_spec.deserialize_aws_json_1_1(item)
        )
    return out

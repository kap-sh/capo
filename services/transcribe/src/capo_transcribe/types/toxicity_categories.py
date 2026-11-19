"""Generated from Smithy shape ``com.amazonaws.transcribe#ToxicityCategories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe.types.toxicity_category

ToxicityCategories: TypeAlias = list[
    "capo_transcribe.types.toxicity_category.ToxicityCategory"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ToxicityCategories) -> list:
    import capo_transcribe.types.toxicity_category

    out: list = []
    for item in value:
        out.append(capo_transcribe.types.toxicity_category.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ToxicityCategories:
    import capo_transcribe.types.toxicity_category

    out: ToxicityCategories = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_transcribe.types.toxicity_category.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ToxicityCategories) -> list:
    import capo_transcribe.types.toxicity_category

    out: list = []
    for item in value:
        out.append(capo_transcribe.types.toxicity_category.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ToxicityCategories:
    import capo_transcribe.types.toxicity_category

    out: ToxicityCategories = []
    for item in data:
        if item is None:
            continue
        out.append(capo_transcribe.types.toxicity_category.deserialize_cbor(item))
    return out

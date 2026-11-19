"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerAugmentedManifestsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.augmented_manifests_list_item

EntityRecognizerAugmentedManifestsList: TypeAlias = list[
    "capo_comprehend.types.augmented_manifests_list_item.AugmentedManifestsListItem"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerAugmentedManifestsList) -> list:
    import capo_comprehend.types.augmented_manifests_list_item

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.augmented_manifests_list_item.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EntityRecognizerAugmentedManifestsList:
    import capo_comprehend.types.augmented_manifests_list_item

    out: EntityRecognizerAugmentedManifestsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.augmented_manifests_list_item.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntityRecognizerAugmentedManifestsList) -> list:
    import capo_comprehend.types.augmented_manifests_list_item

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.augmented_manifests_list_item.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> EntityRecognizerAugmentedManifestsList:
    import capo_comprehend.types.augmented_manifests_list_item

    out: EntityRecognizerAugmentedManifestsList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.augmented_manifests_list_item.deserialize_cbor(item)
        )
    return out

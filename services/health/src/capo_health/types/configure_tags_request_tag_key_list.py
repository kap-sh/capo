"""Generated from Smithy shape ``com.amazonaws.health#ConfigureTagsRequestTagKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_health.types.configure_tags_tag_key

ConfigureTagsRequestTagKeyList: TypeAlias = list[
    "capo_health.types.configure_tags_tag_key.ConfigureTagsTagKey"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigureTagsRequestTagKeyList) -> list:
    import capo_health.types.configure_tags_tag_key

    out: list = []
    for item in value:
        out.append(
            capo_health.types.configure_tags_tag_key.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigureTagsRequestTagKeyList:
    import capo_health.types.configure_tags_tag_key

    out: ConfigureTagsRequestTagKeyList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_health.types.configure_tags_tag_key.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConfigureTagsRequestTagKeyList) -> list:
    import capo_health.types.configure_tags_tag_key

    out: list = []
    for item in value:
        out.append(capo_health.types.configure_tags_tag_key.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ConfigureTagsRequestTagKeyList:
    import capo_health.types.configure_tags_tag_key

    out: ConfigureTagsRequestTagKeyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_health.types.configure_tags_tag_key.deserialize_cbor(item))
    return out

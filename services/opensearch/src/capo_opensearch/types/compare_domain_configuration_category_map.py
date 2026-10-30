"""Generated from Smithy shape ``com.amazonaws.opensearch#CompareDomainConfigurationCategoryMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.category_diff_result
    import capo_opensearch.types.metadata_category

CompareDomainConfigurationCategoryMap: TypeAlias = dict[
    "capo_opensearch.types.metadata_category.MetadataCategory",
    "capo_opensearch.types.category_diff_result.CategoryDiffResult",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CompareDomainConfigurationCategoryMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_opensearch.types.category_diff_result

        out[key] = capo_opensearch.types.category_diff_result.serialize_json(value)
    return out


def deserialize_json(data: dict) -> CompareDomainConfigurationCategoryMap:
    out: CompareDomainConfigurationCategoryMap = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_opensearch.types.category_diff_result

        out[key] = capo_opensearch.types.category_diff_result.deserialize_json(value)
    return out

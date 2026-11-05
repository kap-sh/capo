"""Generated from Smithy shape ``com.amazonaws.s3tables#FindingCategoryCounts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_s3tables.types.finding_category

FindingCategoryCounts: TypeAlias = dict[
    "capo_s3tables.types.finding_category.FindingCategory", "int"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FindingCategoryCounts) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_s3tables.types.finding_category

        out[capo_s3tables.types.finding_category.serialize_json(key)] = value
    return out


def deserialize_json(data: dict) -> FindingCategoryCounts:
    out: FindingCategoryCounts = {}
    for key, value in data.items():
        import capo_s3tables.types.finding_category

        if value is None:
            continue
        out[capo_s3tables.types.finding_category.deserialize_json(key)] = value
    return out

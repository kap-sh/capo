"""Generated from Smithy shape ``com.amazonaws.ecr#ImageTagMutabilityExclusionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_tag_mutability_exclusion_filter_type
    import capo_ecr.types.image_tag_mutability_exclusion_filter_value


class ImageTagMutabilityExclusionFilter(TypedDict, closed=True):
    filter_type: "capo_ecr.types.image_tag_mutability_exclusion_filter_type.ImageTagMutabilityExclusionFilterType"
    """<p>The type of filter to apply for excluding image tags from mutability settings.</p>"""
    filter: "capo_ecr.types.image_tag_mutability_exclusion_filter_value.ImageTagMutabilityExclusionFilterValue"
    """<p>The filter value used to match image tags for exclusion from mutability settings.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageTagMutabilityExclusionFilter) -> dict:
    out: dict = {}
    import capo_ecr.types.image_tag_mutability_exclusion_filter_type

    out["filterType"] = (
        capo_ecr.types.image_tag_mutability_exclusion_filter_type.serialize_aws_json_1_1(
            value["filter_type"]
        )
    )
    out["filter"] = value["filter"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageTagMutabilityExclusionFilter:
    out: ImageTagMutabilityExclusionFilter = {}  # type: ignore[typeddict-item]
    if data.get("filterType") is not None:
        import capo_ecr.types.image_tag_mutability_exclusion_filter_type

        out["filter_type"] = (
            capo_ecr.types.image_tag_mutability_exclusion_filter_type.deserialize_aws_json_1_1(
                data["filterType"]
            )
        )
    else:
        import typing

        out["filter_type"] = typing.cast(
            "capo_ecr.types.image_tag_mutability_exclusion_filter_type.ImageTagMutabilityExclusionFilterType",
            "",
        )
    if data.get("filter") is not None:
        out["filter"] = data["filter"]
    else:
        out["filter"] = ""
    return out

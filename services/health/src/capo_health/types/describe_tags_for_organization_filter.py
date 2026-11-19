"""Generated from Smithy shape ``com.amazonaws.health#DescribeTagsForOrganizationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.organization_tag_type_filter


class DescribeTagsForOrganizationFilter(TypedDict, closed=True):
    tag_types: NotRequired[
        "capo_health.types.organization_tag_type_filter.OrganizationTagTypeFilter"
    ]
    """<p>The types of tags to include in the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTagsForOrganizationFilter) -> dict:
    out: dict = {}
    if "tag_types" in value:
        import capo_health.types.organization_tag_type_filter

        out["tagTypes"] = (
            capo_health.types.organization_tag_type_filter.serialize_aws_json_1_1(
                value["tag_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTagsForOrganizationFilter:
    out: DescribeTagsForOrganizationFilter = {}  # type: ignore[typeddict-item]
    if data.get("tagTypes") is not None:
        import capo_health.types.organization_tag_type_filter

        out["tag_types"] = (
            capo_health.types.organization_tag_type_filter.deserialize_aws_json_1_1(
                data["tagTypes"]
            )
        )
    return out

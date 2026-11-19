"""Generated from Smithy shape ``com.amazonaws.health#DescribeTagsOnboardingStatusForOrganizationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.tags_onboarding_status_for_organization


class DescribeTagsOnboardingStatusForOrganizationResponse(TypedDict, closed=True):
    status: NotRequired[
        "capo_health.types.tags_onboarding_status_for_organization.TagsOnboardingStatusForOrganization"
    ]
    """<p>The current onboarding status of the tags feature for the organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeTagsOnboardingStatusForOrganizationResponse,
) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_health.types.tags_onboarding_status_for_organization

        out["status"] = (
            capo_health.types.tags_onboarding_status_for_organization.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeTagsOnboardingStatusForOrganizationResponse:
    out: DescribeTagsOnboardingStatusForOrganizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_health.types.tags_onboarding_status_for_organization

        out["status"] = (
            capo_health.types.tags_onboarding_status_for_organization.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out

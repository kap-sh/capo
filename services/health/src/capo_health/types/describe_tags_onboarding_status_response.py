"""Generated from Smithy shape ``com.amazonaws.health#DescribeTagsOnboardingStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.tags_onboarding_status


class DescribeTagsOnboardingStatusResponse(TypedDict, closed=True):
    status: NotRequired["capo_health.types.tags_onboarding_status.TagsOnboardingStatus"]
    """<p>The current onboarding status of the tags feature for the account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTagsOnboardingStatusResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_health.types.tags_onboarding_status

        out["status"] = capo_health.types.tags_onboarding_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTagsOnboardingStatusResponse:
    out: DescribeTagsOnboardingStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_health.types.tags_onboarding_status

        out["status"] = (
            capo_health.types.tags_onboarding_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out

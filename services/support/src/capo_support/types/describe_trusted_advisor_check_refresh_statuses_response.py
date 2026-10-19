"""Generated from Smithy shape ``com.amazonaws.support#DescribeTrustedAdvisorCheckRefreshStatusesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_support.types.trusted_advisor_check_refresh_status_list


class DescribeTrustedAdvisorCheckRefreshStatusesResponse(TypedDict, closed=True):
    statuses: "capo_support.types.trusted_advisor_check_refresh_status_list.TrustedAdvisorCheckRefreshStatusList"
    """<p>The refresh status of the specified Trusted Advisor checks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeTrustedAdvisorCheckRefreshStatusesResponse,
) -> dict:
    out: dict = {}
    import capo_support.types.trusted_advisor_check_refresh_status_list

    out["statuses"] = (
        capo_support.types.trusted_advisor_check_refresh_status_list.serialize_aws_json_1_1(
            value["statuses"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeTrustedAdvisorCheckRefreshStatusesResponse:
    out: DescribeTrustedAdvisorCheckRefreshStatusesResponse = {}  # type: ignore[typeddict-item]
    if data.get("statuses") is not None:
        import capo_support.types.trusted_advisor_check_refresh_status_list

        out["statuses"] = (
            capo_support.types.trusted_advisor_check_refresh_status_list.deserialize_aws_json_1_1(
                data["statuses"]
            )
        )
    else:
        out["statuses"] = []
    return out

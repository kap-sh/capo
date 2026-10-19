"""Generated from Smithy shape ``com.amazonaws.health#DescribeEventDetailsForOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.locale
    import capo_health.types.organization_event_detail_filters_list


class DescribeEventDetailsForOrganizationRequest(TypedDict, closed=True):
    organization_event_detail_filters: "capo_health.types.organization_event_detail_filters_list.OrganizationEventDetailFiltersList"
    """<p>A set of JSON elements that includes the <code>awsAccountId</code> and the <code>eventArn</code>.</p>"""
    locale: NotRequired["capo_health.types.locale.locale"]
    """<p>The locale (language) to return information in. English (en) is the default and the only supported value at this time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventDetailsForOrganizationRequest) -> dict:
    out: dict = {}
    import capo_health.types.organization_event_detail_filters_list

    out["organizationEventDetailFilters"] = (
        capo_health.types.organization_event_detail_filters_list.serialize_aws_json_1_1(
            value["organization_event_detail_filters"]
        )
    )
    if "locale" in value:
        out["locale"] = value["locale"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventDetailsForOrganizationRequest:
    out: DescribeEventDetailsForOrganizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("organizationEventDetailFilters") is not None:
        import capo_health.types.organization_event_detail_filters_list

        out["organization_event_detail_filters"] = (
            capo_health.types.organization_event_detail_filters_list.deserialize_aws_json_1_1(
                data["organizationEventDetailFilters"]
            )
        )
    else:
        out["organization_event_detail_filters"] = []
    if data.get("locale") is not None:
        out["locale"] = data["locale"]
    return out

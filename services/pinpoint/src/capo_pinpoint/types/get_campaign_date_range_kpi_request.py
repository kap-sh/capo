"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetCampaignDateRangeKpiRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.__timestamp_iso8601


class GetCampaignDateRangeKpiRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    campaign_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the campaign.</p>"""
    end_time: NotRequired["capo_pinpoint.types.__timestamp_iso8601.__timestampIso8601"]
    """<p>The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019.</p>"""
    kpi_name: "capo_pinpoint.types.__string.__string"
    """<p>The name of the metric, also referred to as a <i>key performance indicator (KPI)</i>, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the <a href="https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html">Amazon Pinpoint Developer Guide</a>.</p>"""
    next_token: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>"""
    page_size: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.</p>"""
    start_time: NotRequired[
        "capo_pinpoint.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCampaignDateRangeKpiRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCampaignDateRangeKpiRequest:
    out: GetCampaignDateRangeKpiRequest = {}  # type: ignore[typeddict-item]
    return out

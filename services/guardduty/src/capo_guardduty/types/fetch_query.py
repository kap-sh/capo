"""Generated from Smithy shape ``com.amazonaws.guardduty#FetchQuery``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.fetch_criteria
    import capo_guardduty.types.fetch_row_limit
    import capo_guardduty.types.fetch_time_window
    import capo_guardduty.types.finding_id
    import capo_guardduty.types.finding_type
    import capo_guardduty.types.indicator_value
    import capo_guardduty.types.investigation_indicator_type
    import capo_guardduty.types.string


class FetchQuery(TypedDict, closed=True):
    criteria: NotRequired["capo_guardduty.types.fetch_criteria.FetchCriteria"]
    """<p>The filter criteria that GuardDuty applied to the request.</p>"""
    time_window: NotRequired["capo_guardduty.types.fetch_time_window.FetchTimeWindow"]
    """<p>The time range of the data that GuardDuty requested.</p>"""
    row_limit: NotRequired["capo_guardduty.types.fetch_row_limit.FetchRowLimit"]
    """<p>The maximum number of rows that GuardDuty requested. Valid values are 1 to 1,000.</p>"""
    account_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services account ID that the request was made for.</p>"""
    indicator: NotRequired["capo_guardduty.types.indicator_value.IndicatorValue"]
    """<p>The threat indicator that GuardDuty looked up, such as an IP address, a domain, or a file hash.</p>"""
    indicator_type: NotRequired[
        "capo_guardduty.types.investigation_indicator_type.InvestigationIndicatorType"
    ]
    """<p>The type of the threat indicator. Possible values are <code>IP</code>, <code>DOMAIN</code>, and <code>FILE</code>.</p>"""
    finding_type: NotRequired["capo_guardduty.types.finding_type.FindingType"]
    """<p>The finding type whose documentation GuardDuty retrieved.</p>"""
    finding_id: NotRequired["capo_guardduty.types.finding_id.FindingId"]
    """<p>The ID of the finding that GuardDuty retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FetchQuery) -> dict:
    out: dict = {}
    if "criteria" in value:
        import capo_guardduty.types.fetch_criteria

        out["criteria"] = capo_guardduty.types.fetch_criteria.serialize_json(
            value["criteria"]
        )
    if "time_window" in value:
        import capo_guardduty.types.fetch_time_window

        out["timeWindow"] = capo_guardduty.types.fetch_time_window.serialize_json(
            value["time_window"]
        )
    if "row_limit" in value:
        out["rowLimit"] = value["row_limit"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "indicator" in value:
        out["indicator"] = value["indicator"]
    if "indicator_type" in value:
        import capo_guardduty.types.investigation_indicator_type

        out["indicatorType"] = (
            capo_guardduty.types.investigation_indicator_type.serialize_json(
                value["indicator_type"]
            )
        )
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    if "finding_id" in value:
        out["findingId"] = value["finding_id"]
    return out


def deserialize_json(data: dict) -> FetchQuery:
    out: FetchQuery = {}  # type: ignore[typeddict-item]
    if data.get("criteria") is not None:
        import capo_guardduty.types.fetch_criteria

        out["criteria"] = capo_guardduty.types.fetch_criteria.deserialize_json(
            data["criteria"]
        )
    if data.get("timeWindow") is not None:
        import capo_guardduty.types.fetch_time_window

        out["time_window"] = capo_guardduty.types.fetch_time_window.deserialize_json(
            data["timeWindow"]
        )
    if data.get("rowLimit") is not None:
        out["row_limit"] = data["rowLimit"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("indicator") is not None:
        out["indicator"] = data["indicator"]
    if data.get("indicatorType") is not None:
        import capo_guardduty.types.investigation_indicator_type

        out["indicator_type"] = (
            capo_guardduty.types.investigation_indicator_type.deserialize_json(
                data["indicatorType"]
            )
        )
    if data.get("findingType") is not None:
        out["finding_type"] = data["findingType"]
    if data.get("findingId") is not None:
        out["finding_id"] = data["findingId"]
    return out


def redact_sensitive(value: FetchQuery) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "indicator" in value:
        out["indicator"] = "*** Sensitive Data Redacted ***"
    return out

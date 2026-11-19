"""Generated from Smithy shape ``com.amazonaws.guardduty#FetchRecord``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.fetch_query
    import capo_guardduty.types.fetch_result
    import capo_guardduty.types.fetch_type


class FetchRecord(TypedDict, closed=True):
    fetch_type: NotRequired["capo_guardduty.types.fetch_type.FetchType"]
    """<p>The kind of data that GuardDuty retrieved. The value determines which members of <code>Query</code> and <code>Result</code> can be set. Possible values:</p> <ul> <li> <p> <code>FINDINGS</code> – GuardDuty findings.</p> </li> <li> <p> <code>DETECTOR</code> – The configuration of a GuardDuty detector.</p> </li> <li> <p> <code>REPUTATION</code> – Reputation information about a threat indicator, such as an IP address, a domain, or a file hash.</p> </li> <li> <p> <code>FINDING_TYPE_DOCUMENTATION</code> – The documentation for a finding type.</p> </li> <li> <p> <code>CLOUD_TRAIL_RAW_EVENTS</code> – Amazon Web Services CloudTrail events.</p> </li> <li> <p> <code>RUNTIME_SIGNALS</code> – Runtime signals.</p> </li> <li> <p> <code>MEMBER_ACCOUNTS</code> – A list of member accounts.</p> </li> </ul>"""
    query: NotRequired["capo_guardduty.types.fetch_query.FetchQuery"]
    """<p>The request that GuardDuty made. Not every record includes a query.</p>"""
    result: NotRequired["capo_guardduty.types.fetch_result.FetchResult"]
    """<p>The data that GuardDuty received in response to the request. Not every record includes a result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FetchRecord) -> dict:
    out: dict = {}
    if "fetch_type" in value:
        import capo_guardduty.types.fetch_type

        out["fetchType"] = capo_guardduty.types.fetch_type.serialize_json(
            value["fetch_type"]
        )
    if "query" in value:
        import capo_guardduty.types.fetch_query

        out["query"] = capo_guardduty.types.fetch_query.serialize_json(value["query"])
    if "result" in value:
        import capo_guardduty.types.fetch_result

        out["result"] = capo_guardduty.types.fetch_result.serialize_json(
            value["result"]
        )
    return out


def deserialize_json(data: dict) -> FetchRecord:
    out: FetchRecord = {}  # type: ignore[typeddict-item]
    if data.get("fetchType") is not None:
        import capo_guardduty.types.fetch_type

        out["fetch_type"] = capo_guardduty.types.fetch_type.deserialize_json(
            data["fetchType"]
        )
    if data.get("query") is not None:
        import capo_guardduty.types.fetch_query

        out["query"] = capo_guardduty.types.fetch_query.deserialize_json(data["query"])
    if data.get("result") is not None:
        import capo_guardduty.types.fetch_result

        out["result"] = capo_guardduty.types.fetch_result.deserialize_json(
            data["result"]
        )
    return out


def redact_sensitive(value: FetchRecord) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "query" in value:
        import capo_guardduty.types.fetch_query

        out["query"] = capo_guardduty.types.fetch_query.redact_sensitive(value["query"])
    return out

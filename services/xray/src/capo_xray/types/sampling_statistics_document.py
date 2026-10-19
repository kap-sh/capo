"""Generated from Smithy shape ``com.amazonaws.xray#SamplingStatisticsDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_xray.types.borrow_count
    import capo_xray.types.client_id
    import capo_xray.types.request_count
    import capo_xray.types.rule_name
    import capo_xray.types.sampled_count
    import capo_xray.types.timestamp


class SamplingStatisticsDocument(TypedDict, closed=True):
    rule_name: "capo_xray.types.rule_name.RuleName"
    """<p>The name of the sampling rule.</p>"""
    client_id: "capo_xray.types.client_id.ClientID"
    """<p>A unique identifier for the service in hexadecimal.</p>"""
    timestamp: "capo_xray.types.timestamp.Timestamp"
    """<p>The current time.</p>"""
    request_count: "capo_xray.types.request_count.RequestCount"
    """<p>The number of requests that matched the rule.</p>"""
    sampled_count: "capo_xray.types.sampled_count.SampledCount"
    """<p>The number of requests recorded.</p>"""
    borrow_count: "capo_xray.types.borrow_count.BorrowCount"
    """<p>The number of requests recorded with borrowed reservoir quota.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingStatisticsDocument) -> dict:
    out: dict = {}
    out["RuleName"] = value["rule_name"]
    out["ClientID"] = value["client_id"]
    import capo_xray.types.timestamp

    out["Timestamp"] = capo_xray.types.timestamp.serialize_json(value["timestamp"])
    out["RequestCount"] = value.get("request_count", 0)
    out["SampledCount"] = value.get("sampled_count", 0)
    out["BorrowCount"] = value.get("borrow_count", 0)
    return out


def deserialize_json(data: dict) -> SamplingStatisticsDocument:
    out: SamplingStatisticsDocument = {}  # type: ignore[typeddict-item]
    if data.get("RuleName") is not None:
        out["rule_name"] = data["RuleName"]
    else:
        out["rule_name"] = ""
    if data.get("ClientID") is not None:
        out["client_id"] = data["ClientID"]
    else:
        out["client_id"] = ""
    if data.get("Timestamp") is not None:
        import capo_xray.types.timestamp

        out["timestamp"] = capo_xray.types.timestamp.deserialize_json(data["Timestamp"])
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("RequestCount") is not None:
        out["request_count"] = data["RequestCount"]
    else:
        out["request_count"] = 0
    if data.get("SampledCount") is not None:
        out["sampled_count"] = data["SampledCount"]
    else:
        out["sampled_count"] = 0
    if data.get("BorrowCount") is not None:
        out["borrow_count"] = data["BorrowCount"]
    else:
        out["borrow_count"] = 0
    return out

"""Generated from Smithy shape ``com.amazonaws.billing#GetCreditAllocationHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_billing.types.account_id
    import capo_billing.types.page_token


class GetCreditAllocationHistoryRequest(TypedDict, closed=True):
    account_id: "capo_billing.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID whose allocation history to retrieve. Must be a 12-digit numeric string.</p>"""
    credit_id: NotRequired["int"]
    """<p>Filters the result to a single credit. When omitted, returns allocation entries for all credits.</p>"""
    start_date: "datetime.datetime"
    """<p>Inclusive start date as Unix epoch seconds. Must be on or before <code>endDate</code>. The range from <code>startDate</code> to <code>endDate</code> cannot exceed 24 billing months.</p>"""
    end_date: "datetime.datetime"
    """<p>Inclusive end date as Unix epoch seconds.</p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p>Pagination token from a previous response. Pass the value returned in <code>nextToken</code> to retrieve the next page of results.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of records to return per page. Range: 1 to 1000. Default: 100.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCreditAllocationHistoryRequest) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    if "credit_id" in value:
        out["creditId"] = value["credit_id"]
    import capo_billing.types._prelude.timestamp

    out["startDate"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
        value["start_date"]
    )
    import capo_billing.types._prelude.timestamp

    out["endDate"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
        value["end_date"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCreditAllocationHistoryRequest:
    out: GetCreditAllocationHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("creditId") is not None:
        out["credit_id"] = data["creditId"]
    if data.get("startDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["start_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startDate"]
            )
        )
    else:
        import datetime

        out["start_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["end_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["endDate"]
            )
        )
    else:
        import datetime

        out["end_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out

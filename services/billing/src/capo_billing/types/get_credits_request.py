"""Generated from Smithy shape ``com.amazonaws.billing#GetCreditsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class GetCreditsRequest(TypedDict, closed=True):
    account_id: "str"
    """<p>The Amazon Web Services account ID. Must be a 12-digit numeric string.</p>"""
    start_date: "datetime.datetime"
    """<p>The start date for the credit period as Unix epoch seconds. Must be a past date that is not more than one year before the current date.</p>"""
    end_date: NotRequired["datetime.datetime"]
    """<p>The end date for the credit period as Unix epoch seconds. Must not be a future date and must be on or after <code>startDate</code>. Defaults to the current date when omitted.</p>"""
    payer_account_flag: NotRequired["bool"]
    """<p>When <code>true</code> and the caller is the management account, the response aggregates credits across the entire consolidated billing family. When <code>false</code> or omitted, returns only credits for the specified <code>accountId</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCreditsRequest) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import capo_billing.types._prelude.timestamp

    out["startDate"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
        value["start_date"]
    )
    if "end_date" in value:
        import capo_billing.types._prelude.timestamp

        out["endDate"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["end_date"]
        )
    if "payer_account_flag" in value:
        out["payerAccountFlag"] = value["payer_account_flag"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCreditsRequest:
    out: GetCreditsRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
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
    if data.get("payerAccountFlag") is not None:
        out["payer_account_flag"] = data["payerAccountFlag"]
    return out

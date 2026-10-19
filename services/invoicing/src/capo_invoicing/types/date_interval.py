"""Generated from Smithy shape ``com.amazonaws.invoicing#DateInterval``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class DateInterval(TypedDict, closed=True):
    start_date: "datetime.datetime"
    """<p> The beginning of the time period that you want invoice-related documents for. The start date is inclusive. For example, if <code>start</code> is <code>2019-01-01</code>, AWS retrieves invoices starting at <code>2019-01-01</code> up to the end date. </p>"""
    end_date: "datetime.datetime"
    """<p> The end of the time period that you want invoice-related documents for. The end date is exclusive. For example, if <code>end</code> is <code>2019-01-10</code>, Amazon Web Services retrieves invoice-related documents from the start date up to, but not including, <code>2018-01-10</code>. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DateInterval) -> dict:
    out: dict = {}
    import capo_invoicing.types._prelude.timestamp

    out["StartDate"] = capo_invoicing.types._prelude.timestamp.serialize_aws_json_1_0(
        value["start_date"]
    )
    import capo_invoicing.types._prelude.timestamp

    out["EndDate"] = capo_invoicing.types._prelude.timestamp.serialize_aws_json_1_0(
        value["end_date"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DateInterval:
    out: DateInterval = {}  # type: ignore[typeddict-item]
    if data.get("StartDate") is not None:
        import capo_invoicing.types._prelude.timestamp

        out["start_date"] = (
            capo_invoicing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["StartDate"]
            )
        )
    else:
        import datetime

        out["start_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndDate") is not None:
        import capo_invoicing.types._prelude.timestamp

        out["end_date"] = (
            capo_invoicing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["EndDate"]
            )
        )
    else:
        import datetime

        out["end_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out

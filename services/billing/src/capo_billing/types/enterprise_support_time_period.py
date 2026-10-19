"""Generated from Smithy shape ``com.amazonaws.billing#EnterpriseSupportTimePeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class EnterpriseSupportTimePeriod(TypedDict, closed=True):
    begin_date: "datetime.datetime"
    """<p>The begin date of the time period.</p>"""
    end_date: NotRequired["datetime.datetime"]
    """<p>The end date of the time period.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnterpriseSupportTimePeriod) -> dict:
    out: dict = {}
    import capo_billing.types._prelude.timestamp

    out["beginDate"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
        value["begin_date"]
    )
    if "end_date" in value:
        import capo_billing.types._prelude.timestamp

        out["endDate"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["end_date"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EnterpriseSupportTimePeriod:
    out: EnterpriseSupportTimePeriod = {}  # type: ignore[typeddict-item]
    if data.get("beginDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["begin_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["beginDate"]
            )
        )
    else:
        import datetime

        out["begin_date"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("endDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["end_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["endDate"]
            )
        )
    return out

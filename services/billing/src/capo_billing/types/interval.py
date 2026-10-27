"""Generated from Smithy shape ``com.amazonaws.billing#Interval``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class Interval(TypedDict, closed=True):
    start_date_inclusive: "datetime.datetime"
    """<p>The start date of the interval. This date is included in the interval.</p>"""
    end_date_inclusive: "datetime.datetime"
    """<p>The end date of the interval. This date is included in the interval.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Interval) -> dict:
    out: dict = {}
    import capo_billing.types._prelude.timestamp

    out["startDateInclusive"] = (
        capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["start_date_inclusive"]
        )
    )
    import capo_billing.types._prelude.timestamp

    out["endDateInclusive"] = (
        capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["end_date_inclusive"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> Interval:
    out: Interval = {}  # type: ignore[typeddict-item]
    if data.get("startDateInclusive") is not None:
        import capo_billing.types._prelude.timestamp

        out["start_date_inclusive"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startDateInclusive"]
            )
        )
    else:
        import datetime

        out["start_date_inclusive"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("endDateInclusive") is not None:
        import capo_billing.types._prelude.timestamp

        out["end_date_inclusive"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["endDateInclusive"]
            )
        )
    else:
        import datetime

        out["end_date_inclusive"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out

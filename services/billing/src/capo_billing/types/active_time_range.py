"""Generated from Smithy shape ``com.amazonaws.billing#ActiveTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class ActiveTimeRange(TypedDict, closed=True):
    active_after_inclusive: "datetime.datetime"
    """<p>The inclusive time range start date.</p>"""
    active_before_inclusive: "datetime.datetime"
    """<p> The inclusive time range end date. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActiveTimeRange) -> dict:
    out: dict = {}
    import capo_billing.types._prelude.timestamp

    out["activeAfterInclusive"] = (
        capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["active_after_inclusive"]
        )
    )
    import capo_billing.types._prelude.timestamp

    out["activeBeforeInclusive"] = (
        capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["active_before_inclusive"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ActiveTimeRange:
    out: ActiveTimeRange = {}  # type: ignore[typeddict-item]
    if data.get("activeAfterInclusive") is not None:
        import capo_billing.types._prelude.timestamp

        out["active_after_inclusive"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["activeAfterInclusive"]
            )
        )
    else:
        import datetime

        out["active_after_inclusive"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("activeBeforeInclusive") is not None:
        import capo_billing.types._prelude.timestamp

        out["active_before_inclusive"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["activeBeforeInclusive"]
            )
        )
    else:
        import datetime

        out["active_before_inclusive"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out

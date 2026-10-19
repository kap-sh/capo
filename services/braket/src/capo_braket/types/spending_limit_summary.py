"""Generated from Smithy shape ``com.amazonaws.braket#SpendingLimitSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_braket.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_braket.types.device_arn
    import capo_braket.types.spending_limit_arn
    import capo_braket.types.tags_map
    import capo_braket.types.time_period


class SpendingLimitSummary(TypedDict, closed=True):
    spending_limit_arn: "capo_braket.types.spending_limit_arn.SpendingLimitArn"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the spending limit.</p>"""
    device_arn: "capo_braket.types.device_arn.DeviceArn"
    """<p>The Amazon Resource Name (ARN) of the quantum device associated with this spending limit.</p>"""
    time_period: "capo_braket.types.time_period.TimePeriod"
    """<p>The time period during which the spending limit is active.</p>"""
    spending_limit: "str"
    """<p>The maximum spending amount allowed for the device during the specified time period, in USD.</p>"""
    queued_spend: "str"
    """<p>The amount currently queued for spending on the device, in USD.</p>"""
    total_spend: "str"
    """<p>The total amount spent on the device so far during the current time period, in USD.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time when the spending limit was created, in epoch seconds.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time when the spending limit was last modified, in epoch seconds.</p>"""
    tags: NotRequired["capo_braket.types.tags_map.TagsMap"]
    """<p>The tags associated with the spending limit. Each tag consists of a key and an optional value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpendingLimitSummary) -> dict:
    out: dict = {}
    out["spendingLimitArn"] = value["spending_limit_arn"]
    out["deviceArn"] = value["device_arn"]
    import capo_braket.types.time_period

    out["timePeriod"] = capo_braket.types.time_period.serialize_json(
        value["time_period"]
    )
    out["spendingLimit"] = value["spending_limit"]
    out["queuedSpend"] = value["queued_spend"]
    out["totalSpend"] = value["total_spend"]
    import capo_braket._protocol.serialize

    out["createdAt"] = capo_braket._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_braket._protocol.serialize

    out["updatedAt"] = capo_braket._protocol.serialize.fmt_date_time(
        value["updated_at"]
    )
    if "tags" in value:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> SpendingLimitSummary:
    out: SpendingLimitSummary = {}  # type: ignore[typeddict-item]
    if data.get("spendingLimitArn") is not None:
        out["spending_limit_arn"] = data["spendingLimitArn"]
    else:
        out["spending_limit_arn"] = ""
    if data.get("deviceArn") is not None:
        out["device_arn"] = data["deviceArn"]
    else:
        out["device_arn"] = ""
    if data.get("timePeriod") is not None:
        import capo_braket.types.time_period

        out["time_period"] = capo_braket.types.time_period.deserialize_json(
            data["timePeriod"]
        )
    else:
        raise DeserializationError("SpendingLimitSummary.time_period required")
    if data.get("spendingLimit") is not None:
        out["spending_limit"] = data["spendingLimit"]
    else:
        out["spending_limit"] = ""
    if data.get("queuedSpend") is not None:
        out["queued_spend"] = data["queuedSpend"]
    else:
        out["queued_spend"] = ""
    if data.get("totalSpend") is not None:
        out["total_spend"] = data["totalSpend"]
    else:
        out["total_spend"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import datetime

        out["updated_at"] = datetime.datetime.fromisoformat(
            data["updatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("tags") is not None:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.deserialize_json(data["tags"])
    return out

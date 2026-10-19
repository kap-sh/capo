"""Generated from Smithy shape ``com.amazonaws.braket#CreateSpendingLimitRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_braket.types.device_arn
    import capo_braket.types.string64
    import capo_braket.types.tags_map
    import capo_braket.types.time_period


class CreateSpendingLimitRequest(TypedDict, closed=True):
    client_token: "capo_braket.types.string64.String64"
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Braket ignores the request, but does not return an error.</p>"""
    device_arn: "capo_braket.types.device_arn.DeviceArn"
    """<p>The Amazon Resource Name (ARN) of the quantum device to apply the spending limit to.</p>"""
    spending_limit: "str"
    """<p>The maximum amount that can be spent on the specified device, in USD.</p>"""
    time_period: NotRequired["capo_braket.types.time_period.TimePeriod"]
    """<p>The time period during which the spending limit is active, including start and end dates.</p>"""
    tags: NotRequired["capo_braket.types.tags_map.TagsMap"]
    """<p>The tags to apply to the spending limit. Each tag consists of a key and an optional value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSpendingLimitRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["deviceArn"] = value["device_arn"]
    out["spendingLimit"] = value["spending_limit"]
    if "time_period" in value:
        import capo_braket.types.time_period

        out["timePeriod"] = capo_braket.types.time_period.serialize_json(
            value["time_period"]
        )
    if "tags" in value:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSpendingLimitRequest:
    out: CreateSpendingLimitRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    if data.get("deviceArn") is not None:
        out["device_arn"] = data["deviceArn"]
    else:
        out["device_arn"] = ""
    if data.get("spendingLimit") is not None:
        out["spending_limit"] = data["spendingLimit"]
    else:
        out["spending_limit"] = ""
    if data.get("timePeriod") is not None:
        import capo_braket.types.time_period

        out["time_period"] = capo_braket.types.time_period.deserialize_json(
            data["timePeriod"]
        )
    if data.get("tags") is not None:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.deserialize_json(data["tags"])
    return out

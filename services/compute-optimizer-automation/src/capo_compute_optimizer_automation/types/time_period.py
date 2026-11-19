"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#TimePeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class TimePeriod(TypedDict, closed=True):
    start_time_inclusive: NotRequired["datetime.datetime"]
    """<p>The start time of the period, inclusive. Events at or after this time are included.</p>"""
    end_time_exclusive: NotRequired["datetime.datetime"]
    """<p>The end time of the period, exclusive. Events before this time are included.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimePeriod) -> dict:
    out: dict = {}
    if "start_time_inclusive" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["startTimeInclusive"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["start_time_inclusive"]
            )
        )
    if "end_time_exclusive" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["endTimeExclusive"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_aws_json_1_0(
                value["end_time_exclusive"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TimePeriod:
    out: TimePeriod = {}  # type: ignore[typeddict-item]
    if data.get("startTimeInclusive") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["start_time_inclusive"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startTimeInclusive"]
            )
        )
    if data.get("endTimeExclusive") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["end_time_exclusive"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["endTimeExclusive"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TimePeriod) -> dict:
    out: dict = {}
    if "start_time_inclusive" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["startTimeInclusive"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_cbor(
                value["start_time_inclusive"]
            )
        )
    if "end_time_exclusive" in value:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["endTimeExclusive"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.serialize_cbor(
                value["end_time_exclusive"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> TimePeriod:
    out: TimePeriod = {}  # type: ignore[typeddict-item]
    if data.get("startTimeInclusive") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["start_time_inclusive"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_cbor(
                data["startTimeInclusive"]
            )
        )
    if data.get("endTimeExclusive") is not None:
        import capo_compute_optimizer_automation.types._prelude.timestamp

        out["end_time_exclusive"] = (
            capo_compute_optimizer_automation.types._prelude.timestamp.deserialize_cbor(
                data["endTimeExclusive"]
            )
        )
    return out

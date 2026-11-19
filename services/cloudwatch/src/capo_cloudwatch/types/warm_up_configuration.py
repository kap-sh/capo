"""Generated from Smithy shape ``com.amazonaws.cloudwatch#WarmUpConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.only_start_evaluating_after_warm_up_period_ends
    import capo_cloudwatch.types.warm_up_period_duration_in_minutes


class WarmUpConfiguration(TypedDict, closed=True):
    warm_up_period_duration_in_minutes: NotRequired[
        "capo_cloudwatch.types.warm_up_period_duration_in_minutes.WarmUpPeriodDurationInMinutes"
    ]
    """<p>The length of the warm-up period, in minutes. After you create or update the alarm, the alarm stays in <code>INSUFFICIENT_DATA</code> for this duration. During this time, the alarm does not perform alarm actions.</p> <p>You can change this value at any time, including after the warm-up period ends. If you change it after the warm-up period ends, the new value does not restart the warm-up period.</p>"""
    only_start_evaluating_after_warm_up_period_ends: NotRequired[
        "capo_cloudwatch.types.only_start_evaluating_after_warm_up_period_ends.OnlyStartEvaluatingAfterWarmUpPeriodEnds"
    ]
    """<p>Specifies whether the alarm waits for the full warm-up period before it starts to evaluate. The default is <code>false</code>. If <code>true</code>, the alarm waits the entire <code>WarmUpPeriodDurationInMinutes</code> before it starts to evaluate, even if metric data arrives earlier. If <code>false</code>, the alarm ends the warm-up period early. Evaluation begins as soon as the alarm has enough metric data to fill its evaluation window.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WarmUpConfiguration) -> dict:
    out: dict = {}
    if "warm_up_period_duration_in_minutes" in value:
        out["WarmUpPeriodDurationInMinutes"] = value[
            "warm_up_period_duration_in_minutes"
        ]
    if "only_start_evaluating_after_warm_up_period_ends" in value:
        out["OnlyStartEvaluatingAfterWarmUpPeriodEnds"] = value[
            "only_start_evaluating_after_warm_up_period_ends"
        ]
    return out


def deserialize_aws_json_1_0(data: dict) -> WarmUpConfiguration:
    out: WarmUpConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("WarmUpPeriodDurationInMinutes") is not None:
        out["warm_up_period_duration_in_minutes"] = data[
            "WarmUpPeriodDurationInMinutes"
        ]
    if data.get("OnlyStartEvaluatingAfterWarmUpPeriodEnds") is not None:
        out["only_start_evaluating_after_warm_up_period_ends"] = data[
            "OnlyStartEvaluatingAfterWarmUpPeriodEnds"
        ]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: WarmUpConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "warm_up_period_duration_in_minutes" in value:
        pairs.append(
            (
                f"{key_prefix}WarmUpPeriodDurationInMinutes",
                str(value["warm_up_period_duration_in_minutes"]),
            )
        )
    if "only_start_evaluating_after_warm_up_period_ends" in value:
        pairs.append(
            (
                f"{key_prefix}OnlyStartEvaluatingAfterWarmUpPeriodEnds",
                "true"
                if value["only_start_evaluating_after_warm_up_period_ends"]
                else "false",
            )
        )


def deserialize_query(el: Element) -> WarmUpConfiguration:
    out: WarmUpConfiguration = {}  # type: ignore[typeddict-item]
    child_warm_up_period_duration_in_minutes = el.find("WarmUpPeriodDurationInMinutes")
    if child_warm_up_period_duration_in_minutes is not None:
        out["warm_up_period_duration_in_minutes"] = int(
            child_warm_up_period_duration_in_minutes.text or ""
        )
    child_only_start_evaluating_after_warm_up_period_ends = el.find(
        "OnlyStartEvaluatingAfterWarmUpPeriodEnds"
    )
    if child_only_start_evaluating_after_warm_up_period_ends is not None:
        out["only_start_evaluating_after_warm_up_period_ends"] = (
            child_only_start_evaluating_after_warm_up_period_ends.text or ""
        ).lower() == "true"
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WarmUpConfiguration) -> dict:
    out: dict = {}
    if "warm_up_period_duration_in_minutes" in value:
        out["WarmUpPeriodDurationInMinutes"] = value[
            "warm_up_period_duration_in_minutes"
        ]
    if "only_start_evaluating_after_warm_up_period_ends" in value:
        out["OnlyStartEvaluatingAfterWarmUpPeriodEnds"] = value[
            "only_start_evaluating_after_warm_up_period_ends"
        ]
    return out


def deserialize_cbor(data: dict) -> WarmUpConfiguration:
    out: WarmUpConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("WarmUpPeriodDurationInMinutes") is not None:
        out["warm_up_period_duration_in_minutes"] = data[
            "WarmUpPeriodDurationInMinutes"
        ]
    if data.get("OnlyStartEvaluatingAfterWarmUpPeriodEnds") is not None:
        out["only_start_evaluating_after_warm_up_period_ends"] = data[
            "OnlyStartEvaluatingAfterWarmUpPeriodEnds"
        ]
    return out

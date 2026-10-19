"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#AlertStateInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cloudwatchomni.types.alert_state
    import capo_cloudwatchomni.types.alert_state_data
    import capo_cloudwatchomni.types.contributor_summary


class AlertStateInfo(TypedDict, closed=True):
    value: "capo_cloudwatchomni.types.alert_state.AlertState"
    """Current flat state."""
    transitioned_at: NotRequired["datetime.datetime"]
    """When the alert transitioned to its current state."""
    contributor_summary: NotRequired[
        "capo_cloudwatchomni.types.contributor_summary.ContributorSummary"
    ]
    """Counts of contributors currently breaching each severity threshold. Present only when contributor-level tracking is active; absent until the first contributor breaches a {@code WARNING} or {@code CRITICAL} threshold."""
    data: NotRequired["capo_cloudwatchomni.types.alert_state_data.AlertStateData"]
    """Structured detail about why the alert is in its current state."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AlertStateInfo) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.alert_state

    out["value"] = capo_cloudwatchomni.types.alert_state.serialize_cbor(value["value"])
    if "transitioned_at" in value:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["transitionedAt"] = (
            capo_cloudwatchomni.types._prelude.timestamp.serialize_cbor(
                value["transitioned_at"]
            )
        )
    if "contributor_summary" in value:
        import capo_cloudwatchomni.types.contributor_summary

        out["contributorSummary"] = (
            capo_cloudwatchomni.types.contributor_summary.serialize_cbor(
                value["contributor_summary"]
            )
        )
    if "data" in value:
        import capo_cloudwatchomni.types.alert_state_data

        out["data"] = capo_cloudwatchomni.types.alert_state_data.serialize_cbor(
            value["data"]
        )
    return out


def deserialize_cbor(data: dict) -> AlertStateInfo:
    out: AlertStateInfo = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        import capo_cloudwatchomni.types.alert_state

        out["value"] = capo_cloudwatchomni.types.alert_state.deserialize_cbor(
            data["value"]
        )
    else:
        import typing

        out["value"] = typing.cast(
            "capo_cloudwatchomni.types.alert_state.AlertState", ""
        )
    if data.get("transitionedAt") is not None:
        import capo_cloudwatchomni.types._prelude.timestamp

        out["transitioned_at"] = (
            capo_cloudwatchomni.types._prelude.timestamp.deserialize_cbor(
                data["transitionedAt"]
            )
        )
    if data.get("contributorSummary") is not None:
        import capo_cloudwatchomni.types.contributor_summary

        out["contributor_summary"] = (
            capo_cloudwatchomni.types.contributor_summary.deserialize_cbor(
                data["contributorSummary"]
            )
        )
    if data.get("data") is not None:
        import capo_cloudwatchomni.types.alert_state_data

        out["data"] = capo_cloudwatchomni.types.alert_state_data.deserialize_cbor(
            data["data"]
        )
    return out

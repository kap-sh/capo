"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#NoData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.alert_state


class NoData(TypedDict, closed=True):
    treat_as: "capo_cloudwatchomni.types.alert_state.AlertState"
    """The state to report when an evaluation produces no data."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NoData) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.alert_state

    out["treatAs"] = capo_cloudwatchomni.types.alert_state.serialize_cbor(
        value["treat_as"]
    )
    return out


def deserialize_cbor(data: dict) -> NoData:
    out: NoData = {}  # type: ignore[typeddict-item]
    if data.get("treatAs") is not None:
        import capo_cloudwatchomni.types.alert_state

        out["treat_as"] = capo_cloudwatchomni.types.alert_state.deserialize_cbor(
            data["treatAs"]
        )
    else:
        import typing

        out["treat_as"] = typing.cast(
            "capo_cloudwatchomni.types.alert_state.AlertState", ""
        )
    return out

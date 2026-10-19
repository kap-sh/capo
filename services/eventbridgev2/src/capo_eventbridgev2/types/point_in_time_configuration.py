"""Generated from Smithy shape ``com.amazonaws.eventbridgev2#PointInTimeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridgev2.types.point_type
    import capo_eventbridgev2.types.timestamp


class PointInTimeConfiguration(TypedDict, closed=True):
    point_type: "capo_eventbridgev2.types.point_type.PointType"
    """Whether to start from the horizon or a specific timestamp."""
    starting_point: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """Timestamp to start from. Required when PointType is TIMESTAMP."""
    end_point: NotRequired["capo_eventbridgev2.types.timestamp.Timestamp"]
    """Timestamp to stop at. Optional."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PointInTimeConfiguration) -> dict:
    out: dict = {}
    import capo_eventbridgev2.types.point_type

    out["PointType"] = capo_eventbridgev2.types.point_type.serialize_cbor(
        value["point_type"]
    )
    if "starting_point" in value:
        import capo_eventbridgev2.types.timestamp

        out["StartingPoint"] = capo_eventbridgev2.types.timestamp.serialize_cbor(
            value["starting_point"]
        )
    if "end_point" in value:
        import capo_eventbridgev2.types.timestamp

        out["EndPoint"] = capo_eventbridgev2.types.timestamp.serialize_cbor(
            value["end_point"]
        )
    return out


def deserialize_cbor(data: dict) -> PointInTimeConfiguration:
    out: PointInTimeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("PointType") is not None:
        import capo_eventbridgev2.types.point_type

        out["point_type"] = capo_eventbridgev2.types.point_type.deserialize_cbor(
            data["PointType"]
        )
    else:
        import typing

        out["point_type"] = typing.cast(
            "capo_eventbridgev2.types.point_type.PointType", ""
        )
    if data.get("StartingPoint") is not None:
        import capo_eventbridgev2.types.timestamp

        out["starting_point"] = capo_eventbridgev2.types.timestamp.deserialize_cbor(
            data["StartingPoint"]
        )
    if data.get("EndPoint") is not None:
        import capo_eventbridgev2.types.timestamp

        out["end_point"] = capo_eventbridgev2.types.timestamp.deserialize_cbor(
            data["EndPoint"]
        )
    return out

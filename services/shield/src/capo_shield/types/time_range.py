"""Generated from Smithy shape ``com.amazonaws.shield#TimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.timestamp


class TimeRange(TypedDict, closed=True):
    from_inclusive: NotRequired["capo_shield.types.timestamp.Timestamp"]
    """<p>The start time, in Unix time in seconds. </p>"""
    to_exclusive: NotRequired["capo_shield.types.timestamp.Timestamp"]
    """<p>The end time, in Unix time in seconds. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeRange) -> dict:
    out: dict = {}
    if "from_inclusive" in value:
        import capo_shield.types.timestamp

        out["FromInclusive"] = capo_shield.types.timestamp.serialize_aws_json_1_1(
            value["from_inclusive"]
        )
    if "to_exclusive" in value:
        import capo_shield.types.timestamp

        out["ToExclusive"] = capo_shield.types.timestamp.serialize_aws_json_1_1(
            value["to_exclusive"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeRange:
    out: TimeRange = {}  # type: ignore[typeddict-item]
    if data.get("FromInclusive") is not None:
        import capo_shield.types.timestamp

        out["from_inclusive"] = capo_shield.types.timestamp.deserialize_aws_json_1_1(
            data["FromInclusive"]
        )
    if data.get("ToExclusive") is not None:
        import capo_shield.types.timestamp

        out["to_exclusive"] = capo_shield.types.timestamp.deserialize_aws_json_1_1(
            data["ToExclusive"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TimeRange) -> dict:
    out: dict = {}
    if "from_inclusive" in value:
        import capo_shield.types.timestamp

        out["FromInclusive"] = capo_shield.types.timestamp.serialize_cbor(
            value["from_inclusive"]
        )
    if "to_exclusive" in value:
        import capo_shield.types.timestamp

        out["ToExclusive"] = capo_shield.types.timestamp.serialize_cbor(
            value["to_exclusive"]
        )
    return out


def deserialize_cbor(data: dict) -> TimeRange:
    out: TimeRange = {}  # type: ignore[typeddict-item]
    if data.get("FromInclusive") is not None:
        import capo_shield.types.timestamp

        out["from_inclusive"] = capo_shield.types.timestamp.deserialize_cbor(
            data["FromInclusive"]
        )
    if data.get("ToExclusive") is not None:
        import capo_shield.types.timestamp

        out["to_exclusive"] = capo_shield.types.timestamp.deserialize_cbor(
            data["ToExclusive"]
        )
    return out

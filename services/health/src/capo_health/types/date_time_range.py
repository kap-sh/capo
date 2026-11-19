"""Generated from Smithy shape ``com.amazonaws.health#DateTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.timestamp

DateTimeRange = TypedDict(
    "DateTimeRange",
    {
        "from": NotRequired["capo_health.types.timestamp.timestamp"],
        "to": NotRequired["capo_health.types.timestamp.timestamp"],
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DateTimeRange) -> dict:
    out: dict = {}
    if "from" in value:
        import capo_health.types.timestamp

        out["from"] = capo_health.types.timestamp.serialize_aws_json_1_1(value["from"])
    if "to" in value:
        import capo_health.types.timestamp

        out["to"] = capo_health.types.timestamp.serialize_aws_json_1_1(value["to"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DateTimeRange:
    out: DateTimeRange = {}  # type: ignore[typeddict-item]
    if data.get("from") is not None:
        import capo_health.types.timestamp

        out["from"] = capo_health.types.timestamp.deserialize_aws_json_1_1(data["from"])
    if data.get("to") is not None:
        import capo_health.types.timestamp

        out["to"] = capo_health.types.timestamp.deserialize_aws_json_1_1(data["to"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DateTimeRange) -> dict:
    out: dict = {}
    if "from" in value:
        import capo_health.types.timestamp

        out["from"] = capo_health.types.timestamp.serialize_cbor(value["from"])
    if "to" in value:
        import capo_health.types.timestamp

        out["to"] = capo_health.types.timestamp.serialize_cbor(value["to"])
    return out


def deserialize_cbor(data: dict) -> DateTimeRange:
    out: DateTimeRange = {}  # type: ignore[typeddict-item]
    if data.get("from") is not None:
        import capo_health.types.timestamp

        out["from"] = capo_health.types.timestamp.deserialize_cbor(data["from"])
    if data.get("to") is not None:
        import capo_health.types.timestamp

        out["to"] = capo_health.types.timestamp.deserialize_cbor(data["to"])
    return out

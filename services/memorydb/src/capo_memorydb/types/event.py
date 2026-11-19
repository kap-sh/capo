"""Generated from Smithy shape ``com.amazonaws.memorydb#Event``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.source_type
    import capo_memorydb.types.string
    import capo_memorydb.types.t_stamp


class Event(TypedDict, closed=True):
    source_name: NotRequired["capo_memorydb.types.string.String"]
    """<p>The name for the source of the event. For example, if the event occurred at the cluster level, the identifier would be the name of the cluster.</p>"""
    source_type: NotRequired["capo_memorydb.types.source_type.SourceType"]
    """<p>Specifies the origin of this event - a cluster, a parameter group, a security group, etc.</p>"""
    message: NotRequired["capo_memorydb.types.string.String"]
    """<p>The text of the event.</p>"""
    date: NotRequired["capo_memorydb.types.t_stamp.TStamp"]
    """<p>The date and time when the event occurred.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Event) -> dict:
    out: dict = {}
    if "source_name" in value:
        out["SourceName"] = value["source_name"]
    if "source_type" in value:
        import capo_memorydb.types.source_type

        out["SourceType"] = capo_memorydb.types.source_type.serialize_aws_json_1_1(
            value["source_type"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "date" in value:
        import capo_memorydb.types.t_stamp

        out["Date"] = capo_memorydb.types.t_stamp.serialize_aws_json_1_1(value["date"])
    return out


def deserialize_aws_json_1_1(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if data.get("SourceName") is not None:
        out["source_name"] = data["SourceName"]
    if data.get("SourceType") is not None:
        import capo_memorydb.types.source_type

        out["source_type"] = capo_memorydb.types.source_type.deserialize_aws_json_1_1(
            data["SourceType"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Date") is not None:
        import capo_memorydb.types.t_stamp

        out["date"] = capo_memorydb.types.t_stamp.deserialize_aws_json_1_1(data["Date"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Event) -> dict:
    out: dict = {}
    if "source_name" in value:
        out["SourceName"] = value["source_name"]
    if "source_type" in value:
        import capo_memorydb.types.source_type

        out["SourceType"] = capo_memorydb.types.source_type.serialize_cbor(
            value["source_type"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "date" in value:
        import capo_memorydb.types.t_stamp

        out["Date"] = capo_memorydb.types.t_stamp.serialize_cbor(value["date"])
    return out


def deserialize_cbor(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if data.get("SourceName") is not None:
        out["source_name"] = data["SourceName"]
    if data.get("SourceType") is not None:
        import capo_memorydb.types.source_type

        out["source_type"] = capo_memorydb.types.source_type.deserialize_cbor(
            data["SourceType"]
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("Date") is not None:
        import capo_memorydb.types.t_stamp

        out["date"] = capo_memorydb.types.t_stamp.deserialize_cbor(data["Date"])
    return out

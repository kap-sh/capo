"""Generated from Smithy shape ``com.amazonaws.neptunedata#SparqlRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptunedata.errors import DeserializationError

if TYPE_CHECKING:
    import capo_neptunedata.types.sparql_data
    import capo_neptunedata.types.string_valued_map


class SparqlRecord(TypedDict, closed=True):
    commit_timestamp_in_millis: "int"
    """<p>The time at which the commit for the transaction was requested, in milliseconds from the Unix epoch.</p>"""
    event_id: "capo_neptunedata.types.string_valued_map.StringValuedMap"
    """<p>The sequence identifier of the stream change record.</p>"""
    data: "capo_neptunedata.types.sparql_data.SparqlData"
    """<p>The serialized SPARQL change record. The serialization formats of each record are described in more detail in <a href="https://docs.aws.amazon.com/neptune/latest/userguide/streams-change-formats.html">Serialization Formats in Neptune Streams</a>.</p>"""
    op: "str"
    """<p>The operation that created the change.</p>"""
    is_last_op: NotRequired["bool"]
    """<p>Only present if this operation is the last one in its transaction. If present, it is set to true. It is useful for ensuring that an entire transaction is consumed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SparqlRecord) -> dict:
    out: dict = {}
    out["commitTimestamp"] = value["commit_timestamp_in_millis"]
    import capo_neptunedata.types.string_valued_map

    out["eventId"] = capo_neptunedata.types.string_valued_map.serialize_json(
        value["event_id"]
    )
    import capo_neptunedata.types.sparql_data

    out["data"] = capo_neptunedata.types.sparql_data.serialize_json(value["data"])
    out["op"] = value["op"]
    if "is_last_op" in value:
        out["isLastOp"] = value["is_last_op"]
    return out


def deserialize_json(data: dict) -> SparqlRecord:
    out: SparqlRecord = {}  # type: ignore[typeddict-item]
    if data.get("commitTimestamp") is not None:
        out["commit_timestamp_in_millis"] = data["commitTimestamp"]
    else:
        raise DeserializationError("SparqlRecord.commit_timestamp_in_millis required")
    if data.get("eventId") is not None:
        import capo_neptunedata.types.string_valued_map

        out["event_id"] = capo_neptunedata.types.string_valued_map.deserialize_json(
            data["eventId"]
        )
    else:
        raise DeserializationError("SparqlRecord.event_id required")
    if data.get("data") is not None:
        import capo_neptunedata.types.sparql_data

        out["data"] = capo_neptunedata.types.sparql_data.deserialize_json(data["data"])
    else:
        raise DeserializationError("SparqlRecord.data required")
    if data.get("op") is not None:
        out["op"] = data["op"]
    else:
        raise DeserializationError("SparqlRecord.op required")
    if data.get("isLastOp") is not None:
        out["is_last_op"] = data["isLastOp"]
    return out

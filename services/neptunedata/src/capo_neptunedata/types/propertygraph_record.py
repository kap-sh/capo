"""Generated from Smithy shape ``com.amazonaws.neptunedata#PropertygraphRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptunedata.errors import DeserializationError

if TYPE_CHECKING:
    import capo_neptunedata.types.propertygraph_data
    import capo_neptunedata.types.string_valued_map


class PropertygraphRecord(TypedDict, closed=True):
    commit_timestamp_in_millis: "int"
    """<p>The time at which the commit for the transaction was requested, in milliseconds from the Unix epoch.</p>"""
    event_id: "capo_neptunedata.types.string_valued_map.StringValuedMap"
    """<p>The sequence identifier of the stream change record.</p>"""
    data: "capo_neptunedata.types.propertygraph_data.PropertygraphData"
    """<p>The serialized Gremlin or openCypher change record.</p>"""
    op: "str"
    """<p>The operation that created the change.</p>"""
    is_last_op: NotRequired["bool"]
    """<p>Only present if this operation is the last one in its transaction. If present, it is set to true. It is useful for ensuring that an entire transaction is consumed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertygraphRecord) -> dict:
    out: dict = {}
    out["commitTimestamp"] = value["commit_timestamp_in_millis"]
    import capo_neptunedata.types.string_valued_map

    out["eventId"] = capo_neptunedata.types.string_valued_map.serialize_json(
        value["event_id"]
    )
    import capo_neptunedata.types.propertygraph_data

    out["data"] = capo_neptunedata.types.propertygraph_data.serialize_json(
        value["data"]
    )
    out["op"] = value["op"]
    if "is_last_op" in value:
        out["isLastOp"] = value["is_last_op"]
    return out


def deserialize_json(data: dict) -> PropertygraphRecord:
    out: PropertygraphRecord = {}  # type: ignore[typeddict-item]
    if data.get("commitTimestamp") is not None:
        out["commit_timestamp_in_millis"] = data["commitTimestamp"]
    else:
        out["commit_timestamp_in_millis"] = 0
    if data.get("eventId") is not None:
        import capo_neptunedata.types.string_valued_map

        out["event_id"] = capo_neptunedata.types.string_valued_map.deserialize_json(
            data["eventId"]
        )
    else:
        out["event_id"] = {}
    if data.get("data") is not None:
        import capo_neptunedata.types.propertygraph_data

        out["data"] = capo_neptunedata.types.propertygraph_data.deserialize_json(
            data["data"]
        )
    else:
        raise DeserializationError("PropertygraphRecord.data required")
    if data.get("op") is not None:
        out["op"] = data["op"]
    else:
        out["op"] = ""
    if data.get("isLastOp") is not None:
        out["is_last_op"] = data["isLastOp"]
    return out

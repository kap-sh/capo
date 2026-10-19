"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetPropertygraphStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.propertygraph_records_list
    import capo_neptunedata.types.string_valued_map


class GetPropertygraphStreamOutput(TypedDict, closed=True):
    last_event_id: "capo_neptunedata.types.string_valued_map.StringValuedMap"
    """<p>Sequence identifier of the last change in the stream response.</p> <p>An event ID is composed of two fields: a <code>commitNum</code>, which identifies a transaction that changed the graph, and an <code>opNum</code>, which identifies a specific operation within that transaction:</p>"""
    last_trx_timestamp_in_millis: "int"
    """<p>The time at which the commit for the transaction was requested, in milliseconds from the Unix epoch.</p>"""
    format: "str"
    """<p>Serialization format for the change records being returned. Currently, the only supported value is <code>PG_JSON</code>.</p>"""
    records: (
        "capo_neptunedata.types.propertygraph_records_list.PropertygraphRecordsList"
    )
    """<p>An array of serialized change-log stream records included in the response.</p>"""
    total_records: "int"
    """<p>The total number of records in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPropertygraphStreamOutput) -> dict:
    out: dict = {}
    import capo_neptunedata.types.string_valued_map

    out["lastEventId"] = capo_neptunedata.types.string_valued_map.serialize_json(
        value["last_event_id"]
    )
    out["lastTrxTimestamp"] = value["last_trx_timestamp_in_millis"]
    out["format"] = value["format"]
    import capo_neptunedata.types.propertygraph_records_list

    out["records"] = capo_neptunedata.types.propertygraph_records_list.serialize_json(
        value["records"]
    )
    out["totalRecords"] = value["total_records"]
    return out


def deserialize_json(data: dict) -> GetPropertygraphStreamOutput:
    out: GetPropertygraphStreamOutput = {}  # type: ignore[typeddict-item]
    if data.get("lastEventId") is not None:
        import capo_neptunedata.types.string_valued_map

        out["last_event_id"] = (
            capo_neptunedata.types.string_valued_map.deserialize_json(
                data["lastEventId"]
            )
        )
    else:
        out["last_event_id"] = {}
    if data.get("lastTrxTimestamp") is not None:
        out["last_trx_timestamp_in_millis"] = data["lastTrxTimestamp"]
    else:
        out["last_trx_timestamp_in_millis"] = 0
    if data.get("format") is not None:
        out["format"] = data["format"]
    else:
        out["format"] = ""
    if data.get("records") is not None:
        import capo_neptunedata.types.propertygraph_records_list

        out["records"] = (
            capo_neptunedata.types.propertygraph_records_list.deserialize_json(
                data["records"]
            )
        )
    else:
        out["records"] = []
    if data.get("totalRecords") is not None:
        out["total_records"] = data["totalRecords"]
    else:
        out["total_records"] = 0
    return out

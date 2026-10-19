"""Generated from Smithy shape ``com.amazonaws.quicksight#DestinationTable``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.destination_table_alias
    import capo_quicksight.types.destination_table_source


class DestinationTable(TypedDict, closed=True):
    alias: "capo_quicksight.types.destination_table_alias.DestinationTableAlias"
    """<p>Alias for the destination table.</p>"""
    source: "capo_quicksight.types.destination_table_source.DestinationTableSource"
    """<p>The source configuration that specifies which transform operation provides data to this destination table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationTable) -> dict:
    out: dict = {}
    out["Alias"] = value["alias"]
    import capo_quicksight.types.destination_table_source

    out["Source"] = capo_quicksight.types.destination_table_source.serialize_json(
        value["source"]
    )
    return out


def deserialize_json(data: dict) -> DestinationTable:
    out: DestinationTable = {}  # type: ignore[typeddict-item]
    if data.get("Alias") is not None:
        out["alias"] = data["Alias"]
    else:
        out["alias"] = ""
    if data.get("Source") is not None:
        import capo_quicksight.types.destination_table_source

        out["source"] = capo_quicksight.types.destination_table_source.deserialize_json(
            data["Source"]
        )
    else:
        raise DeserializationError("DestinationTable.source required")
    return out

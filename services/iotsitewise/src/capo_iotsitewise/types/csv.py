"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Csv``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.column_names


class Csv(TypedDict, closed=True):
    column_names: "capo_iotsitewise.types.column_names.ColumnNames"
    """<p>The column names specified in the .csv file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Csv) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.column_names

    out["columnNames"] = capo_iotsitewise.types.column_names.serialize_json(
        value["column_names"]
    )
    return out


def deserialize_json(data: dict) -> Csv:
    out: Csv = {}  # type: ignore[typeddict-item]
    if data.get("columnNames") is not None:
        import capo_iotsitewise.types.column_names

        out["column_names"] = capo_iotsitewise.types.column_names.deserialize_json(
            data["columnNames"]
        )
    else:
        out["column_names"] = []
    return out

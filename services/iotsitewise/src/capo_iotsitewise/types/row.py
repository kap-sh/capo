"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Row``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.datum_list


class Row(TypedDict, closed=True):
    data: "capo_iotsitewise.types.datum_list.DatumList"
    """<p>List of data points in a single row of the result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Row) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.datum_list

    out["data"] = capo_iotsitewise.types.datum_list.serialize_json(value["data"])
    return out


def deserialize_json(data: dict) -> Row:
    out: Row = {}  # type: ignore[typeddict-item]
    if data.get("data") is not None:
        import capo_iotsitewise.types.datum_list

        out["data"] = capo_iotsitewise.types.datum_list.deserialize_json(data["data"])
    else:
        out["data"] = []
    return out

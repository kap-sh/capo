"""Generated from Smithy shape ``com.amazonaws.neptunedata#ListIndexRebuildsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_neptunedata.types.rebuild_id_list


class ListIndexRebuildsOutput(TypedDict, closed=True):
    rebuild_ids: "capo_neptunedata.types.rebuild_id_list.RebuildIdList"
    """<p>A list of unique identifiers for index rebuild operations. Use each ID with the GetIndexRebuildStatus operation to retrieve detailed status information.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIndexRebuildsOutput) -> dict:
    out: dict = {}
    import capo_neptunedata.types.rebuild_id_list

    out["rebuildIds"] = capo_neptunedata.types.rebuild_id_list.serialize_json(
        value["rebuild_ids"]
    )
    return out


def deserialize_json(data: dict) -> ListIndexRebuildsOutput:
    out: ListIndexRebuildsOutput = {}  # type: ignore[typeddict-item]
    if data.get("rebuildIds") is not None:
        import capo_neptunedata.types.rebuild_id_list

        out["rebuild_ids"] = capo_neptunedata.types.rebuild_id_list.deserialize_json(
            data["rebuildIds"]
        )
    else:
        out["rebuild_ids"] = []
    return out

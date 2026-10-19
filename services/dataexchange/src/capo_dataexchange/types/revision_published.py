"""Generated from Smithy shape ``com.amazonaws.dataexchange#RevisionPublished``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.id


class RevisionPublished(TypedDict, closed=True):
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The data set ID of the published revision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevisionPublished) -> dict:
    out: dict = {}
    out["DataSetId"] = value["data_set_id"]
    return out


def deserialize_json(data: dict) -> RevisionPublished:
    out: RevisionPublished = {}  # type: ignore[typeddict-item]
    if data.get("DataSetId") is not None:
        out["data_set_id"] = data["DataSetId"]
    else:
        out["data_set_id"] = ""
    return out

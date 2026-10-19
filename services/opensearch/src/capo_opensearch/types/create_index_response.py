"""Generated from Smithy shape ``com.amazonaws.opensearch#CreateIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.index_status


class CreateIndexResponse(TypedDict, closed=True):
    status: "capo_opensearch.types.index_status.IndexStatus"
    """<p>The status of the index creation operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIndexResponse) -> dict:
    out: dict = {}
    import capo_opensearch.types.index_status

    out["Status"] = capo_opensearch.types.index_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> CreateIndexResponse:
    out: CreateIndexResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_opensearch.types.index_status

        out["status"] = capo_opensearch.types.index_status.deserialize_json(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_opensearch.types.index_status.IndexStatus", ""
        )
    return out

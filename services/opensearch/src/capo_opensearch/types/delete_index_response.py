"""Generated from Smithy shape ``com.amazonaws.opensearch#DeleteIndexResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.index_status


class DeleteIndexResponse(TypedDict, closed=True):
    status: "capo_opensearch.types.index_status.IndexStatus"
    """<p>The status of the index deletion operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIndexResponse) -> dict:
    out: dict = {}
    import capo_opensearch.types.index_status

    out["Status"] = capo_opensearch.types.index_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DeleteIndexResponse:
    out: DeleteIndexResponse = {}  # type: ignore[typeddict-item]
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

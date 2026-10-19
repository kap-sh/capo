"""Generated from Smithy shape ``com.amazonaws.rtbfabric#DeleteLinkResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.link_id
    import capo_rtbfabric.types.link_status


class DeleteLinkResponse(TypedDict, closed=True):
    link_id: "capo_rtbfabric.types.link_id.LinkId"
    """<p>The unique identifier of the link.</p>"""
    status: "capo_rtbfabric.types.link_status.LinkStatus"
    """<p>The status of the link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteLinkResponse) -> dict:
    out: dict = {}
    out["linkId"] = value["link_id"]
    import capo_rtbfabric.types.link_status

    out["status"] = capo_rtbfabric.types.link_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DeleteLinkResponse:
    out: DeleteLinkResponse = {}  # type: ignore[typeddict-item]
    if data.get("linkId") is not None:
        out["link_id"] = data["linkId"]
    else:
        out["link_id"] = ""
    if data.get("status") is not None:
        import capo_rtbfabric.types.link_status

        out["status"] = capo_rtbfabric.types.link_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_rtbfabric.types.link_status.LinkStatus", "")
    return out

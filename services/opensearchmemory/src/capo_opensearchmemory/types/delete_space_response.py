"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#DeleteSpaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.space_id
    import capo_opensearchmemory.types.space_status


class DeleteSpaceResponse(TypedDict, closed=True):
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The ID of the space.</p>"""
    status: "capo_opensearchmemory.types.space_status.SpaceStatus"
    """<p>The status of the space: <code>DELETING</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteSpaceResponse) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    import capo_opensearchmemory.types.space_status

    out["status"] = capo_opensearchmemory.types.space_status.serialize_aws_json_1_0(
        value["status"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteSpaceResponse:
    out: DeleteSpaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("status") is not None:
        import capo_opensearchmemory.types.space_status

        out["status"] = (
            capo_opensearchmemory.types.space_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_opensearchmemory.types.space_status.SpaceStatus", ""
        )
    return out

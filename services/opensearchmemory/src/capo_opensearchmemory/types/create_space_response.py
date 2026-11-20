"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#CreateSpaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.space_arn
    import capo_opensearchmemory.types.space_id
    import capo_opensearchmemory.types.space_name
    import capo_opensearchmemory.types.space_status
    import capo_opensearchmemory.types.timestamp


class CreateSpaceResponse(TypedDict, closed=True):
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The ID of the space.</p>"""
    arn: "capo_opensearchmemory.types.space_arn.SpaceArn"
    """<p>The Amazon Resource Name (ARN) of the space.</p>"""
    name: "capo_opensearchmemory.types.space_name.SpaceName"
    """<p>The name of the space.</p>"""
    status: "capo_opensearchmemory.types.space_status.SpaceStatus"
    """<p>The status of the space: <code>CREATING</code>.</p>"""
    created_at: "capo_opensearchmemory.types.timestamp.Timestamp"
    """<p>When the space was created.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateSpaceResponse) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import capo_opensearchmemory.types.space_status

    out["status"] = capo_opensearchmemory.types.space_status.serialize_aws_json_1_0(
        value["status"]
    )
    import capo_opensearchmemory.types.timestamp

    out["createdAt"] = capo_opensearchmemory.types.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateSpaceResponse:
    out: CreateSpaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
    if data.get("createdAt") is not None:
        import capo_opensearchmemory.types.timestamp

        out["created_at"] = (
            capo_opensearchmemory.types.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out

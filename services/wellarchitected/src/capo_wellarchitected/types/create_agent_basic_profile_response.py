"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateAgentBasicProfileResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_wellarchitected.types.agent_profile_arn


class CreateAgentBasicProfileResponse(TypedDict, closed=True):
    created_by: "str"
    """<p>The identifier of the user or system that created this resource.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the resource was created.</p>"""
    last_modified_by: NotRequired["str"]
    """<p>The identifier of the user or system that last modified this resource.</p>"""
    last_modified_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the resource was last modified.</p>"""
    arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the created Basic profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentBasicProfileResponse) -> dict:
    out: dict = {}
    out["createdBy"] = value["created_by"]
    import capo_wellarchitected._protocol.serialize

    out["createdAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "last_modified_by" in value:
        out["lastModifiedBy"] = value["last_modified_by"]
    if "last_modified_at" in value:
        import capo_wellarchitected._protocol.serialize

        out["lastModifiedAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
            value["last_modified_at"]
        )
    out["arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateAgentBasicProfileResponse:
    out: CreateAgentBasicProfileResponse = {}  # type: ignore[typeddict-item]
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastModifiedBy") is not None:
        out["last_modified_by"] = data["lastModifiedBy"]
    if data.get("lastModifiedAt") is not None:
        import datetime

        out["last_modified_at"] = datetime.datetime.fromisoformat(
            data["lastModifiedAt"].replace("Z", "+00:00")
        )
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    return out

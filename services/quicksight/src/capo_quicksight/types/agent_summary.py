"""Generated from Smithy shape ``com.amazonaws.quicksight#AgentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_quicksight.types.agent_arn
    import capo_quicksight.types.agent_description
    import capo_quicksight.types.agent_id
    import capo_quicksight.types.agent_name
    import capo_quicksight.types.icon_id


class AgentSummary(TypedDict, closed=True):
    arn: "capo_quicksight.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent.</p>"""
    agent_id: "capo_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent.</p>"""
    name: "capo_quicksight.types.agent_name.AgentName"
    """<p>The name of the agent.</p>"""
    description: NotRequired["capo_quicksight.types.agent_description.AgentDescription"]
    """<p>A description of the agent.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the agent was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time that the agent was last updated.</p>"""
    icon_id: NotRequired["capo_quicksight.types.icon_id.IconId"]
    """<p>The icon identifier for the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentSummary) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["AgentId"] = value["agent_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_quicksight.types._prelude.timestamp

    out["CreatedAt"] = capo_quicksight.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_quicksight.types._prelude.timestamp

    out["UpdatedAt"] = capo_quicksight.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    if "icon_id" in value:
        out["IconId"] = value["icon_id"]
    return out


def deserialize_json(data: dict) -> AgentSummary:
    out: AgentSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("AgentId") is not None:
        out["agent_id"] = data["AgentId"]
    else:
        out["agent_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedAt") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["created_at"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("UpdatedAt") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["updated_at"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("IconId") is not None:
        out["icon_id"] = data["IconId"]
    return out

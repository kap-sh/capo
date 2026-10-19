"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PromptSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.date_timestamp
    import capo_bedrock_agent.types.prompt_arn
    import capo_bedrock_agent.types.prompt_description
    import capo_bedrock_agent.types.prompt_id
    import capo_bedrock_agent.types.prompt_name
    import capo_bedrock_agent.types.version


class PromptSummary(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.prompt_name.PromptName"
    """<p>The name of the prompt.</p>"""
    description: NotRequired[
        "capo_bedrock_agent.types.prompt_description.PromptDescription"
    ]
    """<p>The description of the prompt.</p>"""
    id: "capo_bedrock_agent.types.prompt_id.PromptId"
    """<p>The unique identifier of the prompt.</p>"""
    arn: "capo_bedrock_agent.types.prompt_arn.PromptArn"
    """<p>The Amazon Resource Name (ARN) of the prompt or the prompt version (if you specified a version in the request).</p>"""
    version: "capo_bedrock_agent.types.version.Version"
    """<p>The version of the prompt that this summary applies to.</p>"""
    created_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the prompt was created.</p>"""
    updated_at: "capo_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the prompt was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PromptSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["version"] = value["version"]
    import capo_bedrock_agent.types.date_timestamp

    out["createdAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agent.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> PromptSummary:
    out: PromptSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("createdAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["created_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock_agent.types.date_timestamp

        out["updated_at"] = capo_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out

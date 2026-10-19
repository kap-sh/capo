"""Generated from Smithy shape ``com.amazonaws.wisdom#SessionData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wisdom.types.arn
    import capo_wisdom.types.description
    import capo_wisdom.types.name
    import capo_wisdom.types.session_integration_configuration
    import capo_wisdom.types.tags
    import capo_wisdom.types.uuid


class SessionData(TypedDict, closed=True):
    session_arn: "capo_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the session.</p>"""
    session_id: "capo_wisdom.types.uuid.Uuid"
    """<p>The identifier of the session.</p>"""
    name: "capo_wisdom.types.name.Name"
    """<p>The name of the session.</p>"""
    description: NotRequired["capo_wisdom.types.description.Description"]
    """<p>The description of the session.</p>"""
    tags: NotRequired["capo_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""
    integration_configuration: NotRequired[
        "capo_wisdom.types.session_integration_configuration.SessionIntegrationConfiguration"
    ]
    """<p>The configuration information for the session integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionData) -> dict:
    out: dict = {}
    out["sessionArn"] = value["session_arn"]
    out["sessionId"] = value["session_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.serialize_json(value["tags"])
    if "integration_configuration" in value:
        import capo_wisdom.types.session_integration_configuration

        out["integrationConfiguration"] = (
            capo_wisdom.types.session_integration_configuration.serialize_json(
                value["integration_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> SessionData:
    out: SessionData = {}  # type: ignore[typeddict-item]
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        out["session_arn"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.deserialize_json(data["tags"])
    if data.get("integrationConfiguration") is not None:
        import capo_wisdom.types.session_integration_configuration

        out["integration_configuration"] = (
            capo_wisdom.types.session_integration_configuration.deserialize_json(
                data["integrationConfiguration"]
            )
        )
    return out

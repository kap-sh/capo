"""Generated from Smithy shape ``com.amazonaws.devopsagent#CreatePrivateConnectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.private_connection_mode
    import capo_devops_agent.types.private_connection_name
    import capo_devops_agent.types.tags


class CreatePrivateConnectionInput(TypedDict, closed=True):
    name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
    """<p>Unique name for this Private Connection within the account.</p>"""
    mode: "capo_devops_agent.types.private_connection_mode.PrivateConnectionMode"
    """<p>Private Connection mode configuration.</p>"""
    tags: NotRequired["capo_devops_agent.types.tags.Tags"]
    """<p>Tags to add to the Private Connection at creation time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePrivateConnectionInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_devops_agent.types.private_connection_mode

    out["mode"] = capo_devops_agent.types.private_connection_mode.serialize_json(
        value["mode"]
    )
    if "tags" in value:
        import capo_devops_agent.types.tags

        out["tags"] = capo_devops_agent.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePrivateConnectionInput:
    out: CreatePrivateConnectionInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("mode") is not None:
        import capo_devops_agent.types.private_connection_mode

        out["mode"] = capo_devops_agent.types.private_connection_mode.deserialize_json(
            data["mode"]
        )
    else:
        out["mode"] = {"$unknown": {"name": ""}}
    if data.get("tags") is not None:
        import capo_devops_agent.types.tags

        out["tags"] = capo_devops_agent.types.tags.deserialize_json(data["tags"])
    return out

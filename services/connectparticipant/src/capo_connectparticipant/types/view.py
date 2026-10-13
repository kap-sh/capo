"""Generated from Smithy shape ``com.amazonaws.connectparticipant#View``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.arn
    import capo_connectparticipant.types.view_content
    import capo_connectparticipant.types.view_id
    import capo_connectparticipant.types.view_name
    import capo_connectparticipant.types.view_version


class View(TypedDict, closed=True):
    id: NotRequired["capo_connectparticipant.types.view_id.ViewId"]
    """<p>The identifier of the view.</p>"""
    arn: NotRequired["capo_connectparticipant.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the view.</p>"""
    name: NotRequired["capo_connectparticipant.types.view_name.ViewName"]
    """<p>The name of the view.</p>"""
    version: NotRequired["capo_connectparticipant.types.view_version.ViewVersion"]
    """<p>The current version of the view.</p>"""
    content: NotRequired["capo_connectparticipant.types.view_content.ViewContent"]
    """<p>View content containing all content necessary to render a view except for runtime input data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: View) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    if "content" in value:
        import capo_connectparticipant.types.view_content

        out["Content"] = capo_connectparticipant.types.view_content.serialize_json(
            value["content"]
        )
    return out


def deserialize_json(data: dict) -> View:
    out: View = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("Content") is not None:
        import capo_connectparticipant.types.view_content

        out["content"] = capo_connectparticipant.types.view_content.deserialize_json(
            data["Content"]
        )
    return out


def redact_sensitive(value: View) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "content" in value:
        import capo_connectparticipant.types.view_content

        out["content"] = capo_connectparticipant.types.view_content.redact_sensitive(
            value["content"]
        )
    return out

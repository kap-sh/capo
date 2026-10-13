"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedProject``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.project_id
    import capo_datazone.types.project_name


class SubscribedProject(TypedDict, closed=True):
    id: NotRequired["capo_datazone.types.project_id.ProjectId"]
    """<p>The identifier of the project that has the subscription grant.</p>"""
    name: NotRequired["capo_datazone.types.project_name.ProjectName"]
    """<p>The name of the project that has the subscription grant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedProject) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> SubscribedProject:
    out: SubscribedProject = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out


def redact_sensitive(value: SubscribedProject) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out

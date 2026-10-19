"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DashboardSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.timestamp


class DashboardSummary(TypedDict, closed=True):
    id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the dashboard.</p>"""
    name: "capo_iotsitewise.types.name.Name"
    """<p>The name of the dashboard</p>"""
    description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>The dashboard's description.</p>"""
    creation_date: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>The date the dashboard was created, in Unix epoch time.</p>"""
    last_update_date: NotRequired["capo_iotsitewise.types.timestamp.Timestamp"]
    """<p>The date the dashboard was last updated, in Unix epoch time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "creation_date" in value:
        import capo_iotsitewise.types.timestamp

        out["creationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "last_update_date" in value:
        import capo_iotsitewise.types.timestamp

        out["lastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
            value["last_update_date"]
        )
    return out


def deserialize_json(data: dict) -> DashboardSummary:
    out: DashboardSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("creationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["creation_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    if data.get("lastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["last_update_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["lastUpdateDate"]
        )
    return out

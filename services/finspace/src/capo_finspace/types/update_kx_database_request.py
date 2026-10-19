"""Generated from Smithy shape ``com.amazonaws.finspace#UpdateKxDatabaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.client_token_string
    import capo_finspace.types.database_name
    import capo_finspace.types.description
    import capo_finspace.types.environment_id


class UpdateKxDatabaseRequest(TypedDict, closed=True):
    environment_id: "capo_finspace.types.environment_id.EnvironmentId"
    """<p>A unique identifier for the kdb environment.</p>"""
    database_name: "capo_finspace.types.database_name.DatabaseName"
    """<p>The name of the kdb database.</p>"""
    description: NotRequired["capo_finspace.types.description.Description"]
    """<p>A description of the database.</p>"""
    client_token: "capo_finspace.types.client_token_string.ClientTokenString"
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKxDatabaseRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateKxDatabaseRequest:
    out: UpdateKxDatabaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    else:
        out["client_token"] = ""
    return out

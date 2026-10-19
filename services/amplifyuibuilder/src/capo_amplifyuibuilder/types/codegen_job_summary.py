"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_amplifyuibuilder.types.app_id
    import capo_amplifyuibuilder.types.uuid


class CodegenJobSummary(TypedDict, closed=True):
    app_id: "capo_amplifyuibuilder.types.app_id.AppId"
    """<p>The unique ID of the Amplify app associated with the code generation job.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment associated with the code generation job.</p>"""
    id: "capo_amplifyuibuilder.types.uuid.Uuid"
    """<p>The unique ID for the code generation job summary.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The time that the code generation job summary was created.</p>"""
    modified_at: NotRequired["datetime.datetime"]
    """<p>The time that the code generation job summary was modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodegenJobSummary) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["environmentName"] = value["environment_name"]
    out["id"] = value["id"]
    if "created_at" in value:
        import capo_amplifyuibuilder._protocol.serialize

        out["createdAt"] = capo_amplifyuibuilder._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "modified_at" in value:
        import capo_amplifyuibuilder._protocol.serialize

        out["modifiedAt"] = capo_amplifyuibuilder._protocol.serialize.fmt_date_time(
            value["modified_at"]
        )
    return out


def deserialize_json(data: dict) -> CodegenJobSummary:
    out: CodegenJobSummary = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    else:
        out["environment_name"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("modifiedAt") is not None:
        import datetime

        out["modified_at"] = datetime.datetime.fromisoformat(
            data["modifiedAt"].replace("Z", "+00:00")
        )
    return out

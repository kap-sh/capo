"""Generated from Smithy shape ``com.amazonaws.glue#GetSystemLogsForSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string


class GetSystemLogsForSessionRequest(TypedDict, closed=True):
    id: "capo_glue.types.name_string.NameString"
    """<p>The ID of the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSystemLogsForSessionRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSystemLogsForSessionRequest:
    out: GetSystemLogsForSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.tnb#ListSolFunctionInstanceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class ListSolFunctionInstanceMetadata(TypedDict, closed=True):
    created_at: "datetime.datetime"
    """<p>When the network function instance was created.</p>"""
    last_modified: "datetime.datetime"
    """<p>When the network function instance was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSolFunctionInstanceMetadata) -> dict:
    out: dict = {}
    import capo_tnb._protocol.serialize

    out["createdAt"] = capo_tnb._protocol.serialize.fmt_date_time(value["created_at"])
    import capo_tnb._protocol.serialize

    out["lastModified"] = capo_tnb._protocol.serialize.fmt_date_time(
        value["last_modified"]
    )
    return out


def deserialize_json(data: dict) -> ListSolFunctionInstanceMetadata:
    out: ListSolFunctionInstanceMetadata = {}  # type: ignore[typeddict-item]
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastModified") is not None:
        import datetime

        out["last_modified"] = datetime.datetime.fromisoformat(
            data["lastModified"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["last_modified"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out

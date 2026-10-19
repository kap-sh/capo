"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#StreamingAccessDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime


class StreamingAccessDetails(TypedDict, closed=True):
    service_principal: "str"
    """<p>The service principal of the Amazon Web Services service that has streaming access to your Resource Explorer data. A service principal is a unique identifier for an Amazon Web Services service.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time when streaming access was granted to the Amazon Web Services service, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamingAccessDetails) -> dict:
    out: dict = {}
    out["ServicePrincipal"] = value["service_principal"]
    import capo_resource_explorer_2._protocol.serialize

    out["CreatedAt"] = capo_resource_explorer_2._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> StreamingAccessDetails:
    out: StreamingAccessDetails = {}  # type: ignore[typeddict-item]
    if data.get("ServicePrincipal") is not None:
        out["service_principal"] = data["ServicePrincipal"]
    else:
        out["service_principal"] = ""
    if data.get("CreatedAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["CreatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out

"""Generated from Smithy shape ``com.amazonaws.inspector2#ConnectorHealth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_inspector2.types.connector_health_status


class ConnectorHealth(TypedDict, closed=True):
    connector_status: (
        "capo_inspector2.types.connector_health_status.ConnectorHealthStatus"
    )
    """<p>The health status of the connector.</p>"""
    last_checked_at: "datetime.datetime"
    """<p>The date and time when the connector health was last checked.</p>"""
    message: NotRequired["str"]
    """<p>A message providing additional details about the connector health status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConnectorHealth) -> dict:
    out: dict = {}
    import capo_inspector2.types.connector_health_status

    out["connectorStatus"] = (
        capo_inspector2.types.connector_health_status.serialize_json(
            value["connector_status"]
        )
    )
    import capo_inspector2._protocol.serialize

    out["lastCheckedAt"] = capo_inspector2._protocol.serialize.fmt_date_time(
        value["last_checked_at"]
    )
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ConnectorHealth:
    out: ConnectorHealth = {}  # type: ignore[typeddict-item]
    if data.get("connectorStatus") is not None:
        import capo_inspector2.types.connector_health_status

        out["connector_status"] = (
            capo_inspector2.types.connector_health_status.deserialize_json(
                data["connectorStatus"]
            )
        )
    else:
        import typing

        out["connector_status"] = typing.cast(
            "capo_inspector2.types.connector_health_status.ConnectorHealthStatus", ""
        )
    if data.get("lastCheckedAt") is not None:
        import datetime

        out["last_checked_at"] = datetime.datetime.fromisoformat(
            data["lastCheckedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["last_checked_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out

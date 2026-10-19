"""Generated from Smithy shape ``com.amazonaws.grafana#ServiceAccountTokenSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class ServiceAccountTokenSummary(TypedDict, closed=True):
    id: "str"
    """<p>The unique ID of the service account token.</p>"""
    name: "str"
    """<p>The name of the service account token.</p>"""
    created_at: "datetime.datetime"
    """<p>When the service account token was created.</p>"""
    expires_at: "datetime.datetime"
    """<p>When the service account token will expire.</p>"""
    last_used_at: NotRequired["datetime.datetime"]
    """<p>The last time the token was used to authorize a Grafana HTTP API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceAccountTokenSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_grafana.types._prelude.timestamp

    out["createdAt"] = capo_grafana.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_grafana.types._prelude.timestamp

    out["expiresAt"] = capo_grafana.types._prelude.timestamp.serialize_json(
        value["expires_at"]
    )
    if "last_used_at" in value:
        import capo_grafana.types._prelude.timestamp

        out["lastUsedAt"] = capo_grafana.types._prelude.timestamp.serialize_json(
            value["last_used_at"]
        )
    return out


def deserialize_json(data: dict) -> ServiceAccountTokenSummary:
    out: ServiceAccountTokenSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("createdAt") is not None:
        import capo_grafana.types._prelude.timestamp

        out["created_at"] = capo_grafana.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("expiresAt") is not None:
        import capo_grafana.types._prelude.timestamp

        out["expires_at"] = capo_grafana.types._prelude.timestamp.deserialize_json(
            data["expiresAt"]
        )
    else:
        import datetime

        out["expires_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastUsedAt") is not None:
        import capo_grafana.types._prelude.timestamp

        out["last_used_at"] = capo_grafana.types._prelude.timestamp.deserialize_json(
            data["lastUsedAt"]
        )
    return out

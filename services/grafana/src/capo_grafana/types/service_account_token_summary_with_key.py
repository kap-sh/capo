"""Generated from Smithy shape ``com.amazonaws.grafana#ServiceAccountTokenSummaryWithKey``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.service_account_token_key


class ServiceAccountTokenSummaryWithKey(TypedDict, closed=True):
    id: "str"
    """<p>The unique ID of the service account token.</p>"""
    name: "str"
    """<p>The name of the service account token.</p>"""
    key: "capo_grafana.types.service_account_token_key.ServiceAccountTokenKey"
    """<p>The key for the service account token. Used when making calls to the Grafana HTTP APIs to authenticate and authorize the requests.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceAccountTokenSummaryWithKey) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["key"] = value["key"]
    return out


def deserialize_json(data: dict) -> ServiceAccountTokenSummaryWithKey:
    out: ServiceAccountTokenSummaryWithKey = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    return out


def redact_sensitive(value: ServiceAccountTokenSummaryWithKey) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key" in value:
        out["key"] = "*** Sensitive Data Redacted ***"
    return out

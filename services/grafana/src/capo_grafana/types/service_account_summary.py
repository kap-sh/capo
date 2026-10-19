"""Generated from Smithy shape ``com.amazonaws.grafana#ServiceAccountSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.role


class ServiceAccountSummary(TypedDict, closed=True):
    id: "str"
    """<p>The unique ID of the service account.</p>"""
    name: "str"
    """<p>The name of the service account.</p>"""
    is_disabled: "str"
    """<p>Returns true if the service account is disabled. Service accounts can be disabled and enabled in the Amazon Managed Grafana console.</p>"""
    grafana_role: "capo_grafana.types.role.Role"
    """<p>The role of the service account, which sets the permission level used when calling Grafana APIs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceAccountSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    out["isDisabled"] = value["is_disabled"]
    out["grafanaRole"] = value["grafana_role"]
    return out


def deserialize_json(data: dict) -> ServiceAccountSummary:
    out: ServiceAccountSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("isDisabled") is not None:
        out["is_disabled"] = data["isDisabled"]
    else:
        out["is_disabled"] = ""
    if data.get("grafanaRole") is not None:
        out["grafana_role"] = data["grafanaRole"]
    else:
        out["grafana_role"] = ""
    return out

"""Generated from Smithy shape ``com.amazonaws.geoplaces#BusinessChain``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.sensitive_string


class BusinessChain(TypedDict, closed=True):
    name: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The business chain name.</p>"""
    id: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The Business Chain Id.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BusinessChain) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    return out


def deserialize_json(data: dict) -> BusinessChain:
    out: BusinessChain = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    return out


def redact_sensitive(value: BusinessChain) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "id" in value:
        out["id"] = "*** Sensitive Data Redacted ***"
    return out

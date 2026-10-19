"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ColdStorageOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.boolean


class ColdStorageOptions(TypedDict, closed=True):
    enabled: "capo_elasticsearch_service.types.boolean.Boolean"
    """<p>Enable cold storage option. Accepted values true or false</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColdStorageOptions) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> ColdStorageOptions:
    out: ColdStorageOptions = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out

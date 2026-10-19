"""Generated from Smithy shape ``com.amazonaws.opensearch#PackageVendingOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean


class PackageVendingOptions(TypedDict, closed=True):
    vending_enabled: "capo_opensearch.types.boolean.Boolean"
    """<p>Indicates whether the package vending feature is enabled, allowing the package to be used by other users.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PackageVendingOptions) -> dict:
    out: dict = {}
    out["VendingEnabled"] = value["vending_enabled"]
    return out


def deserialize_json(data: dict) -> PackageVendingOptions:
    out: PackageVendingOptions = {}  # type: ignore[typeddict-item]
    if data.get("VendingEnabled") is not None:
        out["vending_enabled"] = data["VendingEnabled"]
    else:
        out["vending_enabled"] = False
    return out

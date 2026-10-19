"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#PrivateKeyFlagsV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.client_compatibility_v2


class PrivateKeyFlagsV2(TypedDict, closed=True):
    exportable_key: NotRequired["bool"]
    """<p>Allows the private key to be exported.</p>"""
    strong_key_protection_required: NotRequired["bool"]
    """<p>Require user input when using the private key for enrollment.</p>"""
    client_version: (
        "capo_pca_connector_ad.types.client_compatibility_v2.ClientCompatibilityV2"
    )
    """<p>Defines the minimum client compatibility.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivateKeyFlagsV2) -> dict:
    out: dict = {}
    if "exportable_key" in value:
        out["ExportableKey"] = value["exportable_key"]
    if "strong_key_protection_required" in value:
        out["StrongKeyProtectionRequired"] = value["strong_key_protection_required"]
    import capo_pca_connector_ad.types.client_compatibility_v2

    out["ClientVersion"] = (
        capo_pca_connector_ad.types.client_compatibility_v2.serialize_json(
            value["client_version"]
        )
    )
    return out


def deserialize_json(data: dict) -> PrivateKeyFlagsV2:
    out: PrivateKeyFlagsV2 = {}  # type: ignore[typeddict-item]
    if data.get("ExportableKey") is not None:
        out["exportable_key"] = data["ExportableKey"]
    if data.get("StrongKeyProtectionRequired") is not None:
        out["strong_key_protection_required"] = data["StrongKeyProtectionRequired"]
    if data.get("ClientVersion") is not None:
        import capo_pca_connector_ad.types.client_compatibility_v2

        out["client_version"] = (
            capo_pca_connector_ad.types.client_compatibility_v2.deserialize_json(
                data["ClientVersion"]
            )
        )
    else:
        import typing

        out["client_version"] = typing.cast(
            "capo_pca_connector_ad.types.client_compatibility_v2.ClientCompatibilityV2",
            "",
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#PrivateKeyFlagsV3``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.client_compatibility_v3


class PrivateKeyFlagsV3(TypedDict, closed=True):
    exportable_key: NotRequired["bool"]
    """<p>Allows the private key to be exported.</p>"""
    strong_key_protection_required: NotRequired["bool"]
    """<p>Requirer user input when using the private key for enrollment.</p>"""
    require_alternate_signature_algorithm: NotRequired["bool"]
    """<p>Reguires the PKCS #1 v2.1 signature format for certificates. You should verify that your CA, objects, and applications can accept this signature format.</p>"""
    client_version: (
        "capo_pca_connector_ad.types.client_compatibility_v3.ClientCompatibilityV3"
    )
    """<p>Defines the minimum client compatibility.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivateKeyFlagsV3) -> dict:
    out: dict = {}
    if "exportable_key" in value:
        out["ExportableKey"] = value["exportable_key"]
    if "strong_key_protection_required" in value:
        out["StrongKeyProtectionRequired"] = value["strong_key_protection_required"]
    if "require_alternate_signature_algorithm" in value:
        out["RequireAlternateSignatureAlgorithm"] = value[
            "require_alternate_signature_algorithm"
        ]
    import capo_pca_connector_ad.types.client_compatibility_v3

    out["ClientVersion"] = (
        capo_pca_connector_ad.types.client_compatibility_v3.serialize_json(
            value["client_version"]
        )
    )
    return out


def deserialize_json(data: dict) -> PrivateKeyFlagsV3:
    out: PrivateKeyFlagsV3 = {}  # type: ignore[typeddict-item]
    if data.get("ExportableKey") is not None:
        out["exportable_key"] = data["ExportableKey"]
    if data.get("StrongKeyProtectionRequired") is not None:
        out["strong_key_protection_required"] = data["StrongKeyProtectionRequired"]
    if data.get("RequireAlternateSignatureAlgorithm") is not None:
        out["require_alternate_signature_algorithm"] = data[
            "RequireAlternateSignatureAlgorithm"
        ]
    if data.get("ClientVersion") is not None:
        import capo_pca_connector_ad.types.client_compatibility_v3

        out["client_version"] = (
            capo_pca_connector_ad.types.client_compatibility_v3.deserialize_json(
                data["ClientVersion"]
            )
        )
    else:
        import typing

        out["client_version"] = typing.cast(
            "capo_pca_connector_ad.types.client_compatibility_v3.ClientCompatibilityV3",
            "",
        )
    return out

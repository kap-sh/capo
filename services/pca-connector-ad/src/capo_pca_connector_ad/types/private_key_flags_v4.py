"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#PrivateKeyFlagsV4``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.client_compatibility_v4


class PrivateKeyFlagsV4(TypedDict, closed=True):
    exportable_key: NotRequired["bool"]
    """<p>Allows the private key to be exported.</p>"""
    strong_key_protection_required: NotRequired["bool"]
    """<p>Require user input when using the private key for enrollment.</p>"""
    require_alternate_signature_algorithm: NotRequired["bool"]
    """<p>Requires the PKCS #1 v2.1 signature format for certificates. You should verify that your CA, objects, and applications can accept this signature format.</p>"""
    require_same_key_renewal: NotRequired["bool"]
    """<p>Renew certificate using the same private key.</p>"""
    use_legacy_provider: NotRequired["bool"]
    """<p>Specifies the cryptographic service provider category used to generate private keys. Set to TRUE to use Legacy Cryptographic Service Providers and FALSE to use Key Storage Providers.</p>"""
    client_version: (
        "capo_pca_connector_ad.types.client_compatibility_v4.ClientCompatibilityV4"
    )
    """<p>Defines the minimum client compatibility.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivateKeyFlagsV4) -> dict:
    out: dict = {}
    if "exportable_key" in value:
        out["ExportableKey"] = value["exportable_key"]
    if "strong_key_protection_required" in value:
        out["StrongKeyProtectionRequired"] = value["strong_key_protection_required"]
    if "require_alternate_signature_algorithm" in value:
        out["RequireAlternateSignatureAlgorithm"] = value[
            "require_alternate_signature_algorithm"
        ]
    if "require_same_key_renewal" in value:
        out["RequireSameKeyRenewal"] = value["require_same_key_renewal"]
    if "use_legacy_provider" in value:
        out["UseLegacyProvider"] = value["use_legacy_provider"]
    import capo_pca_connector_ad.types.client_compatibility_v4

    out["ClientVersion"] = (
        capo_pca_connector_ad.types.client_compatibility_v4.serialize_json(
            value["client_version"]
        )
    )
    return out


def deserialize_json(data: dict) -> PrivateKeyFlagsV4:
    out: PrivateKeyFlagsV4 = {}  # type: ignore[typeddict-item]
    if data.get("ExportableKey") is not None:
        out["exportable_key"] = data["ExportableKey"]
    if data.get("StrongKeyProtectionRequired") is not None:
        out["strong_key_protection_required"] = data["StrongKeyProtectionRequired"]
    if data.get("RequireAlternateSignatureAlgorithm") is not None:
        out["require_alternate_signature_algorithm"] = data[
            "RequireAlternateSignatureAlgorithm"
        ]
    if data.get("RequireSameKeyRenewal") is not None:
        out["require_same_key_renewal"] = data["RequireSameKeyRenewal"]
    if data.get("UseLegacyProvider") is not None:
        out["use_legacy_provider"] = data["UseLegacyProvider"]
    if data.get("ClientVersion") is not None:
        import capo_pca_connector_ad.types.client_compatibility_v4

        out["client_version"] = (
            capo_pca_connector_ad.types.client_compatibility_v4.deserialize_json(
                data["ClientVersion"]
            )
        )
    else:
        import typing

        out["client_version"] = typing.cast(
            "capo_pca_connector_ad.types.client_compatibility_v4.ClientCompatibilityV4",
            "",
        )
    return out

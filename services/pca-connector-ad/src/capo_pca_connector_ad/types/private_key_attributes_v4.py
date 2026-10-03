"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#PrivateKeyAttributesV4``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pca_connector_ad.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.crypto_providers_list
    import capo_pca_connector_ad.types.key_spec
    import capo_pca_connector_ad.types.key_usage_property
    import capo_pca_connector_ad.types.private_key_algorithm


class PrivateKeyAttributesV4(TypedDict, closed=True):
    minimal_key_length: "int"
    """<p>Set the minimum key length of the private key.</p>"""
    key_spec: "capo_pca_connector_ad.types.key_spec.KeySpec"
    """<p>Defines the purpose of the private key. Set it to "KEY_EXCHANGE" or "SIGNATURE" value.</p>"""
    crypto_providers: NotRequired[
        "capo_pca_connector_ad.types.crypto_providers_list.CryptoProvidersList"
    ]
    """<p>Defines the cryptographic providers used to generate the private key.</p>"""
    key_usage_property: NotRequired[
        "capo_pca_connector_ad.types.key_usage_property.KeyUsageProperty"
    ]
    """<p>The key usage property defines the purpose of the private key contained in the certificate. You can specify specific purposes using property flags or all by using property type ALL.</p>"""
    algorithm: NotRequired[
        "capo_pca_connector_ad.types.private_key_algorithm.PrivateKeyAlgorithm"
    ]
    """<p>Defines the algorithm used to generate the private key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrivateKeyAttributesV4) -> dict:
    out: dict = {}
    out["MinimalKeyLength"] = value["minimal_key_length"]
    import capo_pca_connector_ad.types.key_spec

    out["KeySpec"] = capo_pca_connector_ad.types.key_spec.serialize_json(
        value["key_spec"]
    )
    if "crypto_providers" in value:
        import capo_pca_connector_ad.types.crypto_providers_list

        out["CryptoProviders"] = (
            capo_pca_connector_ad.types.crypto_providers_list.serialize_json(
                value["crypto_providers"]
            )
        )
    if "key_usage_property" in value:
        import capo_pca_connector_ad.types.key_usage_property

        out["KeyUsageProperty"] = (
            capo_pca_connector_ad.types.key_usage_property.serialize_json(
                value["key_usage_property"]
            )
        )
    if "algorithm" in value:
        import capo_pca_connector_ad.types.private_key_algorithm

        out["Algorithm"] = (
            capo_pca_connector_ad.types.private_key_algorithm.serialize_json(
                value["algorithm"]
            )
        )
    return out


def deserialize_json(data: dict) -> PrivateKeyAttributesV4:
    out: PrivateKeyAttributesV4 = {}  # type: ignore[typeddict-item]
    if data.get("MinimalKeyLength") is not None:
        out["minimal_key_length"] = data["MinimalKeyLength"]
    else:
        raise DeserializationError("PrivateKeyAttributesV4.minimal_key_length required")
    if data.get("KeySpec") is not None:
        import capo_pca_connector_ad.types.key_spec

        out["key_spec"] = capo_pca_connector_ad.types.key_spec.deserialize_json(
            data["KeySpec"]
        )
    else:
        raise DeserializationError("PrivateKeyAttributesV4.key_spec required")
    if data.get("CryptoProviders") is not None:
        import capo_pca_connector_ad.types.crypto_providers_list

        out["crypto_providers"] = (
            capo_pca_connector_ad.types.crypto_providers_list.deserialize_json(
                data["CryptoProviders"]
            )
        )
    if data.get("KeyUsageProperty") is not None:
        import capo_pca_connector_ad.types.key_usage_property

        out["key_usage_property"] = (
            capo_pca_connector_ad.types.key_usage_property.deserialize_json(
                data["KeyUsageProperty"]
            )
        )
    if data.get("Algorithm") is not None:
        import capo_pca_connector_ad.types.private_key_algorithm

        out["algorithm"] = (
            capo_pca_connector_ad.types.private_key_algorithm.deserialize_json(
                data["Algorithm"]
            )
        )
    return out

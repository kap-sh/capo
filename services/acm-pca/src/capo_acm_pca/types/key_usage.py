"""Generated from Smithy shape ``com.amazonaws.acmpca#KeyUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.boolean


class KeyUsage(TypedDict, closed=True):
    digital_signature: "capo_acm_pca.types.boolean.Boolean"
    """<p> Key can be used for digital signing.</p>"""
    non_repudiation: "capo_acm_pca.types.boolean.Boolean"
    """<p>Key can be used for non-repudiation.</p>"""
    key_encipherment: "capo_acm_pca.types.boolean.Boolean"
    """<p>Key can be used to encipher data.</p>"""
    data_encipherment: "capo_acm_pca.types.boolean.Boolean"
    """<p>Key can be used to decipher data.</p>"""
    key_agreement: "capo_acm_pca.types.boolean.Boolean"
    """<p>Key can be used in a key-agreement protocol.</p>"""
    key_cert_sign: "capo_acm_pca.types.boolean.Boolean"
    """<p>Key can be used to sign certificates.</p>"""
    crl_sign: "capo_acm_pca.types.boolean.Boolean"
    """<p>Key can be used to sign CRLs.</p>"""
    encipher_only: "capo_acm_pca.types.boolean.Boolean"
    """<p>Key can be used only to encipher data.</p>"""
    decipher_only: "capo_acm_pca.types.boolean.Boolean"
    """<p>Key can be used only to decipher data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyUsage) -> dict:
    out: dict = {}
    out["DigitalSignature"] = value.get("digital_signature", False)
    out["NonRepudiation"] = value.get("non_repudiation", False)
    out["KeyEncipherment"] = value.get("key_encipherment", False)
    out["DataEncipherment"] = value.get("data_encipherment", False)
    out["KeyAgreement"] = value.get("key_agreement", False)
    out["KeyCertSign"] = value.get("key_cert_sign", False)
    out["CRLSign"] = value.get("crl_sign", False)
    out["EncipherOnly"] = value.get("encipher_only", False)
    out["DecipherOnly"] = value.get("decipher_only", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> KeyUsage:
    out: KeyUsage = {}  # type: ignore[typeddict-item]
    if data.get("DigitalSignature") is not None:
        out["digital_signature"] = data["DigitalSignature"]
    else:
        out["digital_signature"] = False
    if data.get("NonRepudiation") is not None:
        out["non_repudiation"] = data["NonRepudiation"]
    else:
        out["non_repudiation"] = False
    if data.get("KeyEncipherment") is not None:
        out["key_encipherment"] = data["KeyEncipherment"]
    else:
        out["key_encipherment"] = False
    if data.get("DataEncipherment") is not None:
        out["data_encipherment"] = data["DataEncipherment"]
    else:
        out["data_encipherment"] = False
    if data.get("KeyAgreement") is not None:
        out["key_agreement"] = data["KeyAgreement"]
    else:
        out["key_agreement"] = False
    if data.get("KeyCertSign") is not None:
        out["key_cert_sign"] = data["KeyCertSign"]
    else:
        out["key_cert_sign"] = False
    if data.get("CRLSign") is not None:
        out["crl_sign"] = data["CRLSign"]
    else:
        out["crl_sign"] = False
    if data.get("EncipherOnly") is not None:
        out["encipher_only"] = data["EncipherOnly"]
    else:
        out["encipher_only"] = False
    if data.get("DecipherOnly") is not None:
        out["decipher_only"] = data["DecipherOnly"]
    else:
        out["decipher_only"] = False
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: KeyUsage) -> dict:
    out: dict = {}
    out["DigitalSignature"] = value.get("digital_signature", False)
    out["NonRepudiation"] = value.get("non_repudiation", False)
    out["KeyEncipherment"] = value.get("key_encipherment", False)
    out["DataEncipherment"] = value.get("data_encipherment", False)
    out["KeyAgreement"] = value.get("key_agreement", False)
    out["KeyCertSign"] = value.get("key_cert_sign", False)
    out["CRLSign"] = value.get("crl_sign", False)
    out["EncipherOnly"] = value.get("encipher_only", False)
    out["DecipherOnly"] = value.get("decipher_only", False)
    return out


def deserialize_cbor(data: dict) -> KeyUsage:
    out: KeyUsage = {}  # type: ignore[typeddict-item]
    if data.get("DigitalSignature") is not None:
        out["digital_signature"] = data["DigitalSignature"]
    else:
        out["digital_signature"] = False
    if data.get("NonRepudiation") is not None:
        out["non_repudiation"] = data["NonRepudiation"]
    else:
        out["non_repudiation"] = False
    if data.get("KeyEncipherment") is not None:
        out["key_encipherment"] = data["KeyEncipherment"]
    else:
        out["key_encipherment"] = False
    if data.get("DataEncipherment") is not None:
        out["data_encipherment"] = data["DataEncipherment"]
    else:
        out["data_encipherment"] = False
    if data.get("KeyAgreement") is not None:
        out["key_agreement"] = data["KeyAgreement"]
    else:
        out["key_agreement"] = False
    if data.get("KeyCertSign") is not None:
        out["key_cert_sign"] = data["KeyCertSign"]
    else:
        out["key_cert_sign"] = False
    if data.get("CRLSign") is not None:
        out["crl_sign"] = data["CRLSign"]
    else:
        out["crl_sign"] = False
    if data.get("EncipherOnly") is not None:
        out["encipher_only"] = data["EncipherOnly"]
    else:
        out["encipher_only"] = False
    if data.get("DecipherOnly") is not None:
        out["decipher_only"] = data["DecipherOnly"]
    else:
        out["decipher_only"] = False
    return out

"""Generated from Smithy shape ``com.amazonaws.acmpca#ApiPassthrough``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm_pca.types.asn1_subject
    import capo_acm_pca.types.extensions


class ApiPassthrough(TypedDict, closed=True):
    extensions: NotRequired["capo_acm_pca.types.extensions.Extensions"]
    """<p>Specifies X.509 extension information for a certificate.</p>"""
    subject: NotRequired["capo_acm_pca.types.asn1_subject.ASN1Subject"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApiPassthrough) -> dict:
    out: dict = {}
    if "extensions" in value:
        import capo_acm_pca.types.extensions

        out["Extensions"] = capo_acm_pca.types.extensions.serialize_aws_json_1_1(
            value["extensions"]
        )
    if "subject" in value:
        import capo_acm_pca.types.asn1_subject

        out["Subject"] = capo_acm_pca.types.asn1_subject.serialize_aws_json_1_1(
            value["subject"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApiPassthrough:
    out: ApiPassthrough = {}  # type: ignore[typeddict-item]
    if data.get("Extensions") is not None:
        import capo_acm_pca.types.extensions

        out["extensions"] = capo_acm_pca.types.extensions.deserialize_aws_json_1_1(
            data["Extensions"]
        )
    if data.get("Subject") is not None:
        import capo_acm_pca.types.asn1_subject

        out["subject"] = capo_acm_pca.types.asn1_subject.deserialize_aws_json_1_1(
            data["Subject"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ApiPassthrough) -> dict:
    out: dict = {}
    if "extensions" in value:
        import capo_acm_pca.types.extensions

        out["Extensions"] = capo_acm_pca.types.extensions.serialize_cbor(
            value["extensions"]
        )
    if "subject" in value:
        import capo_acm_pca.types.asn1_subject

        out["Subject"] = capo_acm_pca.types.asn1_subject.serialize_cbor(
            value["subject"]
        )
    return out


def deserialize_cbor(data: dict) -> ApiPassthrough:
    out: ApiPassthrough = {}  # type: ignore[typeddict-item]
    if data.get("Extensions") is not None:
        import capo_acm_pca.types.extensions

        out["extensions"] = capo_acm_pca.types.extensions.deserialize_cbor(
            data["Extensions"]
        )
    if data.get("Subject") is not None:
        import capo_acm_pca.types.asn1_subject

        out["subject"] = capo_acm_pca.types.asn1_subject.deserialize_cbor(
            data["Subject"]
        )
    return out

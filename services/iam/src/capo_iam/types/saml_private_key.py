"""Generated from Smithy shape ``com.amazonaws.iam#SAMLPrivateKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.date_type
    import capo_iam.types.private_key_id_type


class SAMLPrivateKey(TypedDict, closed=True):
    key_id: NotRequired["capo_iam.types.private_key_id_type.privateKeyIdType"]
    """<p>The unique identifier for the SAML private key.</p>"""
    timestamp: NotRequired["capo_iam.types.date_type.dateType"]
    """<p>The date and time, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time </a> format, when the private key was uploaded.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SAMLPrivateKey, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "key_id" in value:
        pairs.append((f"{key_prefix}KeyId", str(value["key_id"])))
    if "timestamp" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["timestamp"], pairs, f"{key_prefix}Timestamp"
        )


def deserialize_query(el: Element) -> SAMLPrivateKey:
    out: SAMLPrivateKey = {}  # type: ignore[typeddict-item]
    child_key_id = el.find("KeyId")
    if child_key_id is not None:
        out["key_id"] = str(child_key_id.text or "")
    child_timestamp = el.find("Timestamp")
    if child_timestamp is not None:
        import capo_iam.types.date_type

        out["timestamp"] = capo_iam.types.date_type.deserialize_query(child_timestamp)
    return out

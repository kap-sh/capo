"""Generated from Smithy shape ``com.amazonaws.ec2#KeyPair``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.sensitive_user_data
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class KeyPair(TypedDict, closed=True):
    key_pair_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the key pair.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags applied to the key pair.</p>"""
    key_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the key pair.</p>"""
    key_fingerprint: NotRequired["capo_ec2.types.string.String"]
    """<ul> <li> <p>For RSA key pairs, the key fingerprint is the SHA-1 digest of the DER encoded private key.</p> </li> <li> <p>For ED25519 key pairs, the key fingerprint is the base64-encoded SHA-256 digest, which is the default for OpenSSH, starting with OpenSSH 6.8.</p> </li> </ul>"""
    key_material: NotRequired["capo_ec2.types.sensitive_user_data.SensitiveUserData"]
    """<p>An unencrypted PEM encoded RSA or ED25519 private key.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: KeyPair, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "key_pair_id" in value:
        pairs.append((f"{key_prefix}KeyPairId", str(value["key_pair_id"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "key_name" in value:
        pairs.append((f"{key_prefix}KeyName", str(value["key_name"])))
    if "key_fingerprint" in value:
        pairs.append((f"{key_prefix}KeyFingerprint", str(value["key_fingerprint"])))
    if "key_material" in value:
        pairs.append((f"{key_prefix}KeyMaterial", str(value["key_material"])))


def deserialize_ec2_query(el: Element) -> KeyPair:
    out: KeyPair = {}  # type: ignore[typeddict-item]
    child_key_pair_id = el.find("keyPairId")
    if child_key_pair_id is not None:
        out["key_pair_id"] = str(child_key_pair_id.text or "")
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_key_name = el.find("keyName")
    if child_key_name is not None:
        out["key_name"] = str(child_key_name.text or "")
    child_key_fingerprint = el.find("keyFingerprint")
    if child_key_fingerprint is not None:
        out["key_fingerprint"] = str(child_key_fingerprint.text or "")
    child_key_material = el.find("keyMaterial")
    if child_key_material is not None:
        out["key_material"] = str(child_key_material.text or "")
    return out


def redact_sensitive(value: KeyPair) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key_material" in value:
        out["key_material"] = "*** Sensitive Data Redacted ***"
    return out

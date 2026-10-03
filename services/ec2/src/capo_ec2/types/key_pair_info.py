"""Generated from Smithy shape ``com.amazonaws.ec2#KeyPairInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.key_type
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class KeyPairInfo(TypedDict, closed=True):
    key_pair_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the key pair.</p>"""
    key_type: NotRequired["capo_ec2.types.key_type.KeyType"]
    """<p>The type of key pair.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags applied to the key pair.</p>"""
    public_key: NotRequired["capo_ec2.types.string.String"]
    """<p>The public key material.</p>"""
    create_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>If you used Amazon EC2 to create the key pair, this is the date and time when the key was created, in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601 date-time format</a>, in the UTC time zone.</p> <p>If you imported an existing key pair to Amazon EC2, this is the date and time the key was imported, in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601 date-time format</a>, in the UTC time zone.</p>"""
    key_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the key pair.</p>"""
    key_fingerprint: NotRequired["capo_ec2.types.string.String"]
    """<p>If you used <a>CreateKeyPair</a> to create the key pair:</p> <ul> <li> <p>For RSA key pairs, the key fingerprint is the SHA-1 digest of the DER encoded private key.</p> </li> <li> <p>For ED25519 key pairs, the key fingerprint is the base64-encoded SHA-256 digest, which is the default for OpenSSH, starting with <a href="http://www.openssh.com/txt/release-6.8">OpenSSH 6.8</a>.</p> </li> </ul> <p>If you used <a>ImportKeyPair</a> to provide Amazon Web Services the public key:</p> <ul> <li> <p>For RSA key pairs, the key fingerprint is the MD5 public key fingerprint as specified in section 4 of RFC4716.</p> </li> <li> <p>For ED25519 key pairs, the key fingerprint is the base64-encoded SHA-256 digest, which is the default for OpenSSH, starting with <a href="http://www.openssh.com/txt/release-6.8">OpenSSH 6.8</a>.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: KeyPairInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "key_pair_id" in value:
        pairs.append((f"{key_prefix}KeyPairId", str(value["key_pair_id"])))
    if "key_type" in value:
        import capo_ec2.types.key_type

        capo_ec2.types.key_type.serialize_ec2_query(
            value["key_type"], pairs, f"{key_prefix}KeyType"
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "public_key" in value:
        pairs.append((f"{key_prefix}PublicKey", str(value["public_key"])))
    if "create_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["create_time"], pairs, f"{key_prefix}CreateTime"
        )
    if "key_name" in value:
        pairs.append((f"{key_prefix}KeyName", str(value["key_name"])))
    if "key_fingerprint" in value:
        pairs.append((f"{key_prefix}KeyFingerprint", str(value["key_fingerprint"])))


def deserialize_ec2_query(el: Element) -> KeyPairInfo:
    out: KeyPairInfo = {}  # type: ignore[typeddict-item]
    child_key_pair_id = el.find("keyPairId")
    if child_key_pair_id is not None:
        out["key_pair_id"] = str(child_key_pair_id.text or "")
    child_key_type = el.find("keyType")
    if child_key_type is not None:
        import capo_ec2.types.key_type

        out["key_type"] = capo_ec2.types.key_type.deserialize_ec2_query(child_key_type)
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_public_key = el.find("publicKey")
    if child_public_key is not None:
        out["public_key"] = str(child_public_key.text or "")
    child_create_time = el.find("createTime")
    if child_create_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["create_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_create_time
        )
    child_key_name = el.find("keyName")
    if child_key_name is not None:
        out["key_name"] = str(child_key_name.text or "")
    child_key_fingerprint = el.find("keyFingerprint")
    if child_key_fingerprint is not None:
        out["key_fingerprint"] = str(child_key_fingerprint.text or "")
    return out

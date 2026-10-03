"""Generated from Smithy shape ``com.amazonaws.route53#KeySigningKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.signing_key_integer
    import capo_route_53.types.signing_key_name
    import capo_route_53.types.signing_key_status
    import capo_route_53.types.signing_key_status_message
    import capo_route_53.types.signing_key_string
    import capo_route_53.types.signing_key_tag
    import capo_route_53.types.time_stamp


class KeySigningKey(TypedDict, closed=True):
    name: NotRequired["capo_route_53.types.signing_key_name.SigningKeyName"]
    """<p>A string used to identify a key-signing key (KSK). <code>Name</code> can include numbers, letters, and underscores (_). <code>Name</code> must be unique for each key-signing key in the same hosted zone.</p>"""
    kms_arn: NotRequired["capo_route_53.types.signing_key_string.SigningKeyString"]
    """<p>The Amazon resource name (ARN) used to identify the customer managed key in Key Management Service (KMS). The <code>KmsArn</code> must be unique for each key-signing key (KSK) in a single hosted zone.</p> <p>You must configure the customer managed key as follows:</p> <dl> <dt>Status</dt> <dd> <p>Enabled</p> </dd> <dt>Key spec</dt> <dd> <p>ECC_NIST_P256</p> </dd> <dt>Key usage</dt> <dd> <p>Sign and verify</p> </dd> <dt>Key policy</dt> <dd> <p>The key policy must give permission for the following actions:</p> <ul> <li> <p>DescribeKey</p> </li> <li> <p>GetPublicKey</p> </li> <li> <p>Sign</p> </li> </ul> <p>The key policy must also include the Amazon Route 53 service in the principal for your account. Specify the following:</p> <ul> <li> <p> <code>"Service": "dnssec-route53.amazonaws.com"</code> </p> </li> </ul> </dd> </dl> <p>For more information about working with the customer managed key in KMS, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html">Key Management Service concepts</a>.</p>"""
    flag: "capo_route_53.types.signing_key_integer.SigningKeyInteger"
    """<p>An integer that specifies how the key is used. For key-signing key (KSK), this value is always 257.</p>"""
    signing_algorithm_mnemonic: NotRequired[
        "capo_route_53.types.signing_key_string.SigningKeyString"
    ]
    """<p>A string used to represent the signing algorithm. This value must follow the guidelines provided by <a href="https://tools.ietf.org/html/rfc8624#section-3.1">RFC-8624 Section 3.1</a>. </p>"""
    signing_algorithm_type: "capo_route_53.types.signing_key_integer.SigningKeyInteger"
    """<p>An integer used to represent the signing algorithm. This value must follow the guidelines provided by <a href="https://tools.ietf.org/html/rfc8624#section-3.1">RFC-8624 Section 3.1</a>. </p>"""
    digest_algorithm_mnemonic: NotRequired[
        "capo_route_53.types.signing_key_string.SigningKeyString"
    ]
    """<p>A string used to represent the delegation signer digest algorithm. This value must follow the guidelines provided by <a href="https://tools.ietf.org/html/rfc8624#section-3.3">RFC-8624 Section 3.3</a>. </p>"""
    digest_algorithm_type: "capo_route_53.types.signing_key_integer.SigningKeyInteger"
    """<p>An integer used to represent the delegation signer digest algorithm. This value must follow the guidelines provided by <a href="https://tools.ietf.org/html/rfc8624#section-3.3">RFC-8624 Section 3.3</a>.</p>"""
    key_tag: "capo_route_53.types.signing_key_tag.SigningKeyTag"
    """<p>An integer used to identify the DNSSEC record for the domain name. The process used to calculate the value is described in <a href="https://tools.ietf.org/rfc/rfc4034.txt">RFC-4034 Appendix B</a>.</p>"""
    digest_value: NotRequired["capo_route_53.types.signing_key_string.SigningKeyString"]
    """<p>A cryptographic digest of a DNSKEY resource record (RR). DNSKEY records are used to publish the public key that resolvers can use to verify DNSSEC signatures that are used to secure certain kinds of information provided by the DNS system.</p>"""
    public_key: NotRequired["capo_route_53.types.signing_key_string.SigningKeyString"]
    """<p>The public key, represented as a Base64 encoding, as required by <a href="https://tools.ietf.org/rfc/rfc4034.txt"> RFC-4034 Page 5</a>.</p>"""
    ds_record: NotRequired["capo_route_53.types.signing_key_string.SigningKeyString"]
    """<p>A string that represents a delegation signer (DS) record.</p>"""
    dnskey_record: NotRequired[
        "capo_route_53.types.signing_key_string.SigningKeyString"
    ]
    """<p>A string that represents a DNSKEY record.</p>"""
    status: NotRequired["capo_route_53.types.signing_key_status.SigningKeyStatus"]
    """<p>A string that represents the current key-signing key (KSK) status.</p> <p>Status can have one of the following values:</p> <dl> <dt>ACTIVE</dt> <dd> <p>The KSK is being used for signing.</p> </dd> <dt>INACTIVE</dt> <dd> <p>The KSK is not being used for signing.</p> </dd> <dt>DELETING</dt> <dd> <p>The KSK is in the process of being deleted.</p> </dd> <dt>ACTION_NEEDED</dt> <dd> <p>There is a problem with the KSK that requires you to take action to resolve. For example, the customer managed key might have been deleted, or the permissions for the customer managed key might have been changed.</p> </dd> <dt>INTERNAL_FAILURE</dt> <dd> <p>There was an error during a request. Before you can continue to work with DNSSEC signing, including actions that involve this KSK, you must correct the problem. For example, you may need to activate or deactivate the KSK.</p> </dd> </dl>"""
    status_message: NotRequired[
        "capo_route_53.types.signing_key_status_message.SigningKeyStatusMessage"
    ]
    """<p>The status message provided for the following key-signing key (KSK) statuses: <code>ACTION_NEEDED</code> or <code>INTERNAL_FAILURE</code>. The status message includes information about what the problem might be and steps that you can take to correct the issue.</p>"""
    created_date: NotRequired["capo_route_53.types.time_stamp.TimeStamp"]
    """<p>The date when the key-signing key (KSK) was created.</p>"""
    last_modified_date: NotRequired["capo_route_53.types.time_stamp.TimeStamp"]
    """<p>The last time that the key-signing key (KSK) was changed.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: KeySigningKey, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "name" in value:
        SubElement(el, "Name").text = str(value["name"])
    if "kms_arn" in value:
        SubElement(el, "KmsArn").text = str(value["kms_arn"])
    SubElement(el, "Flag").text = str(value.get("flag", 0))
    if "signing_algorithm_mnemonic" in value:
        SubElement(el, "SigningAlgorithmMnemonic").text = str(
            value["signing_algorithm_mnemonic"]
        )
    SubElement(el, "SigningAlgorithmType").text = str(
        value.get("signing_algorithm_type", 0)
    )
    if "digest_algorithm_mnemonic" in value:
        SubElement(el, "DigestAlgorithmMnemonic").text = str(
            value["digest_algorithm_mnemonic"]
        )
    SubElement(el, "DigestAlgorithmType").text = str(
        value.get("digest_algorithm_type", 0)
    )
    SubElement(el, "KeyTag").text = str(value.get("key_tag", 0))
    if "digest_value" in value:
        SubElement(el, "DigestValue").text = str(value["digest_value"])
    if "public_key" in value:
        SubElement(el, "PublicKey").text = str(value["public_key"])
    if "ds_record" in value:
        SubElement(el, "DSRecord").text = str(value["ds_record"])
    if "dnskey_record" in value:
        SubElement(el, "DNSKEYRecord").text = str(value["dnskey_record"])
    if "status" in value:
        SubElement(el, "Status").text = str(value["status"])
    if "status_message" in value:
        SubElement(el, "StatusMessage").text = str(value["status_message"])
    if "created_date" in value:
        import capo_route_53.types.time_stamp

        capo_route_53.types.time_stamp.serialize_xml(
            value["created_date"], el, "CreatedDate"
        )
    if "last_modified_date" in value:
        import capo_route_53.types.time_stamp

        capo_route_53.types.time_stamp.serialize_xml(
            value["last_modified_date"], el, "LastModifiedDate"
        )


def deserialize_xml(el: Element) -> KeySigningKey:
    out: KeySigningKey = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_kms_arn = el.find("KmsArn")
    if child_kms_arn is not None:
        out["kms_arn"] = str(child_kms_arn.text or "")
    child_flag = el.find("Flag")
    if child_flag is not None:
        out["flag"] = int(child_flag.text or "")
    else:
        out["flag"] = 0
    child_signing_algorithm_mnemonic = el.find("SigningAlgorithmMnemonic")
    if child_signing_algorithm_mnemonic is not None:
        out["signing_algorithm_mnemonic"] = str(
            child_signing_algorithm_mnemonic.text or ""
        )
    child_signing_algorithm_type = el.find("SigningAlgorithmType")
    if child_signing_algorithm_type is not None:
        out["signing_algorithm_type"] = int(child_signing_algorithm_type.text or "")
    else:
        out["signing_algorithm_type"] = 0
    child_digest_algorithm_mnemonic = el.find("DigestAlgorithmMnemonic")
    if child_digest_algorithm_mnemonic is not None:
        out["digest_algorithm_mnemonic"] = str(
            child_digest_algorithm_mnemonic.text or ""
        )
    child_digest_algorithm_type = el.find("DigestAlgorithmType")
    if child_digest_algorithm_type is not None:
        out["digest_algorithm_type"] = int(child_digest_algorithm_type.text or "")
    else:
        out["digest_algorithm_type"] = 0
    child_key_tag = el.find("KeyTag")
    if child_key_tag is not None:
        out["key_tag"] = int(child_key_tag.text or "")
    else:
        out["key_tag"] = 0
    child_digest_value = el.find("DigestValue")
    if child_digest_value is not None:
        out["digest_value"] = str(child_digest_value.text or "")
    child_public_key = el.find("PublicKey")
    if child_public_key is not None:
        out["public_key"] = str(child_public_key.text or "")
    child_ds_record = el.find("DSRecord")
    if child_ds_record is not None:
        out["ds_record"] = str(child_ds_record.text or "")
    child_dnskey_record = el.find("DNSKEYRecord")
    if child_dnskey_record is not None:
        out["dnskey_record"] = str(child_dnskey_record.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_created_date = el.find("CreatedDate")
    if child_created_date is not None:
        import capo_route_53.types.time_stamp

        out["created_date"] = capo_route_53.types.time_stamp.deserialize_xml(
            child_created_date
        )
    child_last_modified_date = el.find("LastModifiedDate")
    if child_last_modified_date is not None:
        import capo_route_53.types.time_stamp

        out["last_modified_date"] = capo_route_53.types.time_stamp.deserialize_xml(
            child_last_modified_date
        )
    return out

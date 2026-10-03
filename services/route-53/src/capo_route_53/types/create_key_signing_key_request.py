"""Generated from Smithy shape ``com.amazonaws.route53#CreateKeySigningKeyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.nonce
    import capo_route_53.types.resource_id
    import capo_route_53.types.signing_key_name
    import capo_route_53.types.signing_key_status
    import capo_route_53.types.signing_key_string


class CreateKeySigningKeyRequest(TypedDict, closed=True):
    caller_reference: "capo_route_53.types.nonce.Nonce"
    """<p>A unique string that identifies the request.</p>"""
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The unique string (ID) used to identify a hosted zone.</p>"""
    key_management_service_arn: (
        "capo_route_53.types.signing_key_string.SigningKeyString"
    )
    """<p>The Amazon resource name (ARN) for a customer managed key in Key Management Service (KMS). The <code>KeyManagementServiceArn</code> must be unique for each key-signing key (KSK) in a single hosted zone. To see an example of <code>KeyManagementServiceArn</code> that grants the correct permissions for DNSSEC, scroll down to <b>Example</b>. </p> <p>You must configure the customer managed customer managed key as follows:</p> <dl> <dt>Status</dt> <dd> <p>Enabled</p> </dd> <dt>Key spec</dt> <dd> <p>ECC_NIST_P256</p> </dd> <dt>Key usage</dt> <dd> <p>Sign and verify</p> </dd> <dt>Key policy</dt> <dd> <p>The key policy must give permission for the following actions:</p> <ul> <li> <p>DescribeKey</p> </li> <li> <p>GetPublicKey</p> </li> <li> <p>Sign</p> </li> </ul> <p>The key policy must also include the Amazon Route 53 service in the principal for your account. Specify the following:</p> <ul> <li> <p> <code>"Service": "dnssec-route53.amazonaws.com"</code> </p> </li> </ul> </dd> </dl> <p>For more information about working with a customer managed key in KMS, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html">Key Management Service concepts</a>.</p>"""
    name: "capo_route_53.types.signing_key_name.SigningKeyName"
    """<p>A string used to identify a key-signing key (KSK). <code>Name</code> can include numbers, letters, and underscores (_). <code>Name</code> must be unique for each key-signing key in the same hosted zone.</p>"""
    status: "capo_route_53.types.signing_key_status.SigningKeyStatus"
    """<p>A string specifying the initial status of the key-signing key (KSK). You can set the value to <code>ACTIVE</code> or <code>INACTIVE</code>.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateKeySigningKeyRequest, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "CallerReference").text = str(value["caller_reference"])
    SubElement(el, "HostedZoneId").text = str(value["hosted_zone_id"])
    SubElement(el, "KeyManagementServiceArn").text = str(
        value["key_management_service_arn"]
    )
    SubElement(el, "Name").text = str(value["name"])
    SubElement(el, "Status").text = str(value["status"])


def deserialize_xml(el: Element) -> CreateKeySigningKeyRequest:
    out: CreateKeySigningKeyRequest = {}  # type: ignore[typeddict-item]
    child_caller_reference = el.find("CallerReference")
    if child_caller_reference is not None:
        out["caller_reference"] = str(child_caller_reference.text or "")
    else:
        raise DeserializationError(
            "CreateKeySigningKeyRequest.caller_reference required"
        )
    child_hosted_zone_id = el.find("HostedZoneId")
    if child_hosted_zone_id is not None:
        out["hosted_zone_id"] = str(child_hosted_zone_id.text or "")
    else:
        raise DeserializationError("CreateKeySigningKeyRequest.hosted_zone_id required")
    child_key_management_service_arn = el.find("KeyManagementServiceArn")
    if child_key_management_service_arn is not None:
        out["key_management_service_arn"] = str(
            child_key_management_service_arn.text or ""
        )
    else:
        raise DeserializationError(
            "CreateKeySigningKeyRequest.key_management_service_arn required"
        )
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("CreateKeySigningKeyRequest.name required")
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    else:
        raise DeserializationError("CreateKeySigningKeyRequest.status required")
    return out

"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleClientCertificateAttribute``."""

from typing import Literal, TypeAlias, cast

"""<p>The client certificate attribute to evaluate in a rule condition. These attributes are extracted from the client certificate presented during mutual TLS authentication.</p>"""
RuleClientCertificateAttribute: TypeAlias = Literal[
    "CN",
    "SAN_RFC822_NAME",
    "SAN_DNS_NAME",
    "SAN_DIRECTORY_NAME",
    "SAN_UNIFORM_RESOURCE_IDENTIFIER",
    "SAN_IP_ADDRESS",
    "SAN_REGISTERED_ID",
    "SERIAL_NUMBER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleClientCertificateAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleClientCertificateAttribute:
    return cast(RuleClientCertificateAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleClientCertificateAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> RuleClientCertificateAttribute:
    return cast(RuleClientCertificateAttribute, data)

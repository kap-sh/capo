"""Generated from Smithy shape ``com.amazonaws.datasync#KerberosKeytabFile``."""

import base64
from typing import TypeAlias

KerberosKeytabFile: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KerberosKeytabFile) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> KerberosKeytabFile:
    return base64.b64decode(data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: KerberosKeytabFile) -> KerberosKeytabFile:
    return value


def deserialize_cbor(data: KerberosKeytabFile) -> KerberosKeytabFile:
    return data

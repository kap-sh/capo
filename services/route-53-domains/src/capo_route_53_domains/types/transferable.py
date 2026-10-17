"""Generated from Smithy shape ``com.amazonaws.route53domains#Transferable``."""

from typing import Literal, TypeAlias, cast

"""<p>Whether the domain name can be transferred to Route 53.</p> <note> <p>You can transfer only domains that have a value of <code>TRANSFERABLE</code> or <code>Transferable</code>.</p> </note> <p>Valid values:</p> <dl> <dt>TRANSFERABLE</dt> <dd> <p>The domain name can be transferred to Route 53.</p> </dd> <dt>UNTRANSFERRABLE</dt> <dd> <p>The domain name can't be transferred to Route 53.</p> </dd> <dt>DONT_KNOW</dt> <dd> <p>The TLD registry didn't respond in time or didn't provide a definitive answer about domain transferability, which can occur due to registry maintenance or temporary delays.</p> </dd> <dt>DOMAIN_IN_OWN_ACCOUNT</dt> <dd> <p>The domain already exists in the current Amazon Web Services account.</p> </dd> <dt>DOMAIN_IN_ANOTHER_ACCOUNT</dt> <dd> <p> The domain exists in another Amazon Web Services account.</p> </dd> <dt>PREMIUM_DOMAIN</dt> <dd> <p>Premium domain transfer is not supported.</p> </dd> </dl>"""
Transferable: TypeAlias = Literal[
    "TRANSFERABLE",
    "UNTRANSFERABLE",
    "DONT_KNOW",
    "DOMAIN_IN_OWN_ACCOUNT",
    "DOMAIN_IN_ANOTHER_ACCOUNT",
    "PREMIUM_DOMAIN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Transferable) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Transferable:
    return cast(Transferable, data)

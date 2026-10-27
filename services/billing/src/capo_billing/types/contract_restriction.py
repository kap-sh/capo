"""Generated from Smithy shape ``com.amazonaws.billing#ContractRestriction``."""

from typing import Literal, TypeAlias, cast

"""<p>A restriction that limits the self-service actions you can take on a contract. A contract with no restrictions supports all self-service actions.</p>"""
ContractRestriction: TypeAlias = Literal["ATTESTATION_SELF_SERVICE_BLOCKED",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContractRestriction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContractRestriction:
    return cast(ContractRestriction, data)

"""Generated from Smithy shape ``com.amazonaws.ecs#AttestationPolicyStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of the attestation policy for a task that uses the <code>CONFIDENTIAL_SANDBOX</code> isolation mode.</p>"""
AttestationPolicyStatus: TypeAlias = Literal["CONFIGURED",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttestationPolicyStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AttestationPolicyStatus:
    return cast(AttestationPolicyStatus, data)

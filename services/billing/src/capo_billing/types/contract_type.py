"""Generated from Smithy shape ``com.amazonaws.billing#ContractType``."""

from typing import Literal, TypeAlias, cast

"""<p>The classification of a private pricing contract. A value of <code>Cross-Service</code> indicates that the contract terms apply across multiple Amazon Web Services services. A value of <code>Service-Specific</code> indicates that the contract terms apply to a specific Amazon Web Services service. A value of <code>Other</code> indicates that the contract terms apply to other arrangements.</p>"""
ContractType: TypeAlias = Literal[
    "Cross-Service",
    "Service-Specific",
    "Other",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContractType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContractType:
    return cast(ContractType, data)

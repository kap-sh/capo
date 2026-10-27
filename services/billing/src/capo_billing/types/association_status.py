"""Generated from Smithy shape ``com.amazonaws.billing#AssociationStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Indicates whether a contract is associated with your account. A value of <code>ASSOCIATED</code> indicates that the contract is associated with your account. A value of <code>NOT_ASSOCIATED</code> indicates that the contract is not associated with your account.</p>"""
AssociationStatus: TypeAlias = Literal[
    "ASSOCIATED",
    "NOT_ASSOCIATED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AssociationStatus:
    return cast(AssociationStatus, data)

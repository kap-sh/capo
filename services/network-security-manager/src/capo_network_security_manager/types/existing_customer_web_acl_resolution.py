"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ExistingCustomerWebACLResolution``."""

from typing import Literal, TypeAlias, cast

ExistingCustomerWebACLResolution: TypeAlias = Literal[
    "RETROFIT",
    "OVERRIDE_ASSOCIATION",
    "NO_REMEDIATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExistingCustomerWebACLResolution) -> str:
    return value


def deserialize_json(data: str) -> ExistingCustomerWebACLResolution:
    return cast(ExistingCustomerWebACLResolution, data)

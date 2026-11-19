"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ServiceQuotaWarningStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a service quota warning. Valid values:</p> <p> <code>pending</code> - Region switch submitted a quota increase request that is still open.</p> <p> <code>denied</code> - The quota increase request was denied.</p> <p> <code>insufficientPermissions</code> - The plan's execution role is missing a permission that service quota checks require.</p> <p> <code>maxRegionSwitchRequestsExceeded</code> - Region switch reached its limit on the number of open quota increase requests.</p> <p> <code>maxAccountRequestsExceeded</code> - The account reached the maximum number of open quota increase requests.</p>"""
ServiceQuotaWarningStatus: TypeAlias = Literal[
    "pending",
    "denied",
    "insufficientPermissions",
    "maxRegionSwitchRequestsExceeded",
    "maxAccountRequestsExceeded",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceQuotaWarningStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ServiceQuotaWarningStatus:
    return cast(ServiceQuotaWarningStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ServiceQuotaWarningStatus) -> str:
    return value


def deserialize_cbor(data: str) -> ServiceQuotaWarningStatus:
    return cast(ServiceQuotaWarningStatus, data)

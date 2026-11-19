"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TLSInspectionScopeDeploymentMode``."""

from typing import Literal, TypeAlias, cast

TLSInspectionScopeDeploymentMode: TypeAlias = Literal[
    "TRANSPARENT_FIREWALL_ONLY",
    "EXPLICIT_PROXY_ONLY",
    "ALL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TLSInspectionScopeDeploymentMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TLSInspectionScopeDeploymentMode:
    return cast(TLSInspectionScopeDeploymentMode, data)

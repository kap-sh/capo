"""Generated from Smithy shape ``com.amazonaws.lakeformation#RLSPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.rls_policy

RLSPolicyList: TypeAlias = list["capo_lakeformation.types.rls_policy.RLSPolicy"]


# --- restJson1 ser/de ---
def serialize_json(value: RLSPolicyList) -> list:
    import capo_lakeformation.types.rls_policy

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.rls_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> RLSPolicyList:
    import capo_lakeformation.types.rls_policy

    out: RLSPolicyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lakeformation.types.rls_policy.deserialize_json(item))
    return out

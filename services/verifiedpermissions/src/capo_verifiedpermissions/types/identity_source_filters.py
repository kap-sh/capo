"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#IdentitySourceFilters``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.identity_source_filter

IdentitySourceFilters: TypeAlias = list[
    "capo_verifiedpermissions.types.identity_source_filter.IdentitySourceFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdentitySourceFilters) -> list:
    import capo_verifiedpermissions.types.identity_source_filter

    out: list = []
    for item in value:
        out.append(
            capo_verifiedpermissions.types.identity_source_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> IdentitySourceFilters:
    import capo_verifiedpermissions.types.identity_source_filter

    out: IdentitySourceFilters = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_verifiedpermissions.types.identity_source_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: IdentitySourceFilters) -> list[Any]:
    import capo_verifiedpermissions.types.identity_source_filter

    return [
        capo_verifiedpermissions.types.identity_source_filter.redact_sensitive(item)
        for item in value
    ]

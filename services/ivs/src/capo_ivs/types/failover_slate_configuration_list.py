"""Generated from Smithy shape ``com.amazonaws.ivs#FailoverSlateConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs.types.failover_slate_configuration_summary

FailoverSlateConfigurationList: TypeAlias = list[
    "capo_ivs.types.failover_slate_configuration_summary.FailoverSlateConfigurationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailoverSlateConfigurationList) -> list:
    import capo_ivs.types.failover_slate_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_ivs.types.failover_slate_configuration_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FailoverSlateConfigurationList:
    import capo_ivs.types.failover_slate_configuration_summary

    out: FailoverSlateConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ivs.types.failover_slate_configuration_summary.deserialize_json(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#ConfigurationIssueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_network_security_manager.types.configuration_issue

ConfigurationIssueList: TypeAlias = list[
    "capo_network_security_manager.types.configuration_issue.ConfigurationIssue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationIssueList) -> list:
    import capo_network_security_manager.types.configuration_issue

    out: list = []
    for item in value:
        out.append(
            capo_network_security_manager.types.configuration_issue.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConfigurationIssueList:
    import capo_network_security_manager.types.configuration_issue

    out: ConfigurationIssueList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_network_security_manager.types.configuration_issue.deserialize_json(
                item
            )
        )
    return out

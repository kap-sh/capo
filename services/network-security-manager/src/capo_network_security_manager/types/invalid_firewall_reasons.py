"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#InvalidFirewallReasons``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_security_manager.types.configuration_issue_list


class InvalidFirewallReasons(TypedDict, closed=True):
    incorrect_single_value_configurations: NotRequired[
        "capo_network_security_manager.types.configuration_issue_list.ConfigurationIssueList"
    ]
    """<p>Single-value configuration settings whose values do not match the expected values.</p>"""
    missing_appendable_configuration_values: NotRequired[
        "capo_network_security_manager.types.configuration_issue_list.ConfigurationIssueList"
    ]
    """<p>Appendable configuration values that are expected but missing.</p>"""
    unexpected_appendable_configuration_values: NotRequired[
        "capo_network_security_manager.types.configuration_issue_list.ConfigurationIssueList"
    ]
    """<p>Appendable configuration values that are present but not expected.</p>"""
    incorrect_appendable_configuration_order: NotRequired[
        "capo_network_security_manager.types.configuration_issue_list.ConfigurationIssueList"
    ]
    """<p>Appendable configuration values that are present but in the wrong order.</p>"""
    missing_mergeable_configuration_values: NotRequired[
        "capo_network_security_manager.types.configuration_issue_list.ConfigurationIssueList"
    ]
    """<p>Mergeable configuration values that are expected but missing.</p>"""
    unexpected_mergeable_configuration_values: NotRequired[
        "capo_network_security_manager.types.configuration_issue_list.ConfigurationIssueList"
    ]
    """<p>Mergeable configuration values that are present but not expected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvalidFirewallReasons) -> dict:
    out: dict = {}
    if "incorrect_single_value_configurations" in value:
        import capo_network_security_manager.types.configuration_issue_list

        out["incorrectSingleValueConfigurations"] = (
            capo_network_security_manager.types.configuration_issue_list.serialize_json(
                value["incorrect_single_value_configurations"]
            )
        )
    if "missing_appendable_configuration_values" in value:
        import capo_network_security_manager.types.configuration_issue_list

        out["missingAppendableConfigurationValues"] = (
            capo_network_security_manager.types.configuration_issue_list.serialize_json(
                value["missing_appendable_configuration_values"]
            )
        )
    if "unexpected_appendable_configuration_values" in value:
        import capo_network_security_manager.types.configuration_issue_list

        out["unexpectedAppendableConfigurationValues"] = (
            capo_network_security_manager.types.configuration_issue_list.serialize_json(
                value["unexpected_appendable_configuration_values"]
            )
        )
    if "incorrect_appendable_configuration_order" in value:
        import capo_network_security_manager.types.configuration_issue_list

        out["incorrectAppendableConfigurationOrder"] = (
            capo_network_security_manager.types.configuration_issue_list.serialize_json(
                value["incorrect_appendable_configuration_order"]
            )
        )
    if "missing_mergeable_configuration_values" in value:
        import capo_network_security_manager.types.configuration_issue_list

        out["missingMergeableConfigurationValues"] = (
            capo_network_security_manager.types.configuration_issue_list.serialize_json(
                value["missing_mergeable_configuration_values"]
            )
        )
    if "unexpected_mergeable_configuration_values" in value:
        import capo_network_security_manager.types.configuration_issue_list

        out["unexpectedMergeableConfigurationValues"] = (
            capo_network_security_manager.types.configuration_issue_list.serialize_json(
                value["unexpected_mergeable_configuration_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> InvalidFirewallReasons:
    out: InvalidFirewallReasons = {}  # type: ignore[typeddict-item]
    if data.get("incorrectSingleValueConfigurations") is not None:
        import capo_network_security_manager.types.configuration_issue_list

        out["incorrect_single_value_configurations"] = (
            capo_network_security_manager.types.configuration_issue_list.deserialize_json(
                data["incorrectSingleValueConfigurations"]
            )
        )
    if data.get("missingAppendableConfigurationValues") is not None:
        import capo_network_security_manager.types.configuration_issue_list

        out["missing_appendable_configuration_values"] = (
            capo_network_security_manager.types.configuration_issue_list.deserialize_json(
                data["missingAppendableConfigurationValues"]
            )
        )
    if data.get("unexpectedAppendableConfigurationValues") is not None:
        import capo_network_security_manager.types.configuration_issue_list

        out["unexpected_appendable_configuration_values"] = (
            capo_network_security_manager.types.configuration_issue_list.deserialize_json(
                data["unexpectedAppendableConfigurationValues"]
            )
        )
    if data.get("incorrectAppendableConfigurationOrder") is not None:
        import capo_network_security_manager.types.configuration_issue_list

        out["incorrect_appendable_configuration_order"] = (
            capo_network_security_manager.types.configuration_issue_list.deserialize_json(
                data["incorrectAppendableConfigurationOrder"]
            )
        )
    if data.get("missingMergeableConfigurationValues") is not None:
        import capo_network_security_manager.types.configuration_issue_list

        out["missing_mergeable_configuration_values"] = (
            capo_network_security_manager.types.configuration_issue_list.deserialize_json(
                data["missingMergeableConfigurationValues"]
            )
        )
    if data.get("unexpectedMergeableConfigurationValues") is not None:
        import capo_network_security_manager.types.configuration_issue_list

        out["unexpected_mergeable_configuration_values"] = (
            capo_network_security_manager.types.configuration_issue_list.deserialize_json(
                data["unexpectedMergeableConfigurationValues"]
            )
        )
    return out

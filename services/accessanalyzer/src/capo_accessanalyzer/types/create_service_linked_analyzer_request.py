"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CreateServiceLinkedAnalyzerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_configuration
    import capo_accessanalyzer.types.inline_archive_rules_list
    import capo_accessanalyzer.types.type


class CreateServiceLinkedAnalyzerRequest(TypedDict, closed=True):
    type: "capo_accessanalyzer.types.type.Type"
    """<p>The type of analyzer to create. Valid values are <code>ACCOUNT_UNUSED_ACCESS</code> and <code>ORGANIZATION_UNUSED_ACCESS</code>.</p>"""
    archive_rules: NotRequired[
        "capo_accessanalyzer.types.inline_archive_rules_list.InlineArchiveRulesList"
    ]
    """<p>Specifies the archive rules to add for the analyzer. Archive rules automatically archive findings that meet the criteria you define for the rule.</p>"""
    client_token: NotRequired["str"]
    """<p>A client token.</p>"""
    configuration: NotRequired[
        "capo_accessanalyzer.types.analyzer_configuration.AnalyzerConfiguration"
    ]
    """<p>Specifies the configuration of the analyzer. The specified scope of unused access is used for the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateServiceLinkedAnalyzerRequest) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "archive_rules" in value:
        import capo_accessanalyzer.types.inline_archive_rules_list

        out["archiveRules"] = (
            capo_accessanalyzer.types.inline_archive_rules_list.serialize_json(
                value["archive_rules"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "configuration" in value:
        import capo_accessanalyzer.types.analyzer_configuration

        out["configuration"] = (
            capo_accessanalyzer.types.analyzer_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateServiceLinkedAnalyzerRequest:
    out: CreateServiceLinkedAnalyzerRequest = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("archiveRules") is not None:
        import capo_accessanalyzer.types.inline_archive_rules_list

        out["archive_rules"] = (
            capo_accessanalyzer.types.inline_archive_rules_list.deserialize_json(
                data["archiveRules"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("configuration") is not None:
        import capo_accessanalyzer.types.analyzer_configuration

        out["configuration"] = (
            capo_accessanalyzer.types.analyzer_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out

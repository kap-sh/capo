"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CreateAnalyzerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.analyzer_configuration
    import capo_accessanalyzer.types.analyzer_name
    import capo_accessanalyzer.types.inline_archive_rules_list
    import capo_accessanalyzer.types.tags_map
    import capo_accessanalyzer.types.type


class CreateAnalyzerRequest(TypedDict, closed=True):
    analyzer_name: "capo_accessanalyzer.types.analyzer_name.AnalyzerName"
    """<p>The name of the analyzer to create.</p>"""
    type: "capo_accessanalyzer.types.type.Type"
    """<p>The type of analyzer to create. You can create only one analyzer per account per Region. You can create up to 5 analyzers per organization per Region.</p>"""
    archive_rules: NotRequired[
        "capo_accessanalyzer.types.inline_archive_rules_list.InlineArchiveRulesList"
    ]
    """<p>Specifies the archive rules to add for the analyzer. Archive rules automatically archive findings that meet the criteria you define for the rule.</p>"""
    tags: NotRequired["capo_accessanalyzer.types.tags_map.TagsMap"]
    """<p>An array of key-value pairs to apply to the analyzer. You can use the set of Unicode letters, digits, whitespace, <code>_</code>, <code>.</code>, <code>/</code>, <code>=</code>, <code>+</code>, and <code>-</code>.</p> <p>For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with <code>aws:</code>.</p> <p>For the tag value, you can specify a value that is 0 to 256 characters in length.</p>"""
    client_token: NotRequired["str"]
    """<p>A client token.</p>"""
    configuration: NotRequired[
        "capo_accessanalyzer.types.analyzer_configuration.AnalyzerConfiguration"
    ]
    """<p>Specifies the configuration of the analyzer. If the analyzer is an unused access analyzer, the specified scope of unused access is used for the configuration. If the analyzer is an internal access analyzer, the specified internal access analysis rules are used for the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnalyzerRequest) -> dict:
    out: dict = {}
    out["analyzerName"] = value["analyzer_name"]
    out["type"] = value["type"]
    if "archive_rules" in value:
        import capo_accessanalyzer.types.inline_archive_rules_list

        out["archiveRules"] = (
            capo_accessanalyzer.types.inline_archive_rules_list.serialize_json(
                value["archive_rules"]
            )
        )
    if "tags" in value:
        import capo_accessanalyzer.types.tags_map

        out["tags"] = capo_accessanalyzer.types.tags_map.serialize_json(value["tags"])
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


def deserialize_json(data: dict) -> CreateAnalyzerRequest:
    out: CreateAnalyzerRequest = {}  # type: ignore[typeddict-item]
    if data.get("analyzerName") is not None:
        out["analyzer_name"] = data["analyzerName"]
    else:
        out["analyzer_name"] = ""
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
    if data.get("tags") is not None:
        import capo_accessanalyzer.types.tags_map

        out["tags"] = capo_accessanalyzer.types.tags_map.deserialize_json(data["tags"])
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

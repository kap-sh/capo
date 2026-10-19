"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ListArchiveRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.archive_rules_list
    import capo_accessanalyzer.types.token


class ListArchiveRulesResponse(TypedDict, closed=True):
    archive_rules: "capo_accessanalyzer.types.archive_rules_list.ArchiveRulesList"
    """<p>A list of archive rules created for the specified analyzer.</p>"""
    next_token: NotRequired["capo_accessanalyzer.types.token.Token"]
    """<p>A token used for pagination of results returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListArchiveRulesResponse) -> dict:
    out: dict = {}
    import capo_accessanalyzer.types.archive_rules_list

    out["archiveRules"] = capo_accessanalyzer.types.archive_rules_list.serialize_json(
        value["archive_rules"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListArchiveRulesResponse:
    out: ListArchiveRulesResponse = {}  # type: ignore[typeddict-item]
    if data.get("archiveRules") is not None:
        import capo_accessanalyzer.types.archive_rules_list

        out["archive_rules"] = (
            capo_accessanalyzer.types.archive_rules_list.deserialize_json(
                data["archiveRules"]
            )
        )
    else:
        out["archive_rules"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out

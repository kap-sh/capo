"""Generated from Smithy shape ``com.amazonaws.quicksight#RowLevelPermissionTagRule``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.row_level_permission_tag_delimiter
    import capo_quicksight.types.session_tag_key
    import capo_quicksight.types.session_tag_value
    import capo_quicksight.types.string


class RowLevelPermissionTagRule(TypedDict, closed=True):
    tag_key: "capo_quicksight.types.session_tag_key.SessionTagKey"
    """<p>The unique key for a tag.</p>"""
    column_name: "capo_quicksight.types.string.String"
    """<p>The column name that a tag key is assigned to.</p>"""
    tag_multi_value_delimiter: NotRequired[
        "capo_quicksight.types.row_level_permission_tag_delimiter.RowLevelPermissionTagDelimiter"
    ]
    """<p>A string that you want to use to delimit the values when you pass the values at run time. For example, you can delimit the values with a comma.</p>"""
    match_all_value: NotRequired[
        "capo_quicksight.types.session_tag_value.SessionTagValue"
    ]
    """<p>A string that you want to use to filter by all the values in a column in the dataset and don’t want to list the values one by one. For example, you can use an asterisk as your match all value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RowLevelPermissionTagRule) -> dict:
    out: dict = {}
    out["TagKey"] = value["tag_key"]
    out["ColumnName"] = value["column_name"]
    if "tag_multi_value_delimiter" in value:
        out["TagMultiValueDelimiter"] = value["tag_multi_value_delimiter"]
    if "match_all_value" in value:
        out["MatchAllValue"] = value["match_all_value"]
    return out


def deserialize_json(data: dict) -> RowLevelPermissionTagRule:
    out: RowLevelPermissionTagRule = {}  # type: ignore[typeddict-item]
    if data.get("TagKey") is not None:
        out["tag_key"] = data["TagKey"]
    else:
        out["tag_key"] = ""
    if data.get("ColumnName") is not None:
        out["column_name"] = data["ColumnName"]
    else:
        out["column_name"] = ""
    if data.get("TagMultiValueDelimiter") is not None:
        out["tag_multi_value_delimiter"] = data["TagMultiValueDelimiter"]
    if data.get("MatchAllValue") is not None:
        out["match_all_value"] = data["MatchAllValue"]
    return out


def redact_sensitive(value: RowLevelPermissionTagRule) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "match_all_value" in value:
        out["match_all_value"] = "*** Sensitive Data Redacted ***"
    return out

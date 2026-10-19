"""Generated from Smithy shape ``com.amazonaws.kendra#AclConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.column_name


class AclConfiguration(TypedDict, closed=True):
    allowed_groups_column_name: "capo_kendra.types.column_name.ColumnName"
    """<p>A list of groups, separated by semi-colons, that filters a query response based on user context. The document is only returned to users that are in one of the groups specified in the <code>UserContext</code> field of the <code>Query</code> API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AclConfiguration) -> dict:
    out: dict = {}
    out["AllowedGroupsColumnName"] = value["allowed_groups_column_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AclConfiguration:
    out: AclConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AllowedGroupsColumnName") is not None:
        out["allowed_groups_column_name"] = data["AllowedGroupsColumnName"]
    else:
        out["allowed_groups_column_name"] = ""
    return out

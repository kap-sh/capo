"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GetGroupQueryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group_query


class GetGroupQueryOutput(TypedDict, closed=True):
    group_query: NotRequired["capo_resource_groups.types.group_query.GroupQuery"]
    """<p>The resource query associated with the specified group. For more information about resource queries, see <a href="https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html#gettingstarted-query-cli-tag">Create a tag-based group in Resource Groups</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupQueryOutput) -> dict:
    out: dict = {}
    if "group_query" in value:
        import capo_resource_groups.types.group_query

        out["GroupQuery"] = capo_resource_groups.types.group_query.serialize_json(
            value["group_query"]
        )
    return out


def deserialize_json(data: dict) -> GetGroupQueryOutput:
    out: GetGroupQueryOutput = {}  # type: ignore[typeddict-item]
    if data.get("GroupQuery") is not None:
        import capo_resource_groups.types.group_query

        out["group_query"] = capo_resource_groups.types.group_query.deserialize_json(
            data["GroupQuery"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.mwaa#UpdateTeamsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa.types.team_map
    import capo_mwaa.types.team_name_list


class UpdateTeamsInput(TypedDict, closed=True):
    add_or_update: NotRequired["capo_mwaa.types.team_map.TeamMap"]
    """<p>A map of teams to add to your environment, or to update if they already exist. Each entry maps a team name to its settings. Each team name must match the display name of an Amazon Web Services IAM Identity Center group associated with your environment. You can configure between <code>1</code> and <code>20</code> teams.</p>"""
    remove: NotRequired["capo_mwaa.types.team_name_list.TeamNameList"]
    """<p>A list of team names to remove from your environment. For example, <code>team-a</code>. You can remove between <code>1</code> and <code>20</code> teams in a single update. Removing a team does not delete the team's DAG code from Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTeamsInput) -> dict:
    out: dict = {}
    if "add_or_update" in value:
        import capo_mwaa.types.team_map

        out["AddOrUpdate"] = capo_mwaa.types.team_map.serialize_json(
            value["add_or_update"]
        )
    if "remove" in value:
        import capo_mwaa.types.team_name_list

        out["Remove"] = capo_mwaa.types.team_name_list.serialize_json(value["remove"])
    return out


def deserialize_json(data: dict) -> UpdateTeamsInput:
    out: UpdateTeamsInput = {}  # type: ignore[typeddict-item]
    if data.get("AddOrUpdate") is not None:
        import capo_mwaa.types.team_map

        out["add_or_update"] = capo_mwaa.types.team_map.deserialize_json(
            data["AddOrUpdate"]
        )
    if data.get("Remove") is not None:
        import capo_mwaa.types.team_name_list

        out["remove"] = capo_mwaa.types.team_name_list.deserialize_json(data["Remove"])
    return out

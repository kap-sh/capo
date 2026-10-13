"""Generated from Smithy shape ``com.amazonaws.workdocs#Participants``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.group_metadata_list
    import capo_workdocs.types.user_metadata_list


class Participants(TypedDict, closed=True):
    users: NotRequired["capo_workdocs.types.user_metadata_list.UserMetadataList"]
    """<p>The list of users.</p>"""
    groups: NotRequired["capo_workdocs.types.group_metadata_list.GroupMetadataList"]
    """<p>The list of user groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Participants) -> dict:
    out: dict = {}
    if "users" in value:
        import capo_workdocs.types.user_metadata_list

        out["Users"] = capo_workdocs.types.user_metadata_list.serialize_json(
            value["users"]
        )
    if "groups" in value:
        import capo_workdocs.types.group_metadata_list

        out["Groups"] = capo_workdocs.types.group_metadata_list.serialize_json(
            value["groups"]
        )
    return out


def deserialize_json(data: dict) -> Participants:
    out: Participants = {}  # type: ignore[typeddict-item]
    if data.get("Users") is not None:
        import capo_workdocs.types.user_metadata_list

        out["users"] = capo_workdocs.types.user_metadata_list.deserialize_json(
            data["Users"]
        )
    if data.get("Groups") is not None:
        import capo_workdocs.types.group_metadata_list

        out["groups"] = capo_workdocs.types.group_metadata_list.deserialize_json(
            data["Groups"]
        )
    return out


def redact_sensitive(value: Participants) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "users" in value:
        import capo_workdocs.types.user_metadata_list

        out["users"] = capo_workdocs.types.user_metadata_list.redact_sensitive(
            value["users"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.connect#NotificationRecipientType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.user_id_list
    import capo_connect.types.user_tag_map


class NotificationRecipientType(TypedDict, closed=True):
    user_tags: NotRequired["capo_connect.types.user_tag_map.UserTagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }. Connect Customer users with the specified tags will be notified.</p>"""
    user_ids: NotRequired["capo_connect.types.user_id_list.UserIdList"]
    """<p>A list of user IDs. Supports variable injection of <code>$.ContactLens.ContactEvaluation.Agent.AgentId</code> for <code>OnContactEvaluationSubmit</code> event source. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationRecipientType) -> dict:
    out: dict = {}
    if "user_tags" in value:
        import capo_connect.types.user_tag_map

        out["UserTags"] = capo_connect.types.user_tag_map.serialize_json(
            value["user_tags"]
        )
    if "user_ids" in value:
        import capo_connect.types.user_id_list

        out["UserIds"] = capo_connect.types.user_id_list.serialize_json(
            value["user_ids"]
        )
    return out


def deserialize_json(data: dict) -> NotificationRecipientType:
    out: NotificationRecipientType = {}  # type: ignore[typeddict-item]
    if data.get("UserTags") is not None:
        import capo_connect.types.user_tag_map

        out["user_tags"] = capo_connect.types.user_tag_map.deserialize_json(
            data["UserTags"]
        )
    if data.get("UserIds") is not None:
        import capo_connect.types.user_id_list

        out["user_ids"] = capo_connect.types.user_id_list.deserialize_json(
            data["UserIds"]
        )
    return out

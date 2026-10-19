"""Generated from Smithy shape ``com.amazonaws.personalizeevents#PutUsersRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize_events.types.arn
    import capo_personalize_events.types.user_list


class PutUsersRequest(TypedDict, closed=True):
    dataset_arn: "capo_personalize_events.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Users dataset you are adding the user or users to.</p>"""
    users: "capo_personalize_events.types.user_list.UserList"
    """<p>A list of user data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutUsersRequest) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    import capo_personalize_events.types.user_list

    out["users"] = capo_personalize_events.types.user_list.serialize_json(
        value["users"]
    )
    return out


def deserialize_json(data: dict) -> PutUsersRequest:
    out: PutUsersRequest = {}  # type: ignore[typeddict-item]
    if data.get("datasetArn") is not None:
        out["dataset_arn"] = data["datasetArn"]
    else:
        out["dataset_arn"] = ""
    if data.get("users") is not None:
        import capo_personalize_events.types.user_list

        out["users"] = capo_personalize_events.types.user_list.deserialize_json(
            data["users"]
        )
    else:
        out["users"] = []
    return out


def redact_sensitive(value: PutUsersRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "users" in value:
        import capo_personalize_events.types.user_list

        out["users"] = capo_personalize_events.types.user_list.redact_sensitive(
            value["users"]
        )
    return out

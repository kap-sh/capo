"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EventActor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.actor_type


class EventActor(TypedDict, closed=True):
    type: "capo_resiliencehubv2.types.actor_type.ActorType"
    """<p>The type of actor, either USER or SYSTEM.</p>"""
    principal_id: "str"
    """<p>The principal ID of the actor.</p>"""
    account_id: NotRequired["str"]
    """<p>The AWS account ID of the actor.</p>"""
    user_name: NotRequired["str"]
    """<p>The user name of the actor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventActor) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.actor_type

    out["type"] = capo_resiliencehubv2.types.actor_type.serialize_json(value["type"])
    out["principalId"] = value["principal_id"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "user_name" in value:
        out["userName"] = value["user_name"]
    return out


def deserialize_json(data: dict) -> EventActor:
    out: EventActor = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_resiliencehubv2.types.actor_type

        out["type"] = capo_resiliencehubv2.types.actor_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast("capo_resiliencehubv2.types.actor_type.ActorType", "")
    if data.get("principalId") is not None:
        out["principal_id"] = data["principalId"]
    else:
        out["principal_id"] = ""
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("userName") is not None:
        out["user_name"] = data["userName"]
    return out

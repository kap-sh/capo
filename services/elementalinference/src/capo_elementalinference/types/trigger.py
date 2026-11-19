"""Generated from Smithy shape ``com.amazonaws.elementalinference#Trigger``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_elementalinference.errors import DeserializationError, SerializationError
from capo_elementalinference.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_elementalinference.types.clip_trigger
    import capo_elementalinference.types.fixed_interval_trigger
    import capo_elementalinference.types.scene_trigger
    import capo_elementalinference.types.shot_trigger


class TriggerFixedIntervalMember(TypedDict, closed=True):
    fixedInterval: (
        "capo_elementalinference.types.fixed_interval_trigger.FixedIntervalTrigger"
    )


class TriggerPerShotMember(TypedDict, closed=True):
    perShot: "capo_elementalinference.types.shot_trigger.ShotTrigger"


class TriggerPerSceneMember(TypedDict, closed=True):
    perScene: "capo_elementalinference.types.scene_trigger.SceneTrigger"


class TriggerPerClipMember(TypedDict, closed=True):
    perClip: "capo_elementalinference.types.clip_trigger.ClipTrigger"


Trigger: TypeAlias = (
    TriggerFixedIntervalMember
    | TriggerPerShotMember
    | TriggerPerSceneMember
    | TriggerPerClipMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Trigger) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Trigger: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "fixedInterval" in value:
        import capo_elementalinference.types.fixed_interval_trigger

        return {
            "fixedInterval": capo_elementalinference.types.fixed_interval_trigger.serialize_json(
                value["fixedInterval"]
            )
        }
    elif "perShot" in value:
        import capo_elementalinference.types.shot_trigger

        return {
            "perShot": capo_elementalinference.types.shot_trigger.serialize_json(
                value["perShot"]
            )
        }
    elif "perScene" in value:
        import capo_elementalinference.types.scene_trigger

        return {
            "perScene": capo_elementalinference.types.scene_trigger.serialize_json(
                value["perScene"]
            )
        }
    elif "perClip" in value:
        import capo_elementalinference.types.clip_trigger

        return {
            "perClip": capo_elementalinference.types.clip_trigger.serialize_json(
                value["perClip"]
            )
        }
    else:
        raise SerializationError("Trigger: no variant present")


def deserialize_json(data: dict) -> Trigger:
    if data.get("fixedInterval") is not None:
        import capo_elementalinference.types.fixed_interval_trigger

        return {
            "fixedInterval": capo_elementalinference.types.fixed_interval_trigger.deserialize_json(
                data["fixedInterval"]
            )
        }
    elif data.get("perShot") is not None:
        import capo_elementalinference.types.shot_trigger

        return {
            "perShot": capo_elementalinference.types.shot_trigger.deserialize_json(
                data["perShot"]
            )
        }
    elif data.get("perScene") is not None:
        import capo_elementalinference.types.scene_trigger

        return {
            "perScene": capo_elementalinference.types.scene_trigger.deserialize_json(
                data["perScene"]
            )
        }
    elif data.get("perClip") is not None:
        import capo_elementalinference.types.clip_trigger

        return {
            "perClip": capo_elementalinference.types.clip_trigger.deserialize_json(
                data["perClip"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Trigger: no recognized variant key")

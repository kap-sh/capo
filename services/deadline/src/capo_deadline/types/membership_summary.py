"""Generated from Smithy shape ``com.amazonaws.deadline#MembershipSummary``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError, SerializationError
from capo_deadline.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_deadline.types.farm_member
    import capo_deadline.types.fleet_member
    import capo_deadline.types.job_member
    import capo_deadline.types.queue_member


class _MembershipSummary_farm(TypedDict, closed=True):
    farm: "capo_deadline.types.farm_member.FarmMember"


class _MembershipSummary_queue(TypedDict, closed=True):
    queue: "capo_deadline.types.queue_member.QueueMember"


class _MembershipSummary_fleet(TypedDict, closed=True):
    fleet: "capo_deadline.types.fleet_member.FleetMember"


class _MembershipSummary_job(TypedDict, closed=True):
    job: "capo_deadline.types.job_member.JobMember"


MembershipSummary: TypeAlias = (
    _MembershipSummary_farm
    | _MembershipSummary_queue
    | _MembershipSummary_fleet
    | _MembershipSummary_job
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MembershipSummary) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MembershipSummary: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "farm" in value:
        import capo_deadline.types.farm_member

        return {"farm": capo_deadline.types.farm_member.serialize_json(value["farm"])}
    elif "queue" in value:
        import capo_deadline.types.queue_member

        return {
            "queue": capo_deadline.types.queue_member.serialize_json(value["queue"])
        }
    elif "fleet" in value:
        import capo_deadline.types.fleet_member

        return {
            "fleet": capo_deadline.types.fleet_member.serialize_json(value["fleet"])
        }
    elif "job" in value:
        import capo_deadline.types.job_member

        return {"job": capo_deadline.types.job_member.serialize_json(value["job"])}
    else:
        raise SerializationError("MembershipSummary: no variant present")


def deserialize_json(data: dict) -> MembershipSummary:
    if data.get("farm") is not None:
        import capo_deadline.types.farm_member

        return {"farm": capo_deadline.types.farm_member.deserialize_json(data["farm"])}
    elif data.get("queue") is not None:
        import capo_deadline.types.queue_member

        return {
            "queue": capo_deadline.types.queue_member.deserialize_json(data["queue"])
        }
    elif data.get("fleet") is not None:
        import capo_deadline.types.fleet_member

        return {
            "fleet": capo_deadline.types.fleet_member.deserialize_json(data["fleet"])
        }
    elif data.get("job") is not None:
        import capo_deadline.types.job_member

        return {"job": capo_deadline.types.job_member.deserialize_json(data["job"])}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("MembershipSummary: no recognized variant key")

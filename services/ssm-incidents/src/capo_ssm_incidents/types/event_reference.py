"""Generated from Smithy shape ``com.amazonaws.ssmincidents#EventReference``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError
from capo_ssm_incidents.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm_incidents.types.arn
    import capo_ssm_incidents.types.generated_id


class _EventReference_resource(TypedDict, closed=True):
    resource: "capo_ssm_incidents.types.arn.Arn"


class _EventReference_relatedItemId(TypedDict, closed=True):
    relatedItemId: "capo_ssm_incidents.types.generated_id.GeneratedId"


EventReference: TypeAlias = (
    _EventReference_resource | _EventReference_relatedItemId | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: EventReference) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EventReference: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "resource" in value:
        return {"resource": value["resource"]}
    elif "relatedItemId" in value:
        return {"relatedItemId": value["relatedItemId"]}
    else:
        raise SerializationError("EventReference: no variant present")


def deserialize_json(data: dict) -> EventReference:
    if data.get("resource") is not None:
        return {"resource": data["resource"]}
    elif data.get("relatedItemId") is not None:
        return {"relatedItemId": data["relatedItemId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EventReference: no recognized variant key")

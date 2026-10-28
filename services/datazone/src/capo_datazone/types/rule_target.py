"""Generated from Smithy shape ``com.amazonaws.datazone#RuleTarget``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.domain_unit_target


class RuleTargetDomainUnitTargetMember(TypedDict, closed=True):
    domainUnitTarget: "capo_datazone.types.domain_unit_target.DomainUnitTarget"


RuleTarget: TypeAlias = RuleTargetDomainUnitTargetMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: RuleTarget) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RuleTarget: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "domainUnitTarget" in value:
        import capo_datazone.types.domain_unit_target

        return {
            "domainUnitTarget": capo_datazone.types.domain_unit_target.serialize_json(
                value["domainUnitTarget"]
            )
        }
    else:
        raise SerializationError("RuleTarget: no variant present")


def deserialize_json(data: dict) -> RuleTarget:
    if data.get("domainUnitTarget") is not None:
        import capo_datazone.types.domain_unit_target

        return {
            "domainUnitTarget": capo_datazone.types.domain_unit_target.deserialize_json(
                data["domainUnitTarget"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RuleTarget: no recognized variant key")

"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#EntityReference``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_verifiedpermissions.errors import DeserializationError, SerializationError
from capo_verifiedpermissions.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.entity_identifier


class EntityReferenceUnspecifiedMember(TypedDict, closed=True):
    unspecified: "bool"


class EntityReferenceIdentifierMember(TypedDict, closed=True):
    identifier: "capo_verifiedpermissions.types.entity_identifier.EntityIdentifier"


EntityReference: TypeAlias = (
    EntityReferenceUnspecifiedMember
    | EntityReferenceIdentifierMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EntityReference) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EntityReference: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "unspecified" in value:
        return {"unspecified": value["unspecified"]}
    elif "identifier" in value:
        import capo_verifiedpermissions.types.entity_identifier

        return {
            "identifier": capo_verifiedpermissions.types.entity_identifier.serialize_aws_json_1_0(
                value["identifier"]
            )
        }
    else:
        raise SerializationError("EntityReference: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EntityReference:
    if data.get("unspecified") is not None:
        return {"unspecified": data["unspecified"]}
    elif data.get("identifier") is not None:
        import capo_verifiedpermissions.types.entity_identifier

        return {
            "identifier": capo_verifiedpermissions.types.entity_identifier.deserialize_aws_json_1_0(
                data["identifier"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EntityReference: no recognized variant key")


def redact_sensitive(value: EntityReference) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "identifier" in value:
        import capo_verifiedpermissions.types.entity_identifier

        out["identifier"] = (
            capo_verifiedpermissions.types.entity_identifier.redact_sensitive(
                value["identifier"]
            )
        )
    return out

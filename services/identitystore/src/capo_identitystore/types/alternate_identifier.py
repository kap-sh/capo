"""Generated from Smithy shape ``com.amazonaws.identitystore#AlternateIdentifier``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError, SerializationError
from capo_identitystore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_identitystore.types.external_id
    import capo_identitystore.types.unique_attribute


class AlternateIdentifierExternalIdMember(TypedDict, closed=True):
    ExternalId: "capo_identitystore.types.external_id.ExternalId"


class AlternateIdentifierUniqueAttributeMember(TypedDict, closed=True):
    UniqueAttribute: "capo_identitystore.types.unique_attribute.UniqueAttribute"


AlternateIdentifier: TypeAlias = (
    AlternateIdentifierExternalIdMember
    | AlternateIdentifierUniqueAttributeMember
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlternateIdentifier) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AlternateIdentifier: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ExternalId" in value:
        import capo_identitystore.types.external_id

        return {
            "ExternalId": capo_identitystore.types.external_id.serialize_aws_json_1_1(
                value["ExternalId"]
            )
        }
    elif "UniqueAttribute" in value:
        import capo_identitystore.types.unique_attribute

        return {
            "UniqueAttribute": capo_identitystore.types.unique_attribute.serialize_aws_json_1_1(
                value["UniqueAttribute"]
            )
        }
    else:
        raise SerializationError("AlternateIdentifier: no variant present")


def deserialize_aws_json_1_1(data: dict) -> AlternateIdentifier:
    if data.get("ExternalId") is not None:
        import capo_identitystore.types.external_id

        return {
            "ExternalId": capo_identitystore.types.external_id.deserialize_aws_json_1_1(
                data["ExternalId"]
            )
        }
    elif data.get("UniqueAttribute") is not None:
        import capo_identitystore.types.unique_attribute

        return {
            "UniqueAttribute": capo_identitystore.types.unique_attribute.deserialize_aws_json_1_1(
                data["UniqueAttribute"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AlternateIdentifier: no recognized variant key")


def redact_sensitive(value: AlternateIdentifier) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ExternalId" in value:
        import capo_identitystore.types.external_id

        out["ExternalId"] = capo_identitystore.types.external_id.redact_sensitive(
            value["ExternalId"]
        )
    return out

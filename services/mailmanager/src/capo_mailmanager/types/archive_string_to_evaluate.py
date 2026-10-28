"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveStringToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError
from capo_mailmanager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mailmanager.types.archive_string_email_attribute


class ArchiveStringToEvaluateAttributeMember(TypedDict, closed=True):
    Attribute: "capo_mailmanager.types.archive_string_email_attribute.ArchiveStringEmailAttribute"


ArchiveStringToEvaluate: TypeAlias = (
    ArchiveStringToEvaluateAttributeMember | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveStringToEvaluate) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ArchiveStringToEvaluate: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Attribute" in value:
        import capo_mailmanager.types.archive_string_email_attribute

        return {
            "Attribute": capo_mailmanager.types.archive_string_email_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    else:
        raise SerializationError("ArchiveStringToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> ArchiveStringToEvaluate:
    if data.get("Attribute") is not None:
        import capo_mailmanager.types.archive_string_email_attribute

        return {
            "Attribute": capo_mailmanager.types.archive_string_email_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ArchiveStringToEvaluate: no recognized variant key")

"""Generated from Smithy shape ``com.amazonaws.proton#TemplateVersionSourceInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError, SerializationError
from capo_proton.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_proton.types.s3_object_source


class TemplateVersionSourceInputS3Member(TypedDict, closed=True):
    s3: "capo_proton.types.s3_object_source.S3ObjectSource"


TemplateVersionSourceInput: TypeAlias = (
    TemplateVersionSourceInputS3Member | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TemplateVersionSourceInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TemplateVersionSourceInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "s3" in value:
        import capo_proton.types.s3_object_source

        return {
            "s3": capo_proton.types.s3_object_source.serialize_aws_json_1_0(value["s3"])
        }
    else:
        raise SerializationError("TemplateVersionSourceInput: no variant present")


def deserialize_aws_json_1_0(data: dict) -> TemplateVersionSourceInput:
    if data.get("s3") is not None:
        import capo_proton.types.s3_object_source

        return {
            "s3": capo_proton.types.s3_object_source.deserialize_aws_json_1_0(
                data["s3"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "TemplateVersionSourceInput: no recognized variant key"
        )

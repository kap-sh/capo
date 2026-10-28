"""Generated from Smithy shape ``com.amazonaws.b2bi#FormatOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_b2bi.errors import DeserializationError, SerializationError
from capo_b2bi.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_b2bi.types.x12_details


class FormatOptionsX12Member(TypedDict, closed=True):
    x12: "capo_b2bi.types.x12_details.X12Details"


FormatOptions: TypeAlias = FormatOptionsX12Member | UnknownUnionMember


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FormatOptions) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FormatOptions: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "x12" in value:
        import capo_b2bi.types.x12_details

        return {"x12": capo_b2bi.types.x12_details.serialize_aws_json_1_0(value["x12"])}
    else:
        raise SerializationError("FormatOptions: no variant present")


def deserialize_aws_json_1_0(data: dict) -> FormatOptions:
    if data.get("x12") is not None:
        import capo_b2bi.types.x12_details

        return {
            "x12": capo_b2bi.types.x12_details.deserialize_aws_json_1_0(data["x12"])
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FormatOptions: no recognized variant key")

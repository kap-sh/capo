"""Generated from Smithy shape ``com.amazonaws.b2bi#EdiType``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_b2bi.errors import DeserializationError, SerializationError
from capo_b2bi.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_b2bi.types.x12_details


class EdiTypeX12DetailsMember(TypedDict, closed=True):
    x12Details: "capo_b2bi.types.x12_details.X12Details"


EdiType: TypeAlias = EdiTypeX12DetailsMember | UnknownUnionMember


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EdiType) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"EdiType: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "x12Details" in value:
        import capo_b2bi.types.x12_details

        return {
            "x12Details": capo_b2bi.types.x12_details.serialize_aws_json_1_0(
                value["x12Details"]
            )
        }
    else:
        raise SerializationError("EdiType: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EdiType:
    if data.get("x12Details") is not None:
        import capo_b2bi.types.x12_details

        return {
            "x12Details": capo_b2bi.types.x12_details.deserialize_aws_json_1_0(
                data["x12Details"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("EdiType: no recognized variant key")

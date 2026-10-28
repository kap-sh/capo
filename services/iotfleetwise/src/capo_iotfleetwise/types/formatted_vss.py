"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#FormattedVss``."""

from typing import TypeAlias

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError, SerializationError
from capo_iotfleetwise.types._unknown import UnknownUnionMember


class FormattedVssVssJsonMember(TypedDict, closed=True):
    vssJson: "str"


FormattedVss: TypeAlias = FormattedVssVssJsonMember | UnknownUnionMember


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FormattedVss) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FormattedVss: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "vssJson" in value:
        return {"vssJson": value["vssJson"]}
    else:
        raise SerializationError("FormattedVss: no variant present")


def deserialize_aws_json_1_0(data: dict) -> FormattedVss:
    if data.get("vssJson") is not None:
        return {"vssJson": data["vssJson"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FormattedVss: no recognized variant key")

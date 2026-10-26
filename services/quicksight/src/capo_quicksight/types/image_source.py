"""Generated from Smithy shape ``com.amazonaws.quicksight#ImageSource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError
from capo_quicksight.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_quicksight.types.string


class _ImageSource_PublicUrl(TypedDict, closed=True):
    PublicUrl: "capo_quicksight.types.string.String"


class _ImageSource_S3Uri(TypedDict, closed=True):
    S3Uri: "capo_quicksight.types.string.String"


ImageSource: TypeAlias = (
    _ImageSource_PublicUrl | _ImageSource_S3Uri | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ImageSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ImageSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "PublicUrl" in value:
        return {"PublicUrl": value["PublicUrl"]}
    elif "S3Uri" in value:
        return {"S3Uri": value["S3Uri"]}
    else:
        raise SerializationError("ImageSource: no variant present")


def deserialize_json(data: dict) -> ImageSource:
    if data.get("PublicUrl") is not None:
        return {"PublicUrl": data["PublicUrl"]}
    elif data.get("S3Uri") is not None:
        return {"S3Uri": data["S3Uri"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ImageSource: no recognized variant key")

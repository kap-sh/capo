"""Generated from Smithy shape ``com.amazonaws.acm#SubjectFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError, SerializationError
from capo_acm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_acm.types.common_name_filter


class SubjectFilterCommonNameMember(TypedDict, closed=True):
    CommonName: "capo_acm.types.common_name_filter.CommonNameFilter"


SubjectFilter: TypeAlias = SubjectFilterCommonNameMember | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubjectFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SubjectFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "CommonName" in value:
        import capo_acm.types.common_name_filter

        return {
            "CommonName": capo_acm.types.common_name_filter.serialize_aws_json_1_1(
                value["CommonName"]
            )
        }
    else:
        raise SerializationError("SubjectFilter: no variant present")


def deserialize_aws_json_1_1(data: dict) -> SubjectFilter:
    if data.get("CommonName") is not None:
        import capo_acm.types.common_name_filter

        return {
            "CommonName": capo_acm.types.common_name_filter.deserialize_aws_json_1_1(
                data["CommonName"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SubjectFilter: no recognized variant key")

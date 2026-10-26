"""Generated from Smithy shape ``com.amazonaws.acm#SubjectAlternativeNameFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError, SerializationError
from capo_acm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_acm.types.dns_name_filter


class _SubjectAlternativeNameFilter_DnsName(TypedDict, closed=True):
    DnsName: "capo_acm.types.dns_name_filter.DnsNameFilter"


SubjectAlternativeNameFilter: TypeAlias = (
    _SubjectAlternativeNameFilter_DnsName | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubjectAlternativeNameFilter) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SubjectAlternativeNameFilter: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "DnsName" in value:
        import capo_acm.types.dns_name_filter

        return {
            "DnsName": capo_acm.types.dns_name_filter.serialize_aws_json_1_1(
                value["DnsName"]
            )
        }
    else:
        raise SerializationError("SubjectAlternativeNameFilter: no variant present")


def deserialize_aws_json_1_1(data: dict) -> SubjectAlternativeNameFilter:
    if data.get("DnsName") is not None:
        import capo_acm.types.dns_name_filter

        return {
            "DnsName": capo_acm.types.dns_name_filter.deserialize_aws_json_1_1(
                data["DnsName"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "SubjectAlternativeNameFilter: no recognized variant key"
        )

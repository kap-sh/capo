"""Generated from Smithy shape ``com.amazonaws.acm#PrevalidationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError, SerializationError
from capo_acm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_acm.types.dns_prevalidation_details


class _PrevalidationDetails_DnsPrevalidation(TypedDict, closed=True):
    DnsPrevalidation: "capo_acm.types.dns_prevalidation_details.DnsPrevalidationDetails"


PrevalidationDetails: TypeAlias = (
    _PrevalidationDetails_DnsPrevalidation | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrevalidationDetails) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PrevalidationDetails: cannot serialize unknown variant {value.name!r}"
        )
    elif "DnsPrevalidation" in value:
        import capo_acm.types.dns_prevalidation_details

        return {
            "DnsPrevalidation": capo_acm.types.dns_prevalidation_details.serialize_aws_json_1_1(
                value["DnsPrevalidation"]
            )
        }
    else:
        raise SerializationError("PrevalidationDetails: no variant present")


def deserialize_aws_json_1_1(data: dict) -> PrevalidationDetails:
    if data.get("DnsPrevalidation") is not None:
        import capo_acm.types.dns_prevalidation_details

        return {
            "DnsPrevalidation": capo_acm.types.dns_prevalidation_details.deserialize_aws_json_1_1(
                data["DnsPrevalidation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("PrevalidationDetails: no recognized variant key")

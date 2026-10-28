"""Generated from Smithy shape ``com.amazonaws.acm#PrevalidationOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError, SerializationError
from capo_acm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_acm.types.dns_prevalidation_options


class PrevalidationOptionsDnsPrevalidationMember(TypedDict, closed=True):
    DnsPrevalidation: "capo_acm.types.dns_prevalidation_options.DnsPrevalidationOptions"


PrevalidationOptions: TypeAlias = (
    PrevalidationOptionsDnsPrevalidationMember | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrevalidationOptions) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PrevalidationOptions: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "DnsPrevalidation" in value:
        import capo_acm.types.dns_prevalidation_options

        return {
            "DnsPrevalidation": capo_acm.types.dns_prevalidation_options.serialize_aws_json_1_1(
                value["DnsPrevalidation"]
            )
        }
    else:
        raise SerializationError("PrevalidationOptions: no variant present")


def deserialize_aws_json_1_1(data: dict) -> PrevalidationOptions:
    if data.get("DnsPrevalidation") is not None:
        import capo_acm.types.dns_prevalidation_options

        return {
            "DnsPrevalidation": capo_acm.types.dns_prevalidation_options.deserialize_aws_json_1_1(
                data["DnsPrevalidation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PrevalidationOptions: no recognized variant key")

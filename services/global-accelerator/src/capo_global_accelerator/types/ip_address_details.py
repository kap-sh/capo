"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#IpAddressDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.ip_address_detail

IpAddressDetails: TypeAlias = list[
    "capo_global_accelerator.types.ip_address_detail.IpAddressDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpAddressDetails) -> list:
    import capo_global_accelerator.types.ip_address_detail

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.ip_address_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> IpAddressDetails:
    import capo_global_accelerator.types.ip_address_detail

    out: IpAddressDetails = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_global_accelerator.types.ip_address_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.lightsail#SubdomainList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.subdomain

SubdomainList: TypeAlias = list["capo_lightsail.types.subdomain.Subdomain"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubdomainList) -> list:
    import capo_lightsail.types.subdomain

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.subdomain.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> SubdomainList:
    import capo_lightsail.types.subdomain

    out: SubdomainList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_lightsail.types.subdomain.deserialize_aws_json_1_1(item))
    return out

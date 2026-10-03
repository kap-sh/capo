"""Generated from Smithy shape ``com.amazonaws.mediapackage#AdsOnDeliveryRestrictions``."""

from typing import Literal, TypeAlias, cast

"""This setting allows the delivery restriction flags on SCTE-35 segmentation descriptors to determine whether a message signals an ad. Choosing "NONE" means no SCTE-35 messages become ads. Choosing "RESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that contain delivery restrictions will be treated as ads. Choosing "UNRESTRICTED" means SCTE-35 messages of the types specified in AdTriggers that do not contain delivery restrictions will be treated as ads. Choosing "BOTH" means all SCTE-35 messages of the types specified in AdTriggers will be treated as ads. Note that Splice Insert messages do not have these flags and are always treated as ads if specified in AdTriggers."""
AdsOnDeliveryRestrictions: TypeAlias = Literal[
    "NONE",
    "RESTRICTED",
    "UNRESTRICTED",
    "BOTH",
]


# --- restJson1 ser/de ---
def serialize_json(value: AdsOnDeliveryRestrictions) -> str:
    return value


def deserialize_json(data: str) -> AdsOnDeliveryRestrictions:
    return cast(AdsOnDeliveryRestrictions, data)

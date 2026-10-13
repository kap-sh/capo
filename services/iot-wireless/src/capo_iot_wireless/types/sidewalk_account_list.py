"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkAccountList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_iot_wireless.types.sidewalk_account_info_with_fingerprint

SidewalkAccountList: TypeAlias = list[
    "capo_iot_wireless.types.sidewalk_account_info_with_fingerprint.SidewalkAccountInfoWithFingerprint"
]


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkAccountList) -> list:
    import capo_iot_wireless.types.sidewalk_account_info_with_fingerprint

    out: list = []
    for item in value:
        out.append(
            capo_iot_wireless.types.sidewalk_account_info_with_fingerprint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> SidewalkAccountList:
    import capo_iot_wireless.types.sidewalk_account_info_with_fingerprint

    out: SidewalkAccountList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_iot_wireless.types.sidewalk_account_info_with_fingerprint.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: SidewalkAccountList) -> list[Any]:
    import capo_iot_wireless.types.sidewalk_account_info_with_fingerprint

    return [
        capo_iot_wireless.types.sidewalk_account_info_with_fingerprint.redact_sensitive(
            item
        )
        for item in value
    ]

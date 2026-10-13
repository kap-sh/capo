"""Generated from Smithy shape ``com.amazonaws.evs#LicenseInfoList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_evs.types.license_info

LicenseInfoList: TypeAlias = list["capo_evs.types.license_info.LicenseInfo"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseInfoList) -> list:
    import capo_evs.types.license_info

    out: list = []
    for item in value:
        out.append(capo_evs.types.license_info.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> LicenseInfoList:
    import capo_evs.types.license_info

    out: LicenseInfoList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_evs.types.license_info.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: LicenseInfoList) -> list[Any]:
    import capo_evs.types.license_info

    return [capo_evs.types.license_info.redact_sensitive(item) for item in value]

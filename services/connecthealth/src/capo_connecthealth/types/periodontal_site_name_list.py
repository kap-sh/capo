"""Generated from Smithy shape ``com.amazonaws.connecthealth#PeriodontalSiteNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connecthealth.types.periodontal_site_name

PeriodontalSiteNameList: TypeAlias = list[
    "capo_connecthealth.types.periodontal_site_name.PeriodontalSiteName"
]


# --- restJson1 ser/de ---
def serialize_json(value: PeriodontalSiteNameList) -> list:
    import capo_connecthealth.types.periodontal_site_name

    out: list = []
    for item in value:
        out.append(capo_connecthealth.types.periodontal_site_name.serialize_json(item))
    return out


def deserialize_json(data: list) -> PeriodontalSiteNameList:
    import capo_connecthealth.types.periodontal_site_name

    out: PeriodontalSiteNameList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connecthealth.types.periodontal_site_name.deserialize_json(item)
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.connecthealth#PeriodontalSiteList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connecthealth.types.periodontal_site

PeriodontalSiteList: TypeAlias = list[
    "capo_connecthealth.types.periodontal_site.PeriodontalSite"
]


# --- restJson1 ser/de ---
def serialize_json(value: PeriodontalSiteList) -> list:
    import capo_connecthealth.types.periodontal_site

    out: list = []
    for item in value:
        out.append(capo_connecthealth.types.periodontal_site.serialize_json(item))
    return out


def deserialize_json(data: list) -> PeriodontalSiteList:
    import capo_connecthealth.types.periodontal_site

    out: PeriodontalSiteList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connecthealth.types.periodontal_site.deserialize_json(item))
    return out


def redact_sensitive(value: PeriodontalSiteList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)

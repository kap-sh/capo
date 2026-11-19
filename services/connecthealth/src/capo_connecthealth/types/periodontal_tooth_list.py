"""Generated from Smithy shape ``com.amazonaws.connecthealth#PeriodontalToothList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connecthealth.types.periodontal_tooth

PeriodontalToothList: TypeAlias = list[
    "capo_connecthealth.types.periodontal_tooth.PeriodontalTooth"
]


# --- restJson1 ser/de ---
def serialize_json(value: PeriodontalToothList) -> list:
    import capo_connecthealth.types.periodontal_tooth

    out: list = []
    for item in value:
        out.append(capo_connecthealth.types.periodontal_tooth.serialize_json(item))
    return out


def deserialize_json(data: list) -> PeriodontalToothList:
    import capo_connecthealth.types.periodontal_tooth

    out: PeriodontalToothList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_connecthealth.types.periodontal_tooth.deserialize_json(item))
    return out


def redact_sensitive(value: PeriodontalToothList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)

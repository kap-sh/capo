"""Generated from Smithy shape ``com.amazonaws.appconfig#ValidatorList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_appconfig.types.validator

ValidatorList: TypeAlias = list["capo_appconfig.types.validator.Validator"]


# --- restJson1 ser/de ---
def serialize_json(value: ValidatorList) -> list:
    import capo_appconfig.types.validator

    out: list = []
    for item in value:
        out.append(capo_appconfig.types.validator.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValidatorList:
    import capo_appconfig.types.validator

    out: ValidatorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appconfig.types.validator.deserialize_json(item))
    return out


def redact_sensitive(value: ValidatorList) -> list[Any]:
    import capo_appconfig.types.validator

    return [capo_appconfig.types.validator.redact_sensitive(item) for item in value]

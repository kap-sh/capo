"""Generated from Smithy shape ``com.amazonaws.deadline#PathMappingRules``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.path_mapping_rule

PathMappingRules: TypeAlias = list[
    "capo_deadline.types.path_mapping_rule.PathMappingRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: PathMappingRules) -> list:
    import capo_deadline.types.path_mapping_rule

    out: list = []
    for item in value:
        out.append(capo_deadline.types.path_mapping_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> PathMappingRules:
    import capo_deadline.types.path_mapping_rule

    out: PathMappingRules = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.path_mapping_rule.deserialize_json(item))
    return out


def redact_sensitive(value: PathMappingRules) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)

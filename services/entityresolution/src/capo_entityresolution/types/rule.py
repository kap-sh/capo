"""Generated from Smithy shape ``com.amazonaws.entityresolution#Rule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_entityresolution.types.matching_keys


class Rule(TypedDict, closed=True):
    rule_name: "str"
    """<p>A name for the matching rule.</p>"""
    matching_keys: "capo_entityresolution.types.matching_keys.MatchingKeys"
    """<p>A list of <code>MatchingKeys</code>. The <code>MatchingKeys</code> must have been defined in the <code>SchemaMapping</code>. Two records are considered to match according to this rule if all of the <code>MatchingKeys</code> match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Rule) -> dict:
    out: dict = {}
    out["ruleName"] = value["rule_name"]
    import capo_entityresolution.types.matching_keys

    out["matchingKeys"] = capo_entityresolution.types.matching_keys.serialize_json(
        value["matching_keys"]
    )
    return out


def deserialize_json(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if data.get("ruleName") is not None:
        out["rule_name"] = data["ruleName"]
    else:
        out["rule_name"] = ""
    if data.get("matchingKeys") is not None:
        import capo_entityresolution.types.matching_keys

        out["matching_keys"] = (
            capo_entityresolution.types.matching_keys.deserialize_json(
                data["matchingKeys"]
            )
        )
    else:
        out["matching_keys"] = []
    return out

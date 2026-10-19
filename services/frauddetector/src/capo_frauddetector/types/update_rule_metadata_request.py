"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateRuleMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.rule


class UpdateRuleMetadataRequest(TypedDict, closed=True):
    rule: "capo_frauddetector.types.rule.Rule"
    """<p>The rule to update.</p>"""
    description: "capo_frauddetector.types.description.description"
    """<p>The rule description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRuleMetadataRequest) -> dict:
    out: dict = {}
    import capo_frauddetector.types.rule

    out["rule"] = capo_frauddetector.types.rule.serialize_aws_json_1_1(value["rule"])
    out["description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRuleMetadataRequest:
    out: UpdateRuleMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("rule") is not None:
        import capo_frauddetector.types.rule

        out["rule"] = capo_frauddetector.types.rule.deserialize_aws_json_1_1(
            data["rule"]
        )
    else:
        raise DeserializationError("UpdateRuleMetadataRequest.rule required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    return out

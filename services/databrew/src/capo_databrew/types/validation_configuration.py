"""Generated from Smithy shape ``com.amazonaws.databrew#ValidationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.arn
    import capo_databrew.types.validation_mode


class ValidationConfiguration(TypedDict, closed=True):
    ruleset_arn: "capo_databrew.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) for the ruleset to be validated in the profile job. The TargetArn of the selected ruleset should be the same as the Amazon Resource Name (ARN) of the dataset that is associated with the profile job.</p>"""
    validation_mode: NotRequired["capo_databrew.types.validation_mode.ValidationMode"]
    """<p>Mode of data quality validation. Default mode is “CHECK_ALL” which verifies all rules defined in the selected ruleset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationConfiguration) -> dict:
    out: dict = {}
    out["RulesetArn"] = value["ruleset_arn"]
    if "validation_mode" in value:
        import capo_databrew.types.validation_mode

        out["ValidationMode"] = capo_databrew.types.validation_mode.serialize_json(
            value["validation_mode"]
        )
    return out


def deserialize_json(data: dict) -> ValidationConfiguration:
    out: ValidationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RulesetArn") is not None:
        out["ruleset_arn"] = data["RulesetArn"]
    else:
        out["ruleset_arn"] = ""
    if data.get("ValidationMode") is not None:
        import capo_databrew.types.validation_mode

        out["validation_mode"] = capo_databrew.types.validation_mode.deserialize_json(
            data["ValidationMode"]
        )
    return out

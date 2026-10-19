"""Generated from Smithy shape ``com.amazonaws.codepipeline#SuccessConditions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.condition_list


class SuccessConditions(TypedDict, closed=True):
    conditions: "capo_codepipeline.types.condition_list.ConditionList"
    """<p>The conditions that are success conditions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SuccessConditions) -> dict:
    out: dict = {}
    import capo_codepipeline.types.condition_list

    out["conditions"] = capo_codepipeline.types.condition_list.serialize_aws_json_1_1(
        value["conditions"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SuccessConditions:
    out: SuccessConditions = {}  # type: ignore[typeddict-item]
    if data.get("conditions") is not None:
        import capo_codepipeline.types.condition_list

        out["conditions"] = (
            capo_codepipeline.types.condition_list.deserialize_aws_json_1_1(
                data["conditions"]
            )
        )
    else:
        out["conditions"] = []
    return out

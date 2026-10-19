"""Generated from Smithy shape ``com.amazonaws.codepipeline#BeforeEntryConditions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.condition_list


class BeforeEntryConditions(TypedDict, closed=True):
    conditions: "capo_codepipeline.types.condition_list.ConditionList"
    """<p>The conditions that are configured as entry conditions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BeforeEntryConditions) -> dict:
    out: dict = {}
    import capo_codepipeline.types.condition_list

    out["conditions"] = capo_codepipeline.types.condition_list.serialize_aws_json_1_1(
        value["conditions"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BeforeEntryConditions:
    out: BeforeEntryConditions = {}  # type: ignore[typeddict-item]
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

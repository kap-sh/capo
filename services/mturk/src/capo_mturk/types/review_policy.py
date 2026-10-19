"""Generated from Smithy shape ``com.amazonaws.mturk#ReviewPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.policy_parameter_list
    import capo_mturk.types.string


class ReviewPolicy(TypedDict, closed=True):
    policy_name: "capo_mturk.types.string.String"
    """<p> Name of a Review Policy: SimplePlurality/2011-09-01 or ScoreMyKnownAnswers/2011-09-01 </p>"""
    parameters: NotRequired[
        "capo_mturk.types.policy_parameter_list.PolicyParameterList"
    ]
    """<p>Name of the parameter from the Review policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReviewPolicy) -> dict:
    out: dict = {}
    out["PolicyName"] = value["policy_name"]
    if "parameters" in value:
        import capo_mturk.types.policy_parameter_list

        out["Parameters"] = (
            capo_mturk.types.policy_parameter_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReviewPolicy:
    out: ReviewPolicy = {}  # type: ignore[typeddict-item]
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    else:
        out["policy_name"] = ""
    if data.get("Parameters") is not None:
        import capo_mturk.types.policy_parameter_list

        out["parameters"] = (
            capo_mturk.types.policy_parameter_list.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    return out

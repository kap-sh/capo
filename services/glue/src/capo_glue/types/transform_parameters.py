"""Generated from Smithy shape ``com.amazonaws.glue#TransformParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.find_matches_parameters
    import capo_glue.types.transform_type


class TransformParameters(TypedDict, closed=True):
    transform_type: "capo_glue.types.transform_type.TransformType"
    """<p>The type of machine learning transform.</p> <p>For information about the types of machine learning transforms, see <a href="https://docs.aws.amazon.com/glue/latest/dg/add-job-machine-learning-transform.html">Creating Machine Learning Transforms</a>.</p>"""
    find_matches_parameters: NotRequired[
        "capo_glue.types.find_matches_parameters.FindMatchesParameters"
    ]
    """<p>The parameters for the find matches algorithm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformParameters) -> dict:
    out: dict = {}
    import capo_glue.types.transform_type

    out["TransformType"] = capo_glue.types.transform_type.serialize_aws_json_1_1(
        value["transform_type"]
    )
    if "find_matches_parameters" in value:
        import capo_glue.types.find_matches_parameters

        out["FindMatchesParameters"] = (
            capo_glue.types.find_matches_parameters.serialize_aws_json_1_1(
                value["find_matches_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformParameters:
    out: TransformParameters = {}  # type: ignore[typeddict-item]
    if data.get("TransformType") is not None:
        import capo_glue.types.transform_type

        out["transform_type"] = capo_glue.types.transform_type.deserialize_aws_json_1_1(
            data["TransformType"]
        )
    else:
        raise DeserializationError("TransformParameters.transform_type required")
    if data.get("FindMatchesParameters") is not None:
        import capo_glue.types.find_matches_parameters

        out["find_matches_parameters"] = (
            capo_glue.types.find_matches_parameters.deserialize_aws_json_1_1(
                data["FindMatchesParameters"]
            )
        )
    return out

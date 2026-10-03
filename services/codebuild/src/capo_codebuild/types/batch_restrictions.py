"""Generated from Smithy shape ``com.amazonaws.codebuild#BatchRestrictions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.compute_types_allowed
    import capo_codebuild.types.fleets_allowed
    import capo_codebuild.types.wrapper_int


class BatchRestrictions(TypedDict, closed=True):
    maximum_builds_allowed: NotRequired["capo_codebuild.types.wrapper_int.WrapperInt"]
    """<p>Specifies the maximum number of builds allowed.</p>"""
    compute_types_allowed: NotRequired[
        "capo_codebuild.types.compute_types_allowed.ComputeTypesAllowed"
    ]
    """<p>An array of strings that specify the compute types that are allowed for the batch build. See <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-compute-types.html">Build environment compute types</a> in the <i>CodeBuild User Guide</i> for these values. </p>"""
    fleets_allowed: NotRequired["capo_codebuild.types.fleets_allowed.FleetsAllowed"]
    """<p>An array of strings that specify the fleets that are allowed for the batch build. See <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/fleets.html">Run builds on reserved capacity fleets</a> in the <i>CodeBuild User Guide</i> for more information. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchRestrictions) -> dict:
    out: dict = {}
    if "maximum_builds_allowed" in value:
        out["maximumBuildsAllowed"] = value["maximum_builds_allowed"]
    if "compute_types_allowed" in value:
        import capo_codebuild.types.compute_types_allowed

        out["computeTypesAllowed"] = (
            capo_codebuild.types.compute_types_allowed.serialize_aws_json_1_1(
                value["compute_types_allowed"]
            )
        )
    if "fleets_allowed" in value:
        import capo_codebuild.types.fleets_allowed

        out["fleetsAllowed"] = (
            capo_codebuild.types.fleets_allowed.serialize_aws_json_1_1(
                value["fleets_allowed"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchRestrictions:
    out: BatchRestrictions = {}  # type: ignore[typeddict-item]
    if data.get("maximumBuildsAllowed") is not None:
        out["maximum_builds_allowed"] = data["maximumBuildsAllowed"]
    if data.get("computeTypesAllowed") is not None:
        import capo_codebuild.types.compute_types_allowed

        out["compute_types_allowed"] = (
            capo_codebuild.types.compute_types_allowed.deserialize_aws_json_1_1(
                data["computeTypesAllowed"]
            )
        )
    if data.get("fleetsAllowed") is not None:
        import capo_codebuild.types.fleets_allowed

        out["fleets_allowed"] = (
            capo_codebuild.types.fleets_allowed.deserialize_aws_json_1_1(
                data["fleetsAllowed"]
            )
        )
    return out

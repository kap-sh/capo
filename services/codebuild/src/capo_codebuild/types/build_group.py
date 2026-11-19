"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.boolean
    import capo_codebuild.types.build_summaries
    import capo_codebuild.types.build_summary
    import capo_codebuild.types.identifiers
    import capo_codebuild.types.string


class BuildGroup(TypedDict, closed=True):
    identifier: NotRequired["capo_codebuild.types.string.String"]
    """<p>Contains the identifier of the build group.</p>"""
    depends_on: NotRequired["capo_codebuild.types.identifiers.Identifiers"]
    """<p>An array of strings that contain the identifiers of the build groups that this build group depends on.</p>"""
    ignore_failure: "capo_codebuild.types.boolean.Boolean"
    """<p>Specifies if failures in this build group can be ignored.</p>"""
    current_build_summary: NotRequired[
        "capo_codebuild.types.build_summary.BuildSummary"
    ]
    """<p>A <code>BuildSummary</code> object that contains a summary of the current build group.</p>"""
    prior_build_summary_list: NotRequired[
        "capo_codebuild.types.build_summaries.BuildSummaries"
    ]
    """<p>An array of <code>BuildSummary</code> objects that contain summaries of previous build groups.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildGroup) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "depends_on" in value:
        import capo_codebuild.types.identifiers

        out["dependsOn"] = capo_codebuild.types.identifiers.serialize_aws_json_1_1(
            value["depends_on"]
        )
    out["ignoreFailure"] = value.get("ignore_failure", False)
    if "current_build_summary" in value:
        import capo_codebuild.types.build_summary

        out["currentBuildSummary"] = (
            capo_codebuild.types.build_summary.serialize_aws_json_1_1(
                value["current_build_summary"]
            )
        )
    if "prior_build_summary_list" in value:
        import capo_codebuild.types.build_summaries

        out["priorBuildSummaryList"] = (
            capo_codebuild.types.build_summaries.serialize_aws_json_1_1(
                value["prior_build_summary_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BuildGroup:
    out: BuildGroup = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    if data.get("dependsOn") is not None:
        import capo_codebuild.types.identifiers

        out["depends_on"] = capo_codebuild.types.identifiers.deserialize_aws_json_1_1(
            data["dependsOn"]
        )
    if data.get("ignoreFailure") is not None:
        out["ignore_failure"] = data["ignoreFailure"]
    else:
        out["ignore_failure"] = False
    if data.get("currentBuildSummary") is not None:
        import capo_codebuild.types.build_summary

        out["current_build_summary"] = (
            capo_codebuild.types.build_summary.deserialize_aws_json_1_1(
                data["currentBuildSummary"]
            )
        )
    if data.get("priorBuildSummaryList") is not None:
        import capo_codebuild.types.build_summaries

        out["prior_build_summary_list"] = (
            capo_codebuild.types.build_summaries.deserialize_aws_json_1_1(
                data["priorBuildSummaryList"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuildGroup) -> dict:
    out: dict = {}
    if "identifier" in value:
        out["identifier"] = value["identifier"]
    if "depends_on" in value:
        import capo_codebuild.types.identifiers

        out["dependsOn"] = capo_codebuild.types.identifiers.serialize_cbor(
            value["depends_on"]
        )
    out["ignoreFailure"] = value.get("ignore_failure", False)
    if "current_build_summary" in value:
        import capo_codebuild.types.build_summary

        out["currentBuildSummary"] = capo_codebuild.types.build_summary.serialize_cbor(
            value["current_build_summary"]
        )
    if "prior_build_summary_list" in value:
        import capo_codebuild.types.build_summaries

        out["priorBuildSummaryList"] = (
            capo_codebuild.types.build_summaries.serialize_cbor(
                value["prior_build_summary_list"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> BuildGroup:
    out: BuildGroup = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    if data.get("dependsOn") is not None:
        import capo_codebuild.types.identifiers

        out["depends_on"] = capo_codebuild.types.identifiers.deserialize_cbor(
            data["dependsOn"]
        )
    if data.get("ignoreFailure") is not None:
        out["ignore_failure"] = data["ignoreFailure"]
    else:
        out["ignore_failure"] = False
    if data.get("currentBuildSummary") is not None:
        import capo_codebuild.types.build_summary

        out["current_build_summary"] = (
            capo_codebuild.types.build_summary.deserialize_cbor(
                data["currentBuildSummary"]
            )
        )
    if data.get("priorBuildSummaryList") is not None:
        import capo_codebuild.types.build_summaries

        out["prior_build_summary_list"] = (
            capo_codebuild.types.build_summaries.deserialize_cbor(
                data["priorBuildSummaryList"]
            )
        )
    return out

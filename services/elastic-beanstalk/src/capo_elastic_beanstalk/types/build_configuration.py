"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#BuildConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.boxed_int
    import capo_elastic_beanstalk.types.compute_type
    import capo_elastic_beanstalk.types.non_empty_string
    import capo_elastic_beanstalk.types.string


class BuildConfiguration(TypedDict, closed=True):
    artifact_name: NotRequired["capo_elastic_beanstalk.types.string.String"]
    """<p>The name of the artifact of the CodeBuild build. If provided, Elastic Beanstalk stores the build artifact in the S3 location <i>S3-bucket</i>/resources/<i>application-name</i>/codebuild/codebuild-<i>version-label</i>-<i>artifact-name</i>.zip. If not provided, Elastic Beanstalk stores the build artifact in the S3 location <i>S3-bucket</i>/resources/<i>application-name</i>/codebuild/codebuild-<i>version-label</i>.zip. </p>"""
    code_build_service_role: (
        "capo_elastic_beanstalk.types.non_empty_string.NonEmptyString"
    )
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that enables CodeBuild to interact with dependent Amazon Web Services service on behalf of the Amazon Web Services account.</p>"""
    compute_type: NotRequired["capo_elastic_beanstalk.types.compute_type.ComputeType"]
    """<p>Information about the compute resources the build project will use.</p> <ul> <li> <p> <code>BUILD_GENERAL1_SMALL: Use up to 3 GB memory and 2 vCPUs for builds</code> </p> </li> <li> <p> <code>BUILD_GENERAL1_MEDIUM: Use up to 7 GB memory and 4 vCPUs for builds</code> </p> </li> <li> <p> <code>BUILD_GENERAL1_LARGE: Use up to 15 GB memory and 8 vCPUs for builds</code> </p> </li> </ul>"""
    image: "capo_elastic_beanstalk.types.non_empty_string.NonEmptyString"
    """<p>The ID of the Docker image to use for this build project.</p>"""
    timeout_in_minutes: NotRequired["capo_elastic_beanstalk.types.boxed_int.BoxedInt"]
    """<p>How long in minutes, from 5 to 480 (8 hours), for CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BuildConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "artifact_name" in value:
        pairs.append((f"{key_prefix}ArtifactName", str(value["artifact_name"])))
    pairs.append(
        (f"{key_prefix}CodeBuildServiceRole", str(value["code_build_service_role"]))
    )
    if "compute_type" in value:
        import capo_elastic_beanstalk.types.compute_type

        capo_elastic_beanstalk.types.compute_type.serialize_query(
            value["compute_type"], pairs, f"{key_prefix}ComputeType"
        )
    pairs.append((f"{key_prefix}Image", str(value["image"])))
    if "timeout_in_minutes" in value:
        pairs.append(
            (f"{key_prefix}TimeoutInMinutes", str(value["timeout_in_minutes"]))
        )


def deserialize_query(el: Element) -> BuildConfiguration:
    out: BuildConfiguration = {}  # type: ignore[typeddict-item]
    child_artifact_name = el.find("ArtifactName")
    if child_artifact_name is not None:
        out["artifact_name"] = str(child_artifact_name.text or "")
    child_code_build_service_role = el.find("CodeBuildServiceRole")
    if child_code_build_service_role is not None:
        out["code_build_service_role"] = str(child_code_build_service_role.text or "")
    else:
        out["code_build_service_role"] = ""
    child_compute_type = el.find("ComputeType")
    if child_compute_type is not None:
        import capo_elastic_beanstalk.types.compute_type

        out["compute_type"] = (
            capo_elastic_beanstalk.types.compute_type.deserialize_query(
                child_compute_type
            )
        )
    child_image = el.find("Image")
    if child_image is not None:
        out["image"] = str(child_image.text or "")
    else:
        out["image"] = ""
    child_timeout_in_minutes = el.find("TimeoutInMinutes")
    if child_timeout_in_minutes is not None:
        out["timeout_in_minutes"] = int(child_timeout_in_minutes.text or "")
    return out

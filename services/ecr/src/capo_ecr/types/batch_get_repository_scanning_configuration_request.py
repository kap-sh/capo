"""Generated from Smithy shape ``com.amazonaws.ecr#BatchGetRepositoryScanningConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.scanning_configuration_repository_name_list


class BatchGetRepositoryScanningConfigurationRequest(TypedDict, closed=True):
    repository_names: "capo_ecr.types.scanning_configuration_repository_name_list.ScanningConfigurationRepositoryNameList"
    """<p>One or more repository names to get the scanning configuration for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: BatchGetRepositoryScanningConfigurationRequest,
) -> dict:
    out: dict = {}
    import capo_ecr.types.scanning_configuration_repository_name_list

    out["repositoryNames"] = (
        capo_ecr.types.scanning_configuration_repository_name_list.serialize_aws_json_1_1(
            value["repository_names"]
        )
    )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> BatchGetRepositoryScanningConfigurationRequest:
    out: BatchGetRepositoryScanningConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("repositoryNames") is not None:
        import capo_ecr.types.scanning_configuration_repository_name_list

        out["repository_names"] = (
            capo_ecr.types.scanning_configuration_repository_name_list.deserialize_aws_json_1_1(
                data["repositoryNames"]
            )
        )
    else:
        out["repository_names"] = []
    return out

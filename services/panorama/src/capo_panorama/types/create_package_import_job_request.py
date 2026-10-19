"""Generated from Smithy shape ``com.amazonaws.panorama#CreatePackageImportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_panorama.errors import DeserializationError

if TYPE_CHECKING:
    import capo_panorama.types.client_token
    import capo_panorama.types.job_tags_list
    import capo_panorama.types.package_import_job_input_config
    import capo_panorama.types.package_import_job_output_config
    import capo_panorama.types.package_import_job_type


class CreatePackageImportJobRequest(TypedDict, closed=True):
    job_type: "capo_panorama.types.package_import_job_type.PackageImportJobType"
    """<p>A job type for the package import job.</p>"""
    input_config: "capo_panorama.types.package_import_job_input_config.PackageImportJobInputConfig"
    """<p>An input config for the package import job.</p>"""
    output_config: "capo_panorama.types.package_import_job_output_config.PackageImportJobOutputConfig"
    """<p>An output config for the package import job.</p>"""
    client_token: "capo_panorama.types.client_token.ClientToken"
    """<p>A client token for the package import job.</p>"""
    job_tags: NotRequired["capo_panorama.types.job_tags_list.JobTagsList"]
    """<p>Tags for the package import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePackageImportJobRequest) -> dict:
    out: dict = {}
    out["JobType"] = value["job_type"]
    import capo_panorama.types.package_import_job_input_config

    out["InputConfig"] = (
        capo_panorama.types.package_import_job_input_config.serialize_json(
            value["input_config"]
        )
    )
    import capo_panorama.types.package_import_job_output_config

    out["OutputConfig"] = (
        capo_panorama.types.package_import_job_output_config.serialize_json(
            value["output_config"]
        )
    )
    out["ClientToken"] = value["client_token"]
    if "job_tags" in value:
        import capo_panorama.types.job_tags_list

        out["JobTags"] = capo_panorama.types.job_tags_list.serialize_json(
            value["job_tags"]
        )
    return out


def deserialize_json(data: dict) -> CreatePackageImportJobRequest:
    out: CreatePackageImportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobType") is not None:
        out["job_type"] = data["JobType"]
    else:
        out["job_type"] = ""
    if data.get("InputConfig") is not None:
        import capo_panorama.types.package_import_job_input_config

        out["input_config"] = (
            capo_panorama.types.package_import_job_input_config.deserialize_json(
                data["InputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePackageImportJobRequest.input_config required"
        )
    if data.get("OutputConfig") is not None:
        import capo_panorama.types.package_import_job_output_config

        out["output_config"] = (
            capo_panorama.types.package_import_job_output_config.deserialize_json(
                data["OutputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePackageImportJobRequest.output_config required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    if data.get("JobTags") is not None:
        import capo_panorama.types.job_tags_list

        out["job_tags"] = capo_panorama.types.job_tags_list.deserialize_json(
            data["JobTags"]
        )
    return out

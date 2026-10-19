"""Generated from Smithy shape ``com.amazonaws.translate#UpdateParallelDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_translate.errors import DeserializationError

if TYPE_CHECKING:
    import capo_translate.types.client_token_string
    import capo_translate.types.description
    import capo_translate.types.parallel_data_config
    import capo_translate.types.resource_name


class UpdateParallelDataRequest(TypedDict, closed=True):
    name: "capo_translate.types.resource_name.ResourceName"
    """<p>The name of the parallel data resource being updated.</p>"""
    description: NotRequired["capo_translate.types.description.Description"]
    """<p>A custom description for the parallel data resource in Amazon Translate.</p>"""
    parallel_data_config: "capo_translate.types.parallel_data_config.ParallelDataConfig"
    """<p>Specifies the format and S3 location of the parallel data input file.</p>"""
    client_token: "capo_translate.types.client_token_string.ClientTokenString"
    """<p>A unique identifier for the request. This token is automatically generated when you use Amazon Translate through an AWS SDK.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateParallelDataRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_translate.types.parallel_data_config

    out["ParallelDataConfig"] = (
        capo_translate.types.parallel_data_config.serialize_aws_json_1_1(
            value["parallel_data_config"]
        )
    )
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateParallelDataRequest:
    out: UpdateParallelDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ParallelDataConfig") is not None:
        import capo_translate.types.parallel_data_config

        out["parallel_data_config"] = (
            capo_translate.types.parallel_data_config.deserialize_aws_json_1_1(
                data["ParallelDataConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateParallelDataRequest.parallel_data_config required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    return out

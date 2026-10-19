"""Generated from Smithy shape ``com.amazonaws.glue#UpdateRegistryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.description_string
    import capo_glue.types.registry_id


class UpdateRegistryInput(TypedDict, closed=True):
    registry_id: "capo_glue.types.registry_id.RegistryId"
    """<p>This is a wrapper structure that may contain the registry name and Amazon Resource Name (ARN).</p>"""
    description: "capo_glue.types.description_string.DescriptionString"
    """<p>A description of the registry. If description is not provided, this field will not be updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRegistryInput) -> dict:
    out: dict = {}
    import capo_glue.types.registry_id

    out["RegistryId"] = capo_glue.types.registry_id.serialize_aws_json_1_1(
        value["registry_id"]
    )
    out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRegistryInput:
    out: UpdateRegistryInput = {}  # type: ignore[typeddict-item]
    if data.get("RegistryId") is not None:
        import capo_glue.types.registry_id

        out["registry_id"] = capo_glue.types.registry_id.deserialize_aws_json_1_1(
            data["RegistryId"]
        )
    else:
        raise DeserializationError("UpdateRegistryInput.registry_id required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    return out

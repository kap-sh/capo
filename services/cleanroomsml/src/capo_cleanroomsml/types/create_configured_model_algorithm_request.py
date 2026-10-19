"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateConfiguredModelAlgorithmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.container_config
    import capo_cleanroomsml.types.iam_role_arn
    import capo_cleanroomsml.types.inference_container_config
    import capo_cleanroomsml.types.kms_key_arn
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.tag_map


class CreateConfiguredModelAlgorithmRequest(TypedDict, closed=True):
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the configured model algorithm.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured model algorithm.</p>"""
    role_arn: "capo_cleanroomsml.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the role that is used to access the repository.</p>"""
    training_container_config: NotRequired[
        "capo_cleanroomsml.types.container_config.ContainerConfig"
    ]
    """<p>Configuration information for the training container, including entrypoints and arguments.</p>"""
    inference_container_config: NotRequired[
        "capo_cleanroomsml.types.inference_container_config.InferenceContainerConfig"
    ]
    """<p>Configuration information for the inference container that is used when you run an inference job on a configured model algorithm.</p>"""
    tags: NotRequired["capo_cleanroomsml.types.tag_map.TagMap"]
    """<p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>"""
    kms_key_arn: NotRequired["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the configured ML model algorithm and associated data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredModelAlgorithmRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["roleArn"] = value["role_arn"]
    if "training_container_config" in value:
        import capo_cleanroomsml.types.container_config

        out["trainingContainerConfig"] = (
            capo_cleanroomsml.types.container_config.serialize_json(
                value["training_container_config"]
            )
        )
    if "inference_container_config" in value:
        import capo_cleanroomsml.types.inference_container_config

        out["inferenceContainerConfig"] = (
            capo_cleanroomsml.types.inference_container_config.serialize_json(
                value["inference_container_config"]
            )
        )
    if "tags" in value:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> CreateConfiguredModelAlgorithmRequest:
    out: CreateConfiguredModelAlgorithmRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("trainingContainerConfig") is not None:
        import capo_cleanroomsml.types.container_config

        out["training_container_config"] = (
            capo_cleanroomsml.types.container_config.deserialize_json(
                data["trainingContainerConfig"]
            )
        )
    if data.get("inferenceContainerConfig") is not None:
        import capo_cleanroomsml.types.inference_container_config

        out["inference_container_config"] = (
            capo_cleanroomsml.types.inference_container_config.deserialize_json(
                data["inferenceContainerConfig"]
            )
        )
    if data.get("tags") is not None:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out

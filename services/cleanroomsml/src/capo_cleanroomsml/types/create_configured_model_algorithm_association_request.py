"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateConfiguredModelAlgorithmAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_model_algorithm_arn
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.privacy_configuration
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.uuid


class CreateConfiguredModelAlgorithmAssociationRequest(TypedDict, closed=True):
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member who is associating this configured model algorithm.</p>"""
    configured_model_algorithm_arn: "capo_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm that you want to associate.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the configured model algorithm association.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured model algorithm association.</p>"""
    privacy_configuration: NotRequired[
        "capo_cleanroomsml.types.privacy_configuration.PrivacyConfiguration"
    ]
    """<p>Specifies the privacy configuration information for the configured model algorithm association. This information includes the maximum data size that can be exported.</p>"""
    tags: NotRequired["capo_cleanroomsml.types.tag_map.TagMap"]
    """<p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredModelAlgorithmAssociationRequest) -> dict:
    out: dict = {}
    out["configuredModelAlgorithmArn"] = value["configured_model_algorithm_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "privacy_configuration" in value:
        import capo_cleanroomsml.types.privacy_configuration

        out["privacyConfiguration"] = (
            capo_cleanroomsml.types.privacy_configuration.serialize_json(
                value["privacy_configuration"]
            )
        )
    if "tags" in value:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConfiguredModelAlgorithmAssociationRequest:
    out: CreateConfiguredModelAlgorithmAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("configuredModelAlgorithmArn") is not None:
        out["configured_model_algorithm_arn"] = data["configuredModelAlgorithmArn"]
    else:
        out["configured_model_algorithm_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("privacyConfiguration") is not None:
        import capo_cleanroomsml.types.privacy_configuration

        out["privacy_configuration"] = (
            capo_cleanroomsml.types.privacy_configuration.deserialize_json(
                data["privacyConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    return out

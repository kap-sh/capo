"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateMLInputChannelRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn_list
    import capo_cleanroomsml.types.input_channel
    import capo_cleanroomsml.types.kms_key_arn
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.payer_configuration
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.uuid


class CreateMLInputChannelRequest(TypedDict, closed=True):
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that is creating the ML input channel.</p>"""
    configured_model_algorithm_associations: "capo_cleanroomsml.types.configured_model_algorithm_association_arn_list.ConfiguredModelAlgorithmAssociationArnList"
    """<p>The associated configured model algorithms that are necessary to create this ML input channel.</p>"""
    input_channel: "capo_cleanroomsml.types.input_channel.InputChannel"
    """<p>The input data that is used to create this ML input channel.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the ML input channel.</p>"""
    retention_in_days: "int"
    """<p>The number of days that the data in the ML input channel is retained.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the ML input channel.</p>"""
    kms_key_arn: NotRequired["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key that is used to access the input channel.</p>"""
    tags: NotRequired["capo_cleanroomsml.types.tag_map.TagMap"]
    """<p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>"""
    payer_configuration: NotRequired[
        "capo_cleanroomsml.types.payer_configuration.PayerConfiguration"
    ]
    """<p>The payer configuration for the ML input channel. Determines which member account pays for compute and synthetic data costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMLInputChannelRequest) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn_list

    out["configuredModelAlgorithmAssociations"] = (
        capo_cleanroomsml.types.configured_model_algorithm_association_arn_list.serialize_json(
            value["configured_model_algorithm_associations"]
        )
    )
    import capo_cleanroomsml.types.input_channel

    out["inputChannel"] = capo_cleanroomsml.types.input_channel.serialize_json(
        value["input_channel"]
    )
    out["name"] = value["name"]
    out["retentionInDays"] = value["retention_in_days"]
    if "description" in value:
        out["description"] = value["description"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    if "payer_configuration" in value:
        import capo_cleanroomsml.types.payer_configuration

        out["payerConfiguration"] = (
            capo_cleanroomsml.types.payer_configuration.serialize_json(
                value["payer_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMLInputChannelRequest:
    out: CreateMLInputChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("configuredModelAlgorithmAssociations") is not None:
        import capo_cleanroomsml.types.configured_model_algorithm_association_arn_list

        out["configured_model_algorithm_associations"] = (
            capo_cleanroomsml.types.configured_model_algorithm_association_arn_list.deserialize_json(
                data["configuredModelAlgorithmAssociations"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMLInputChannelRequest.configured_model_algorithm_associations required"
        )
    if data.get("inputChannel") is not None:
        import capo_cleanroomsml.types.input_channel

        out["input_channel"] = capo_cleanroomsml.types.input_channel.deserialize_json(
            data["inputChannel"]
        )
    else:
        raise DeserializationError("CreateMLInputChannelRequest.input_channel required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateMLInputChannelRequest.name required")
    if data.get("retentionInDays") is not None:
        out["retention_in_days"] = data["retentionInDays"]
    else:
        raise DeserializationError(
            "CreateMLInputChannelRequest.retention_in_days required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("tags") is not None:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    if data.get("payerConfiguration") is not None:
        import capo_cleanroomsml.types.payer_configuration

        out["payer_configuration"] = (
            capo_cleanroomsml.types.payer_configuration.deserialize_json(
                data["payerConfiguration"]
            )
        )
    return out


def redact_sensitive(value: CreateMLInputChannelRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_channel" in value:
        import capo_cleanroomsml.types.input_channel

        out["input_channel"] = capo_cleanroomsml.types.input_channel.redact_sensitive(
            value["input_channel"]
        )
    return out

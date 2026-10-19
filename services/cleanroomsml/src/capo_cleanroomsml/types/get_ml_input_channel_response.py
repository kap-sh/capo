"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetMLInputChannelResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.configured_model_algorithm_association_arn_list
    import capo_cleanroomsml.types.input_channel
    import capo_cleanroomsml.types.kms_key_arn
    import capo_cleanroomsml.types.ml_input_channel_arn
    import capo_cleanroomsml.types.ml_input_channel_status
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.payer_configuration
    import capo_cleanroomsml.types.privacy_budgets
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.status_details
    import capo_cleanroomsml.types.synthetic_data_configuration
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.uuid


class GetMLInputChannelResponse(TypedDict, closed=True):
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the membership that contains the ML input channel.</p>"""
    collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the ML input channel.</p>"""
    ml_input_channel_arn: (
        "capo_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ML input channel.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the ML input channel.</p>"""
    configured_model_algorithm_associations: "capo_cleanroomsml.types.configured_model_algorithm_association_arn_list.ConfiguredModelAlgorithmAssociationArnList"
    """<p>The configured model algorithm associations that were used to create the ML input channel.</p>"""
    status: "capo_cleanroomsml.types.ml_input_channel_status.MLInputChannelStatus"
    """<p>The status of the ML input channel.</p>"""
    status_details: NotRequired["capo_cleanroomsml.types.status_details.StatusDetails"]
    retention_in_days: "int"
    """<p>The number of days to keep the data in the ML input channel.</p>"""
    number_of_records: NotRequired["int"]
    """<p>The number of records in the ML input channel.</p>"""
    privacy_budgets: NotRequired[
        "capo_cleanroomsml.types.privacy_budgets.PrivacyBudgets"
    ]
    """<p>Returns the privacy budgets that control access to this Clean Rooms ML input channel. Use these budgets to monitor and limit resource consumption over specified time periods.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the ML input channel.</p>"""
    synthetic_data_configuration: NotRequired[
        "capo_cleanroomsml.types.synthetic_data_configuration.SyntheticDataConfiguration"
    ]
    """<p>The synthetic data configuration for this ML input channel, including parameters for generating privacy-preserving synthetic data and evaluation scores for measuring the privacy of the generated data.</p>"""
    payer_configuration: NotRequired[
        "capo_cleanroomsml.types.payer_configuration.PayerConfiguration"
    ]
    """<p>The payer configuration for the ML input channel.</p>"""
    create_time: "datetime.datetime"
    """<p>The time at which the ML input channel was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the ML input channel was updated.</p>"""
    input_channel: "capo_cleanroomsml.types.input_channel.InputChannel"
    """<p>The input channel that was used to create the ML input channel.</p>"""
    protected_query_identifier: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The ID of the protected query that was used to create the ML input channel.</p>"""
    number_of_files: NotRequired["float"]
    """<p>The number of files in the ML input channel.</p>"""
    size_in_gb: NotRequired["float"]
    """<p>The size, in GB, of the ML input channel.</p>"""
    kms_key_arn: NotRequired["capo_cleanroomsml.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key that was used to create the ML input channel.</p>"""
    tags: NotRequired["capo_cleanroomsml.types.tag_map.TagMap"]
    """<p>The optional metadata that you applied to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMLInputChannelResponse) -> dict:
    out: dict = {}
    out["membershipIdentifier"] = value["membership_identifier"]
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    out["mlInputChannelArn"] = value["ml_input_channel_arn"]
    out["name"] = value["name"]
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn_list

    out["configuredModelAlgorithmAssociations"] = (
        capo_cleanroomsml.types.configured_model_algorithm_association_arn_list.serialize_json(
            value["configured_model_algorithm_associations"]
        )
    )
    import capo_cleanroomsml.types.ml_input_channel_status

    out["status"] = capo_cleanroomsml.types.ml_input_channel_status.serialize_json(
        value["status"]
    )
    if "status_details" in value:
        import capo_cleanroomsml.types.status_details

        out["statusDetails"] = capo_cleanroomsml.types.status_details.serialize_json(
            value["status_details"]
        )
    out["retentionInDays"] = value["retention_in_days"]
    if "number_of_records" in value:
        out["numberOfRecords"] = value["number_of_records"]
    if "privacy_budgets" in value:
        import capo_cleanroomsml.types.privacy_budgets

        out["privacyBudgets"] = capo_cleanroomsml.types.privacy_budgets.serialize_json(
            value["privacy_budgets"]
        )
    if "description" in value:
        out["description"] = value["description"]
    if "synthetic_data_configuration" in value:
        import capo_cleanroomsml.types.synthetic_data_configuration

        out["syntheticDataConfiguration"] = (
            capo_cleanroomsml.types.synthetic_data_configuration.serialize_json(
                value["synthetic_data_configuration"]
            )
        )
    if "payer_configuration" in value:
        import capo_cleanroomsml.types.payer_configuration

        out["payerConfiguration"] = (
            capo_cleanroomsml.types.payer_configuration.serialize_json(
                value["payer_configuration"]
            )
        )
    import capo_cleanroomsml._protocol.serialize

    out["createTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["create_time"]
    )
    import capo_cleanroomsml._protocol.serialize

    out["updateTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["update_time"]
    )
    import capo_cleanroomsml.types.input_channel

    out["inputChannel"] = capo_cleanroomsml.types.input_channel.serialize_json(
        value["input_channel"]
    )
    if "protected_query_identifier" in value:
        out["protectedQueryIdentifier"] = value["protected_query_identifier"]
    if "number_of_files" in value:
        out["numberOfFiles"] = (
            "NaN"
            if value["number_of_files"] != value["number_of_files"]
            else "Infinity"
            if value["number_of_files"] == float("inf")
            else "-Infinity"
            if value["number_of_files"] == float("-inf")
            else value["number_of_files"]
        )
    if "size_in_gb" in value:
        out["sizeInGb"] = (
            "NaN"
            if value["size_in_gb"] != value["size_in_gb"]
            else "Infinity"
            if value["size_in_gb"] == float("inf")
            else "-Infinity"
            if value["size_in_gb"] == float("-inf")
            else value["size_in_gb"]
        )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetMLInputChannelResponse:
    out: GetMLInputChannelResponse = {}  # type: ignore[typeddict-item]
    if data.get("membershipIdentifier") is not None:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        out["membership_identifier"] = ""
    if data.get("collaborationIdentifier") is not None:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        out["collaboration_identifier"] = ""
    if data.get("mlInputChannelArn") is not None:
        out["ml_input_channel_arn"] = data["mlInputChannelArn"]
    else:
        out["ml_input_channel_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("configuredModelAlgorithmAssociations") is not None:
        import capo_cleanroomsml.types.configured_model_algorithm_association_arn_list

        out["configured_model_algorithm_associations"] = (
            capo_cleanroomsml.types.configured_model_algorithm_association_arn_list.deserialize_json(
                data["configuredModelAlgorithmAssociations"]
            )
        )
    else:
        out["configured_model_algorithm_associations"] = []
    if data.get("status") is not None:
        import capo_cleanroomsml.types.ml_input_channel_status

        out["status"] = (
            capo_cleanroomsml.types.ml_input_channel_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cleanroomsml.types.ml_input_channel_status.MLInputChannelStatus", ""
        )
    if data.get("statusDetails") is not None:
        import capo_cleanroomsml.types.status_details

        out["status_details"] = capo_cleanroomsml.types.status_details.deserialize_json(
            data["statusDetails"]
        )
    if data.get("retentionInDays") is not None:
        out["retention_in_days"] = data["retentionInDays"]
    else:
        out["retention_in_days"] = 0
    if data.get("numberOfRecords") is not None:
        out["number_of_records"] = data["numberOfRecords"]
    if data.get("privacyBudgets") is not None:
        import capo_cleanroomsml.types.privacy_budgets

        out["privacy_budgets"] = (
            capo_cleanroomsml.types.privacy_budgets.deserialize_json(
                data["privacyBudgets"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("syntheticDataConfiguration") is not None:
        import capo_cleanroomsml.types.synthetic_data_configuration

        out["synthetic_data_configuration"] = (
            capo_cleanroomsml.types.synthetic_data_configuration.deserialize_json(
                data["syntheticDataConfiguration"]
            )
        )
    if data.get("payerConfiguration") is not None:
        import capo_cleanroomsml.types.payer_configuration

        out["payer_configuration"] = (
            capo_cleanroomsml.types.payer_configuration.deserialize_json(
                data["payerConfiguration"]
            )
        )
    if data.get("createTime") is not None:
        import datetime

        out["create_time"] = datetime.datetime.fromisoformat(
            data["createTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import datetime

        out["update_time"] = datetime.datetime.fromisoformat(
            data["updateTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("inputChannel") is not None:
        import capo_cleanroomsml.types.input_channel

        out["input_channel"] = capo_cleanroomsml.types.input_channel.deserialize_json(
            data["inputChannel"]
        )
    else:
        raise DeserializationError("GetMLInputChannelResponse.input_channel required")
    if data.get("protectedQueryIdentifier") is not None:
        out["protected_query_identifier"] = data["protectedQueryIdentifier"]
    if data.get("numberOfFiles") is not None:
        out["number_of_files"] = float(data["numberOfFiles"])
    if data.get("sizeInGb") is not None:
        out["size_in_gb"] = float(data["sizeInGb"])
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("tags") is not None:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: GetMLInputChannelResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "input_channel" in value:
        import capo_cleanroomsml.types.input_channel

        out["input_channel"] = capo_cleanroomsml.types.input_channel.redact_sensitive(
            value["input_channel"]
        )
    return out

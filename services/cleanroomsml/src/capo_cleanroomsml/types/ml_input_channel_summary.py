"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#MLInputChannelSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.configured_model_algorithm_association_arn_list
    import capo_cleanroomsml.types.ml_input_channel_arn
    import capo_cleanroomsml.types.ml_input_channel_status
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.payer_configuration
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.uuid


class MLInputChannelSummary(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the ML input channel was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the ML input channel was updated.</p>"""
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the membership that contains the ML input channel.</p>"""
    collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the ML input channel.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the ML input channel.</p>"""
    configured_model_algorithm_associations: "capo_cleanroomsml.types.configured_model_algorithm_association_arn_list.ConfiguredModelAlgorithmAssociationArnList"
    """<p>The associated configured model algorithms used to create the ML input channel.</p>"""
    protected_query_identifier: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The ID of the protected query that was used to create the ML input channel.</p>"""
    ml_input_channel_arn: (
        "capo_cleanroomsml.types.ml_input_channel_arn.MLInputChannelArn"
    )
    """<p>The Amazon Resource Name (ARN) of the ML input channel.</p>"""
    status: "capo_cleanroomsml.types.ml_input_channel_status.MLInputChannelStatus"
    """<p>The status of the ML input channel.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the ML input channel.</p>"""
    payer_configuration: NotRequired[
        "capo_cleanroomsml.types.payer_configuration.PayerConfiguration"
    ]
    """<p>The payer configuration for the ML input channel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MLInputChannelSummary) -> dict:
    out: dict = {}
    import capo_cleanroomsml._protocol.serialize

    out["createTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["create_time"]
    )
    import capo_cleanroomsml._protocol.serialize

    out["updateTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["update_time"]
    )
    out["membershipIdentifier"] = value["membership_identifier"]
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    out["name"] = value["name"]
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn_list

    out["configuredModelAlgorithmAssociations"] = (
        capo_cleanroomsml.types.configured_model_algorithm_association_arn_list.serialize_json(
            value["configured_model_algorithm_associations"]
        )
    )
    if "protected_query_identifier" in value:
        out["protectedQueryIdentifier"] = value["protected_query_identifier"]
    out["mlInputChannelArn"] = value["ml_input_channel_arn"]
    import capo_cleanroomsml.types.ml_input_channel_status

    out["status"] = capo_cleanroomsml.types.ml_input_channel_status.serialize_json(
        value["status"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "payer_configuration" in value:
        import capo_cleanroomsml.types.payer_configuration

        out["payerConfiguration"] = (
            capo_cleanroomsml.types.payer_configuration.serialize_json(
                value["payer_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MLInputChannelSummary:
    out: MLInputChannelSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("membershipIdentifier") is not None:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        out["membership_identifier"] = ""
    if data.get("collaborationIdentifier") is not None:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        out["collaboration_identifier"] = ""
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
    if data.get("protectedQueryIdentifier") is not None:
        out["protected_query_identifier"] = data["protectedQueryIdentifier"]
    if data.get("mlInputChannelArn") is not None:
        out["ml_input_channel_arn"] = data["mlInputChannelArn"]
    else:
        out["ml_input_channel_arn"] = ""
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
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("payerConfiguration") is not None:
        import capo_cleanroomsml.types.payer_configuration

        out["payer_configuration"] = (
            capo_cleanroomsml.types.payer_configuration.deserialize_json(
                data["payerConfiguration"]
            )
        )
    return out

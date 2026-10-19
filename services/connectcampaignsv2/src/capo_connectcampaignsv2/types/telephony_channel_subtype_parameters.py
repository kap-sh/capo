"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TelephonyChannelSubtypeParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.answer_machine_detection_config
    import capo_connectcampaignsv2.types.attributes
    import capo_connectcampaignsv2.types.destination_phone_number
    import capo_connectcampaignsv2.types.ring_timeout
    import capo_connectcampaignsv2.types.source_phone_number


class TelephonyChannelSubtypeParameters(TypedDict, closed=True):
    destination_phone_number: (
        "capo_connectcampaignsv2.types.destination_phone_number.DestinationPhoneNumber"
    )
    attributes: "capo_connectcampaignsv2.types.attributes.Attributes"
    connect_source_phone_number: NotRequired[
        "capo_connectcampaignsv2.types.source_phone_number.SourcePhoneNumber"
    ]
    answer_machine_detection_config: NotRequired[
        "capo_connectcampaignsv2.types.answer_machine_detection_config.AnswerMachineDetectionConfig"
    ]
    ring_timeout: NotRequired["capo_connectcampaignsv2.types.ring_timeout.RingTimeout"]


# --- restJson1 ser/de ---
def serialize_json(value: TelephonyChannelSubtypeParameters) -> dict:
    out: dict = {}
    out["destinationPhoneNumber"] = value["destination_phone_number"]
    import capo_connectcampaignsv2.types.attributes

    out["attributes"] = capo_connectcampaignsv2.types.attributes.serialize_json(
        value["attributes"]
    )
    if "connect_source_phone_number" in value:
        out["connectSourcePhoneNumber"] = value["connect_source_phone_number"]
    if "answer_machine_detection_config" in value:
        import capo_connectcampaignsv2.types.answer_machine_detection_config

        out["answerMachineDetectionConfig"] = (
            capo_connectcampaignsv2.types.answer_machine_detection_config.serialize_json(
                value["answer_machine_detection_config"]
            )
        )
    if "ring_timeout" in value:
        out["ringTimeout"] = value["ring_timeout"]
    return out


def deserialize_json(data: dict) -> TelephonyChannelSubtypeParameters:
    out: TelephonyChannelSubtypeParameters = {}  # type: ignore[typeddict-item]
    if data.get("destinationPhoneNumber") is not None:
        out["destination_phone_number"] = data["destinationPhoneNumber"]
    else:
        out["destination_phone_number"] = ""
    if data.get("attributes") is not None:
        import capo_connectcampaignsv2.types.attributes

        out["attributes"] = capo_connectcampaignsv2.types.attributes.deserialize_json(
            data["attributes"]
        )
    else:
        out["attributes"] = {}
    if data.get("connectSourcePhoneNumber") is not None:
        out["connect_source_phone_number"] = data["connectSourcePhoneNumber"]
    if data.get("answerMachineDetectionConfig") is not None:
        import capo_connectcampaignsv2.types.answer_machine_detection_config

        out["answer_machine_detection_config"] = (
            capo_connectcampaignsv2.types.answer_machine_detection_config.deserialize_json(
                data["answerMachineDetectionConfig"]
            )
        )
    if data.get("ringTimeout") is not None:
        out["ring_timeout"] = data["ringTimeout"]
    return out


def redact_sensitive(value: TelephonyChannelSubtypeParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "destination_phone_number" in value:
        out["destination_phone_number"] = "*** Sensitive Data Redacted ***"
    if "attributes" in value:
        out["attributes"] = "*** Sensitive Data Redacted ***"
    return out

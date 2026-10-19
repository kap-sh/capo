"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TelephonyOutboundConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.answer_machine_detection_config
    import capo_connectcampaignsv2.types.contact_flow_id
    import capo_connectcampaignsv2.types.ring_timeout
    import capo_connectcampaignsv2.types.source_phone_number


class TelephonyOutboundConfig(TypedDict, closed=True):
    connect_contact_flow_id: (
        "capo_connectcampaignsv2.types.contact_flow_id.ContactFlowId"
    )
    connect_source_phone_number: NotRequired[
        "capo_connectcampaignsv2.types.source_phone_number.SourcePhoneNumber"
    ]
    answer_machine_detection_config: NotRequired[
        "capo_connectcampaignsv2.types.answer_machine_detection_config.AnswerMachineDetectionConfig"
    ]
    ring_timeout: NotRequired["capo_connectcampaignsv2.types.ring_timeout.RingTimeout"]


# --- restJson1 ser/de ---
def serialize_json(value: TelephonyOutboundConfig) -> dict:
    out: dict = {}
    out["connectContactFlowId"] = value["connect_contact_flow_id"]
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


def deserialize_json(data: dict) -> TelephonyOutboundConfig:
    out: TelephonyOutboundConfig = {}  # type: ignore[typeddict-item]
    if data.get("connectContactFlowId") is not None:
        out["connect_contact_flow_id"] = data["connectContactFlowId"]
    else:
        out["connect_contact_flow_id"] = ""
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

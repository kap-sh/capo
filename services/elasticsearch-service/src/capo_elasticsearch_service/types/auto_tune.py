"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutoTune``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.auto_tune_details
    import capo_elasticsearch_service.types.auto_tune_type


class AutoTune(TypedDict, closed=True):
    auto_tune_type: NotRequired[
        "capo_elasticsearch_service.types.auto_tune_type.AutoTuneType"
    ]
    """<p>Specifies Auto-Tune type. Valid value is SCHEDULED_ACTION. </p>"""
    auto_tune_details: NotRequired[
        "capo_elasticsearch_service.types.auto_tune_details.AutoTuneDetails"
    ]
    """<p>Specifies details of the Auto-Tune action. See the <a href="https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/auto-tune.html" target="_blank">Developer Guide</a> for more information. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTune) -> dict:
    out: dict = {}
    if "auto_tune_type" in value:
        import capo_elasticsearch_service.types.auto_tune_type

        out["AutoTuneType"] = (
            capo_elasticsearch_service.types.auto_tune_type.serialize_json(
                value["auto_tune_type"]
            )
        )
    if "auto_tune_details" in value:
        import capo_elasticsearch_service.types.auto_tune_details

        out["AutoTuneDetails"] = (
            capo_elasticsearch_service.types.auto_tune_details.serialize_json(
                value["auto_tune_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutoTune:
    out: AutoTune = {}  # type: ignore[typeddict-item]
    if data.get("AutoTuneType") is not None:
        import capo_elasticsearch_service.types.auto_tune_type

        out["auto_tune_type"] = (
            capo_elasticsearch_service.types.auto_tune_type.deserialize_json(
                data["AutoTuneType"]
            )
        )
    if data.get("AutoTuneDetails") is not None:
        import capo_elasticsearch_service.types.auto_tune_details

        out["auto_tune_details"] = (
            capo_elasticsearch_service.types.auto_tune_details.deserialize_json(
                data["AutoTuneDetails"]
            )
        )
    return out

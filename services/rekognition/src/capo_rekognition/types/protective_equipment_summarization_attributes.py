"""Generated from Smithy shape ``com.amazonaws.rekognition#ProtectiveEquipmentSummarizationAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.percent
    import capo_rekognition.types.protective_equipment_types


class ProtectiveEquipmentSummarizationAttributes(TypedDict, closed=True):
    min_confidence: "capo_rekognition.types.percent.Percent"
    """<p>The minimum confidence level for which you want summary information. The confidence level applies to person detection, body part detection, equipment detection, and body part coverage. Amazon Rekognition doesn't return summary information with a confidence than this specified value. There isn't a default value.</p> <p>Specify a <code>MinConfidence</code> value that is between 50-100% as <code>DetectProtectiveEquipment</code> returns predictions only where the detection confidence is between 50% - 100%. If you specify a value that is less than 50%, the results are the same specifying a value of 50%.</p> <p> </p>"""
    required_equipment_types: (
        "capo_rekognition.types.protective_equipment_types.ProtectiveEquipmentTypes"
    )
    """<p>An array of personal protective equipment types for which you want summary information. If a person is detected wearing a required requipment type, the person's ID is added to the <code>PersonsWithRequiredEquipment</code> array field returned in <a>ProtectiveEquipmentSummary</a> by <code>DetectProtectiveEquipment</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProtectiveEquipmentSummarizationAttributes) -> dict:
    out: dict = {}
    out["MinConfidence"] = (
        "NaN"
        if value["min_confidence"] != value["min_confidence"]
        else "Infinity"
        if value["min_confidence"] == float("inf")
        else "-Infinity"
        if value["min_confidence"] == float("-inf")
        else value["min_confidence"]
    )
    import capo_rekognition.types.protective_equipment_types

    out["RequiredEquipmentTypes"] = (
        capo_rekognition.types.protective_equipment_types.serialize_aws_json_1_1(
            value["required_equipment_types"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProtectiveEquipmentSummarizationAttributes:
    out: ProtectiveEquipmentSummarizationAttributes = {}  # type: ignore[typeddict-item]
    if data.get("MinConfidence") is not None:
        out["min_confidence"] = float(data["MinConfidence"])
    else:
        out["min_confidence"] = 0.0
    if data.get("RequiredEquipmentTypes") is not None:
        import capo_rekognition.types.protective_equipment_types

        out["required_equipment_types"] = (
            capo_rekognition.types.protective_equipment_types.deserialize_aws_json_1_1(
                data["RequiredEquipmentTypes"]
            )
        )
    else:
        out["required_equipment_types"] = []
    return out

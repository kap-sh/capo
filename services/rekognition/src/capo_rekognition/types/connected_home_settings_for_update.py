"""Generated from Smithy shape ``com.amazonaws.rekognition#ConnectedHomeSettingsForUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.connected_home_labels
    import capo_rekognition.types.percent


class ConnectedHomeSettingsForUpdate(TypedDict, closed=True):
    labels: NotRequired[
        "capo_rekognition.types.connected_home_labels.ConnectedHomeLabels"
    ]
    """<p> Specifies what you want to detect in the video, such as people, packages, or pets. The current valid labels you can include in this list are: "PERSON", "PET", "PACKAGE", and "ALL". </p>"""
    min_confidence: NotRequired["capo_rekognition.types.percent.Percent"]
    """<p> The minimum confidence required to label an object in the video. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectedHomeSettingsForUpdate) -> dict:
    out: dict = {}
    if "labels" in value:
        import capo_rekognition.types.connected_home_labels

        out["Labels"] = (
            capo_rekognition.types.connected_home_labels.serialize_aws_json_1_1(
                value["labels"]
            )
        )
    if "min_confidence" in value:
        out["MinConfidence"] = (
            "NaN"
            if value["min_confidence"] != value["min_confidence"]
            else "Infinity"
            if value["min_confidence"] == float("inf")
            else "-Infinity"
            if value["min_confidence"] == float("-inf")
            else value["min_confidence"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectedHomeSettingsForUpdate:
    out: ConnectedHomeSettingsForUpdate = {}  # type: ignore[typeddict-item]
    if data.get("Labels") is not None:
        import capo_rekognition.types.connected_home_labels

        out["labels"] = (
            capo_rekognition.types.connected_home_labels.deserialize_aws_json_1_1(
                data["Labels"]
            )
        )
    if data.get("MinConfidence") is not None:
        out["min_confidence"] = float(data["MinConfidence"])
    return out

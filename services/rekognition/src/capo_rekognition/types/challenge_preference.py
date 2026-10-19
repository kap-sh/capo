"""Generated from Smithy shape ``com.amazonaws.rekognition#ChallengePreference``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.challenge_type
    import capo_rekognition.types.versions


class ChallengePreference(TypedDict, closed=True):
    type: "capo_rekognition.types.challenge_type.ChallengeType"
    """<p>The types of challenges that have been selected for the Face Liveness session.</p>"""
    versions: NotRequired["capo_rekognition.types.versions.Versions"]
    """<p>The version of the challenges that have been selected for the Face Liveness session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChallengePreference) -> dict:
    out: dict = {}
    import capo_rekognition.types.challenge_type

    out["Type"] = capo_rekognition.types.challenge_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "versions" in value:
        import capo_rekognition.types.versions

        out["Versions"] = capo_rekognition.types.versions.serialize_aws_json_1_1(
            value["versions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ChallengePreference:
    out: ChallengePreference = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_rekognition.types.challenge_type

        out["type"] = capo_rekognition.types.challenge_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_rekognition.types.challenge_type.ChallengeType", ""
        )
    if data.get("Versions") is not None:
        import capo_rekognition.types.versions

        out["versions"] = capo_rekognition.types.versions.deserialize_aws_json_1_1(
            data["Versions"]
        )
    return out

"""Generated from Smithy shape ``com.amazonaws.rekognition#Challenge``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.challenge_type
    import capo_rekognition.types.version


class Challenge(TypedDict, closed=True):
    type: "capo_rekognition.types.challenge_type.ChallengeType"
    """<p>The type of the challenge being used for the Face Liveness session.</p>"""
    version: "capo_rekognition.types.version.Version"
    """<p>The version of the challenge being used for the Face Liveness session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Challenge) -> dict:
    out: dict = {}
    import capo_rekognition.types.challenge_type

    out["Type"] = capo_rekognition.types.challenge_type.serialize_aws_json_1_1(
        value["type"]
    )
    out["Version"] = value["version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Challenge:
    out: Challenge = {}  # type: ignore[typeddict-item]
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
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    else:
        out["version"] = ""
    return out

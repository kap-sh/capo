"""Generated from Smithy shape ``com.amazonaws.bedrock#FoundationModelLifecycle``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.foundation_model_lifecycle_status
    import capo_bedrock.types.timestamp


class FoundationModelLifecycle(TypedDict, closed=True):
    status: "capo_bedrock.types.foundation_model_lifecycle_status.FoundationModelLifecycleStatus"
    """<p>Specifies whether a model version is available (<code>ACTIVE</code>) or deprecated (<code>LEGACY</code>.</p>"""
    start_of_life_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Launch time when the model first becomes available</p>"""
    end_of_life_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Time when the model is no longer available for use</p>"""
    legacy_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Time when the model enters legacy state. Models in legacy state can still be used, but users should plan to transition to an Active model before the end of life time</p>"""
    public_extended_access_time: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>Public extended access portion of the legacy period, when users should expect higher pricing</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FoundationModelLifecycle) -> dict:
    out: dict = {}
    import capo_bedrock.types.foundation_model_lifecycle_status

    out["status"] = capo_bedrock.types.foundation_model_lifecycle_status.serialize_json(
        value["status"]
    )
    if "start_of_life_time" in value:
        import capo_bedrock.types.timestamp

        out["startOfLifeTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["start_of_life_time"]
        )
    if "end_of_life_time" in value:
        import capo_bedrock.types.timestamp

        out["endOfLifeTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["end_of_life_time"]
        )
    if "legacy_time" in value:
        import capo_bedrock.types.timestamp

        out["legacyTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["legacy_time"]
        )
    if "public_extended_access_time" in value:
        import capo_bedrock.types.timestamp

        out["publicExtendedAccessTime"] = capo_bedrock.types.timestamp.serialize_json(
            value["public_extended_access_time"]
        )
    return out


def deserialize_json(data: dict) -> FoundationModelLifecycle:
    out: FoundationModelLifecycle = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        import capo_bedrock.types.foundation_model_lifecycle_status

        out["status"] = (
            capo_bedrock.types.foundation_model_lifecycle_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock.types.foundation_model_lifecycle_status.FoundationModelLifecycleStatus",
            "",
        )
    if data.get("startOfLifeTime") is not None:
        import capo_bedrock.types.timestamp

        out["start_of_life_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["startOfLifeTime"]
        )
    if data.get("endOfLifeTime") is not None:
        import capo_bedrock.types.timestamp

        out["end_of_life_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["endOfLifeTime"]
        )
    if data.get("legacyTime") is not None:
        import capo_bedrock.types.timestamp

        out["legacy_time"] = capo_bedrock.types.timestamp.deserialize_json(
            data["legacyTime"]
        )
    if data.get("publicExtendedAccessTime") is not None:
        import capo_bedrock.types.timestamp

        out["public_extended_access_time"] = (
            capo_bedrock.types.timestamp.deserialize_json(
                data["publicExtendedAccessTime"]
            )
        )
    return out

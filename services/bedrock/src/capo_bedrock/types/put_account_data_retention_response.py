"""Generated from Smithy shape ``com.amazonaws.bedrock#PutAccountDataRetentionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.data_retention_mode
    import capo_bedrock.types.timestamp


class PutAccountDataRetentionResponse(TypedDict, closed=True):
    mode: "capo_bedrock.types.data_retention_mode.DataRetentionMode"
    """<p>The data retention mode set for the account.</p>"""
    updated_at: NotRequired["capo_bedrock.types.timestamp.Timestamp"]
    """<p>The time at which the data retention mode was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountDataRetentionResponse) -> dict:
    out: dict = {}
    import capo_bedrock.types.data_retention_mode

    out["mode"] = capo_bedrock.types.data_retention_mode.serialize_json(value["mode"])
    if "updated_at" in value:
        import capo_bedrock.types.timestamp

        out["updatedAt"] = capo_bedrock.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> PutAccountDataRetentionResponse:
    out: PutAccountDataRetentionResponse = {}  # type: ignore[typeddict-item]
    if data.get("mode") is not None:
        import capo_bedrock.types.data_retention_mode

        out["mode"] = capo_bedrock.types.data_retention_mode.deserialize_json(
            data["mode"]
        )
    else:
        import typing

        out["mode"] = typing.cast(
            "capo_bedrock.types.data_retention_mode.DataRetentionMode", ""
        )
    if data.get("updatedAt") is not None:
        import capo_bedrock.types.timestamp

        out["updated_at"] = capo_bedrock.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out

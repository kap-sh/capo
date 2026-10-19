"""Generated from Smithy shape ``com.amazonaws.bedrock#PutAccountDataRetentionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.data_retention_mode


class PutAccountDataRetentionRequest(TypedDict, closed=True):
    mode: "capo_bedrock.types.data_retention_mode.DataRetentionMode"
    """<p>The data retention mode to set for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountDataRetentionRequest) -> dict:
    out: dict = {}
    import capo_bedrock.types.data_retention_mode

    out["mode"] = capo_bedrock.types.data_retention_mode.serialize_json(value["mode"])
    return out


def deserialize_json(data: dict) -> PutAccountDataRetentionRequest:
    out: PutAccountDataRetentionRequest = {}  # type: ignore[typeddict-item]
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
    return out

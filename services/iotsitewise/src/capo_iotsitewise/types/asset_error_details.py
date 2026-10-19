"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetErrorDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.asset_error_code
    import capo_iotsitewise.types.asset_error_message
    import capo_iotsitewise.types.id


class AssetErrorDetails(TypedDict, closed=True):
    asset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the asset, in UUID format.</p>"""
    code: "capo_iotsitewise.types.asset_error_code.AssetErrorCode"
    """<p>The error code.</p>"""
    message: "capo_iotsitewise.types.asset_error_message.AssetErrorMessage"
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetErrorDetails) -> dict:
    out: dict = {}
    out["assetId"] = value["asset_id"]
    import capo_iotsitewise.types.asset_error_code

    out["code"] = capo_iotsitewise.types.asset_error_code.serialize_json(value["code"])
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AssetErrorDetails:
    out: AssetErrorDetails = {}  # type: ignore[typeddict-item]
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        out["asset_id"] = ""
    if data.get("code") is not None:
        import capo_iotsitewise.types.asset_error_code

        out["code"] = capo_iotsitewise.types.asset_error_code.deserialize_json(
            data["code"]
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_iotsitewise.types.asset_error_code.AssetErrorCode", ""
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out

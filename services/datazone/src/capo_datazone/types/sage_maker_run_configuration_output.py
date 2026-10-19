"""Generated from Smithy shape ``com.amazonaws.datazone#SageMakerRunConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.tracking_assets


class SageMakerRunConfigurationOutput(TypedDict, closed=True):
    account_id: NotRequired["str"]
    """<p>The Amazon SageMaker account ID.</p>"""
    region: NotRequired["str"]
    """<p>The Amazon SageMaker Region.</p>"""
    tracking_assets: "capo_datazone.types.tracking_assets.TrackingAssets"
    """<p>The tracking assets of the Amazon SageMaker.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SageMakerRunConfigurationOutput) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "region" in value:
        out["region"] = value["region"]
    import capo_datazone.types.tracking_assets

    out["trackingAssets"] = capo_datazone.types.tracking_assets.serialize_json(
        value["tracking_assets"]
    )
    return out


def deserialize_json(data: dict) -> SageMakerRunConfigurationOutput:
    out: SageMakerRunConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("trackingAssets") is not None:
        import capo_datazone.types.tracking_assets

        out["tracking_assets"] = capo_datazone.types.tracking_assets.deserialize_json(
            data["trackingAssets"]
        )
    else:
        out["tracking_assets"] = {}
    return out

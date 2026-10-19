"""Generated from Smithy shape ``com.amazonaws.migrationhubconfig#CreateHomeRegionControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_migrationhub_config.errors import DeserializationError

if TYPE_CHECKING:
    import capo_migrationhub_config.types.dry_run
    import capo_migrationhub_config.types.home_region
    import capo_migrationhub_config.types.target


class CreateHomeRegionControlRequest(TypedDict, closed=True):
    home_region: "capo_migrationhub_config.types.home_region.HomeRegion"
    """<p>The name of the home region of the calling account.</p>"""
    target: "capo_migrationhub_config.types.target.Target"
    """<p>The account for which this command sets up a home region control. The <code>Target</code> is always of type <code>ACCOUNT</code>.</p>"""
    dry_run: NotRequired["capo_migrationhub_config.types.dry_run.DryRun"]
    """<p>Optional Boolean flag to indicate whether any effect should take place. It tests whether the caller has permission to make the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHomeRegionControlRequest) -> dict:
    out: dict = {}
    out["HomeRegion"] = value["home_region"]
    import capo_migrationhub_config.types.target

    out["Target"] = capo_migrationhub_config.types.target.serialize_aws_json_1_1(
        value["target"]
    )
    if "dry_run" in value:
        out["DryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHomeRegionControlRequest:
    out: CreateHomeRegionControlRequest = {}  # type: ignore[typeddict-item]
    if data.get("HomeRegion") is not None:
        out["home_region"] = data["HomeRegion"]
    else:
        out["home_region"] = ""
    if data.get("Target") is not None:
        import capo_migrationhub_config.types.target

        out["target"] = capo_migrationhub_config.types.target.deserialize_aws_json_1_1(
            data["Target"]
        )
    else:
        raise DeserializationError("CreateHomeRegionControlRequest.target required")
    if data.get("DryRun") is not None:
        out["dry_run"] = data["DryRun"]
    return out

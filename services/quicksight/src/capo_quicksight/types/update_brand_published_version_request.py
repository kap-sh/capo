"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateBrandPublishedVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.aws_account_id
    import capo_quicksight.types.short_restrictive_resource_id


class UpdateBrandPublishedVersionRequest(TypedDict, closed=True):
    aws_account_id: "capo_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that owns the brand.</p>"""
    brand_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the Quick brand.</p>"""
    version_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the published version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBrandPublishedVersionRequest) -> dict:
    out: dict = {}
    out["VersionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> UpdateBrandPublishedVersionRequest:
    out: UpdateBrandPublishedVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    else:
        out["version_id"] = ""
    return out

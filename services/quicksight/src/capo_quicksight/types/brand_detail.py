"""Generated from Smithy shape ``com.amazonaws.quicksight#BrandDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_quicksight.types.arn
    import capo_quicksight.types.brand_status
    import capo_quicksight.types.brand_version_status
    import capo_quicksight.types.error_list
    import capo_quicksight.types.logo
    import capo_quicksight.types.short_restrictive_resource_id


class BrandDetail(TypedDict, closed=True):
    brand_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID of the Quick brand.</p>"""
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the brand.</p>"""
    brand_status: NotRequired["capo_quicksight.types.brand_status.BrandStatus"]
    """<p>The status of the brand.</p>"""
    created_time: NotRequired["datetime.datetime"]
    """<p>The time that the brand was created.</p>"""
    last_updated_time: NotRequired["datetime.datetime"]
    """<p>The last time the brand was updated.</p>"""
    version_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the version.</p>"""
    version_status: NotRequired[
        "capo_quicksight.types.brand_version_status.BrandVersionStatus"
    ]
    """<p>The status of the version.</p>"""
    errors: NotRequired["capo_quicksight.types.error_list.ErrorList"]
    """<p>A list of errors that occurred during the most recent brand operation.</p>"""
    logo: NotRequired["capo_quicksight.types.logo.Logo"]
    """<p>The logo details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrandDetail) -> dict:
    out: dict = {}
    out["BrandId"] = value["brand_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "brand_status" in value:
        import capo_quicksight.types.brand_status

        out["BrandStatus"] = capo_quicksight.types.brand_status.serialize_json(
            value["brand_status"]
        )
    if "created_time" in value:
        import capo_quicksight.types._prelude.timestamp

        out["CreatedTime"] = capo_quicksight.types._prelude.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import capo_quicksight.types._prelude.timestamp

        out["LastUpdatedTime"] = (
            capo_quicksight.types._prelude.timestamp.serialize_json(
                value["last_updated_time"]
            )
        )
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "version_status" in value:
        import capo_quicksight.types.brand_version_status

        out["VersionStatus"] = (
            capo_quicksight.types.brand_version_status.serialize_json(
                value["version_status"]
            )
        )
    if "errors" in value:
        import capo_quicksight.types.error_list

        out["Errors"] = capo_quicksight.types.error_list.serialize_json(value["errors"])
    if "logo" in value:
        import capo_quicksight.types.logo

        out["Logo"] = capo_quicksight.types.logo.serialize_json(value["logo"])
    return out


def deserialize_json(data: dict) -> BrandDetail:
    out: BrandDetail = {}  # type: ignore[typeddict-item]
    if data.get("BrandId") is not None:
        out["brand_id"] = data["BrandId"]
    else:
        out["brand_id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("BrandStatus") is not None:
        import capo_quicksight.types.brand_status

        out["brand_status"] = capo_quicksight.types.brand_status.deserialize_json(
            data["BrandStatus"]
        )
    if data.get("CreatedTime") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["created_time"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("LastUpdatedTime") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["last_updated_time"] = (
            capo_quicksight.types._prelude.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    if data.get("VersionStatus") is not None:
        import capo_quicksight.types.brand_version_status

        out["version_status"] = (
            capo_quicksight.types.brand_version_status.deserialize_json(
                data["VersionStatus"]
            )
        )
    if data.get("Errors") is not None:
        import capo_quicksight.types.error_list

        out["errors"] = capo_quicksight.types.error_list.deserialize_json(
            data["Errors"]
        )
    if data.get("Logo") is not None:
        import capo_quicksight.types.logo

        out["logo"] = capo_quicksight.types.logo.deserialize_json(data["Logo"])
    return out
